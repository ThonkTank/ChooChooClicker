"""Spielmechaniken rund um den Zug und den Tick-Zyklus."""
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Protocol

from world import Cell, GameMap


Vector = Cell


@dataclass(frozen=True)
class TrainState:
    """Momentaufnahme der Zugparameter für Rendering und UI."""

    position: Cell
    direction: Vector
    momentum: int
    max_momentum: int


class TickListener(Protocol):
    """Interface für UI- oder Logging-Schichten."""

    def __call__(self, tick_result: "TickResult") -> None:  # pragma: no cover - protocol
        ...


@dataclass
class Train:
    """Zugmodell mit Momentum- und Bewegungslogik."""

    position: Cell
    direction: Vector
    momentum: int = 0
    max_momentum: int = 10

    def add_momentum(self, amount: int = 1) -> None:
        """Erhöht den Momentum-Speicher bis zum konfigurierten Maximum."""

        self.momentum = min(self.max_momentum, self.momentum + amount)

    def consume_momentum(self) -> bool:
        """Verbraucht eine Momentum-Einheit, sofern verfügbar."""

        if self.momentum <= 0:
            return False
        self.momentum -= 1
        return True

    def try_move(self, game_map: GameMap) -> bool:
        """Versucht, entlang vorhandener Verbindungen eine Zelle voranzurücken."""

        current = self.position
        dx, dy = self.direction
        next_cell = (current[0] + dx, current[1] + dy)
        connections = game_map.get_connections(current)
        if next_cell in connections:
            self.position = next_cell
            return True

        previous_cell = (current[0] - dx, current[1] - dy)
        for neighbour in connections:
            if neighbour == previous_cell:
                continue
            self.direction = (
                neighbour[0] - current[0],
                neighbour[1] - current[1],
            )
            self.position = neighbour
            return True
        return False

    def snapshot(self) -> TrainState:
        """Erzeugt eine unveränderliche Momentaufnahme."""

        return TrainState(
            position=self.position,
            direction=self.direction,
            momentum=self.momentum,
            max_momentum=self.max_momentum,
        )


@dataclass(frozen=True)
class TickResult:
    """Datentransferobjekt für Tick-Listener."""

    train: TrainState
    moved: bool


class GameEngine:
    """Koordiniert Momentum-Verbrauch, Bewegung und Tick-Events."""

    def __init__(self, game_map: GameMap, train: Train) -> None:
        self._map = game_map
        self._train = train
        self._listeners: List[TickListener] = []

    @property
    def game_map(self) -> GameMap:
        return self._map

    def add_tick_listener(self, listener: TickListener) -> None:
        self._listeners.append(listener)

    def remove_tick_listener(self, listener: TickListener) -> None:
        self._listeners = [cb for cb in self._listeners if cb is not listener]

    def current_state(self) -> TrainState:
        return self._train.snapshot()

    def push_train(self, amount: int = 1) -> TrainState:
        self._train.add_momentum(amount)
        state = self._train.snapshot()
        return state

    def tick(self) -> TickResult:
        moved = False
        if self._train.consume_momentum():
            moved = self._train.try_move(self._map)
            if not moved:
                # Bewegung fehlgeschlagen → Momentum zurückgeben, um Verlust zu vermeiden.
                self._train.add_momentum()
        result = TickResult(train=self._train.snapshot(), moved=moved)
        for listener in list(self._listeners):
            listener(result)
        return result


__all__ = ["GameEngine", "TickResult", "Train", "TrainState"]
