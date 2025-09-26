# Test-Suite `tests/`

```text
tests/
├── README.md
├── game/
│   ├── README.md
│   └── test_train.py
└── world/
    ├── README.md
    ├── test_game_map.py
    └── test_integration.py
```

## Zweck des Ordners
Der Ordner `tests/` enthält automatisierte Tests für die Module in [`src/`](../src/README.md). Alle Tests basieren auf `pytest` und laufen ohne GUI-Abhängigkeit.

## Wichtige Komponenten
- **`game/`** – Tests für Momentum- und Tick-Logik.
- **`world/`** – Tests und Integrationsfälle für das Kartenmodell.

## Standards & Konventionen
- Gemeinsame Fixtures gehören in `conftest.py`, sobald mehrere Module sie benötigen.
- Pfade werden über `pytest.ini` konfiguriert (`pythonpath = src`). Zusätzliche `sys.path`-Manipulation ist nicht erlaubt.
- Jeder neue Testordner benötigt eine README mit Struktur- und Konventionsbeschreibung.

## Weiterführende Dokumentation
- [pytest-Konfiguration](../pytest.ini)
- [Paket-Readmes in `src/`](../src/README.md)
