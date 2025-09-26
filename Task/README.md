# Task-Dokumentationsknoten

```text
Task/
├── README.md
├── analysis-plan.md
└── rendering-notes.md
```

Dieses Verzeichnis bündelt alle laufenden Untersuchungen und Ad-hoc-Analysen für Choo Choo Clicker. Es dient als Arbeitsbereich für Hypothesen, Messungen und Vergleichsnotizen, bevor die Ergebnisse als To-dos oder dauerhafte Dokumentation übernommen werden.

## Zweck & Einbindung
- **Arbeitsprotokolle bündeln:** Hier werden temporäre Rechercheergebnisse, Debug-Notizen und explorative Erkenntnisse gesammelt.
- **Verlinkung zu offenen Punkten:** Jede Untersuchung, die zu einer konkreten Maßnahme führt, erhält einen Eintrag im [`todo/`](../todo/README.md)-Verzeichnis. Rückverweise halten den Bezug zwischen Erkenntnissen und To-dos nachvollziehbar.
- **Strukturierte Ablage:** Einzelne Themen werden als eigene Markdown-Dateien geführt und in diesem README gelistet.

## Struktur & Konventionen
- **Dateinamensschema:** `Task/<schwerpunkt>-notes.md` für themenspezifische Notizen.
- **Inhaltliche Mindeststruktur:** Datum, Ausgangsbeobachtung, Analyse, nächste Schritte / Hand-off.
- **Verlinkungen:** Immer betroffene Module, Screenshots oder externe Messungen referenzieren. Bei neuen To-dos in `todo/` bitte auf beide Richtungen verweisen.

Aktuell vorhandene Dokumente:
- [`analysis-plan.md`](./analysis-plan.md) – Zentrales Dossier mit Fortschrittstabelle, Verantwortlichkeiten und Verlinkung zu den Folge-To-dos im [`todo/`](../todo/README.md)-Verzeichnis.
- [`rendering-notes.md`](./rendering-notes.md) – Laufende Sammlung der Rendering-Abweichungen inklusive Querverweise zu betroffenen Modulen.

## Offene Untersuchungen
Die folgenden Analysen sind vorbereitet und warten auf detaillierte Ausarbeitung:
- **Sprite-Audit:** Sichtprüfung aller Assets auf Skalierung, Transparenz und Layering-Probleme.
- **Map-Vergleich:** Gegenüberstellung der In-Game-Karte mit den erwarteten Layouts aus dem User-Wiki.
- **Rotations-Checks:** Validierung der Sprite-Rotationen gegenüber den Steuerungsereignissen.

**Vorgehen für neue Notizen:**
1. Eine neue Datei im Muster `Task/<thema>-notes.md` anlegen und hier verlinken.
2. Einstieg mit Kontext (Datum, Reporter, Bezug) und klarer Problemhypothese.
3. Beobachtungen, Messungen und Entscheidungen dokumentieren.
4. Resultierende Maßnahmen als To-do im [`todo/`](../todo/README.md)-Verzeichnis hinterlegen und gegenseitig verlinken.
5. Wenn das Thema abgeschlossen ist, den Status hier aktualisieren (z. B. „abgeschlossen“ oder Verweis auf finale Dokumentation).

## Pflegeprozess für das Analyse-Dossier
- **Aktualisierung:** Nach jedem Stand-up oder sobald eine Untersuchung neuen Erkenntnisstand erreicht, die Fortschrittstabelle in [`analysis-plan.md`](./analysis-plan.md) aktualisieren (Status, Blocker, Owner).
- **Abschluss:** Wenn eine Untersuchung umgesetzt wurde und das zugehörige To-do geschlossen ist, den Eintrag im Dossier mit Abschlussdatum versehen und ggf. ins Archiv verschieben.
- **Synchronisation:** Neue Beobachtungen aus einzelnen Notizen (z. B. [`rendering-notes.md`](./rendering-notes.md)) zuerst dort dokumentieren und anschließend im Dossier verlinken, damit der Informationsfluss nachvollziehbar bleibt.

## Querverweise
- [`todo/README.md`](../todo/README.md) – Kanonische Liste der offenen Aufgaben.
- Modul-Dokumentationen in `src/` – Für Details zu den betroffenen Implementierungen.

Weitere Unterordner oder Detaildokumente werden bei Bedarf ergänzt und hier aufgenommen.
