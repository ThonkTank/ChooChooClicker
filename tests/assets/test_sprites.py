"""Tests für `SpriteSheet`-Rotationen (90° = Uhrzeigersinn).

Die Tests verwenden kleine synthetische `PhotoImage`-Fallbacks, damit keine echte Tk-Instanz
notwendig ist. Dadurch lässt sich die Koordinatenannahme (x nach rechts, y nach unten) klar
überprüfen."""

from __future__ import annotations

from typing import Sequence

import pytest

from assets import sprites

from tests_support.asset_fakes import FakePhotoImage, make_sheet


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
    sheet = make_sheet(tile_size=3)
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
    sheet = make_sheet(tile_size=3)
    source = FakePhotoImage(master=None, width=3, height=3, pixels=source_pixels)

    rotated = sheet._rotate_tile(source, angle)

    assert rotated.snapshot() == [list(row) for row in expected]
    assert source.snapshot() == source_pixels  # Quelle bleibt unverändert.
