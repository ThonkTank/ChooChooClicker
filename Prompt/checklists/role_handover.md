---
id: checklist_role_handover
title: Rollen-Übergaben Checkliste
author: Autonomous Prompt Maintainer
date: 2025-09-28
tags: [process, handover]
status: active
---

## Zweck
Diese Checkliste beschreibt die verpflichtenden Übergaben zwischen den Rollen Visionary → Planner → Architect → Engineer → Reviewer → Supervisor → Visionary. Jede Übergabe stellt sicher, dass Loop-Notizen, Artefakte und Sicherheitsrichtlinien konsistent bleiben.

## Allgemeine Prinzipien
- **Loop-Notizen als Single Source of Truth:** Vor jeder Übergabe aktualisiert die abgebende Rolle [`Prompt/loop_notes.md`](../loop_notes.md) (Felder `current_role`, `last_steps`, `next_steps`, `blockers`, `validation_state`, `decision_log`).
- **Response-Contract-Konformität:** Übergabeberichte folgen dem Schema aus [`Prompt/templates/Response-Contracts.md`](../templates/Response-Contracts.md) – auch wenn keine großen Änderungen anstehen.
- **Guardrails bestätigen:** Jede Rolle verweist vor der Übergabe auf [`Prompt/policies/guardrails.md`](../policies/guardrails.md) und bestätigt die Einhaltung sicherheitsrelevanter Vorgaben.
- **Retrieval-Priorität beachten:** Konflikte werden gemäß [`Prompt/policies/retrieval_priority.md`](../policies/retrieval_priority.md) dokumentiert und mit Quellen versehen.

## Übergaben im Detail
### Visionary → Planner
- Visionary fasst die Vision laut [`Prompt/roles/visionary.md`](../roles/visionary.md) zusammen und verlinkt geänderte Wiki-Seiten.
- Planner bestätigt, dass Aufgabenableitungen im Rollenprompt [`Prompt/roles/planner.md`](../roles/planner.md) abgedeckt sind und offene Fragen als Tickets/Blocker vorliegen.

### Planner → Architect
- Planner liefert priorisierte Tasks mit klaren Akzeptanzkriterien (siehe [`Prompt/roles/planner.md`](../roles/planner.md)).
- Architect prüft Architekturimplikationen gemäß [`Prompt/roles/architect.md`](../roles/architect.md) und ergänzt technische Annahmen oder ADR-Hinweise.

### Architect → Engineer
- Architect übergibt Architekturentscheidungen inklusive Referenzen zu ADRs/Design-Notizen.
- Engineer verifiziert gemäß [`Prompt/roles/engineer.md`](../roles/engineer.md), dass Implementierungsplan, Tests und Guardrails klar sind.

### Engineer → Reviewer
- Engineer liefert Code, Tests und Dokumentation inklusive Testnachweise.
- Reviewer kontrolliert nach [`Prompt/roles/reviewer.md`](../roles/reviewer.md) die Qualität, stellt Fragen zum Response-Contract und notiert Findings in den Loop-Notizen.

### Reviewer → Supervisor
- Reviewer dokumentiert Freigabeempfehlung oder Blocker.
- Supervisor nutzt [`Prompt/roles/supervisor.md`](../roles/supervisor.md), um Qualitätssicherung, Eskalationen und Abschlussentscheidungen festzuhalten.

### Supervisor → Visionary
- Supervisor bestätigt abgeschlossene Arbeiten, aktualisiert `validation_state` und benennt strategische Implikationen.
- Visionary übernimmt die Ergebnisse, aktualisiert die Vision (siehe [`Prompt/roles/visionary.md`](../roles/visionary.md)) und startet den nächsten Loop.

## Abschlusscheck pro Übergabe
- Response-Contract-Abschnitt im Übergabedokument ist vollständig (Deliverable, Begründung, Nächste Schritte).
- Alle referenzierten Artefakte sind im Repository versioniert und verlinkt.
- Guardrail- und Sicherheitsprüfungen dokumentiert; offene Risiken als Blocker erfasst.
