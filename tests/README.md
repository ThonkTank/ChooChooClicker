# Test-Suite `tests/`

```text
tests/
├── README.md
└── world/
    ├── README.md
    └── test_game_map.py
```

## Zweck des Ordners
Der Ordner `tests/` enthält automatisierte Tests für die Python-Module im Verzeichnis [`src/`](../src/README.md).
Alle Tests basieren auf `pytest` und dienen der Absicherung zentraler Spielmechaniken.

## Wichtige Komponenten
- **`world/`** – Tests für die Karten- und Weltlogik.

## Standards & Konventionen
- Alle neuen Testmodule müssen in der Strukturübersicht oben ergänzt werden.
- Gemeinsame Fixtures werden hier dokumentiert oder in `conftest.py` gespeichert, sobald Bedarf besteht.
- Testfälle sollen klar beschreiben, welches Verhalten abgesichert wird und auf welche Dokumentation sie referenzieren.

## Weiterführende Dokumentation
- [tests/world/README.md](world/README.md) – Details zu Welt-bezogenen Tests und den abgedeckten Szenarien.
