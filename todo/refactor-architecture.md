# Refactoring der Spiel-Architektur

## Kontext
`src/app.py` bündelt aktuell Spielzustand, Kartenlogik, Rendering und Tkinter-UI. Diese Monolith-Struktur erschwert Tests, Erweiterungen und Portierungen. Details siehe [Struktur-Review](../docs/structure-review.md#1-monolithische-app.py).

## Betroffene Module
- [`src/app.py`](../src/README.md)
- zukünftige Unterordner innerhalb von `src/` (z. B. `src/game/`, `src/ui/`)

## Zielbild & Lösungsideen
1. **Schichten aufbrechen**
   - `game`-Paket für reine Spiellogik (Trainbewegung, Momentum, Ressourcen).
   - `map`- oder `world`-Paket für Tiles, Strecken und deren Serialisierung.
   - `ui`-Paket für Tkinter-spezifische Widgets und Event-Handling.
2. **Klare Schnittstellen definieren**
   - Spiellogik darf keine Tkinter-Objekte kennen; stattdessen Events oder Callbacks.
   - Rendering konsumiert ein reines Datenmodell (z. B. Liste von Tiles, Zugposition).
3. **Tests ermöglichen**
   - Spiel- und Map-Logik durch Unit-Tests abdecken, ohne GUI zu initialisieren.
4. **Dokumentation erweitern**
   - Für neue Pakete eigene `README.md` anlegen und im Root-Index verlinken.

## Offene Fragen
- Welche Spielfunktionen sind kurzfristig geplant (z. B. Ressourcensystem), die beim Zuschnitt der Module berücksichtigt werden müssen?
- Soll ein zukünftiger Speicherslot/Savegame-Mechanismus berücksichtigt werden?
