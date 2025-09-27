"""Tests für Bounding-Box-Messung und Offset-Anwendung im SpriteSheet."""
from __future__ import annotations

import pytest

from assets import sprites

from tests_support.asset_fakes import FakePhotoImage, make_sheet


def _build_sheet(tile_pixels: list[list[str | None]]) -> sprites.SpriteSheet:
    tile_size = len(tile_pixels)
    sheet = make_sheet(tile_size=tile_size, spacing=0)
    sheet.sheet = FakePhotoImage(master=None, width=tile_size, height=tile_size, pixels=tile_pixels)
    return sheet


@pytest.fixture
def sprite_sheet(monkeypatch: pytest.MonkeyPatch) -> sprites.SpriteSheet:
    monkeypatch.setattr(sprites, "tk", type("_FakeTkModule", (), {"PhotoImage": FakePhotoImage}))
    pixels = [
        [None, None, None, None],
        [None, None, "A1", "A2"],
        [None, None, "B1", "B2"],
        [None, None, None, None],
    ]
    return _build_sheet(pixels)


def test_measure_bounds_raw_values(sprite_sheet: sprites.SpriteSheet) -> None:
    bounds = sprite_sheet.measure_bounds(0, 0, apply_offsets=False)
    assert bounds == (2, 1, 3, 2)


def test_measure_bounds_with_offset(sprite_sheet: sprites.SpriteSheet, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setitem(sprites.SPRITE_OFFSETS, (0, 0), (-1, -1))
    bounds = sprite_sheet.measure_bounds(0, 0, apply_offsets=True)
    assert bounds == (1, 0, 2, 1)

    tile = sprite_sheet.get_tile(0, 0)
    assert tile.snapshot() == [
        [None, "A1", "A2", None],
        [None, "B1", "B2", None],
        [None, None, None, None],
        [None, None, None, None],
    ]
