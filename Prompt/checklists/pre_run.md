---
id: checklist_pre_run
title: Pre-Run Checklist
author: Autonomous Prompt Maintainer
date: 2025-09-28
tags: [process, startup]
status: active
---

## Ziel
Diese Checkliste stellt sicher, dass vor jeder Session alle globalen Pflichtschritte eingehalten werden, damit die Rollenarbeit konsistent, sicher und nachvollziehbar bleibt.

## Pflichtschritte vor dem Start
1. **Repository-Struktur prüfen**
   - Vergleiche die aktuelle Struktur mit den Vorgaben in [`Prompt/README.md#Dokumentationsstruktur`](../README.md#dokumentationsstruktur) und den Richtlinien aus dem [`Prompt/guides/StyleGuide.md`](../guides/StyleGuide.md).
   - Dokumentiere Abweichungen in den Loop-Notizen und plane Korrekturen.
2. **Loop-Notizen laden und aktualisieren**
   - Öffne [`Prompt/loop_notes.md`](../loop_notes.md), lese `last_steps`, `next_steps`, `blockers` und `decision_log`.
   - Setze `current_role` auf deine aktive Rolle und verlinke das passende Rollen-Template gemäß [`Prompt/AGENTS.md`](../AGENTS.md).
3. **Response-Contract aktivieren**
   - Orientiere dich an [`Prompt/templates/Response-Contracts.md`](../templates/Response-Contracts.md) und strukturiere alle Antworten strikt nach „Deliverable → Begründung → Nächste Schritte“.
   - Bestätige, dass alle geplanten Outputs dieses Format einhalten und in den Loop-Notizen erwähnt sind.
4. **Guardrails verankern**
   - Lies die Sicherheitsvorgaben aus [`Prompt/policies/guardrails.md`](../policies/guardrails.md) und prüfe, ob anstehende Schritte damit konform sind.
   - Notiere Sicherheitsrisiken oder offene Fragen als Blocker und eskaliere bei Bedarf.

## Validierung vor dem ersten Output
- **Template-Verweise testweise öffnen**: Stelle sicher, dass alle in dieser Checkliste referenzierten Dokumente verfügbar sind und die aktuellste Version widerspiegeln.
- **Konfliktprüfung gemäß Retrieval-Priorität**: Falls Informationen kollidieren, folge dem Schema aus [`Prompt/policies/retrieval_priority.md`](../policies/retrieval_priority.md) und dokumentiere Entscheidungen im `decision_log`.
- **Werkzeug- und Testbereitschaft**: Bestätige, dass notwendige Tools, Testbefehle und Zugangsdaten bereitstehen und den Guardrails entsprechen.

## Abschluss
Erst wenn alle Schritte erfüllt und dokumentiert wurden, darf die produktive Arbeit beginnen. Aktualisiere die Loop-Notizen mit dem Validierungsstatus und bestätige, dass der Response-Contract aktiv ist.
