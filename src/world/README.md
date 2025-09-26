# Paket `src/world/`

```text
src/world/
├── README.md
├── __init__.py
└── game_map.py
```

## Zweck
`src/world/` kapselt die Spielfeld- und Weltlogik. Das Modul stellt die Karte (`GameMap`) bereit, deren Informationen von der Spiel-Engine (`src/game/`) und vom UI (`src/ui/`) gleichermaßen genutzt werden.

## Module & Hauptfunktionen
- **`game_map.py`**
  - `GameMap` – Verwaltung von belegten Tiles und gerichteten Verbindungen.
  - `TrackPiece` & `TrackShape` – strukturierte Rückgaben für das Rendering.
  - `Direction` – Kardinalrichtungen inklusive `delta`-/`opposite`-Hilfsfunktionen.
- **`__init__.py`** – Exportiert die oben genannten Typen für einfachere Imports.

## Standards & Konventionen
- Kartenänderungen müssen Tests in `tests/world/` erweitern.
- Funktionen, die Seiteneffekte haben (z. B. `auto_connect`), geben ihre Änderungen als Sets zurück, um UI/Gameplay über neue Verbindungen zu informieren.
- Erweiterungen des Weltmodells sollen zuerst hier dokumentiert werden und anschließend Querverweise in den Paket-Readmes erhalten.

## Weiterführende Dokumentation
- [Gameplay `src/game/`](../game/README.md)
- [UI `src/ui/`](../ui/README.md)
- [Testübersicht](../../tests/README.md)
