"""Einstiegspunkt und Komposition der Anwendung."""
from __future__ import annotations

from pathlib import Path
import tkinter as tk

from game import GameEngine, Train
from ui import ChooChooApp
from world import Cell, GameMap


def _build_initial_ring(game_map: GameMap) -> None:
    """Platziert eine geschlossene Ringstrecke entlang des Kartenrandes."""

    w, h = game_map.width, game_map.height
    ring_cells: list[Cell] = []

    for x in range(w):
        ring_cells.append((x, 0))
    for y in range(1, h):
        ring_cells.append((w - 1, y))
    if h > 1:
        for x in range(w - 2, -1, -1):
            ring_cells.append((x, h - 1))
    if w > 1:
        for y in range(h - 2, 0, -1):
            ring_cells.append((0, y))

    for cell in ring_cells:
        game_map.place_track(cell)

    for idx, cell in enumerate(ring_cells):
        next_cell = ring_cells[(idx + 1) % len(ring_cells)]
        game_map.connect(cell, next_cell)
        game_map.connect(next_cell, cell)


def create_engine(*, width: int = 12, height: int = 12) -> GameEngine:
    """Erzeugt `GameEngine` mit Standardkarte und Zug."""

    game_map = GameMap(width=width, height=height)
    _build_initial_ring(game_map)
    train = Train(position=(0, 0), direction=(1, 0))
    return GameEngine(game_map, train)


def main() -> None:
    root = tk.Tk()
    engine = create_engine()
    sprite_path = Path(__file__).resolve().parent.parent / "Ground-Rails.png"
    _app = ChooChooApp(root, engine, sprite_path)
    root.mainloop()


if __name__ == "__main__":
    main()
