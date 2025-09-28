# Dokumentationsstruktur

Diese Datei beschreibt die einheitliche Dokumentationsstruktur des Projekts. Alle beteiligten Agenten müssen sich an diese Struktur halten, um sicherzustellen, dass relevante Informationen an einer festen Stelle gespeichert sind und von Codex über Sessions hinweg wiedergefunden werden können.

## Hauptverzeichnisse

| Ordner | Inhalt | Zweck |
| --- | --- | --- |
| `docs/` | Menschenlesbare Dokumentation: `project_overview.md`, `decisions/`, `CHANGELOG.md`, `loop_notes.md`, `documentation_structure.md` | Stellt Ziele, Architektur, ADRs, Änderungsprotokolle und den aktuellen Stand des Arbeitszyklus bereit. |
| `context/` | Maschinenlesbarer Kontext: `knowledge.jsonl`, `glossary.md`, `standards/` | Enthält Chunks mit Metadaten, Glossar, Coding‑ und Dokumentationsstandards. |
| `memory/` | Session‑Snapshots und Entscheidungslog: `session_<Datum>.md`, `decisions.jsonl`, `logbook/` | Bewahrt die Historie jeder Arbeitssession, einschließlich Zusammenfassungen, Entscheidungen und offener Fragen. |
| `tasks/` | Aufgabenmanagement: `backlog.jsonl`, `dag.json` | Enthält das versionierte Backlog und den Abhängigkeitsgraphen für alle Tasks. |
| `system/` | Globaler Prompt und Guardrails | Enthält `system_prompt.md` (oder `.yaml`) sowie ergänzende Regeln und Richtlinien. |
| `ops/roles/` | Rollen‑Prompts und Checklisten | Definiert die detaillierten Arbeitsanweisungen für Planer, Ausführer, Dokumentations‑Agent und Supervisor. |

## Dateiformate und Metadaten

- **Markdown mit YAML‑Frontmatter** für menschenlesbare Dateien: Jede Datei beginnt mit einem Frontmatter‑Block (`---`), der Metadaten wie `id`, `title`, `author`, `date`, `tags` und `status` enthält.
- **JSONL (JSON‑Lines)** für maschinenlesbare Daten (`knowledge.jsonl`, `backlog.jsonl`, `decisions.jsonl`): Jede Zeile ist ein eigenständiges JSON‑Objekt mit eindeutiger `id`, `source`, `timestamp`, `summary`, `text` und optionalen Feldern.
- **Versionierung**: Alle Dokumente liegen in einem Versionskontrollsystem. Alte Versionen werden nicht gelöscht, sondern archiviert und mit Tags versehen (`superseded`, `deprecated`).

## Aktualisierungsregeln

1. **Loop‑Notizen** werden nach jeder Rolle ergänzt, um den nächsten Zyklus‑Schritt und benötigte Informationen festzuhalten.
2. **ADRs und Changelogs** werden aktualisiert, wenn Entscheidungen getroffen oder Funktionen geändert werden.
3. **Glossar und Standards** werden erweitert, wenn neue Begriffe oder Regeln eingeführt werden.

Durch diese klar definierte Struktur kann Codex fehlendes Langzeitgedächtnis überbrücken: alle relevanten Informationen befinden sich an bekannten, versionierten Orten und werden konsequent gepflegt.
