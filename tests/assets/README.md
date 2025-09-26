# Test-Modul `tests/assets/`

```text
tests/assets/
├── README.md
└── test_sprites.py
```

## Zweck
Dieser Ordner enthält Unit-Tests für die Sprite-bezogenen Assets. Fokus ist die Validierung der Rotationslogik aus
[`src/assets/sprites.py`](../../src/assets/sprites.py), sodass Rendering-Komponenten auf reproduzierbare Koordinatensysteme
vertrauen können.

## Tests & Hauptfunktionen
- **`test_sprites.py`** – überprüft `_rotate_point` und `_rotate_tile` der `SpriteSheet`-Klasse anhand synthetischer
  `PhotoImage`-Ersatzobjekte. Dokumentiert explizit die Drehrichtung (90° = Uhrzeigersinn) und die Koordinatenannahmen.

## Standards & Konventionen
- Tests in diesem Ordner verzichten auf reale Tkinter-Instanzen und verwenden Mock-/Fallback-Implementierungen für
  `PhotoImage`.
- Neue Tests müssen ihre Annahmen über Achsensystem und Orientierung dokumentieren, um Regressionen durch alternative
  Rendering-Frameworks zu vermeiden.

## Weiterführende Dokumentation
- [Übersicht der Testsuite](../README.md)
- [Asset-Dokumentation](../../src/assets/README.md)
