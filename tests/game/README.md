# Tests für `src/game/`

```text
tests/game/
├── README.md
└── test_train.py
```

## Zweck
Absicherung der Momentum- und Tick-Logik aus [`src/game/`](../../src/game/README.md) ohne UI-Abhängigkeiten.

## Testfälle
- **`test_add_momentum_capped`** – Überprüft die Deckelung des Momentum-Speichers.
- **`test_try_move_advances_along_connection`** – Validiert die Bewegung entlang verbundener Tiles.
- **`test_game_engine_refunds_failed_move`** – Stellt sicher, dass bei fehlgeschlagenem Zug kein Momentum verloren geht.
- **`test_game_engine_invokes_listener`** – Prüft, dass Tick-Callbacks ausgelöst werden.

## Konventionen
- Nutze Hilfsfunktionen wie `build_linear_map`, um Karten-Setups konsistent zu halten.
- Listener werden in Tests über einfache Listensammler validiert.
- Tests bleiben GUI-frei und laufen in Headless-Umgebungen.
