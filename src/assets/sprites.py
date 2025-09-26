"""Asset-Handling für Sprite-Sheets inkl. Caching."""
from __future__ import annotations

from pathlib import Path
from typing import Dict, Tuple

import tkinter as tk


TileKey = Tuple[int, int, int]


class SpriteSheet:
    """Lädt Tiles aus einem Sprite-Sheet und cached Rotationen."""

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
        self._base_cache: Dict[Tuple[int, int], tk.PhotoImage] = {}
        self._rotation_cache: Dict[TileKey, tk.PhotoImage] = {}

    def get_tile(self, column: int, row: int, *, rotation: int = 0) -> tk.PhotoImage:
        key = (column, row, rotation % 360)
        if key in self._rotation_cache:
            return self._rotation_cache[key]

        base = self._get_base_tile(column, row)
        if key[2] == 0:
            self._rotation_cache[key] = base
            return base

        rotated = self._rotate_tile(base, key[2])
        self._rotation_cache[key] = rotated
        return rotated

    def _get_base_tile(self, column: int, row: int) -> tk.PhotoImage:
        base_key = (column, row)
        if base_key in self._base_cache:
            return self._base_cache[base_key]
        x1 = column * self.tile_offset
        y1 = row * self.tile_offset
        x2 = x1 + self.tile_size - 1
        y2 = y1 + self.tile_size - 1
        tile = tk.PhotoImage(master=self.master, width=self.tile_size, height=self.tile_size)
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
        self._base_cache[base_key] = tile
        return tile

    def _rotate_tile(self, source: tk.PhotoImage, angle: int) -> tk.PhotoImage:
        normalized = angle % 360
        if normalized not in {90, 180, 270}:
            raise ValueError(f"Unsupported rotation angle: {angle}")
        rotated = tk.PhotoImage(master=self.master, width=self.tile_size, height=self.tile_size)
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
        # Bildschirmkoordinaten wachsen nach rechts (x) und nach unten (y).
        # Dementsprechend entspricht eine positive 90°-Rotation einer Drehung im Uhrzeigersinn.
        if angle == 90:
            return max_index - y, x
        if angle == 180:
            return max_index - x, max_index - y
        if angle == 270:
            return y, max_index - x
        raise ValueError(f"Unsupported rotation angle: {angle}")


__all__ = ["SpriteSheet"]
