export type Direction = "north" | "east" | "south" | "west";

export interface Coordinate {
  x: number;
  y: number;
}

export type TrackType = "straight" | "curve" | "intersection";

interface TrackBase {
  type: TrackType;
  /**
   * Directions that are connected by this track piece. For example, a straight
   * horizontal segment would connect west ↔ east.
   */
  connections: Direction[];
}

export interface StraightTrack extends TrackBase {
  type: "straight";
}

export interface CurveTrack extends TrackBase {
  type: "curve";
}

export interface IntersectionTrack extends TrackBase {
  type: "intersection";
  /**
   * Mapping for each incoming direction to the outgoing direction the switch
   * currently routes to.
   */
  switches: Partial<Record<Direction, Direction>>;
}

export type TrackPiece = StraightTrack | CurveTrack | IntersectionTrack;

export interface MomentumState {
  current: number;
  max: number;
}

export type TrainStatus = "idle" | "moving" | "stopped";

export interface TrainState {
  position: Coordinate;
  facing: Direction;
  status: TrainStatus;
}

export interface GridDimensions {
  width: number;
  height: number;
}

export type TrackMap = Record<string, TrackPiece>;

export interface GameState {
  dimensions: GridDimensions;
  tracks: TrackMap;
  momentum: MomentumState;
  train: TrainState;
}

export const MOMENTUM_MAX = 10;
