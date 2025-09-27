"""Tkinter-Benutzeroberfläche für Choo Choo Clicker."""
from __future__ import annotations

import tkinter as tk
from pathlib import Path
from typing import Dict, FrozenSet

from assets import SpriteSheet
from game import GameEngine, TickResult, TrainState
from ui.camera import CameraView
from ui.scaling import compute_scaling
from world import Cell, Direction, TrackShape


class ChooChooApp:
    BASE_CELL_SIZE = 32
    BG_COLOR = "#1a1b26"
    GRID_COLOR = "#2d3143"
    TRAIN_COLOR = "#f7768e"
    TRAIN_OUTLINE = "#ff9cac"

    def __init__(self, root: tk.Tk, engine: GameEngine, sprite_sheet_path: Path) -> None:
        self.root = root
        self.engine = engine
        self.root.title("Choo Choo Clicker")

        self._scaling = compute_scaling(root)
        # Tk skaliert Fonts und Geometriedefaults mit diesem Faktor. Wir wenden ihn direkt an,
        # damit alle Widgets konsistent reagieren.
        self.root.tk.call("tk", "scaling", self._scaling)

        self.cell_size = max(1, round(self.BASE_CELL_SIZE * self._scaling))

        self._train_state: TrainState = self.engine.current_state()
        self._sprites: Dict[str, tk.PhotoImage] = {}
        self._sprite_sheet = SpriteSheet(self.root, sprite_sheet_path)
        self._show_grid = True
        self._camera: CameraView | None = None

        self._create_widgets()
        self._load_sprites()
        self._initialize_camera()
        self._draw_map()
        self._update_resource_display(self._train_state)

        self.engine.add_tick_listener(self._on_tick)
        self._schedule_tick()

    def _create_widgets(self) -> None:
        top_frame = tk.Frame(self.root, bg=self.BG_COLOR)
        top_frame.pack(side=tk.TOP, fill=tk.X)
        self.momentum_label = tk.Label(
            top_frame,
            text="Momentum: 0 / 0",
            font=("Arial", self._scaled_font_size(16), "bold"),
            fg="#e0e0e0",
            bg=self.BG_COLOR,
            padx=self._scaled_length(10),
            pady=self._scaled_length(10),
        )
        self.momentum_label.pack(side=tk.LEFT)

        main_frame = tk.Frame(self.root, bg=self.BG_COLOR)
        main_frame.pack(fill=tk.BOTH, expand=True)

        canvas_width = self.engine.game_map.width * self.cell_size
        canvas_height = self.engine.game_map.height * self.cell_size
        self.canvas = tk.Canvas(
            main_frame,
            width=canvas_width,
            height=canvas_height,
            bg=self.BG_COLOR,
            highlightthickness=0,
        )
        self.canvas.pack(
            side=tk.LEFT,
            padx=self._scaled_length(10),
            pady=self._scaled_length(10),
        )
        self.canvas.bind("<Button-1>", self._handle_click)

        sidebar = tk.Frame(main_frame, width=self._scaled_length(150), bg="#222433")
        sidebar.pack(side=tk.RIGHT, fill=tk.Y)

        action_label = tk.Label(
            sidebar,
            text="Aktionen",
            font=("Arial", self._scaled_font_size(14), "bold"),
            fg="#f8f8f2",
            bg="#222433",
        )
        action_label.pack(
            pady=(self._scaled_length(20), self._scaled_length(10))
        )

        push_button = tk.Button(
            sidebar,
            text="Schieben",
            command=self._push_train,
            font=("Arial", self._scaled_font_size(12), "bold"),
            bg="#3c3f58",
            fg="#f8f8f2",
            activebackground="#4e5272",
            activeforeground="#ffffff",
            width=12,
            pady=self._scaled_length(8),
        )
        push_button.pack()

    def _initialize_camera(self) -> None:
        game_map = self.engine.game_map
        viewport_size = (
            game_map.width * self.cell_size,
            game_map.height * self.cell_size,
        )
        self._camera = CameraView(
            cell_size=self.cell_size,
            map_size=(game_map.width, game_map.height),
            viewport_size=viewport_size,
        )
        self._camera.center_on(self._train_state.position)

    def _load_sprites(self) -> None:
        self._sprites = {
            "ground": self._sprite_sheet.get_tile(0, 0),
            "track_straight_ns": self._sprite_sheet.get_tile(1, 1),
            "track_straight_ew": self._sprite_sheet.get_tile(1, 1, rotation=90),
            "track_curve_ne": self._sprite_sheet.get_tile(2, 1),
            "track_curve_se": self._sprite_sheet.get_tile(2, 1, rotation=90),
            "track_curve_sw": self._sprite_sheet.get_tile(2, 1, rotation=180),
            "track_curve_nw": self._sprite_sheet.get_tile(2, 1, rotation=270),
            "track_t_north": self._sprite_sheet.get_tile(0, 1),
            "track_t_east": self._sprite_sheet.get_tile(2, 3),
            "track_t_south": self._sprite_sheet.get_tile(0, 2),
            "track_t_west": self._sprite_sheet.get_tile(1, 3),
            "track_cross": self._sprite_sheet.get_tile(0, 3),
        }

    def _draw_map(self) -> None:
        self.canvas.delete("all")
        game_map = self.engine.game_map
        for x in range(game_map.width):
            for y in range(game_map.height):
                x1 = x * self.cell_size
                y1 = y * self.cell_size
                cell = (x, y)
                self.canvas.create_image(
                    x1, y1, anchor=tk.NW, image=self._sprites["ground"]
                )
                if game_map.has_track(cell):
                    sprite_key = self._select_track_sprite(cell)
                    sprite_image = self._sprites.get(sprite_key)
                    if sprite_image is None:
                        sprite_image = self._sprites["track_straight_ns"]
                    self.canvas.create_image(
                        x1, y1, anchor=tk.NW, image=sprite_image
                    )

        if self._show_grid:
            width_px = game_map.width * self.cell_size
            height_px = game_map.height * self.cell_size
            line_width = self._scaled_line_width()
            for x in range(game_map.width + 1):
                px = x * self.cell_size
                self.canvas.create_line(
                    px,
                    0,
                    px,
                    height_px,
                    fill=self.GRID_COLOR,
                    width=line_width,
                )
            for y in range(game_map.height + 1):
                py = y * self.cell_size
                self.canvas.create_line(
                    0,
                    py,
                    width_px,
                    py,
                    fill=self.GRID_COLOR,
                    width=line_width,
                )

        tx, ty = self._train_state.position
        margin = self._scaled_length(8)
        diameter = max(1, self.cell_size - 2 * margin)
        x1 = tx * self.cell_size + margin
        y1 = ty * self.cell_size + margin
        x2 = x1 + diameter
        y2 = y1 + diameter
        self.canvas.create_oval(
            x1,
            y1,
            x2,
            y2,
            fill=self.TRAIN_COLOR,
            outline=self.TRAIN_OUTLINE,
            width=self._scaled_line_width(base=3),
        )

        if self._camera is not None:
            self._camera.apply(self.canvas)

    def _handle_click(self, event: tk.Event) -> None:  # type: ignore[type-arg]
        grid_x = event.x // self.cell_size
        grid_y = event.y // self.cell_size
        game_map = self.engine.game_map
        if 0 <= grid_x < game_map.width and 0 <= grid_y < game_map.height:
            cell = (grid_x, grid_y)
            if not game_map.has_track(cell):
                game_map.place_track(cell)
                game_map.auto_connect(cell)
                self._draw_map()

    def _push_train(self) -> None:
        state = self.engine.push_train(1)
        self._update_resource_display(state)

    def _update_resource_display(self, state: TrainState) -> None:
        self.momentum_label.config(
            text=f"Momentum: {state.momentum} / {state.max_momentum}"
        )

    def _schedule_tick(self) -> None:
        self.root.after(600, self._game_tick)

    def _game_tick(self) -> None:
        self.engine.tick()
        self._schedule_tick()

    def _on_tick(self, result: TickResult) -> None:
        self._train_state = result.train
        if result.moved:
            if self._camera is not None:
                self._camera.center_on(result.train.position)
            self._draw_map()
        self._update_resource_display(result.train)

    def _select_track_sprite(self, cell: Cell) -> str:
        piece = self.engine.game_map.get_track_piece(cell)
        if piece is None:
            return "ground"

        connections = piece.connections

        if piece.shape in {TrackShape.ISOLATED, TrackShape.DEAD_END}:
            if Direction.NORTH in connections or Direction.SOUTH in connections:
                return "track_straight_ns"
            if Direction.EAST in connections or Direction.WEST in connections:
                return "track_straight_ew"
            return "track_straight_ns"

        if piece.shape == TrackShape.STRAIGHT:
            if {Direction.NORTH, Direction.SOUTH}.issubset(connections):
                return "track_straight_ns"
            return "track_straight_ew"

        if piece.shape == TrackShape.CURVE:
            curve_map: Dict[frozenset[Direction], str] = {
                frozenset({Direction.NORTH, Direction.EAST}): "track_curve_ne",
                frozenset({Direction.EAST, Direction.SOUTH}): "track_curve_se",
                frozenset({Direction.SOUTH, Direction.WEST}): "track_curve_sw",
                frozenset({Direction.WEST, Direction.NORTH}): "track_curve_nw",
            }
            return curve_map.get(connections, "track_curve_ne")

        if piece.shape == TrackShape.T_JUNCTION:
            t_map: Dict[FrozenSet[Direction], str] = {
                frozenset({Direction.EAST, Direction.SOUTH, Direction.WEST}): "track_t_north",
                frozenset({Direction.NORTH, Direction.EAST, Direction.WEST}): "track_t_south",
                frozenset({Direction.NORTH, Direction.SOUTH, Direction.EAST}): "track_t_west",
                frozenset({Direction.NORTH, Direction.SOUTH, Direction.WEST}): "track_t_east",
            }
            return t_map.get(connections, "track_t_north")

        if piece.shape == TrackShape.CROSS:
            cross_map: Dict[FrozenSet[Direction], str] = {
                frozenset(
                    {
                        Direction.NORTH,
                        Direction.EAST,
                        Direction.SOUTH,
                        Direction.WEST,
                    }
                ): "track_cross"
            }
            return cross_map.get(connections, "track_cross")

        return "track_straight_ns"

    def _scaled_length(self, value: int | float) -> int:
        return max(1, round(float(value) * self._scaling))

    def _scaled_font_size(self, base: int) -> int:
        return max(1, round(base * self._scaling))

    def _scaled_line_width(self, *, base: int = 1) -> int:
        return max(1, round(base * self._scaling))


__all__ = ["ChooChooApp"]
