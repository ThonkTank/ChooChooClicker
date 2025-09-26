"""Tests für `SpriteSheet`-Rotationen (90° = Uhrzeigersinn).

Die Tests verwenden kleine synthetische `PhotoImage`-Fallbacks, damit keine echte Tk-Instanz
notwendig ist. Dadurch lässt sich die Koordinatenannahme (x nach rechts, y nach unten) klar
überprüfen."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Sequence

import pytest

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
        # `_rotate_tile` kopiert immer einzelne Pixel: x1 == x2, y1 == y2.
        assert x1 == x2 and y1 == y2, "Nur Pixel-genaue Kopien werden unterstützt."
        target.set_pixel(tx, ty, source.get_pixel(x1, y1))


class FakePhotoImage:
    """Reduzierte `PhotoImage`-Implementation für Rotations-Tests."""

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

    def snapshot(self) -> List[List[str | None]]:
        """Liefert eine Kopie der aktuellen Pixelmatrix zur Validierung."""

        return [list(row) for row in self._pixels]


def _make_sheet(tile_size: int) -> sprites.SpriteSheet:
    sheet = sprites.SpriteSheet.__new__(sprites.SpriteSheet)
    sheet.master = object()
    sheet.tile_size = tile_size
    sheet.spacing = 0
    sheet.tile_offset = tile_size
    sheet.sheet = None
    sheet._base_cache = {}
    sheet._rotation_cache = {}
    return sheet


@pytest.mark.parametrize(
    ("angle", "point", "expected"),
    [
        (90, (0, 0), (2, 0)),  # 90° = Uhrzeigersinn: oben links -> oben rechts
        (90, (1, 0), (2, 1)),
        (180, (0, 0), (2, 2)),  # 180° = invertiert beide Achsen
        (180, (2, 1), (0, 1)),
        (270, (0, 0), (0, 2)),  # 270° = 90° gegen den Uhrzeigersinn
        (270, (2, 1), (1, 0)),
    ],
)
def test_rotate_point_clockwise_reference(angle: int, point: tuple[int, int], expected: tuple[int, int]) -> None:
    sheet = _make_sheet(tile_size=3)
    assert sheet._rotate_point(*point, angle) == expected


@pytest.mark.parametrize(
    ("angle", "expected"),
    [
        (
            90,
            [
                ["C1", "B1", "A1"],
                ["C2", "B2", "A2"],
                ["C3", "B3", "A3"],
            ],
        ),
        (
            180,
            [
                ["C3", "C2", "C1"],
                ["B3", "B2", "B1"],
                ["A3", "A2", "A1"],
            ],
        ),
        (
            270,
            [
                ["A3", "B3", "C3"],
                ["A2", "B2", "C2"],
                ["A1", "B1", "C1"],
            ],
        ),
    ],
)
def test_rotate_tile_matches_coordinate_assumptions(monkeypatch: pytest.MonkeyPatch, angle: int, expected: Sequence[Sequence[str]]) -> None:
    monkeypatch.setattr(sprites, "tk", type("_FakeTkModule", (), {"PhotoImage": FakePhotoImage}))
    source_pixels = [
        ["A1", "A2", "A3"],  # y = 0 (oben)
        ["B1", "B2", "B3"],
        ["C1", "C2", "C3"],  # y = 2 (unten)
    ]
    sheet = _make_sheet(tile_size=3)
    source = FakePhotoImage(master=None, width=3, height=3, pixels=source_pixels)

    rotated = sheet._rotate_tile(source, angle)

    assert rotated.snapshot() == [list(row) for row in expected]
    assert source.snapshot() == source_pixels  # Quelle bleibt unverändert.
