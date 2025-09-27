# UI-Testpaket `tests/ui/`

```text
tests/ui/
├── README.md
├── test_camera_initialization.py
└── test_track_sprite_selection.py
```

## Zweck des Ordners
Der Ordner `tests/ui/` bündelt UI-nahe Regressionstests, die ohne echte Tk-Oberfläche laufen. Sie
prüfen insbesondere die Sprite-Auswahl und andere visuelle Ableitungen anhand der Engine-Daten.

## Standards & Konventionen
- Tests simulieren UI-Interaktionen über Dummy-Objekte oder Helper, sodass kein GUI-Toolkit
  initialisiert werden muss.
- Erwartete Sprite-Keys werden stets explizit dokumentiert, damit Abweichungen nachvollziehbar
  bleiben.
- Neue Tests erhalten klare Kontext-Kommentare (z. B. Randfälle, Assets) und referenzieren relevante
  Tickets oder Notizen im Ordner [`Task/`](../../Task/README.md).
- Kamera-Regressionen werden mit Fake-Canvas-Implementierungen überprüft, um `moveto`/`scan_dragto`-
  Aufrufe deterministisch zählen zu können.

## Weiterführende Dokumentation
- [Hauptübersicht der Tests](../README.md)
- [Rendering-Notizen & offene Fragen](../../Task/rendering-notes.md)
