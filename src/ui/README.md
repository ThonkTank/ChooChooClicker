# Paket `src/ui/`

```text
src/ui/
├── README.md
├── __init__.py
├── app.py
└── camera.py
```

## Zweck
Dieses Paket enthält alle Tkinter-Komponenten. Es konsumiert die Spiel- und Weltlogik über Callbacks (`GameEngine.add_tick_listener`) und übernimmt Rendering sowie User-Interaktion.

## Module & Hauptfunktionen
- **`app.py`**
  - `ChooChooApp` – Hauptfenster, bindet das `GameEngine`-Interface ein, verwaltet das Canvas-Rendering und die Momentum-Steuerung per Button.
- **`camera.py`**
  - `CameraView` – berechnet den sichtbaren Ausschnitt des Karten-Canvas, kapselt die Zentrierung auf Zellen und synchronisiert Scrollpositionen ohne direkten Tk-Abhängigkeiten.

## Standards & Konventionen
- UI-Code interagiert ausschließlich über öffentliche APIs aus `game` und `world`.
- Tick-Handling erfolgt über `GameEngine.tick()` und Listener, nicht über direkte Zustandsänderung.
- Neue UI-Komponenten benötigen eigene Unterordner samt README, falls sie umfangreicher werden (z. B. `src/ui/widgets/`).

## Kamera/Viewport
- `CameraView` verwaltet Zellgröße, Kartenabmessungen und Viewport als unveränderliche Parameter. Änderungen erfolgen ausschließlich über `center_on(Cell)`.
- `apply(SupportsCanvas)` setzt die Scrollregion und berechnet Canvas-Offsets ausschließlich dann, wenn sich der Ziel-Viewport tatsächlich verändert hat.
- `ChooChooApp` initialisiert die Kamera vor dem ersten Renderdurchlauf und aktualisiert sie nur bei echten Bewegungen des Zuges, wodurch das frühere Kamera-Flackern aus [todo/camera-initialization-timing.md](../../todo/archive/camera-initialization-timing.md) entfällt. Der Abschluss ist im [Analyse-Dossier](../../Task/analysis-plan.md) dokumentiert.

## Weiterführende Dokumentation
- [Spiel-Logik `src/game/`](../game/README.md)
- [Asset-Verwaltung `src/assets/`](../assets/README.md)
- [Projektstart](../../README.md)
