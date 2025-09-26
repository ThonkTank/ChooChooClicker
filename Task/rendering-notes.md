# Rendering-Abweichungen & Beobachtungen

Diese Notizen verfolgen aktuelle Abweichungen zwischen erwartetem und tatsächlichem Rendering. Die Dokumentation dient als Zwischenschritt, bis konkrete Maßnahmen als To-do erfasst und umgesetzt sind.

## Aktueller Befund (Stand: laufende Untersuchung) {#statuslaufend}
- **UI-Skalierung im Hauptfenster** – Text- und Button-Elemente skalieren auf hochauflösenden Displays unscharf. Vermutete Ursache: Layout- und DPI-Behandlung in [`src/ui/app.py`](../src/ui/app.py).
- **Sprite-Offsets bei Assets** – Mehrere Fahrzeug-Sprites erscheinen um 1–2 Pixel verschoben, besonders während Animationen. Prüfung der Sprite-Daten und Bounding-Boxes in [`src/assets/sprites.py`](../src/assets/sprites.py) erforderlich.
- **Rotationen des SpriteSheets** – Die neuen Tests [`tests/assets/test_sprites.py`](../tests/assets/test_sprites.py) bestätigen die korrekte Uhrzeigersinn-Interpretation der 90°-Rotation; derzeit kein Handlungsbedarf.
- **Kamera-Tracking beim Start** – Beim Initialisieren der Karte springt die Kamera kurzzeitig an eine falsche Position, bevor sie sich fängt. Der initiale Szenenaufbau in [`src/main.py`](../src/main.py) muss auf Timing und Update-Reihenfolge überprüft werden.

## Geplante Vertiefungen
- Messung der tatsächlichen Sprite-Abmessungen gegenüber den Source-Dateien.
- Vergleich der Render-Logs zwischen verschiedenen Plattformen (Windows/Linux).
- Erfassung von Screenshots für Vorher/Nachher-Dokumentation.

## Nächste Schritte & Übergaben
1. Hypothesen durch Tests oder Debug-Ausgaben verifizieren.
2. Erkenntnisse als spezifische To-dos im [`todo/`](../todo/README.md)-Verzeichnis erfassen.
3. Umsetzungsergebnisse in den Modul-Readmes spiegeln; diese Datei anschließend aktualisieren oder archivieren.

## Platz für weitere Beobachtungen {#weitere-beobachtungen}
- _Neue Beobachtungen hier ergänzen (mit Datum, Kontext und betroffenen Modulen)._
- **2024-05-09** _Track-Sprite-Selektion_: Neuer Pytest
  [`tests/ui/test_track_sprite_selection.py`](../tests/ui/test_track_sprite_selection.py) bestätigt die
  erwarteten Sprite-Keys für alle Randzellen des Initial-Rings (Kurven + Gerade). Keine Abweichungen
  festgestellt.
  - Offene Frage: Für T-Kreuzungen (`TrackShape.T_JUNCTION`) und Kreuzungen (`TrackShape.CROSS`) fehlen
    weiterhin explizite Sprite-Mappings im UI-Code und damit Testabdeckung.

## Hand-off
- Die Statusübersicht, Verantwortlichkeiten und Folge-To-dos sind im [Analyse-Dossier](./analysis-plan.md) konsolidiert.
- Offene Arbeiten zu UI-Skalierung, Sprite-Offsets, Kamera-Start und Track-Sprite-Mappings werden dort verfolgt und auf die jeweiligen [`todo/`-Einträge](../todo/README.md) referenziert.

