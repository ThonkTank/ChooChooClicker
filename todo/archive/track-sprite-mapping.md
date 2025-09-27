# Track-Sprite-Mappings für Sonderfälle ergänzen (Archiv)

## Kontext
Die PyTests deckten die Sprite-Keys für Randzellen ab, jedoch fehlten T-Kreuzungen (`TrackShape.T_JUNCTION`) und Kreuzungen (`TrackShape.CROSS`). Die Beobachtung wurde im Abschnitt "Platz für weitere Beobachtungen" der [Rendering-Notizen](../../Task/rendering-notes.md) dokumentiert.

## Betroffene Module
- [`src/ui/`](../../src/ui/README.md)
- Tests unter [`tests/ui/`](../../tests/ui/README.md)

## Umsetzung & Abschluss
- Sprite-Mappings in [`src/ui/app.py`](../../src/ui/app.py) um dedizierte Keys für T-Varianten sowie Kreuzungen erweitert.
- Dokumentation der Tile-Positionen in [`src/ui/README.md`](../../src/ui/README.md#sprite-belegung-ground-railspng) ergänzt.
- Regressionstests in [`tests/ui/test_track_sprite_selection.py`](../../tests/ui/test_track_sprite_selection.py) prüfen nun T-Junctions und Kreuzungen explizit.
- Abschlussreferenz im [Analyse-Dossier](../../Task/analysis-plan.md) aktualisiert; Beobachtung aus den [Rendering-Notizen](../../Task/rendering-notes.md#weitere-beobachtungen) ausgetragen.

## Lessons Learned
- Sprite-Sheets ohne Metadaten benötigen eine explizite Tabelle der belegten Tiles, damit zukünftige Varianten gezielt adressiert werden können.
- Tests sollten die vollständige Kombinatorik einer Topologie abdecken (hier: alle Richtungssets von `TrackShape.T_JUNCTION`).
