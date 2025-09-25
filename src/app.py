import tkinter as tk
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

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

        self._create_widgets()
        self._draw_map()
        self._update_resource_display()
        self._schedule_tick()

    def _setup_initial_ring(self) -> None:
        w, h = self.map.width, self.map.height
        ring_cells = []
        for x in range(w):
            ring_cells.append((x, 0))
            ring_cells.append((x, h - 1))
        for y in range(1, h - 1):
            ring_cells.append((0, y))
            ring_cells.append((w - 1, y))

        unique_cells = []
        seen = set()
        for cell in ring_cells:
            if cell not in seen:
                seen.add(cell)
                unique_cells.append(cell)

        for cell in unique_cells:
            self.map.add_track(cell, None)

        # Connect the ring sequentially
        for idx, cell in enumerate(unique_cells):
            next_cell = unique_cells[(idx + 1) % len(unique_cells)]
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

    def _draw_map(self) -> None:
        self.canvas.delete("all")
        for x in range(self.map.width):
            for y in range(self.map.height):
                x1 = x * self.CELL_SIZE
                y1 = y * self.CELL_SIZE
                x2 = x1 + self.CELL_SIZE
                y2 = y1 + self.CELL_SIZE
                self.canvas.create_rectangle(
                    x1,
                    y1,
                    x2,
                    y2,
                    fill=self.BG_COLOR,
                    outline=self.GRID_COLOR,
                )
                if self.map.has_track((x, y)):
                    padding = 6
                    self.canvas.create_rectangle(
                        x1 + padding,
                        y1 + padding,
                        x2 - padding,
                        y2 - padding,
                        fill=self.TRACK_COLOR,
                        outline="",
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
