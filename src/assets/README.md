# Paket `src/assets/`

```text
src/assets/
├── README.md
├── __init__.py
└── sprites.py
```

## Zweck
Dieses Paket bündelt alle Asset- und Sprite-bezogenen Funktionen. Es stellt einen zentralen Zugriffspunkt zum Laden und Cachen der Tiles aus `Ground-Rails.png` bereit.

## Module & Hauptfunktionen
- **`sprites.py`**
  - `SpriteSheet` – lädt ein Sprite-Sheet über Tkinter, cached Basistiles und Rotationen (`rotation`-Argument in `get_tile`).

## Standards & Konventionen
- Sprite-Funktionen behalten alle Tkinter-Abhängigkeiten in diesem Paket. Andere Module interagieren ausschließlich über die API von `SpriteSheet`.
- Verwende das optionale `rotation`-Argument statt eigener Rotationslogik in UI-Komponenten.
- Neue Asset-Typen müssen ihre eigenen README-Abschnitte und ggf. einen `docs/`-Unterordner hinzufügen.

## Weiterführende Dokumentation
- [UI-Schicht](../ui/README.md) – beschreibt, wie Sprites beim Rendering eingesetzt werden.
- [Projektübersicht](../../README.md)
