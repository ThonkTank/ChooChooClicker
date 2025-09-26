# Überarbeitung der GameMap-API

## Kontext
`GameMap` koppelt die Existenz von Schienen an ihre Nachbarschaften. Neue Tiles nutzen aktuell die private Methode `_neighbours`, damit `add_track` bidirektionale Verbindungen erzeugt. Dadurch sind Tote-Enden oder vorbereitete Weichen nicht darstellbar. Details siehe [Struktur-Review](../docs/structure-review.md#2-schwach-gekapselte-karten-api).

## Betroffene Module
- [`src/app.py`](../src/README.md) – UI und Rendering, das direkt auf `GameMap` zugreift.

## Zielbild & Lösungsideen
1. **Explizite Track-Repräsentation**
   - `GameMap` sollte zwischen "Tile belegt" und "Verbindungen zu Nachbarn" unterscheiden (z. B. `has_tile` vs. `connections`).
2. **Öffentliche API bereitstellen**
   - Methoden wie `connect(a, b)` und `place_track(cell)` statt Nutzung privater Helfer.
   - Rückgaben mit Fehlercodes/Exceptions, falls Verbindungen unzulässig sind.
3. **Rendering entkoppeln**
   - `_select_track_sprite` sollte keine Rohdaten interpretieren müssen, sondern einen strukturierten Tile-Typ erhalten (z. B. Enum).
4. **Weichen & Kreuzungen vorbereiten**
   - Junctions (mehr als zwei Verbindungen) benötigen neue Sprites oder Notfalls Platzhalter; die API muss solche Fälle unterscheiden können.

## Offene Fragen
- Wie sollen automatische Verbindungsregeln aussehen (Grid-basierte Autoverkabelung vs. manuelles Verbinden)?
- Werden zukünftig unterschiedliche Schienentypen (z. B. Hochgeschwindigkeit) benötigt?
