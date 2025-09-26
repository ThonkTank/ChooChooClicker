# Paket `src/game/`

```text
src/game/
├── README.md
├── __init__.py
└── train.py
```

## Zweck
Dieses Paket kapselt Spiellogik, die unabhängig vom UI-Framework funktionieren muss. Insbesondere verwaltet `train.py` den Zugzustand, Momentum-Regeln sowie die Tick-Verarbeitung.

## Module & Hauptfunktionen
- **`train.py`**
  - `Train` – Datenmodell für Position, Richtung und Momentum.
  - `TrainState` – unveränderliche Momentaufnahme für Rendering-Schichten.
  - `GameEngine` – koordiniert Tick-Zyklen, verteilt Ergebnisse über `TickListener`-Callbacks.
  - `TickResult` – Payload für Tick-Events.

## Standards & Konventionen
- Spiellogik darf keine UI- oder Tkinter-spezifischen Typen importieren.
- Datenübergaben erfolgen über dataklassen-basierte Snapshots (`TrainState`, `TickResult`).
- Neue Spielsysteme müssen Callbacks nutzen, um Ereignisse nach außen zu publizieren, statt direkt UI-Objekte zu manipulieren.

## Weiterführende Dokumentation
- [Projektübersicht](../../README.md)
- [Weltmodell `src/world/`](../world/README.md) – referenziert durch `GameEngine.game_map`.
- [UI-Schicht `src/ui/`](../ui/README.md) – konsumiert die Tick-Events für Rendering.
