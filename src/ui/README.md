# Paket `src/ui/`

```text
src/ui/
├── README.md
├── __init__.py
├── app.py
├── camera.py
└── scaling.py
```

## Zweck
Dieses Paket enthält alle Tkinter-Komponenten. Es konsumiert die Spiel- und Weltlogik über Callbacks (`GameEngine.add_tick_listener`) und übernimmt Rendering sowie User-Interaktion.

## Module & Hauptfunktionen
- **`app.py`**
  - `ChooChooApp` – Hauptfenster, bindet das `GameEngine`-Interface ein, verwaltet das Canvas-Rendering und die Momentum-Steuerung per Button.
- **`camera.py`**
  - `CameraView` – berechnet den sichtbaren Ausschnitt des Karten-Canvas, kapselt die Zentrierung auf Zellen und synchronisiert Scrollpositionen ohne direkten Tk-Abhängigkeiten.
- **`scaling.py`**
  - `compute_scaling(root)` – liest den DPI-Faktor über Tk, begrenzt ihn auf 0.75–3.0 und erlaubt eine Überschreibung via `CHOOCHOO_TK_SCALING`.

## Standards & Konventionen
- UI-Code interagiert ausschließlich über öffentliche APIs aus `game` und `world`.
- Tick-Handling erfolgt über `GameEngine.tick()` und Listener, nicht über direkte Zustandsänderung.
- Neue UI-Komponenten benötigen eigene Unterordner samt README, falls sie umfangreicher werden (z. B. `src/ui/widgets/`).
- DPI-Anpassungen nutzen `compute_scaling` und setzen `root.tk.call("tk", "scaling", factor)` bevor Widgets erstellt werden.
- Feste Pixelwerte (Fonts, Abstände, Cell-Size) werden über Hilfsfunktionen skaliert; Overrides sind über `CHOOCHOO_TK_SCALING` möglich.

## Sprite-Belegung `Ground-Rails.png`

| Sprite-Key | Tile (Spalte, Zeile) | Form | Hinweise |
| --- | --- | --- | --- |
| `ground` | `(0, 0)` | Grundfläche | Vollflächiger Untergrund, Grundlage für alle Tiles. |
| `track_straight_ns` | `(1, 1)` | Gerade (Nord/Süd) | 90°-Rotation liefert `track_straight_ew`. |
| `track_curve_ne` | `(2, 1)` | Kurve (Nord→Ost) | Rotationen erzeugen `track_curve_se`, `track_curve_sw`, `track_curve_nw`. |
| `track_t_north` | `(0, 1)` | T-Kreuzung (ohne Nordanschluss) | Öffnet nach Ost/Süd/West; das Key-Suffix benennt die fehlende Richtung. |
| `track_t_east` | `(2, 3)` | T-Kreuzung (ohne Ostanschluss) | Öffnet nach Nord/Süd/West. |
| `track_t_south` | `(0, 2)` | T-Kreuzung (ohne Südanschluss) | Öffnet nach Nord/Ost/West. |
| `track_t_west` | `(1, 3)` | T-Kreuzung (ohne Westanschluss) | Öffnet nach Nord/Ost/Süd. |
| `track_cross` | `(0, 3)` | Vier-Wege-Kreuzung | Alle vier Richtungen aktiv. |

## Kamera/Viewport
- `CameraView` verwaltet Zellgröße, Kartenabmessungen und Viewport als unveränderliche Parameter. Änderungen erfolgen ausschließlich über `center_on(Cell)`.
- `apply(SupportsCanvas)` setzt die Scrollregion und berechnet Canvas-Offsets ausschließlich dann, wenn sich der Ziel-Viewport tatsächlich verändert hat.
- `ChooChooApp` initialisiert die Kamera vor dem ersten Renderdurchlauf und aktualisiert sie nur bei echten Bewegungen des Zuges, wodurch das frühere Kamera-Flackern aus [todo/camera-initialization-timing.md](../../todo/archive/camera-initialization-timing.md) entfällt. Der Abschluss ist im [Analyse-Dossier](../../Task/analysis-plan.md) dokumentiert.
- Der DPI-Workflow ist in [todo/ui-scaling-dpi.md](../../todo/ui-scaling-dpi.md) nachverfolgt; Endanwender erhalten eine Anleitung im [User-Wiki](../../UserWiki/ui-dpi-skalierung.md).

## Weiterführende Dokumentation
- [Spiel-Logik `src/game/`](../game/README.md)
- [Asset-Verwaltung `src/assets/`](../assets/README.md)
- [Projektstart](../../README.md)
