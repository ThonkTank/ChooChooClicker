"""Regressionstest für die Sprite-Auswahl entlang des vorinitialisierten Kartenrings."""
from __future__ import annotations

from types import SimpleNamespace

import pytest

from main import create_engine
from ui.app import ChooChooApp
from world import Cell, Direction, GameMap, TrackPiece, TrackShape


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


def _build_test_app(center: Cell, directions: set[Direction]) -> SimpleNamespace:
    """Erzeugt eine Dummy-App mit gezielten Gleisverbindungen um `center`."""

    game_map = GameMap(width=5, height=5)
    cells = {center}
    for direction in directions:
        dx, dy = direction.delta
        neighbour = (center[0] + dx, center[1] + dy)
        game_map.place_track(neighbour)
        cells.add(neighbour)
    game_map.place_track(center)
    for cell in cells:
        game_map.auto_connect(cell)
    engine_stub = SimpleNamespace(game_map=game_map)
    return SimpleNamespace(engine=engine_stub)


@pytest.mark.parametrize(
    "directions, expected_key",
    [
        ({Direction.EAST, Direction.SOUTH, Direction.WEST}, "track_t_north"),
        ({Direction.NORTH, Direction.EAST, Direction.WEST}, "track_t_south"),
        ({Direction.NORTH, Direction.SOUTH, Direction.EAST}, "track_t_west"),
        ({Direction.NORTH, Direction.SOUTH, Direction.WEST}, "track_t_east"),
    ],
)
def test_track_sprite_selection_for_t_junctions(directions, expected_key):
    """Alle Richtungsvarianten der T-Kreuzung nutzen die dokumentierten Sprite-Keys."""

    center = (2, 2)
    dummy_app = _build_test_app(center, set(directions))
    sprite_key = ChooChooApp._select_track_sprite(dummy_app, center)
    assert (
        sprite_key == expected_key
    ), f"Erwarteter Key {expected_key} für Richtungen {directions}, erhalten {sprite_key}"


def test_track_sprite_selection_for_cross():
    """Eine 4-Wege-Kreuzung wird auf den spezifischen Kreuzungs-Sprite gemappt."""

    center = (2, 2)
    directions = {Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST}
    dummy_app = _build_test_app(center, directions)
    sprite_key = ChooChooApp._select_track_sprite(dummy_app, center)
    assert (
        sprite_key == "track_cross"
    ), f"Kreuzung sollte 'track_cross' liefern, erhalten {sprite_key}"
