from main import create_engine
from game import Train
from world import Direction, GameMap


def test_initial_ring_tracks_cover_perimeter() -> None:
    engine = create_engine(width=4, height=3)
    game_map = engine.game_map
    expected = {
        (0, 0), (1, 0), (2, 0), (3, 0),
        (3, 1), (3, 2),
        (2, 2), (1, 2), (0, 2),
        (0, 1),
    }
    assert set(game_map.iter_tracks()) == expected
    for cell in expected:
        connections = game_map.get_connections(cell)
        assert connections, f"Cell {cell} should be connected in ring"


def test_auto_connect_and_train_logic_integration() -> None:
    game_map = GameMap(width=3, height=3)
    for cell in [(1, 1), (2, 1), (1, 2)]:
        game_map.place_track(cell)
    for cell in [(1, 1), (2, 1), (1, 2)]:
        game_map.auto_connect(cell)

    train = Train(position=(1, 1), direction=Direction.NORTH.delta, momentum=1)
    assert train.consume_momentum() is True
    moved = train.try_move(game_map)
    assert moved is True
    assert train.position == (2, 1)
    assert train.direction == Direction.EAST.delta
