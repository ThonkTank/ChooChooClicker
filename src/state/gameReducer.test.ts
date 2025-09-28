import { describe, expect, it } from "vitest";
import { IntersectionTrack, MOMENTUM_MAX, TrackPiece } from "./gameTypes";
import {
  coordinateToKey,
  createInitialGameState,
  gameReducer,
  GameAction,
} from "./gameReducer";

function dispatch(state = createInitialGameState(), action: GameAction) {
  return gameReducer(state, action);
}

describe("gameReducer", () => {
  it("creates an initial state with defaults", () => {
    const state = createInitialGameState({ width: 8, height: 6 });
    expect(state.dimensions).toEqual({ width: 8, height: 6 });
    expect(state.momentum).toEqual({ current: 0, max: MOMENTUM_MAX });
    expect(state.tracks).toEqual({});
    expect(state.train.position.x).toBeGreaterThanOrEqual(0);
    expect(state.train.position.y).toBeGreaterThanOrEqual(0);
  });

  it("increases momentum up to the maximum", () => {
    const state = createInitialGameState();
    const next = dispatch(state, { type: "addMomentum", amount: MOMENTUM_MAX + 5 });
    expect(next.momentum.current).toBe(MOMENTUM_MAX);
  });

  it("throws when consuming more momentum than available", () => {
    const state = createInitialGameState();
    expect(() => dispatch(state, { type: "consumeMomentum", amount: 1 })).toThrow();
  });

  it("places and removes tracks on the grid", () => {
    const state = createInitialGameState({ width: 4, height: 4 });
    const coordinate = { x: 1, y: 1 };
    const track: TrackPiece = { type: "straight", connections: ["east", "west"] };

    const withTrack = dispatch(state, { type: "placeTrack", coordinate, track });
    const key = coordinateToKey(coordinate);
    expect(withTrack.tracks[key]).toEqual(track);

    const removed = dispatch(withTrack, { type: "removeTrack", coordinate });
    expect(removed.tracks[key]).toBeUndefined();
  });

  it("updates switch directions on intersections", () => {
    const state = createInitialGameState({ width: 5, height: 5 });
    const coordinate = { x: 2, y: 2 };
    const intersection: IntersectionTrack = {
      type: "intersection",
      connections: ["north", "east", "south", "west"],
      switches: { north: "east", south: "west" },
    };

    const withIntersection = dispatch(state, {
      type: "placeTrack",
      coordinate,
      track: intersection,
    });

    const updated = dispatch(withIntersection, {
      type: "setSwitch",
      coordinate,
      entry: "north",
      exit: "south",
    });

    const key = coordinateToKey(coordinate);
    expect((updated.tracks[key] as IntersectionTrack).switches.north).toBe("south");
  });

  it("moves the train within grid bounds", () => {
    const state = createInitialGameState({ width: 3, height: 3 });
    const moved = dispatch(state, {
      type: "setTrainPosition",
      position: { x: 1, y: 2 },
      facing: "south",
    });

    expect(moved.train.position).toEqual({ x: 1, y: 2 });
    expect(moved.train.facing).toBe("south");
    expect(moved.train.status).toBe("moving");
  });
});
