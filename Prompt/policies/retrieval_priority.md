# Retrieval-Prioritäten

## Reihenfolge der Quellen
1. **Architecture Decision Records (ADR)**
2. **Changelog**
3. **`project_overview`-Dokumente**
4. **`intended_experience`-Dokumentation**
5. **Tickets** (z. B. in `tasks/tickets/`)
6. **Weitere Quellen** (Code, Wikis, sonstige Dokumente)

Nutze diese Reihenfolge sowohl beim Sammeln von Informationen als auch bei widersprüchlichen Vorgaben. Höher priorisierte Quellen überstimmen niedrigere.

## Zitierregeln
- Beziehe dich in Statusberichten und Dokumentation explizit auf die verwendeten Quellen (Dateipfad oder Chunk-ID).
- Wenn mehrere Quellen zusammengefasst werden, führe jede relevante Quelle separat auf.

## Konfliktlösung
- Priorisierte Quelle gewinnt: Stelle fest, welche Anweisung aus der höher priorisierten Quelle stammt, und folge dieser.
- Unklare oder gleichrangige Konflikte dokumentierst du im `decision_log` der Loop-Notizen und holst bei Bedarf eine Entscheidung der Projektleitung ein.
- Erfordert der Konflikt eine schnelle Klärung, nutze den Clarification-Prozess und eskaliere an den Supervisor.

---
**Zusammenspiel mit `AGENTS.md`:** Diese Prioritäten erweitern die hierarchischen Vorgaben aus `AGENTS.md`. Prüfe zuerst die für deinen Arbeitsbereich gültigen `AGENTS.md`-Dateien und ordne anschließend alle weiteren Informationen gemäß obiger Liste ein.
