# Übersicht: `src`

```
src/
├── app.py      # Hauptanwendung mit Spiel-Logik und Rendering
└── OVERVIEW.md # Diese Übersicht
```

## Features & Hauptzuständigkeiten

- **Sprite-basiertes Spielfeld** – Verwaltung des 12×12-Rasters und Rendering über 32×32-Tiles aus `Ground-Rails.png` inklusive automatischer Auswahl passender Schienenabschnitte.
- **Zug & Momentum** – Pflege des Zugzustands inklusive Momentum-Ressource sowie automatische Bewegung.
- **Spielinteraktion** – Mausklick zum Bauen neuer Schienen, Button-Aktion zum Erhöhen des Momentums.

## Skriptbeschreibungen

### `app.py`
Zentrale Tkinter-Anwendung. Enthält `GameMap` zur Pflege der Schienenverbindungen, `Train` zur Verwaltung von Position, Richtung und Momentum sowie `ChooChooClicker` für UI-Aufbau, Tick-Logik und spritebasiertes Rendering. Ein `SpriteSheetLoader` extrahiert Boden- und Schienentiles, während `_select_track_sprite` anhand der Nachbarschaft passende Gerade- bzw. Kurvenstücke auswählt und `_draw_map` diese auf dem Canvas stapelt.
