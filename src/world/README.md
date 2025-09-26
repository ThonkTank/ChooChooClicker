# Modul `src/world/`

```text
src/world/
├── __init__.py
└── game_map.py
```

## Zweck des Ordners
`src/world/` kapselt die Spielfeld- und Weltlogik von Choo Choo Clicker.
Ziel ist eine klare Trennung zwischen Datenmodell (z. B. belegte Tiles) und UI-spezifischem Rendering, das über vorbereitete Value-Objekte erfolgt.

## Module
- **`game_map.py`** – Enthält `GameMap`, `TrackPiece` und zugehörige Enums (`Direction`, `TrackShape`).
  Die Karte verwaltet:
  - belegte Tiles per `place_track`/`remove_track`,
  - gerichtete Verbindungen per `connect`/`disconnect`,
  - automatische Nachbarschaftsverkabelung via `auto_connect`,
  - strukturierte Rückgaben für das Rendering (`get_track_piece`).
- **`__init__.py`** – Stellt die zentralen Klassen und Typen für andere Module bereit.

## Standards & Konventionen
- Richtungsinformationen werden ausschließlich über das `Direction`-Enum modelliert.
- Neue Weltmodule müssen die hier dokumentierte Trennung von Zuständen respektieren.
- Ergänzende Hilfsfunktionen bitte mit ausführlichen Docstrings und Verweisen auf zugehörige Tests versehen.

## Weiterführende Dokumentation
- [src/README.md](../README.md) – Überblick über die Gesamtstruktur des Anwendungs-Codes.
- [tests/world/README.md](../../tests/world/README.md) – Abdeckung und Szenarien der zugehörigen Unit-Tests.
