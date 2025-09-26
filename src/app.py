import tkinter as tk
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, FrozenSet, List, Optional, Tuple

Cell = Tuple[int, int]


@dataclass
class Train:
    position: Cell
    direction: Cell
    momentum: int = 0
    max_momentum: int = 10

    def add_momentum(self, amount: int = 1) -> None:
        self.momentum = min(self.max_momentum, self.momentum + amount)

    def consume_momentum(self) -> bool:
        if self.momentum <= 0:
            return False
        self.momentum -= 1
        return True


@dataclass
class GameMap:
    width: int
    height: int
    tracks: Dict[Cell, List[Cell]] = field(default_factory=dict)

    def __post_init__(self) -> None:
        for x in range(self.width):
            for y in range(self.height):
                self.tracks.setdefault((x, y), [])

    def add_track(self, a: Cell, b: Optional[Cell] = None) -> None:
        if b is None:
            self.tracks[a] = self._neighbours(a)
            return
        self.tracks.setdefault(a, [])
        self.tracks.setdefault(b, [])
        if b not in self.tracks[a]:
            self.tracks[a].append(b)
        if a not in self.tracks[b]:
            self.tracks[b].append(a)

    def has_track(self, cell: Cell) -> bool:
        return len(self.tracks.get(cell, [])) > 0

    def _neighbours(self, cell: Cell) -> List[Cell]:
        x, y = cell
        neighbours: List[Cell] = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height and self.has_track((nx, ny)):
                neighbours.append((nx, ny))
        return neighbours


class SpriteSheetLoader:
    def __init__(
        self,
        master: tk.Misc,
        image_path: Path,
        *,
        tile_size: int = 32,
        spacing: int = 16,
    ) -> None:
        self.master = master
        self.tile_size = tile_size
        self.spacing = spacing
        self.tile_offset = tile_size + spacing
        self.sheet = tk.PhotoImage(master=self.master, file=str(image_path))

    def get_tile(self, column: int, row: int) -> tk.PhotoImage:
        x1 = column * self.tile_offset
        y1 = row * self.tile_offset
        x2 = x1 + self.tile_size - 1
        y2 = y1 + self.tile_size - 1
        tile = tk.PhotoImage(
            master=self.master, width=self.tile_size, height=self.tile_size
        )
        tile.tk.call(
            tile,
            "copy",
            self.sheet,
            "-from",
            x1,
            y1,
            x2,
            y2,
            "-to",
            0,
            0,
        )
        return tile

    def rotate_tile(self, source: tk.PhotoImage, angle: int) -> tk.PhotoImage:
        normalized = angle % 360
        if normalized == 0:
            return source
        rotated = tk.PhotoImage(
            master=self.master, width=self.tile_size, height=self.tile_size
        )
        for x in range(self.tile_size):
            for y in range(self.tile_size):
                nx, ny = self._rotate_point(x, y, normalized)
                rotated.tk.call(
                    rotated,
                    "copy",
                    source,
                    "-from",
                    x,
                    y,
                    x,
                    y,
                    "-to",
                    nx,
                    ny,
                )
        return rotated

    def _rotate_point(self, x: int, y: int, angle: int) -> Tuple[int, int]:
        max_index = self.tile_size - 1
        if angle == 90:
            return max_index - y, x
        if angle == 180:
            return max_index - x, max_index - y
        if angle == 270:
            return y, max_index - x
        raise ValueError(f"Unsupported rotation angle: {angle}")


class ChooChooClicker:
    CELL_SIZE = 32
    BG_COLOR = "#1a1b26"
    GRID_COLOR = "#2d3143"
    TRACK_COLOR = "#c9b458"
    TRAIN_COLOR = "#f7768e"
    TRAIN_OUTLINE = "#ff9cac"

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Choo Choo Clicker")

        self.map = GameMap(width=12, height=12)
        self.train = Train(position=(0, 0), direction=(1, 0))
        self._setup_initial_ring()
        self.train.position = (0, 0)

        self.sprites: Dict[str, tk.PhotoImage] = {}
        self.show_grid = True
        self._load_sprites()

        self._create_widgets()
        self._draw_map()
        self._update_resource_display()
        self._schedule_tick()

    def _setup_initial_ring(self) -> None:
        w, h = self.map.width, self.map.height
        ring_cells = []

        # Top edge: left to right
        for x in range(w):
            ring_cells.append((x, 0))

        # Right edge: top to bottom (excluding the top corner already added)
        for y in range(1, h):
            ring_cells.append((w - 1, y))

        # Bottom edge: right to left (excluding the bottom-right corner already added)
        if h > 1:
            for x in range(w - 2, -1, -1):
                ring_cells.append((x, h - 1))

        # Left edge: bottom to top (excluding the corners already added)
        if w > 1:
            for y in range(h - 2, 0, -1):
                ring_cells.append((0, y))

        for cell in ring_cells:
            self.map.add_track(cell, None)

        # Connect the ring sequentially
        for idx, cell in enumerate(ring_cells):
            next_cell = ring_cells[(idx + 1) % len(ring_cells)]
            self.map.add_track(cell, next_cell)

    def _create_widgets(self) -> None:
        top_frame = tk.Frame(self.root, bg=self.BG_COLOR)
        top_frame.pack(side=tk.TOP, fill=tk.X)
        self.momentum_label = tk.Label(
            top_frame,
            text="Momentum: 0 / 10",
            font=("Arial", 16, "bold"),
            fg="#e0e0e0",
            bg=self.BG_COLOR,
            padx=10,
            pady=10,
        )
        self.momentum_label.pack(side=tk.LEFT)

        main_frame = tk.Frame(self.root, bg=self.BG_COLOR)
        main_frame.pack(fill=tk.BOTH, expand=True)

        canvas_width = self.map.width * self.CELL_SIZE
        canvas_height = self.map.height * self.CELL_SIZE
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
        sprite_path = Path(__file__).resolve().parent.parent / "Ground-Rails.png"
        loader = SpriteSheetLoader(self.root, sprite_path)
        ground = loader.get_tile(0, 0)
        straight_ns = loader.get_tile(1, 1)
        straight_ew = loader.rotate_tile(straight_ns, 90)
        curve_ne = loader.get_tile(2, 1)
        curve_se = loader.rotate_tile(curve_ne, 90)
        curve_sw = loader.rotate_tile(curve_ne, 180)
        curve_nw = loader.rotate_tile(curve_ne, 270)
        self.sprites = {
            "ground": ground,
            "track_straight_ns": straight_ns,
            "track_straight_ew": straight_ew,
            "track_curve_ne": curve_ne,
            "track_curve_se": curve_se,
            "track_curve_sw": curve_sw,
            "track_curve_nw": curve_nw,
        }

    def _draw_map(self) -> None:
        self.canvas.delete("all")
        for x in range(self.map.width):
            for y in range(self.map.height):
                x1 = x * self.CELL_SIZE
                y1 = y * self.CELL_SIZE
                cell = (x, y)
                self.canvas.create_image(
                    x1, y1, anchor=tk.NW, image=self.sprites["ground"]
                )
                if self.map.has_track(cell):
                    sprite_key = self._select_track_sprite(cell)
                    sprite_image = self.sprites.get(sprite_key)
                    if sprite_image is None:
                        sprite_image = self.sprites["track_straight_ns"]
                    self.canvas.create_image(
                        x1, y1, anchor=tk.NW, image=sprite_image
                    )

        if self.show_grid:
            width_px = self.map.width * self.CELL_SIZE
            height_px = self.map.height * self.CELL_SIZE
            for x in range(self.map.width + 1):
                px = x * self.CELL_SIZE
                self.canvas.create_line(
                    px, 0, px, height_px, fill=self.GRID_COLOR, width=1
                )
            for y in range(self.map.height + 1):
                py = y * self.CELL_SIZE
                self.canvas.create_line(
                    0, py, width_px, py, fill=self.GRID_COLOR, width=1
                )

        tx, ty = self.train.position
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
        if 0 <= grid_x < self.map.width and 0 <= grid_y < self.map.height:
            cell = (grid_x, grid_y)
            if not self.map.has_track(cell):
                self.map.add_track(cell, None)
                for neighbour in self.map._neighbours(cell):
                    self.map.add_track(cell, neighbour)
                self._draw_map()

    def _push_train(self) -> None:
        self.train.add_momentum(1)
        self._update_resource_display()

    def _update_resource_display(self) -> None:
        self.momentum_label.config(
            text=f"Momentum: {self.train.momentum} / {self.train.max_momentum}"
        )

    def _schedule_tick(self) -> None:
        self.root.after(600, self._game_tick)

    def _game_tick(self) -> None:
        moved = False
        if self.train.consume_momentum():
            moved = self._attempt_move()
            if not moved:
                # refund momentum if movement failed
                self.train.add_momentum()
        if moved:
            self._draw_map()
        self._update_resource_display()
        self._schedule_tick()

    def _select_track_sprite(self, cell: Cell) -> str:
        neighbours = self.map.tracks.get(cell, [])
        vectors = {
            (nx - cell[0], ny - cell[1])
            for nx, ny in neighbours
            if (nx, ny) != cell
        }

        if len(vectors) <= 1:
            if vectors:
                dx, dy = next(iter(vectors))
                return "track_straight_ew" if dx != 0 else "track_straight_ns"
            return "ground"

        if len(vectors) > 2:
            # Placeholder until junction sprites are available
            return "track_straight_ns"

        vec_list = list(vectors)
        first, second = vec_list
        if first == (-second[0], -second[1]):
            return "track_straight_ns" if first[0] == 0 else "track_straight_ew"

        direction_set = frozenset(vectors)
        curve_map: Dict[FrozenSet[Cell], str] = {
            frozenset({(0, -1), (1, 0)}): "track_curve_ne",
            frozenset({(1, 0), (0, 1)}): "track_curve_se",
            frozenset({(0, 1), (-1, 0)}): "track_curve_sw",
            frozenset({(-1, 0), (0, -1)}): "track_curve_nw",
        }
        return curve_map.get(direction_set, "track_straight_ns")

    def _attempt_move(self) -> bool:
        current = self.train.position
        dx, dy = self.train.direction
        next_cell = (current[0] + dx, current[1] + dy)
        if next_cell in self.map.tracks.get(current, []):
            self.train.position = next_cell
            return True

        # Try to choose a new direction if blocked
        for neighbour in self.map.tracks.get(current, []):
            if neighbour != (current[0] - dx, current[1] - dy):
                self.train.direction = (
                    neighbour[0] - current[0],
                    neighbour[1] - current[1],
                )
                self.train.position = neighbour
                return True
        return False


def main() -> None:
    root = tk.Tk()
    app = ChooChooClicker(root)
    root.mainloop()


if __name__ == "__main__":
    main()
