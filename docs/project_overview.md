---
id: project_overview
title: Projektüberblick
status: draft
date: 2025-09-29
tags: [overview, architecture, state-management]
---

# Choo Choo Clicker – Projektüberblick

## Zielbild & Nutzererlebnis
- Referenzvision: `docs/intended_experience/overview.md` beschreibt das entspannte Clicker-Erlebnis mit Kurbel-Momentum und frei platzierbaren Schienen.
- Fokus: Eine lokal laufende React-Anwendung, die Momentum-Management, Gleisbau und Zugsteuerung in einem klar strukturierten UI vereint.

## Technische Architektur
- **Frontend-Stack:** Vite + React + TypeScript (lokale SPA).
- **State-Management:** Zentraler Reducer (`src/state/gameReducer.ts`) plus React Context (`src/state/GameStateContext.tsx`) stellen Spielzustand und Aktionen bereit.
- **Typing:** Gemeinsame Datentypen liegen in `src/state/gameTypes.ts` und werden via `src/state/index.ts` re-exportiert.
- **Testing:** Vitest-Suite `src/state/gameReducer.test.ts` deckt Kernaktionen (Momentum, Gleise, Weichen, Zugbewegung) ab.

## Spielzustand & Aktionen
- `createInitialGameState` erzeugt ein 12×12-Grid mit leerem Gleisnetz, Momentum-Limit (0–10) und einem zentral positionierten Zug.
- Momentum-Aktionen (`addMomentum`, `consumeMomentum`, `setMomentum`) validieren Grenzen, so dass nie mehr als das Maximalmomentum gespeichert oder verbraucht wird.
- Gleisaktionen (`placeTrack`, `removeTrack`) verwalten das `tracks`-Mapping, wobei Koordinaten außerhalb des Grids abgefangen werden.
- `setSwitch` aktualisiert Weichen ausschließlich für Kreuzungssegmente und verhindert Fehlkonfigurationen für andere Gleisarten.
- `setTrainPosition` begrenzt Zugbewegungen auf gültige Rasterfelder und markiert den Zugstatus als `moving`.

## Integration im React-Tree
- `GameStateProvider` kapselt `useReducer` und stellt `state`/`dispatch` via getrennten Contexts bereit.
- Hilfshooks `useGameState`, `useGameDispatch`, `useGameStore` verhindern Fehlverwendung außerhalb des Providers.
- Komponenten importieren State-Funktionen über `src/state/index.ts`, wodurch Tests und UI denselben Vertrag teilen.

## Offene Arbeiten / Roadmap
- UI muss noch konkreten Zugriff auf das State-Modul erhalten (z. B. Canvas-/Panel-Komponenten anbinden).
- Momentum- und Gleisinteraktionen im UI benötigen Integrationstests, sobald die visuellen Module stehen.
- Dokumentation der Rendering- und UI-Module ergänzen, sobald diese implementiert sind.
