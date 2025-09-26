"""Domainmodell für die Spielfeld-Logik."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, FrozenSet, Iterable, Optional, Set, Tuple

Cell = Tuple[int, int]


class Direction(Enum):
    """Orthogonale Richtungen innerhalb des Gitters."""

    NORTH = (0, -1)
    EAST = (1, 0)
    SOUTH = (0, 1)
    WEST = (-1, 0)

    @property
    def delta(self) -> Cell:
        return self.value

    @property
    def opposite(self) -> "Direction":
        mapping = {
            Direction.NORTH: Direction.SOUTH,
            Direction.EAST: Direction.WEST,
            Direction.SOUTH: Direction.NORTH,
            Direction.WEST: Direction.EAST,
        }
        return mapping[self]

    @staticmethod
    def from_delta(delta: Cell) -> "Direction":
        for direction in Direction:
            if direction.value == delta:
                return direction
        raise ValueError(f"Delta {delta} entspricht keiner kardinalen Richtung")


class TrackShape(Enum):
    """Formklassifikation eines Schienenstücks basierend auf Verbindungen."""

    ISOLATED = auto()
    DEAD_END = auto()
    STRAIGHT = auto()
    CURVE = auto()
    T_JUNCTION = auto()
    CROSS = auto()


@dataclass(frozen=True)
class TrackPiece:
    """Beschreibt die Verbindungstopologie eines Tiles."""

    cell: Cell
    connections: FrozenSet[Direction]
    shape: TrackShape

    @classmethod
    def from_connections(cls, cell: Cell, connections: Iterable[Direction]) -> "TrackPiece":
        direction_set: FrozenSet[Direction] = frozenset(connections)
        shape = classify_shape(direction_set)
        return cls(cell=cell, connections=direction_set, shape=shape)


def classify_shape(directions: FrozenSet[Direction]) -> TrackShape:
    count = len(directions)
    if count == 0:
        return TrackShape.ISOLATED
    if count == 1:
        return TrackShape.DEAD_END
    if count == 2:
        first, second = tuple(directions)
        if first.opposite is second:
            return TrackShape.STRAIGHT
        return TrackShape.CURVE
    if count == 3:
        return TrackShape.T_JUNCTION
    if count == 4:
        return TrackShape.CROSS
    raise ValueError(f"Unbekannte Richtungsanzahl: {count}")


class GameMap:
    """Verwaltet belegte Tiles und gerichtete Verbindungen."""

    def __init__(self, *, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self._tracks: Set[Cell] = set()
        self._connections: Dict[Cell, Set[Cell]] = {}

    def in_bounds(self, cell: Cell) -> bool:
        x, y = cell
        return 0 <= x < self.width and 0 <= y < self.height

    def place_track(self, cell: Cell) -> None:
        if not self.in_bounds(cell):
            raise ValueError(f"Zelle {cell} liegt außerhalb der Karte")
        self._tracks.add(cell)
        self._connections.setdefault(cell, set())

    def remove_track(self, cell: Cell) -> None:
        if cell not in self._tracks:
            return
        self._tracks.remove(cell)
        self._connections.pop(cell, None)
        for neighbours in self._connections.values():
            neighbours.discard(cell)

    def has_track(self, cell: Cell) -> bool:
        return cell in self._tracks

    def connect(self, origin: Cell, target: Cell) -> None:
        self._validate_track(origin)
        self._validate_track(target)
        self._connections.setdefault(origin, set()).add(target)

    def disconnect(self, origin: Cell, target: Cell) -> None:
        if origin in self._connections:
            self._connections[origin].discard(target)

    def auto_connect(self, cell: Cell) -> Set[Tuple[Cell, Cell]]:
        self._validate_track(cell)
        created: Set[Tuple[Cell, Cell]] = set()
        for direction in Direction:
            dx, dy = direction.delta
            neighbour = (cell[0] + dx, cell[1] + dy)
            if not self.in_bounds(neighbour):
                continue
            if neighbour not in self._tracks:
                continue
            if neighbour not in self._connections.get(cell, set()):
                self.connect(cell, neighbour)
                created.add((cell, neighbour))
            if cell not in self._connections.get(neighbour, set()):
                self.connect(neighbour, cell)
                created.add((neighbour, cell))
        return created

    def get_connections(self, cell: Cell) -> FrozenSet[Cell]:
        return frozenset(self._connections.get(cell, set()))

    def get_track_piece(self, cell: Cell) -> Optional[TrackPiece]:
        if cell not in self._tracks:
            return None
        connections = self._connections.get(cell, set())
        directions = []
        for neighbour in connections:
            delta = (neighbour[0] - cell[0], neighbour[1] - cell[1])
            try:
                direction = Direction.from_delta(delta)
            except ValueError:
                # Nur orthogonale Verbindungen werden klassifiziert.
                continue
            directions.append(direction)
        return TrackPiece.from_connections(cell, directions)

    def iter_tracks(self) -> Iterable[Cell]:
        return iter(self._tracks.copy())

    def _validate_track(self, cell: Cell) -> None:
        if cell not in self._tracks:
            raise ValueError(f"Für {cell} ist keine Strecke platziert")


__all__ = [
    "Cell",
    "Direction",
    "GameMap",
    "TrackPiece",
    "TrackShape",
]
