from game import GameEngine, Train
from world import Direction, GameMap


def build_linear_map(length: int = 3) -> GameMap:
    game_map = GameMap(width=length, height=1)
    for x in range(length):
        game_map.place_track((x, 0))
    for x in range(length - 1):
        current = (x, 0)
        nxt = (x + 1, 0)
        game_map.connect(current, nxt)
        game_map.connect(nxt, current)
    return game_map


def test_add_momentum_capped() -> None:
    train = Train(position=(0, 0), direction=(1, 0), max_momentum=3)
    train.add_momentum(5)
    assert train.momentum == 3


def test_try_move_advances_along_connection() -> None:
    game_map = build_linear_map()
    train = Train(position=(0, 0), direction=Direction.EAST.delta, momentum=0)
    train.add_momentum(1)
    assert train.consume_momentum() is True
    assert train.try_move(game_map) is True
    assert train.position == (1, 0)


def test_game_engine_refunds_failed_move() -> None:
    game_map = GameMap(width=2, height=1)
    game_map.place_track((0, 0))
    train = Train(position=(0, 0), direction=(1, 0), momentum=0)
    engine = GameEngine(game_map, train)
    engine.push_train(1)
    result = engine.tick()
    assert result.moved is False
    assert result.train.momentum == 1


def test_game_engine_invokes_listener() -> None:
    game_map = build_linear_map()
    train = Train(position=(0, 0), direction=(1, 0), momentum=0)
    engine = GameEngine(game_map, train)
    engine.push_train(1)

    calls = []

    def listener(result) -> None:
        calls.append(result)

    engine.add_tick_listener(listener)
    engine.tick()
    assert len(calls) == 1
    assert calls[0].moved is True
    assert calls[0].train.position == (1, 0)
