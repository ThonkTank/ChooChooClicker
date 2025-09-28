# Choo Choo Clicker – Projektleitfaden

Choo Choo Clicker ist ein Clicker-Spiel rund um einen kleinen Zug. Die Anwendung soll lokal laufen.
Der grundlegende Gameplay Loop besteht darin, den zug über eine aus einem Grid bestehende Karte fahren zu lassen. Der user kann eine Kurbel betätigen, um dem Zug Momentum zu geben. Momentum wird pro Schritt zur nächsten Kachel verbraucht. Es kann bis zu 10 Momentum gespeichert werden. Mit Rechtsklick kann der Spieler schienen entfernen oder hinzufügen. Dabei gibt es grade schienen, kurven und kreuzungen. An Kreuzungen hat jeder ausgang eine Weiche, welche bestimmt wie der Zug abbiegt. Die Weiche kann mit linksklick gestellt werden.

Die UI besteht aus drei Komponenten. Einem Karten Fenster links, einer Menü Leiste mit resourcen trackern oben und einem Ui Panel rechts. Die Karte enthält die graphische Darstellung der Welt, das Ui panel die Klicker-menü elemente.

## Architektur & Spielzustand

- **State-Management:** `src/state/gameReducer.ts` bündelt alle Spielaktionen (Momentum, Gleise, Weichen, Zugbewegung). Der Reducer wird über den `GameStateProvider` (`src/state/GameStateContext.tsx`) als React Context bereitgestellt.
- **Typisierung:** Gemeinsame Datentypen liegen in `src/state/gameTypes.ts` und werden über `src/state/index.ts` re-exportiert.
- **Initialzustand:** `createInitialGameState` erzeugt ein 12×12-Grid, setzt den Zug mittig und begrenzt Momentum standardmäßig auf 10.
- **Tests:** `src/state/gameReducer.test.ts` prüft Momentum-Grenzen, Gleisplatzierung, Weichen-Updates und Zugbewegungen.

Weitere Details zur Zielvision und Architektur findest du in `docs/project_overview.md`.

## Entwicklung

```bash
npm install
npm run dev
```

## Tests

```bash
npm test
```
