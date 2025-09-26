# Kamera-Initialisierung stabilisieren

## Kontext
Beim Spielstart springt die Kamera kurzzeitig an eine falsche Position. Die Problembeschreibung stammt aus den [Rendering-Notizen](../Task/rendering-notes.md).

## Betroffene Module
- [`src/main.py`](../src/main.py)
- Event-Loop / Initialisierung der Szene

## Lösungsideen
- Initiale Kamera- und Map-Setup-Sequenz profilen (Frame-für-Frame).
- Reihenfolge der Update- und Render-Calls anpassen, um Race-Conditions zu eliminieren.
- Regressionstest schreiben, der das Kamera-Verhalten beim Start validiert.

## Offene Fragen & Verantwortlichkeit
- **Verantwortlich:** Gameplay-Engineering (Owner zu bestätigen im [Analyse-Dossier](../Task/analysis-plan.md)).
- **Offene Frage:** Müssen wir die Szene bereits vor dem ersten Render-Frame vorinitialisieren, um Jitter zu vermeiden?
