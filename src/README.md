# Modulübersicht `src/`

```text
src/
├── README.md
├── app.py        # Hauptanwendung mit Spiel-Logik und Rendering
└── world/        # Weltmodell inkl. GameMap
    ├── README.md
    ├── __init__.py
    └── game_map.py
```

## Zweck des Ordners
Der Ordner `src/` bündelt die ausführbare Python-Anwendung von Choo Choo Clicker. Alle Spielsysteme – vom Rendering über die Ressourcenerzeugung bis zur Bewegung des Zuges – befinden sich hier in einer einzelnen Datei, die als klar strukturierter Einstiegspunkt dient.

## Komponenten in `app.py`
- **`SpriteSheetLoader`** – Lädt `Ground-Rails.png`, zerlegt das Sprite-Sheet in 32×32-Pixel-Tiles und stellt sie der Karte bereit.
- **`Train`** – Speichert Position, Fahrtrichtung und Momentum-Speicher. Enthält Hilfsfunktionen, um Momentum zu verbrauchen oder zu gewinnen.
- **`ChooChooClicker`** – Tkinter-Anwendung, die Oberfläche, Event-Handling und Tick-Zyklus orchestriert. Die Methode `_setup_initial_ring` baut den Start-Ring im Uhrzeigersinn auf, `_handle_click` platziert Schienen via `GameMap.place_track` und `GameMap.auto_connect`, `_push_train` erhöht das Momentum und `_schedule_tick` bewegt den Zug alle 600 ms.

## Weltmodell in `world/`
- **`GameMap`** – Separates Modul für die Kartenlogik. Trennt Tile-Belegung (`place_track`/`remove_track`) von gerichteten Verbindungen (`connect`/`disconnect`) und stellt über `get_track_piece` vorbereitete Topologie-Informationen für das Rendering zur Verfügung.
- **`TrackPiece` & `TrackShape`** – Strukturierte Rückgaben, die `_select_track_sprite` direkt auswertet, ohne Nachbarschaften selbst berechnen zu müssen.
- **`Direction`** – Enum der vier kardinalen Richtungen; dient als verbindliche Basis für alle Schienentopologien.

  _Hinweis:_ Die aktuelle Bündelung von Spiellogik, Rendering und UI in dieser Klasse ist im To-do [„Refactoring der Spiel-Architektur“](../todo/refactor-architecture.md) adressiert.

## Architektur- und Stilrichtlinien
- Halte Logik, Rendering und UI-Konstruktion in klar getrennten Methoden. Bevorzuge kleine, fokussierte Hilfsfunktionen.
- Kommentiere bedeutende Designentscheidungen direkt im Code (z. B. warum bestimmte Bewegungsregeln gelten).
- Bei Erweiterungen bitte neue Module in Unterordnern mit eigener `README.md` anlegen, um diese Übersicht schlank zu halten.

## Weiterführende Hinweise
- Assets (z. B. `Ground-Rails.png`) werden direkt von `app.py` relativ zum Projekt-Root geladen.
- Für To-dos oder größere Umbauten verweise aus Docstrings und Kommentaren in den passenden Eintrag im [`todo/`-Verzeichnis](../todo/README.md).
