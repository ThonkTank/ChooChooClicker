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

## Sprite-Schlüssel & Bedeutung
| Sprite-Key | Tile (`Spalte,Zeile`) | Beschreibung |
| ---------- | -------------------- | ------------ |
| `ground` | `(0,0)` | Bodentextur der Karte. |
| `track_straight_ns` | `(1,3)` | Nord↔Süd-Verbindung, Schienen verlaufen entlang der Ostkante des Tiles. |
| `track_straight_ew` | `(0,1)` | Ost↔West-Verbindung, nutzt die native horizontale Variante des Sheets. |
| `track_curve_ne` | `(1,2)` | Kurve von Norden nach Osten. |
| `track_curve_se` | `(1,2)` (Rotation `90°`) | Kurve von Osten nach Süden. |
| `track_curve_sw` | `(1,2)` (Rotation `180°`) | Kurve von Süden nach Westen. |
| `track_curve_nw` | `(1,2)` (Rotation `270°`) | Kurve von Westen nach Norden. |

Die zugrunde liegenden Tile-Orientierungen sind in [`Task/rendering-notes.md`](../../Task/rendering-notes.md) detailliert beschrieben und werden durch [`tests/ui/test_sprite_mapping.py`](../../tests/ui/test_sprite_mapping.py) automatisiert überprüft. Die Implementation referenziert die Konstantentabelle `SPRITE_COORDINATES` in [`app.py`](./app.py), sodass Dokumentation und Tests auf dieselben Metadaten zugreifen.

## Standards & Konventionen
- UI-Code interagiert ausschließlich über öffentliche APIs aus `game` und `world`.
- Tick-Handling erfolgt über `GameEngine.tick()` und Listener, nicht über direkte Zustandsänderung.
- Neue UI-Komponenten benötigen eigene Unterordner samt README, falls sie umfangreicher werden (z. B. `src/ui/widgets/`).

## Weiterführende Dokumentation
- [Spiel-Logik `src/game/`](../game/README.md)
- [Asset-Verwaltung `src/assets/`](../assets/README.md)
- [Projektstart](../../README.md)
