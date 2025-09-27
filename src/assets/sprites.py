"""Asset-Handling für Sprite-Sheets inkl. Caching."""
from __future__ import annotations

from pathlib import Path
from typing import Dict, Iterable, Tuple

import tkinter as tk


TileKey = Tuple[int, int, int]

# Manuell kalibrierte Offsets, die die Bounding-Box auf die Tile-Mitte zentrieren.
#
# Die Messung basiert auf `SpriteSheet.measure_bounds(..., apply_offsets=False)`
# für die Sprites in `Ground-Rails.png`. Positive Werte verschieben den sichtbaren
# Inhalt nach rechts/unten, negative Werte nach links/oben.
SPRITE_OFFSETS: Dict[Tuple[int, int], Tuple[int, int]] = {
    # Straight segments (north/south orientiert im Sheet)
    (0, 1): (0, -8),
    (1, 1): (-8, -8),
    (2, 1): (8, -8),
    (3, 1): (0, -8),
    # Curves
    (0, 2): (0, 8),
    (1, 2): (-8, 8),
    (2, 2): (8, 8),
    (3, 2): (0, 8),
    # Junction caps (T- und Kreuzungs-Segmente)
    (1, 3): (-8, 0),
    (2, 3): (8, 0),
}


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
        tile = self._copy_tile(column, row, x1, y1, x2, y2)

        dx, dy = self._offset_for(column, row)
        if dx or dy:
            tile = self._apply_offset(tile, dx, dy)

        self._base_cache[base_key] = tile
        return tile

    def measure_bounds(
        self,
        column: int,
        row: int,
        *,
        apply_offsets: bool = True,
    ) -> Tuple[int, int, int, int] | None:
        """Ermittelt die Bounding-Box der nicht-transparenten Pixel eines Tiles.

        Args:
            column: Spaltenindex im Sprite-Sheet.
            row: Zeilenindex im Sprite-Sheet.
            apply_offsets: Ob manuelle Offsets angewendet werden sollen.

        Returns:
            `(min_x, min_y, max_x, max_y)` relativ zum Tile oder `None`, wenn
            das Tile vollständig transparent ist.
        """

        base = self._copy_tile(column, row)
        if apply_offsets:
            dx, dy = self._offset_for(column, row)
            if dx or dy:
                base = self._apply_offset(base, dx, dy)

        min_x = self.tile_size
        min_y = self.tile_size
        max_x = -1
        max_y = -1

        for y in range(self.tile_size):
            for x in range(self.tile_size):
                if not self._is_transparent(base, x, y):
                    if x < min_x:
                        min_x = x
                    if y < min_y:
                        min_y = y
                    if x > max_x:
                        max_x = x
                    if y > max_y:
                        max_y = y

        if max_x < 0:
            return None
        return min_x, min_y, max_x, max_y

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

    def _copy_tile(
        self,
        column: int,
        row: int,
        x1: int | None = None,
        y1: int | None = None,
        x2: int | None = None,
        y2: int | None = None,
    ) -> tk.PhotoImage:
        if x1 is None or y1 is None or x2 is None or y2 is None:
            x1, y1, x2, y2 = self._tile_bounds(column, row)
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
        return tile

    def _tile_bounds(self, column: int, row: int) -> Tuple[int, int, int, int]:
        x1 = column * self.tile_offset
        y1 = row * self.tile_offset
        x2 = x1 + self.tile_size - 1
        y2 = y1 + self.tile_size - 1
        return x1, y1, x2, y2

    def _offset_for(self, column: int, row: int) -> Tuple[int, int]:
        return SPRITE_OFFSETS.get((column, row), (0, 0))

    def _apply_offset(self, source: tk.PhotoImage, dx: int, dy: int) -> tk.PhotoImage:
        target = tk.PhotoImage(master=self.master, width=self.tile_size, height=self.tile_size)

        src_x1 = max(0, -dx)
        src_y1 = max(0, -dy)
        src_x2 = min(self.tile_size, self.tile_size - dx)
        src_y2 = min(self.tile_size, self.tile_size - dy)
        dst_x = max(0, dx)
        dst_y = max(0, dy)

        if src_x1 >= src_x2 or src_y1 >= src_y2:
            return target

        target.tk.call(
            target,
            "copy",
            source,
            "-from",
            src_x1,
            src_y1,
            src_x2 - 1,
            src_y2 - 1,
            "-to",
            dst_x,
            dst_y,
        )
        return target

    def _is_transparent(self, image: tk.PhotoImage, x: int, y: int) -> bool:
        value = self._read_pixel(image, x, y)
        if value is None:
            return True
        if isinstance(value, str):
            normalized = value.strip().lower()
            if not normalized or normalized == "transparent" or normalized == "{}":
                return True
            if normalized.startswith("#") and len(normalized) == 9 and normalized.endswith("00"):
                return True
            parts = normalized.split()
            if len(parts) == 4 and parts[-1] == "0":
                return True
            return False
        if isinstance(value, Iterable):
            seq = list(value)
            if len(seq) == 4:
                return seq[3] == 0
            return False
        if isinstance(value, int):
            return value == 0
        return False

    def _read_pixel(self, image: tk.PhotoImage, x: int, y: int):
        if hasattr(image, "get_pixel"):
            return image.get_pixel(x, y)
        getter = getattr(image, "get", None)
        if callable(getter):
            return getter(x, y)
        tk_interp = getattr(image, "tk", None)
        if tk_interp is None:
            raise AttributeError("Image does not expose pixel access APIs")
        try:
            return tk_interp.call(image, "get", x, y)
        except tk.TclError:
            return tk_interp.call("image", "get", str(image), x, y)


__all__ = ["SpriteSheet"]
