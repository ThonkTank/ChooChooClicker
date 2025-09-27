"""Gemeinsame Fake-Klassen für SpriteSheet-Tests."""
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Sequence

from assets import sprites


@dataclass
class FakeInterpreter:
    """Minimaler Ersatz für `PhotoImage.tk`, der `copy`-Operationen unterstützt."""

    def call(self, target: "FakePhotoImage", command: str, source: "FakePhotoImage", *args) -> None:
        if command != "copy":  # pragma: no cover - würde eine fehlerhafte Nutzung signalisieren.
            raise NotImplementedError(command)
        if len(args) != 8:
            raise AssertionError(f"Unerwartete Argumentlänge: {args}")
        flag_from, x1, y1, x2, y2, flag_to, tx, ty = args
        assert flag_from == "-from", "Der Tk-Befehl muss die Quelle definieren."
        assert flag_to == "-to", "Der Tk-Befehl muss das Ziel definieren."
        assert x1 <= x2 and y1 <= y2, "Koordinaten müssen eine positive Fläche beschreiben."

        width = x2 - x1 + 1
        height = y2 - y1 + 1
        for dy in range(height):
            for dx in range(width):
                target.set_pixel(tx + dx, ty + dy, source.get_pixel(x1 + dx, y1 + dy))


class FakePhotoImage:
    """Reduzierte `PhotoImage`-Implementation für Tests."""

    def __init__(self, *, master=None, width: int, height: int, pixels: Sequence[Sequence[str]] | None = None) -> None:
        self.master = master
        self.width = width
        self.height = height
        if pixels is None:
            self._pixels: List[List[str | None]] = [[None for _ in range(width)] for _ in range(height)]
        else:
            self._pixels = [list(row) for row in pixels]
        self.tk = FakeInterpreter()

    def get_pixel(self, x: int, y: int) -> str | None:
        return self._pixels[y][x]

    def set_pixel(self, x: int, y: int, value: str | None) -> None:
        self._pixels[y][x] = value

    def get(self, x: int, y: int) -> str | None:
        return self.get_pixel(x, y)

    def snapshot(self) -> List[List[str | None]]:
        """Liefert eine Kopie der aktuellen Pixelmatrix zur Validierung."""

        return [list(row) for row in self._pixels]


def make_sheet(tile_size: int, *, spacing: int = 0) -> sprites.SpriteSheet:
    sheet = sprites.SpriteSheet.__new__(sprites.SpriteSheet)
    sheet.master = object()
    sheet.tile_size = tile_size
    sheet.spacing = spacing
    sheet.tile_offset = tile_size + spacing
    sheet.sheet = None
    sheet._base_cache = {}
    sheet._rotation_cache = {}
    return sheet
