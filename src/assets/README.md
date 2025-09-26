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

## Rotation Tests
- Die Datei [`tests/assets/test_sprites.py`](../../tests/assets/test_sprites.py) prüft `_rotate_point` sowie `_rotate_tile` der
  `SpriteSheet`-Klasse mit synthetischen `PhotoImage`-Fallbacks.
- Annahmen: Bildschirmkoordinaten wachsen nach rechts (`x`) und nach unten (`y`); eine 90°-Rotation folgt dem Uhrzeigersinn.
  Diese Konvention wird in den Tests explizit dokumentiert und sollte bei Erweiterungen eingehalten werden.

## Weiterführende Dokumentation
- [UI-Schicht](../ui/README.md) – beschreibt, wie Sprites beim Rendering eingesetzt werden.
- [Projektübersicht](../../README.md)
