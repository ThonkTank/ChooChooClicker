"""Tkinter-Benutzeroberfläche für Choo Choo Clicker."""
from __future__ import annotations

import tkinter as tk
from pathlib import Path
from typing import Dict

from assets import SpriteSheet
from game import GameEngine, TickResult, TrainState
from world import Cell, Direction, TrackShape


class ChooChooApp:
    CELL_SIZE = 32
    BG_COLOR = "#1a1b26"
    GRID_COLOR = "#2d3143"
    TRAIN_COLOR = "#f7768e"
    TRAIN_OUTLINE = "#ff9cac"

    def __init__(self, root: tk.Tk, engine: GameEngine, sprite_sheet_path: Path) -> None:
        self.root = root
        self.engine = engine
        self.root.title("Choo Choo Clicker")

        self._train_state: TrainState = self.engine.current_state()
        self._sprites: Dict[str, tk.PhotoImage] = {}
        self._sprite_sheet = SpriteSheet(self.root, sprite_sheet_path)
        self._show_grid = True

        self._create_widgets()
        self._load_sprites()
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
            font=("Arial", 16, "bold"),
            fg="#e0e0e0",
            bg=self.BG_COLOR,
            padx=10,
            pady=10,
        )
        self.momentum_label.pack(side=tk.LEFT)

        main_frame = tk.Frame(self.root, bg=self.BG_COLOR)
        main_frame.pack(fill=tk.BOTH, expand=True)

        canvas_width = self.engine.game_map.width * self.CELL_SIZE
        canvas_height = self.engine.game_map.height * self.CELL_SIZE
        self.canvas = tk.Canvas(
            main_frame,
            width=canvas_width,
            height=canvas_height,
            bg=self.BG_COLOR,
            highlightthickness=0,
        )
        self.canvas.pack(side=tk.LEFT, padx=10, pady=10)
        self.canvas.bind("<Button-1>", self._handle_click)

        sidebar = tk.Frame(main_frame, width=150, bg="#222433")
        sidebar.pack(side=tk.RIGHT, fill=tk.Y)

        action_label = tk.Label(
            sidebar,
            text="Aktionen",
            font=("Arial", 14, "bold"),
            fg="#f8f8f2",
            bg="#222433",
        )
        action_label.pack(pady=(20, 10))

        push_button = tk.Button(
            sidebar,
            text="Schieben",
            command=self._push_train,
            font=("Arial", 12, "bold"),
            bg="#3c3f58",
            fg="#f8f8f2",
            activebackground="#4e5272",
            activeforeground="#ffffff",
            width=12,
            pady=8,
        )
        push_button.pack()

    def _load_sprites(self) -> None:
        # Tile-Koordinaten siehe Task/rendering-notes.md → „Ground-Rails-Sheet (Tile-Orientierungen)“.
        self._sprites = {
            "ground": self._sprite_sheet.get_tile(0, 0),
            "track_straight_ns": self._sprite_sheet.get_tile(1, 3),
            "track_straight_ew": self._sprite_sheet.get_tile(1, 3, rotation=90),
            "track_curve_ne": self._sprite_sheet.get_tile(1, 2),
            "track_curve_se": self._sprite_sheet.get_tile(1, 2, rotation=90),
            "track_curve_sw": self._sprite_sheet.get_tile(1, 2, rotation=180),
            "track_curve_nw": self._sprite_sheet.get_tile(1, 2, rotation=270),
        }

    def _draw_map(self) -> None:
        self.canvas.delete("all")
        game_map = self.engine.game_map
        for x in range(game_map.width):
            for y in range(game_map.height):
                x1 = x * self.CELL_SIZE
                y1 = y * self.CELL_SIZE
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
            width_px = game_map.width * self.CELL_SIZE
            height_px = game_map.height * self.CELL_SIZE
            for x in range(game_map.width + 1):
                px = x * self.CELL_SIZE
                self.canvas.create_line(
                    px, 0, px, height_px, fill=self.GRID_COLOR, width=1
                )
            for y in range(game_map.height + 1):
                py = y * self.CELL_SIZE
                self.canvas.create_line(
                    0, py, width_px, py, fill=self.GRID_COLOR, width=1
                )

        tx, ty = self._train_state.position
        x1 = tx * self.CELL_SIZE + 8
        y1 = ty * self.CELL_SIZE + 8
        x2 = x1 + self.CELL_SIZE - 16
        y2 = y1 + self.CELL_SIZE - 16
        self.canvas.create_oval(
            x1,
            y1,
            x2,
            y2,
            fill=self.TRAIN_COLOR,
            outline=self.TRAIN_OUTLINE,
            width=3,
        )

    def _handle_click(self, event: tk.Event) -> None:  # type: ignore[type-arg]
        grid_x = event.x // self.CELL_SIZE
        grid_y = event.y // self.CELL_SIZE
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

        return "track_straight_ns"


__all__ = ["ChooChooApp"]
