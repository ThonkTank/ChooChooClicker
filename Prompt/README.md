# Prompt-Verzeichnis

## Zweck
Dieses Verzeichnis dient als zentrale Quelle für alle Projektprompts, Guardrails und Arbeitsunterlagen, damit jede Rolle im Loop konsistent arbeiten kann. Es bündelt die Vorgaben aus `AGENTS.md`, liefert Rollen-spezifische Hilfen und stellt wiederverwendbare Vorlagen bereit.

## Zielgruppe
Die Materialien richten sich an alle Projektrollen (Visionary, Planner, Implementation, Documentation, Supervisor), die nach dem kanonischen Bootstrap-Prozess arbeiten und während einer Session Entscheidungen dokumentieren müssen.

## Strukturüberblick
- [`AGENTS.md`](./AGENTS.md): Systemweiter Rahmen mit Guardrails, Retrieval-Priorität und Bootstrap-Regeln.
- [`loop_notes.md`](./loop_notes.md): Laufende Session-Notizen mit aktuellem Status und Übergaben.
- [`roles/`](./roles/): Rollenprompts mit detaillierten Aufträgen und Checklisten-Verweisen.
- [`templates/`](./templates/): Antwort-Contracts, Klarstellungs-Templates und andere Textbausteine.
- [`policies/`](./policies/): Sicherheits-, Retrieval- und weitere Richtlinien.
- [`checklists/`](./checklists/): Schritt-für-Schritt-Listen für Bootstrap, Reviews und Pflichtprüfungen.
- [`guides/`](./guides/): Style- und Prompt-Guides für Struktur, Chunking und Metadaten.

## Kernartefakte & Bootstrap-Bezug
- **`AGENTS.md`**: Beschreibt den verbindlichen Start inklusive Strukturprüfung, Lesen und Aktualisieren von `loop_notes.md`, Setzen von `current_role` sowie die Nutzung des Response-Contracts.
- **`loop_notes.md`**: Dokumentiert `current_role`, `last_steps`, `next_steps`, `blockers`, `validation_state`, `decision_log` und `role_prompt`; wird in jedem Bootstrap-Schritt gepflegt.
- **Rollenprompts (`roles/`)**: Legen für jede Rolle Aufgaben, Übergaben und erforderliche Checklisten fest.
- **Checklisten (`checklists/`)**: Enthalten unter anderem `pre_run` für den Bootstrap und Qualitätssicherungslisten für Reviews.
- **Vorlagen (`templates/`)**: Stellen den Response-Contract und Formate für Klarstellungen bereit, die laut Bootstrap sofort zu aktivieren sind.
- **Richtlinien (`policies/`)**: Ergänzen den Bootstrap um Guardrails (z. B. Sicherheits- und Retrieval-Priorität).
- **Leitfäden (`guides/`)**: Unterfüttern Bootstrap-Anforderungen zu Stil, Chunking und Metadaten.

## Benutzungsschritte
1. Befolge den kanonischen Bootstrap aus [`AGENTS.md`](./AGENTS.md): Struktur prüfen, `loop_notes.md` lesen/aktualisieren, `current_role` setzen und den Response-Contract aktivieren.
2. Öffne `loop_notes.md`, um die aktuell zu erfüllende Rolle und nächste Schritte zu identifizieren.
3. Lade den passenden Rollenprompt in [`roles/`](./roles/) und konsultiere die referenzierte Checkliste in [`checklists/`](./checklists/).
4. Nutze bei Antworten die Vorlagen aus [`templates/`](./templates/) und halte dich an Stil- und Guardrail-Vorgaben aus [`guides/`](./guides/) sowie [`policies/`](./policies/).
5. Dokumentiere neue Erkenntnisse oder Entscheidungen direkt in `loop_notes.md` oder in den verlinkten Artefakten und wiederhole den Bootstrap bei Rollenwechsel.

## Ausdrücklich nicht enthalten
- Keine CI-, Build- oder Deployment-Skripte.
- Keine produktiven Source-Code-Dateien oder Bibliotheken.
- Keine externen Abhängigkeiten oder Pakete.
- Keine Laufzeitkonfiguration für Anwendungen.
