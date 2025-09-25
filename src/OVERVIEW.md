# Übersicht: `src`

```
src/
├── app.py      # Hauptanwendung mit Spiel-Logik und Rendering
└── OVERVIEW.md # Diese Übersicht
```

## Features & Hauptzuständigkeiten

- **Spielfeld & Raster** – Verwaltung des 12×12-Rasters und Zeichnen der Pixelart-Schienen.
- **Zug & Momentum** – Pflege des Zugzustands inklusive Momentum-Ressource sowie automatische Bewegung.
- **Spielinteraktion** – Mausklick zum Bauen neuer Schienen, Button-Aktion zum Erhöhen des Momentums.

## Skriptbeschreibungen

### `app.py`
Zentrale Tkinter-Anwendung. Enthält `GameMap` zur Pflege der Schienenverbindungen, `Train` zur Verwaltung von Position, Richtung und Momentum sowie die Klasse `ChooChooClicker` für UI-Aufbau, Tick-Logik und Rendering.
