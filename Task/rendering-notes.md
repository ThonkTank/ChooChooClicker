# Rendering-Abweichungen & Beobachtungen

Diese Notizen verfolgen aktuelle Abweichungen zwischen erwartetem und tatsächlichem Rendering. Die Dokumentation dient als Zwischenschritt, bis konkrete Maßnahmen als To-do erfasst und umgesetzt sind.

## Ground-Rails-Sheet (Tile-Orientierungen)

Die folgenden Koordinaten beziehen sich auf das `32x32`-Raster des Sprite-Sheets `Ground-Rails.png` **ohne** Zwischenabstände. Die Zuordnung wurde mit dem Hilfsskript [`Task/ground_rails_summary.py`](./ground_rails_summary.py) ermittelt (`python Task/ground_rails_summary.py Ground-Rails.png`).

| Spalte | Zeile | Beschreibung | Verwendet durch |
| ------ | ----- | ------------ | --------------- |
| 0 | 0 | Erd-/Grund-Texture, vollflächig | `ground` |
| 0 | 1 | Gerade Ost↔West, Schienenband im unteren Halbfeld | `track_straight_ew` |
| 0 | 2 | Gerade Ost↔West, Schienenband im oberen Halbfeld | – (Reserve) |
| 1 | 2 | Kurve Nord→Ost (NE) | `track_curve_ne` |
| 1 | 3 | Gerade Nord↔Süd, Schienenband an der Ostkante | `track_straight_ns` |
| 2 | 1 | Kurve Süd→West (SW) | Rotation aus `track_curve_ne` |
| 2 | 2 | Kurve Nord→West (NW) | Rotation aus `track_curve_ne` |
| 2 | 3 | Gerade Nord↔Süd, Schienenband an der Westkante | – (Reserve) |
| 3 | 1 | Gerade Ost↔West, Alternative (unten, stärkerer Schatten) | – (Reserve) |
| 3 | 2 | Gerade Ost↔West, Alternative (oben, stärkerer Schatten) | – (Reserve) |
| 3 | 3 | Bodendetail / Kurve ohne Schienenanteil | – (Reserve) |

Weitere Tiles (z. B. `(3,1)`/`(3,2)` horizontale Varianten oder `(0,3)` zusätzliche Bodentextur) bleiben vorerst ungenutzt. Die aktive Auswahl wird in [`src/ui/app.py`](../src/ui/app.py) dokumentiert und durch die Tests in [`tests/ui/test_sprite_mapping.py`](../tests/ui/test_sprite_mapping.py) abgesichert.

## Aktueller Befund (Stand: laufende Untersuchung)
- **UI-Skalierung im Hauptfenster** – Text- und Button-Elemente skalieren auf hochauflösenden Displays unscharf. Vermutete Ursache: Layout- und DPI-Behandlung in [`src/ui/app.py`](../src/ui/app.py).
- **Sprite-Offsets bei Assets** – Mehrere Fahrzeug-Sprites erscheinen um 1–2 Pixel verschoben, besonders während Animationen. Prüfung der Sprite-Daten und Bounding-Boxes in [`src/assets/sprites.py`](../src/assets/sprites.py) erforderlich.
- **Kamera-Tracking beim Start** – Beim Initialisieren der Karte springt die Kamera kurzzeitig an eine falsche Position, bevor sie sich fängt. Der initiale Szenenaufbau in [`src/main.py`](../src/main.py) muss auf Timing und Update-Reihenfolge überprüft werden.

## Geplante Vertiefungen
- Messung der tatsächlichen Sprite-Abmessungen gegenüber den Source-Dateien.
- Vergleich der Render-Logs zwischen verschiedenen Plattformen (Windows/Linux).
- Erfassung von Screenshots für Vorher/Nachher-Dokumentation.

## Nächste Schritte & Übergaben
1. Hypothesen durch Tests oder Debug-Ausgaben verifizieren.
2. Erkenntnisse als spezifische To-dos im [`todo/`](../todo/README.md)-Verzeichnis erfassen.
3. Umsetzungsergebnisse in den Modul-Readmes spiegeln; diese Datei anschließend aktualisieren oder archivieren.

## Platz für weitere Beobachtungen
- _Neue Beobachtungen hier ergänzen (mit Datum, Kontext und betroffenen Modulen)._ 

