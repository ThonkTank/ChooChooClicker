# Tests für `src/world/`

```text
tests/world/
├── README.md
├── test_game_map.py
└── test_integration.py
```

## Zweck
Sichert die Spielfeld-API (`GameMap`, `TrackPiece`, `Direction`) und deren Zusammenspiel mit der Spiel-Logik ab.

## Testfälle
- **`test_game_map.py`** – Einzeltests für Tile-Topologien (Dead Ends, T-Kreuzungen, Kreuzungen).
- **`test_integration.py`** – Verifiziert das Zusammenspiel von Kartenlogik und Zug/Engine (z. B. Start-Ring, alternative Routen).

## Konventionen
- Karten-Setups immer über kleine Hilfsfunktionen oder Fixtures dokumentieren.
- Erwartete Verbindungen als Mengen (`set`) definieren, um Reihenfolgeabhängigkeiten zu vermeiden.
- Erweiterungen der Weltlogik zuerst hier mit Tests untermauern, bevor UI-Änderungen erfolgen.
