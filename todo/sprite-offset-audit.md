# Sprite-Offsets kalibrieren

## Kontext
Mehrere Fahrzeug-Sprites sind beim Rendern um 1–2 Pixel verschoben. Details zur Beobachtung finden sich im Abschnitt "Sprite-Offsets" der [Rendering-Notizen](../Task/rendering-notes.md).

## Betroffene Module
- [`src/assets/sprites.py`](../src/assets/sprites.py)
- Asset-Quellen im `assets/`-Ordner (extern verwaltet)

## Lösungsideen
- Bounding-Boxes gegen die Quelldateien messen und Abweichungen dokumentieren.
- Automatisierten Check in den Tests ergänzen, um künftige Regressionen zu verhindern.
- Anpassungen am SpriteSheet-Exporter dokumentieren.

## Offene Fragen & Verantwortlichkeit
- **Verantwortlich:** Art-Team (Bestätigung ausstehend) – Koordination über Tech Lead.
- **Offene Frage:** Müssen wir einen temporären Hotfix im Renderer implementieren, bis die Assets korrigiert sind?

## Messmethode 2024-05-10
- Neue Utility [`SpriteSheet.measure_bounds`](../src/assets/sprites.py) eingeführt, um nicht-transparente Pixel pro Tile zu bestimmen.
- Für die initiale Messreihe wurde das Sprite-Sheet `Ground-Rails.png` über das Utility (Offsets deaktiviert) ausgelesen. Ergänzend dient ein Python-Skript mit direkter PNG-Dekompression als Quervergleich (keine Abweichungen festgestellt).
- Transparenz wird als Alpha = 0 bzw. `None` interpretiert; Bounding-Boxes liefern `(min_x, min_y, max_x, max_y)` relativ zum 32×32-Tile.

## Ergebnisse & Offsets
| Tile (Spalte, Zeile) | Bounding-Box (roh) | Empfohlener Offset (x, y) |
| --- | --- | --- |
| (0, 1) | (0, 16, 31, 31) | (0, -8) |
| (1, 1) | (16, 16, 31, 31) | (-8, -8) |
| (2, 1) | (0, 16, 15, 31) | (8, -8) |
| (3, 1) | (0, 16, 31, 31) | (0, -8) |
| (0, 2) | (0, 0, 31, 15) | (0, 8) |
| (1, 2) | (16, 0, 31, 15) | (-8, 8) |
| (2, 2) | (0, 0, 15, 15) | (8, 8) |
| (3, 2) | (0, 0, 31, 15) | (0, 8) |
| (1, 3) | (16, 0, 31, 31) | (-8, 0) |
| (2, 3) | (0, 0, 15, 31) | (8, 0) |

- Die Offsets sind in `SPRITE_OFFSETS` hinterlegt und werden beim Kopieren in `_get_base_tile` angewendet.
- Regressionstests: [`tests/assets/test_sprite_offsets.py`](../tests/assets/test_sprite_offsets.py) deckt Messung und Offset-Anwendung ab.

## Nächste Schritte
- Sichtprüfung der übrigen Tiles (Spalte 0/Zeile 0 ff.) – bislang keine Abweichungen festgestellt, aber künftige Art-Updates beobachten.
- UI-Validierung: neue Screenshots im Rendering-Dossier ergänzen, sobald die Offsets im Spiel bestätigt wurden.
- Abstimmung mit dem Art-Team zur dauerhaften Anpassung der Quelldateien; bis dahin bleiben die Offsets aktiv.
