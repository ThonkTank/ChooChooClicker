# Struktur-Review – März 2024

Diese Analyse bewertet den aktuellen Aufbau von Choo Choo Clicker auf Ordnungs-, Modul- und API-Ebene. Ziel ist es, strukturelle Risiken frühzeitig zu adressieren und nachhaltige Verbesserungen zu planen. Konkrete Umsetzungsaufgaben sind als To-dos im [`todo/`-Verzeichnis](../todo/README.md) hinterlegt.

## Überblick
- Die Anwendung besteht vollständig aus einer einzigen Python-Datei (`src/app.py`).
- Gameplay, Rendering, UI-Widgets, Sprite-Laden und Kartenlogik sind eng miteinander verflochten.
- Das Datenmodell (`GameMap`, `Train`) wird direkt von Tkinter-spezifischen Klassen aus gesteuert, wodurch eine klare Schichtentrennung fehlt.

## Identifizierte Strukturprobleme

### 1. Monolithische `app.py`
**Beobachtung:** Spielzustand, Rendering und UI-Event-Handling leben in einer Datei und Klasse (`ChooChooClicker`). Interne Hilfsklassen (`GameMap`, `Train`, `SpriteSheetLoader`) werden dort gleichzeitig instanziiert und gesteuert.

**Risiken:**
- Geringe Testbarkeit, da Logik-Aufrufe immer das Tkinter-UI initialisieren.
- Erweiterungen (z. B. neue Ressourcen, mehrere Züge, Menü) erhöhen die Komplexität einer einzigen Datei.
- Fehlende Schnittstellen erschweren spätere Portierungen (z. B. Web, CLI).

**Empfohlene Richtung:** Siehe To-do [`todo/refactor-architecture.md`](../todo/refactor-architecture.md).

### 2. Schwach gekapselte Karten-API
**Beobachtung:** `GameMap` stellt nur eine kombinierte Methode `add_track` bereit. Für automatische Verbindungen ruft der Aufrufer intern `_neighbours` auf, obwohl diese Methode als privat markiert ist. Die Existenz von Schienen wird indirekt über die Anzahl der Nachbarn bestimmt (`has_track` prüft `len(...) > 0`).

**Risiken:**
- Fragile Kopplung zwischen UI und Map-Logik, weil private Methoden von außen genutzt werden.
- Keine Möglichkeit, tote Enden oder vorkonfigurierte Weichen korrekt abzubilden (eine Schiene ohne Nachbarn wird als "kein Track" behandelt und nicht gerendert).
- Junctions (>2 Nachbarn) liefern im Rendering nur Platzhalter, sodass zukünftige Streckenpläne visuell nicht unterstützt werden.

**Empfohlene Richtung:** Siehe To-do [`todo/game-map-api.md`](../todo/game-map-api.md).

### 3. Sprite-Verarbeitung als Performance-Risiko
**Beobachtung:** `SpriteSheetLoader.rotate_tile` rotiert Tiles zur Laufzeit per Pixelkopie in verschachtelten Schleifen. Caching oder vorberechnete Assets existieren nicht.

**Risiken:**
- Auf schwächeren Systemen oder bei größerem Sprite-Sheet droht spürbarer Delay beim Start.
- Folgefeatures (z. B. animierte Tiles) würden den Ansatz sprengen.

**Empfohlene Richtung:** Im Zuge der Architekturtrennung sollte das Asset-Handling eine eigene Verantwortlichkeit erhalten und vorberechnete Varianten cachen.

## Fazit
Kurzfristig funktioniert das Spiel, langfristig blockiert die monolithische Struktur aber neue Features. Die priorisierten Schritte sind in den verlinkten To-dos beschrieben. Bei deren Umsetzung muss die Dokumentation der betroffenen Ordner aktualisiert werden.
