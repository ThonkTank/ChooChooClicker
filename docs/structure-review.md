# Struktur-Review – Mai 2024

Diese Analyse bewertet den Aufbau von Choo Choo Clicker auf Ordnungs-, Modul- und API-Ebene. Ziel ist es, strukturelle Risiken frühzeitig zu adressieren und nachhaltige Verbesserungen zu planen. Konkrete Umsetzungsaufgaben sind – falls vorhanden – als To-dos im [`todo/`-Verzeichnis](../todo/README.md) dokumentiert.

## Überblick
- Die Anwendung folgt jetzt einer paketbasierten Struktur: `src/game/`, `src/world/`, `src/assets/`, `src/ui/` werden über [`src/main.py`](../src/main.py) kombiniert.
- Spiellogik (`GameEngine`, `Train`) ist komplett von Tkinter entkoppelt und kann isoliert getestet werden.
- Sprite-Laden und Tkinter-spezifische Komponenten sind kapselt, sodass alternative Frontends leichter denkbar sind.

## Status wichtiger Architekturthemen

### 1. Aufbrechen der monolithischen `app.py`
**Ausgangslage:** Bis April 2024 vereinte eine Datei (`src/app.py`) Gameplay, Rendering, Sprite-Verarbeitung und UI-Event-Handling.

**Umsetzung:** Die Verantwortlichkeiten wurden in vier Pakete aufgeteilt (siehe [src/README.md](../src/README.md)). `src/main.py` ist die einzige Stelle, an der Tkinter instanziiert wird. Die Spiel-Engine (`src/game/train.py`) publiziert Tick-Ergebnisse über Callbacks, welche die UI konsumiert.

**Absicherung:** Neue Tests unter [`tests/game/test_train.py`](../tests/game/test_train.py) prüfen Momentum und Tick-Verhalten ohne GUI. Integrationsfälle liegen in [`tests/world/test_integration.py`](../tests/world/test_integration.py).

### 2. Karten-API und Rendering
**Status:** Das modulare Weltmodell aus [`src/world/game_map.py`](../src/world/game_map.py) bleibt bestehen. Die UI nutzt weiterhin `TrackPiece`/`TrackShape`, aber Rendering-Entscheidungen leben jetzt ausschließlich in `src/ui/app.py`. Damit bleibt die Kartenlogik weiterhin frei von Framework-Abhängigkeiten.

### 3. Sprite-Verarbeitung
**Status:** Das neue Modul [`src/assets/sprites.py`](../src/assets/sprites.py) cached Basistiles und Rotationen. Die UI ruft `SpriteSheet.get_tile(..., rotation=...)` auf und benötigt keine eigene Rotationslogik mehr.

## Fazit
Die Architektur ist nun in klar abgegrenzte Pakete gegliedert und testbar. Offene Verbesserungen werden künftig über dedizierte To-dos erfasst. Regelmäßige Reviews sollten sicherstellen, dass neue Features die Paketgrenzen respektieren und ihre Dokumentation erweitern.
