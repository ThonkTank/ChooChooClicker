# Test-Suite `tests/`

```text
tests/
├── README.md
├── game/
│   ├── README.md
│   └── test_train.py
├── ui/
│   ├── README.md
│   └── test_track_sprite_selection.py
└── world/
    ├── README.md
    ├── test_game_map.py
    └── test_integration.py
```

## Zweck des Ordners
Der Ordner `tests/` enthält automatisierte Tests für die Module in [`src/`](../src/README.md). Alle Tests basieren auf `pytest` und laufen ohne GUI-Abhängigkeit.

## Wichtige Komponenten
- **`game/`** – Tests für Momentum- und Tick-Logik.
- **`ui/`** – Headless Rendering-Checks für Sprite- und Layoutlogik.
- **`world/`** – Tests und Integrationsfälle für das Kartenmodell.

## UI Rendering Checks
- [`test_track_sprite_selection.py`](ui/test_track_sprite_selection.py) validiert die Sprite-Auswahl
  entlang der vorinitialisierten Ringstrecke ohne Tk-Abhängigkeiten.

## Standards & Konventionen
- Gemeinsame Fixtures gehören in `conftest.py`, sobald mehrere Module sie benötigen.
- Pfade werden über `pytest.ini` konfiguriert (`pythonpath = src`). Zusätzliche `sys.path`-Manipulation ist nicht erlaubt.
- Jeder neue Testordner benötigt eine README mit Struktur- und Konventionsbeschreibung.

## Weiterführende Dokumentation
- [pytest-Konfiguration](../pytest.ini)
- [Paket-Readmes in `src/`](../src/README.md)
