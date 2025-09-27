# UI-Skalierung: DPI-Anpassung überprüfen

## Kontext
Auf hochauflösenden Displays sind Texte und Buttons unscharf. Die Beobachtungen und Hypothesen sind in den [Rendering-Notizen](../Task/rendering-notes.md) dokumentiert.

## Betroffene Module
- [`src/ui/app.py`](../src/ui/app.py)
- UI-Konfigurationspfade (Theme-, DPI-Handling)

## Lösungsideen
- DPI-Auto-Detection im App-Initialisierer prüfen und bei Bedarf einen expliziten Skalierungsfaktor setzen.
- Screenshot-Vergleich (100 %, 150 %, 200 %) erstellen, um Verbesserungen zu verifizieren.
- Ergebnis nach Umsetzung im User-Wiki dokumentieren.

## Testergebnisse (2025-09-27)
- `pytest tests/ui/test_scaling.py` – simuliert 75–250 % DPI und prüft Canvas-/Font-Skalierung sowie den Override über `CHOOCHOO_TK_SCALING`.

## Folgeaktivitäten
- Anleitung für Anwender:innen im [User-Wiki](../UserWiki/ui-dpi-skalierung.md) hinterlegen (erledigt).

## Offene Fragen & Verantwortlichkeit
- **Verantwortlich:** TBD – zuweisen nach Bestätigung im [Analyse-Dossier](../Task/analysis-plan.md).
- **Offene Frage:** Welche Mindestanforderungen haben wir für UI-Schärfe auf 4k-Monitoren?
