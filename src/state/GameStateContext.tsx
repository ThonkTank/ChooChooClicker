import { createContext, Dispatch, ReactNode, useContext, useReducer } from "react";
import { GameState } from "./gameTypes";
import { createInitialGameState, GameAction, gameReducer } from "./gameReducer";

const GameStateContext = createContext<GameState | undefined>(undefined);
const GameDispatchContext = createContext<Dispatch<GameAction> | undefined>(undefined);

interface GameStateProviderProps {
  children: ReactNode;
  initialState?: GameState;
}

export function GameStateProvider({ children, initialState }: GameStateProviderProps) {
  const [state, dispatch] = useReducer(gameReducer, initialState ?? createInitialGameState());

  return (
    <GameStateContext.Provider value={state}>
      <GameDispatchContext.Provider value={dispatch}>
        {children}
      </GameDispatchContext.Provider>
    </GameStateContext.Provider>
  );
}

export function useGameState(): GameState {
  const context = useContext(GameStateContext);
  if (!context) {
    throw new Error("useGameState must be used within a GameStateProvider");
  }
  return context;
}

export function useGameDispatch(): Dispatch<GameAction> {
  const context = useContext(GameDispatchContext);
  if (!context) {
    throw new Error("useGameDispatch must be used within a GameStateProvider");
  }
  return context;
}

export function useGameStore() {
  return { state: useGameState(), dispatch: useGameDispatch() };
}
