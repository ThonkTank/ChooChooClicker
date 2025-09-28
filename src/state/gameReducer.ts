import {
  Coordinate,
  Direction,
  GameState,
  GridDimensions,
  IntersectionTrack,
  MOMENTUM_MAX,
  TrackPiece,
} from "./gameTypes";

export type GameAction =
  | { type: "addMomentum"; amount: number }
  | { type: "consumeMomentum"; amount: number }
  | { type: "setMomentum"; value: number }
  | { type: "placeTrack"; coordinate: Coordinate; track: TrackPiece }
  | { type: "removeTrack"; coordinate: Coordinate }
  | { type: "setSwitch"; coordinate: Coordinate; entry: Direction; exit: Direction }
  | { type: "setTrainPosition"; position: Coordinate; facing?: Direction };

export const DEFAULT_GRID_DIMENSIONS: GridDimensions = { width: 12, height: 12 };

export function coordinateToKey({ x, y }: Coordinate): string {
  return `${x},${y}`;
}

function isWithinGrid(coordinate: Coordinate, dimensions: GridDimensions): boolean {
  return (
    coordinate.x >= 0 &&
    coordinate.y >= 0 &&
    coordinate.x < dimensions.width &&
    coordinate.y < dimensions.height
  );
}

export function createInitialGameState(
  dimensions: GridDimensions = DEFAULT_GRID_DIMENSIONS,
): GameState {
  return {
    dimensions,
    tracks: {},
    momentum: {
      current: 0,
      max: MOMENTUM_MAX,
    },
    train: {
      position: {
        x: Math.floor(dimensions.width / 2),
        y: Math.floor(dimensions.height / 2),
      },
      facing: "east",
      status: "idle",
    },
  };
}

function ensurePositiveAmount(amount: number, action: string) {
  if (amount < 0) {
    throw new Error(`${action} requires a non-negative amount`);
  }
}

export function gameReducer(state: GameState, action: GameAction): GameState {
  switch (action.type) {
    case "addMomentum": {
      ensurePositiveAmount(action.amount, "addMomentum");
      const next = Math.min(state.momentum.current + action.amount, state.momentum.max);
      if (next === state.momentum.current) {
        return state;
      }
      return {
        ...state,
        momentum: {
          ...state.momentum,
          current: next,
        },
      };
    }
    case "consumeMomentum": {
      ensurePositiveAmount(action.amount, "consumeMomentum");
      if (action.amount > state.momentum.current) {
        throw new Error("Cannot consume more momentum than currently available");
      }
      return {
        ...state,
        momentum: {
          ...state.momentum,
          current: state.momentum.current - action.amount,
        },
      };
    }
    case "setMomentum": {
      const value = Math.max(0, Math.min(action.value, state.momentum.max));
      if (value === state.momentum.current) {
        return state;
      }
      return {
        ...state,
        momentum: {
          ...state.momentum,
          current: value,
        },
      };
    }
    case "placeTrack": {
      if (!isWithinGrid(action.coordinate, state.dimensions)) {
        throw new Error("Cannot place track outside of the grid bounds");
      }
      const key = coordinateToKey(action.coordinate);
      return {
        ...state,
        tracks: {
          ...state.tracks,
          [key]: action.track,
        },
      };
    }
    case "removeTrack": {
      const key = coordinateToKey(action.coordinate);
      if (!state.tracks[key]) {
        return state;
      }
      const { [key]: _removed, ...rest } = state.tracks;
      return {
        ...state,
        tracks: rest,
      };
    }
    case "setSwitch": {
      const key = coordinateToKey(action.coordinate);
      const track = state.tracks[key];
      if (!track) {
        throw new Error("Cannot set switch for a missing track");
      }
      if (track.type !== "intersection") {
        throw new Error("Switches can only be updated on intersection tracks");
      }
      const intersection: IntersectionTrack = {
        ...track,
        switches: {
          ...track.switches,
          [action.entry]: action.exit,
        },
      };
      return {
        ...state,
        tracks: {
          ...state.tracks,
          [key]: intersection,
        },
      };
    }
    case "setTrainPosition": {
      if (!isWithinGrid(action.position, state.dimensions)) {
        throw new Error("Cannot move train outside of the grid bounds");
      }
      return {
        ...state,
        train: {
          ...state.train,
          position: action.position,
          facing: action.facing ?? state.train.facing,
          status: "moving",
        },
      };
    }
    default: {
      const exhaustive: never = action;
      return exhaustive;
    }
  }
}
