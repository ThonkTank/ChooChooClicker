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
  - `SpriteSheet.measure_bounds(column, row, *, apply_offsets=True)` – bestimmt die Bounding-Box nicht transparenter Pixel und bildet die Grundlage für Offsets.
  - `SPRITE_OFFSETS` – Mapping der gemessenen Korrekturen für `Ground-Rails.png`.

## Standards & Konventionen
- Sprite-Funktionen behalten alle Tkinter-Abhängigkeiten in diesem Paket. Andere Module interagieren ausschließlich über die API von `SpriteSheet`.
- Verwende das optionale `rotation`-Argument statt eigener Rotationslogik in UI-Komponenten.
- Neue Asset-Typen müssen ihre eigenen README-Abschnitte und ggf. einen `docs/`-Unterordner hinzufügen.
- Bounding-Box-Messungen werden im [To-do `sprite-offset-audit`](../../todo/sprite-offset-audit.md) dokumentiert; Abweichungen sind mit Tests zu hinterlegen und im Mapping `SPRITE_OFFSETS` abzulegen.

## Rotation Tests
- Die Datei [`tests/assets/test_sprites.py`](../../tests/assets/test_sprites.py) prüft `_rotate_point` sowie `_rotate_tile` der `SpriteSheet`-Klasse mit synthetischen `PhotoImage`-Fallbacks.
- Annahmen: Bildschirmkoordinaten wachsen nach rechts (`x`) und nach unten (`y`); eine 90°-Rotation folgt dem Uhrzeigersinn. Diese Konvention wird in den Tests explizit dokumentiert und sollte bei Erweiterungen eingehalten werden.

## Offset-Validierung
- [`tests/assets/test_sprite_offsets.py`](../../tests/assets/test_sprite_offsets.py) validiert `measure_bounds` sowie die Anwendung der optionalen Offsets.
- Die aktuell hinterlegten Korrekturen sind in [`todo/sprite-offset-audit.md`](../../todo/sprite-offset-audit.md) hergeleitet.

## Weiterführende Dokumentation
- [UI-Schicht](../ui/README.md) – beschreibt, wie Sprites beim Rendering eingesetzt werden.
- [Projektübersicht](../../README.md)
