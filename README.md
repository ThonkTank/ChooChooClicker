# Choo Choo Clicker

Choo Choo Clicker ist ein minimalistisches Pixelart-Clicker-Spiel rund um einen kleinen Zug. Das Spiel läuft in einer eigenständigen Python-Anwendung auf Basis von Tkinter und kommt ganz ohne Game-Engine aus. Diese Version liefert die ersten Grundfunktionen: ein schienengebundenes Spielfeld, einfache Ressourcenverwaltung und eine Schieben-Aktion, mit der der Zug Momentum sammelt, um sich über die Schienen zu bewegen.

## Features

- **Sprite-basiertes Kartendesign** – Die Spielfläche besteht aus einem 12×12-Raster, das vollständig mit 32×32-Pixel-Tiles aus `Ground-Rails.png` gerendert wird. Jede Zelle lässt sich anklicken, um neue Schienen zu platzieren.
- **Initialer Schienenring** – Das Spiel erzeugt automatisch einen geschlossenen Schienenring am Rand der Karte. Der Zug startet in der linken oberen Ecke auf diesem Ring.
- **Pixelart-Zug** – Der Zug wird mit einfachen Formen dargestellt und bewegt sich entlang der Schienen.
- **Aktion "Schieben"** – Im rechten Seitenbereich befindet sich ein Button, der Momentum erzeugt. Momentum ist auf zehn Einheiten begrenzt.
- **Momentum-Ressource** – Eine Anzeige am oberen Bildschirmrand zeigt den aktuellen Momentum-Vorrat. Jede Schiebe-Aktion erhöht den Vorrat, bis der Speicher voll ist.
- **Automatische Bewegung** – Alle 600 Millisekunden verbraucht der Zug automatisch eine Momentum-Einheit, um sich um ein Feld weiterzubewegen. Ist die aktuelle Fahrtrichtung blockiert, versucht der Zug automatisch einen passenden Schienenabschnitt zu wählen.

## Projektstruktur

```
.
├── README.md         # Dokumentation zu Features, Architektur und Ausführung
├── start_game.bat    # Windows-Shortcut zum Starten der Anwendung
├── start_game.sh     # Unix-Shortcut zum Starten der Anwendung
└── src
    └── app.py        # Hauptanwendung mit Spiel-Logik und Rendering
```

## Implementierungsdetails

### `src/app.py`

- **Technologie-Stack**: Verwendet Tkinter für die Fenster- und Canvas-Erstellung. Boden- und Schienen-Tiles stammen aus einem Sprite-Sheet und werden per `tk.PhotoImage` auf den Canvas gerendert.
- **Spielzustand**: `GameMap` verwaltet das Raster sowie Verbindungen zwischen Schienenzellen. `Train` hält Position, Fahrtrichtung und Momentum-Speicher des Zuges.
- **Initialisierung**: `ChooChooClicker._setup_initial_ring` erzeugt den äußeren Schienenring und verbindet die Abschnitte miteinander.
- **Interaktion**: `ChooChooClicker._handle_click` erlaubt es, durch Anklicken neuer Felder Schienenabschnitte hinzuzufügen. `ChooChooClicker._push_train` füllt den Momentum-Speicher auf.
- **Spielablauf**: Ein Timer (`_schedule_tick`) sorgt für periodische Spielzyklen. Pro Zyklus wird Momentum verbraucht, um den Zug weiterzubewegen. Dabei wird zuerst versucht, in der aktuellen Richtung zu fahren. Falls das nicht möglich ist, wird eine alternative Verbindung gewählt.
- **Rendering**: Ein `SpriteSheetLoader` extrahiert 32×32-Pixel-Tiles aus `Ground-Rails.png`. `_select_track_sprite` wertet pro Zelle die vorhandenen Nachbarn aus, um automatisch den passenden Boden-, Gerade- oder Kurven-Tile zu bestimmen. `_draw_map` zeichnet zunächst den Bodentile und legt anschließend den berechneten Schienenabschnitt darüber. Optional lassen sich Rasterlinien weiterhin einblenden.

## Ausführen

Das Spiel benötigt eine Python-Installation (Version 3.10 oder neuer empfohlen). Tkinter ist Bestandteil vieler Standard-Distributionen, unter Windows kann es bei der Python-Installation optional ausgewählt werden. Im Zweifel lässt sich Tkinter über die Paketverwaltung des Systems nachrüsten.

### Schnellstart über Shortcut

- **Linux/macOS**: `./start_game.sh`
- **Windows**: Doppelklick auf `start_game.bat` oder Aufruf im Terminal via `start_game.bat`

Die Skripte wählen automatisch den passenden Python-Interpreter (priorisiert `python3` bzw. `py`).

### Manuelle Ausführung

Falls Sie die Anwendung lieber direkt starten möchten, nutzen Sie einen der folgenden Befehle im Projektverzeichnis:

- `python src/app.py` (allgemein)
- `python3 src/app.py` (Linux/macOS)
- `py src/app.py` (Windows)

Beim Start öffnet sich ein Fenster mit Karte, Ressourcenleiste und Aktionsbereich. Nutzen Sie den Button **Schieben**, um Momentum aufzubauen, und platzieren Sie neue Schienen, indem Sie auf Felder des Rasters klicken.
