import pytest

from world import Direction, GameMap, TrackShape


@pytest.fixture
def empty_map() -> GameMap:
    return GameMap(width=5, height=5)


def test_track_piece_dead_end_supports_single_direction(empty_map: GameMap) -> None:
    start = (2, 2)
    neighbour = (2, 3)
    empty_map.place_track(start)
    empty_map.place_track(neighbour)
    empty_map.connect(start, neighbour)

    piece = empty_map.get_track_piece(start)
    assert piece is not None
    assert piece.shape == TrackShape.DEAD_END
    assert piece.connections == frozenset({Direction.SOUTH})


def test_track_piece_t_junction_via_auto_connect(empty_map: GameMap) -> None:
    center = (2, 2)
    north = (2, 1)
    south = (2, 3)
    east = (3, 2)

    for cell in [center, north, south, east]:
        empty_map.place_track(cell)
    empty_map.auto_connect(center)

    piece = empty_map.get_track_piece(center)
    assert piece is not None
    assert piece.shape == TrackShape.T_JUNCTION
    assert piece.connections == frozenset({Direction.NORTH, Direction.SOUTH, Direction.EAST})


def test_track_piece_crossroads_detected(empty_map: GameMap) -> None:
    center = (2, 2)
    neighbours = [(2, 1), (2, 3), (3, 2), (1, 2)]

    empty_map.place_track(center)
    for cell in neighbours:
        empty_map.place_track(cell)
    empty_map.auto_connect(center)

    piece = empty_map.get_track_piece(center)
    assert piece is not None
    assert piece.shape == TrackShape.CROSS
    assert piece.connections == frozenset(
        {Direction.NORTH, Direction.SOUTH, Direction.EAST, Direction.WEST}
    )
