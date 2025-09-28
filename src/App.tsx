import "./App.css";
import { AppLayout } from "./components/layout/AppLayout";
import { GameStateProvider } from "./state";

function App() {
  return (
    <GameStateProvider>
      <AppLayout />
    </GameStateProvider>
  );
}

export default App;
