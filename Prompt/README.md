# Prompt-Paket Übersicht

Dieses Verzeichnis bündelt alle Arbeitsanweisungen, Rollenprompts, Leitfäden und Vorlagen, die den Projektzyklus strukturieren. Lies vor jeder Session `loop_notes.md`, konsultiere dann den passenden Rollenprompt unter `roles/` und befolge die in `AGENTS.md` beschriebenen Guardrails.

## Dokumentationsstruktur

| Ordner | Inhalt | Zweck |
| --- | --- | --- |
| `docs/` | Menschenlesbare Dokumentation: `project_overview.md`, `decisions/`, `CHANGELOG.md`, `loop_notes.md`, `documentation_structure.md` | Stellt Ziele, Architektur, ADRs, Änderungsprotokolle und den aktuellen Stand des Arbeitszyklus bereit. |
| `context/` | Maschinenlesbarer Kontext: `knowledge.jsonl`, `glossary.md`, `standards/` | Enthält Chunks mit Metadaten, Glossar, Coding- und Dokumentationsstandards. |
| `memory/` | Session-Snapshots und Entscheidungslog: `session_<Datum>.md`, `decisions.jsonl`, `logbook/` | Bewahrt die Historie jeder Arbeitssession, einschließlich Zusammenfassungen, Entscheidungen und offener Fragen. |
| `tasks/` | Aufgabenmanagement: `backlog.jsonl`, `dag.json` | Enthält das versionierte Backlog und den Abhängigkeitsgraphen für alle Tasks. |
| `system/` | Globaler Prompt und Guardrails | Enthält `system_prompt.md` (oder `.yaml`) sowie ergänzende Regeln und Richtlinien. |
| `Prompt/roles/` | Rollen-Prompts und Checklisten | Definiert die detaillierten Arbeitsanweisungen für Planer, Ausführer, Dokumentations-Agent und Supervisor. |

**Metadaten & Pflege:**
- Nutze Markdown mit YAML-Frontmatter für menschenlesbare Dateien (`id`, `title`, `author`, `date`, `tags`, `status`).
- Speichere maschinenlesbare Daten als JSON-Lines (`id`, `source`, `timestamp`, `summary`, `text`).
- Versioniere Änderungen statt Dateien zu löschen; markiere alte Fassungen als `superseded` oder `deprecated`.
- Aktualisiere `loop_notes.md` nach jeder Rolle, pflege ADRs & Changelog bei Entscheidungen und halte Glossar sowie Standards auf dem neuesten Stand.

## Projektüberblick

### Zielsetzung und Nutzererlebnis
Halte die Vision des Projekts prägnant fest: gewünschtes Verhalten, Nutzerinteraktionen und Qualitätskriterien. Ausführliche Beschreibungen zur intended user experience leben im Wiki unter `docs/intended_experience/`. Die Einstiegsseite `docs/intended_experience/overview.md` verlinkt Feature-Seiten (`docs/intended_experience/features/`) und Detailseiten (`docs/intended_experience/details/`). Pflege diese Struktur gemeinsam mit dem Visionary, markiere veraltete Inhalte als `superseded` und dokumentiere Änderungen nachvollziehbar.

### Architekturprinzipien & Roadmap
Skizziere grundlegende Architekturprinzipien, Module und Meilensteine im Projekt-README oder in ADRs. Verweise bei Entscheidungen auf entsprechende ADRs in `docs/decisions/` und halte das Changelog aktuell, sodass jede Rolle schnell den Status des Systems nachvollziehen kann.
