"""Regressionstest für die Sprite-Auswahl entlang des vorinitialisierten Kartenrings."""
from __future__ import annotations

from types import SimpleNamespace

import pytest

from main import create_engine
from ui.app import ChooChooApp
from world import Cell, Direction, TrackPiece, TrackShape


@pytest.fixture(scope="module")
def engine():
    """Erzeugt den Standard-Enginezustand mit Ringstrecke."""

    return create_engine()


def _iter_border_cells(width: int, height: int):
    """Liefert alle Zellen am Kartenrand ohne Duplikate."""

    border: set[Cell] = set()
    for x in range(width):
        border.add((x, 0))
        border.add((x, height - 1))
    for y in range(height):
        border.add((0, y))
        border.add((width - 1, y))
    return sorted(border)


def test_track_sprite_selection_on_initial_ring(engine):
    """Alle Randzellen müssen konsistente Sprite-Keys liefern."""

    game_map = engine.game_map
    dummy_app = SimpleNamespace(engine=engine)

    expected_keys = {
        frozenset({Direction.NORTH, Direction.SOUTH}): "track_straight_ns",
        frozenset({Direction.EAST, Direction.WEST}): "track_straight_ew",
        frozenset({Direction.NORTH, Direction.EAST}): "track_curve_ne",
        frozenset({Direction.EAST, Direction.SOUTH}): "track_curve_se",
        frozenset({Direction.SOUTH, Direction.WEST}): "track_curve_sw",
        frozenset({Direction.WEST, Direction.NORTH}): "track_curve_nw",
    }

    for cell in _iter_border_cells(game_map.width, game_map.height):
        piece: TrackPiece | None = game_map.get_track_piece(cell)
        assert piece is not None, f"Randzelle {cell} sollte Teil des Rings sein"
        assert piece.shape in {TrackShape.STRAIGHT, TrackShape.CURVE}

        expected_key = expected_keys.get(piece.connections)
        assert (
            expected_key is not None
        ), f"Für die Verbindungen {piece.connections} fehlt eine Sprite-Zuordnung"

        sprite_key = ChooChooApp._select_track_sprite(dummy_app, cell)
        assert (
            sprite_key == expected_key
        ), f"Falscher Sprite-Key für {cell}: erwartet {expected_key}, erhalten {sprite_key}"
