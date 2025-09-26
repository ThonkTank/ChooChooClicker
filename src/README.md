# Modulübersicht `src/`

```text
src/
├── app.py   # Hauptanwendung mit Spiel-Logik und Rendering
└── README.md
```

## Zweck des Ordners
Der Ordner `src/` bündelt die ausführbare Python-Anwendung von Choo Choo Clicker. Alle Spielsysteme – vom Rendering über die Ressourcenerzeugung bis zur Bewegung des Zuges – befinden sich hier in einer einzelnen Datei, die als klar strukturierter Einstiegspunkt dient.

## Komponenten in `app.py`
- **`SpriteSheetLoader`** – Lädt `Ground-Rails.png`, zerlegt das Sprite-Sheet in 32×32-Pixel-Tiles und stellt sie der Karte bereit.
- **`GameMap`** – Hält das 12×12-Gitter, verwaltet Schienenverbindungen und liefert Nachbarschaftsinformationen für das automatische Tile-Mapping. Offene Fragen zur API-Kapselung sind im To-do [„Überarbeitung der GameMap-API“](../todo/game-map-api.md) dokumentiert.
- **`Train`** – Speichert Position, Fahrtrichtung und Momentum-Speicher. Enthält Hilfsfunktionen, um Momentum zu verbrauchen oder zu gewinnen.
- **`ChooChooClicker`** – Tkinter-Anwendung, die Oberfläche, Event-Handling und Tick-Zyklus orchestriert. Die Methode `_setup_initial_ring` baut den Start-Ring im Uhrzeigersinn auf, `_handle_click` fügt Schienen hinzu, `_push_train` erhöht das Momentum und `_schedule_tick` bewegt den Zug alle 600 ms.

  _Hinweis:_ Die aktuelle Bündelung von Spiellogik, Rendering und UI in dieser Klasse ist im To-do [„Refactoring der Spiel-Architektur“](../todo/refactor-architecture.md) adressiert.

## Architektur- und Stilrichtlinien
- Halte Logik, Rendering und UI-Konstruktion in klar getrennten Methoden. Bevorzuge kleine, fokussierte Hilfsfunktionen.
- Kommentiere bedeutende Designentscheidungen direkt im Code (z. B. warum bestimmte Bewegungsregeln gelten).
- Bei Erweiterungen bitte neue Module in Unterordnern mit eigener `README.md` anlegen, um diese Übersicht schlank zu halten.

## Weiterführende Hinweise
- Assets (z. B. `Ground-Rails.png`) werden direkt von `app.py` relativ zum Projekt-Root geladen.
- Für To-dos oder größere Umbauten verweise aus Docstrings und Kommentaren in den passenden Eintrag im [`todo/`-Verzeichnis](../todo/README.md).
