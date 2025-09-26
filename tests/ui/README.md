# Testmodul `tests/ui/`

```text
tests/ui/
├── README.md
└── test_sprite_mapping.py
```

## Zweck
Die UI-Testfälle prüfen Mapping-Regeln der Sprite-Auswahl ohne eine Tkinter-Oberfläche starten zu müssen. Dadurch können Rendering-Regeln deterministisch und headless validiert werden.
Zusätzlich wird die statische Metadaten-Tabelle `SPRITE_COORDINATES` gegen die dokumentierten Tile-Koordinaten geprüft.

## Standards & Konventionen
- Tests nutzen `ChooChooApp._select_track_sprite` in einer minimalen Stub-Instanz (`__new__` + manuelle Attribute).
- Track-Konfigurationen werden direkt über `GameMap` aufgebaut, um dieselben Verbindungs-APIs wie die UI zu nutzen.
- Neue Tests müssen sicherstellen, dass Sprite-Schlüssel in [`src/ui/app.py`](../../src/ui/app.py) und Dokumentation in [`Task/rendering-notes.md`](../../Task/rendering-notes.md) konsistent bleiben.

## Weiterführende Dokumentation
- [UI-Rendering-Dokumentation](../../src/ui/README.md)
- [Allgemeine Testübersicht](../README.md)
