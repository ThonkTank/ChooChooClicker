# Tests für `src/world/`

```text
tests/world/
├── README.md
└── test_game_map.py
```

## Zweck
Dieses Teilverzeichnis bündelt Unit-Tests für die Weltlogik rund um das [`GameMap`-Modul](../../src/world/README.md).
Der Fokus liegt auf der Topologie von Schienen sowie deren Klassifikation für das Rendering.

## Testabdeckung
- **`test_game_map.py`** – Prüft Dead-Ends, T-Stücke und Kreuzungen der `GameMap` sowie die bidirektionale Auto-Verkabelung.

## Standards & Konventionen
- Jeder Testfall benennt das erwartete Verhalten explizit (`dead_end`, `t_junction`, `crossroads`).
- Neue Tests sollen auf konkrete Dokumentationsabschnitte verweisen und bei Bedarf zusätzliche Fixtures einführen.
- Für komplexere Szenarien bitte zusätzliche Detaildokumente unter `tests/world/docs/` anlegen.

## Weiterführende Dokumentation
- [src/world/README.md](../../src/world/README.md) – Hintergrund zur Implementierung der Kartenlogik.
