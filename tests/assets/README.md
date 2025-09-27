# Test-Modul `tests/assets/`

```text
tests/assets/
├── README.md
├── test_sprite_offsets.py
└── test_sprites.py
```

## Zweck
Dieser Ordner enthält Unit-Tests für die Sprite-bezogenen Assets. Fokus ist die Validierung der Rotationslogik aus
[`src/assets/sprites.py`](../../src/assets/sprites.py), sodass Rendering-Komponenten auf reproduzierbare Koordinatensysteme
vertrauen können.

## Tests & Hauptfunktionen
- **`tests/asset_fakes.py`** – stellt `FakePhotoImage` und `make_sheet` bereit, um SpriteSheet-Logik ohne echte Tk-Instanz zu testen.
- **`test_sprites.py`** – überprüft `_rotate_point` und `_rotate_tile` der `SpriteSheet`-Klasse anhand synthetischer
  `PhotoImage`-Ersatzobjekte. Dokumentiert explizit die Drehrichtung (90° = Uhrzeigersinn) und die Koordinatenannahmen.
- **`test_sprite_offsets.py`** – misst Bounding-Boxes künstlicher Sprites und stellt sicher, dass optionale Offset-Korrekturen
  beim Kopieren und Caching angewendet werden.

## Standards & Konventionen
- Tests in diesem Ordner verzichten auf reale Tkinter-Instanzen und verwenden Mock-/Fallback-Implementierungen für
  `PhotoImage`.
- Neue Tests müssen ihre Annahmen über Achsensystem und Orientierung dokumentieren, um Regressionen durch alternative
  Rendering-Frameworks zu vermeiden.

## Weiterführende Dokumentation
- [Übersicht der Testsuite](../README.md)
- [Asset-Dokumentation](../../src/assets/README.md)
