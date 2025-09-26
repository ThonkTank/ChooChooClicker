"""Headless Sprite-Mapping-Tests (vgl. Task/rendering-notes.md)."""
from __future__ import annotations

from types import SimpleNamespace
from typing import Iterable, Sequence

import pytest

from ui.app import ChooChooApp
from world import Direction, GameMap, TrackShape


def _build_app_with_tracks(directions: Iterable[Direction]) -> tuple[ChooChooApp, GameMap, tuple[int, int]]:
    game_map = GameMap(width=5, height=5)
    center = (2, 2)
    game_map.place_track(center)

    for direction in directions:
        dx, dy = direction.delta
        neighbour = (center[0] + dx, center[1] + dy)
        game_map.place_track(neighbour)
        game_map.connect(center, neighbour)
        game_map.connect(neighbour, center)

    app = ChooChooApp.__new__(ChooChooApp)
    app.engine = SimpleNamespace(game_map=game_map)
    return app, game_map, center


@pytest.mark.parametrize(
    ("directions", "expected_key", "expected_shape"),
    [
        ((Direction.NORTH, Direction.SOUTH), "track_straight_ns", TrackShape.STRAIGHT),
        ((Direction.EAST, Direction.WEST), "track_straight_ew", TrackShape.STRAIGHT),
        ((Direction.NORTH, Direction.EAST), "track_curve_ne", TrackShape.CURVE),
        ((Direction.EAST, Direction.SOUTH), "track_curve_se", TrackShape.CURVE),
        ((Direction.SOUTH, Direction.WEST), "track_curve_sw", TrackShape.CURVE),
        ((Direction.WEST, Direction.NORTH), "track_curve_nw", TrackShape.CURVE),
    ],
)
def test_sprite_key_matches_game_map_connections(
    directions: Sequence[Direction], expected_key: str, expected_shape: TrackShape
) -> None:
    app, game_map, cell = _build_app_with_tracks(directions)

    piece = game_map.get_track_piece(cell)
    assert piece is not None
    assert piece.connections == frozenset(directions)
    assert piece.shape == expected_shape

    sprite_key = app._select_track_sprite(cell)
    assert sprite_key == expected_key
