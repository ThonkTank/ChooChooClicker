# Track-Sprite-Mappings für Sonderfälle ergänzen

## Kontext
Die PyTests decken die Sprite-Keys für Randzellen ab, aber T-Kreuzungen (`TrackShape.T_JUNCTION`) und Kreuzungen (`TrackShape.CROSS`) fehlen weiterhin. Die Beobachtung ist im Abschnitt "Platz für weitere Beobachtungen" der [Rendering-Notizen](../Task/rendering-notes.md) dokumentiert.

## Betroffene Module
- [`src/ui/`](../src/ui/README.md)
- Tests unter [`tests/ui/`](../tests/ui/README.md)

## Lösungsideen
- Sprite-Mappings im UI-Code ergänzen und dokumentieren.
- Tests erweitern, um neue Formen zu validieren.
- Render-Regressionstestbilder erstellen (optional) und dokumentieren.

## Offene Fragen & Verantwortlichkeit
- **Verantwortlich:** UI-Team (Owner TBD – Eintrag im [Analyse-Dossier](../Task/analysis-plan.md) aktualisieren).
- **Offene Frage:** Müssen wir die Asset-Pipeline erweitern, um die zusätzlichen Sprites automatisiert zu generieren?
