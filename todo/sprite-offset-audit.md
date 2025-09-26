# Sprite-Offsets kalibrieren

## Kontext
Mehrere Fahrzeug-Sprites sind beim Rendern um 1–2 Pixel verschoben. Details zur Beobachtung finden sich im Abschnitt "Sprite-Offsets" der [Rendering-Notizen](../Task/rendering-notes.md).

## Betroffene Module
- [`src/assets/sprites.py`](../src/assets/sprites.py)
- Asset-Quellen im `assets/`-Ordner (extern verwaltet)

## Lösungsideen
- Bounding-Boxes gegen die Quelldateien messen und Abweichungen dokumentieren.
- Automatisierten Check in den Tests ergänzen, um künftige Regressionen zu verhindern.
- Anpassungen am SpriteSheet-Exporter dokumentieren.

## Offene Fragen & Verantwortlichkeit
- **Verantwortlich:** Art-Team (Bestätigung ausstehend) – Koordination über Tech Lead.
- **Offene Frage:** Müssen wir einen temporären Hotfix im Renderer implementieren, bis die Assets korrigiert sind?
