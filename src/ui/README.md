# Paket `src/ui/`

```text
src/ui/
├── README.md
├── __init__.py
└── app.py
```

## Zweck
Dieses Paket enthält alle Tkinter-Komponenten. Es konsumiert die Spiel- und Weltlogik über Callbacks (`GameEngine.add_tick_listener`) und übernimmt Rendering sowie User-Interaktion.

## Module & Hauptfunktionen
- **`app.py`**
  - `ChooChooApp` – Hauptfenster, bindet das `GameEngine`-Interface ein, verwaltet das Canvas-Rendering und die Momentum-Steuerung per Button.

## Standards & Konventionen
- UI-Code interagiert ausschließlich über öffentliche APIs aus `game` und `world`.
- Tick-Handling erfolgt über `GameEngine.tick()` und Listener, nicht über direkte Zustandsänderung.
- Neue UI-Komponenten benötigen eigene Unterordner samt README, falls sie umfangreicher werden (z. B. `src/ui/widgets/`).

## Weiterführende Dokumentation
- [Spiel-Logik `src/game/`](../game/README.md)
- [Asset-Verwaltung `src/assets/`](../assets/README.md)
- [Projektstart](../../README.md)
