---
current_role: planner
last_steps:
  - "Vision aktualisiert: docs/intended_experience/overview.md"
  - "Features dokumentiert: Momentum, Schienenbau, UI-Panel"
  - "Details ergänzt: Momentum-Ressource, UI-Layout"
  - "Offene Fragen im Backlog erfasst"
next_steps:
  - "Feature-Vision in umsetzbare Tasks und User-Stories zerlegen"
  - "Offene Fragen priorisieren und Klärung planen"
blockers: []
validation_state: "pending"
decision_log: []
role_prompt: "Prompt/roles/planner_prompt.md"
---

# Loop‑Notizen

Diese Datei muss **nach jedem Arbeitsschritt von der jeweils aktiven Rolle** aktualisiert werden. Nur wenn die Loop‑Notizen gepflegt sind, weiß der nächste Agent, welche Rolle auszuführen ist und wo der zugehörige Prompt zu finden ist. Sie dient ausschließlich dazu, dem Agent mitzuteilen:

1. **Welche Rolle als Nächstes auszuführen ist** (`current_role`).
2. **Was in den letzten Schritten erledigt wurde** (`last_steps`), als kurze Liste.
3. **Was als Nächstes zu tun ist** (`next_steps`), ebenfalls als Liste.
4. **Wo sich der entsprechende Rollen‑Prompt befindet** (`role_prompt`), damit der Agent die detaillierten Anweisungen nachlesen kann.

Visionary → Planner → Implementation → Documentation → Supervisor → Visionary

Alle anderen Informationen finden sich in den jeweiligen Rollen‑Prompts oder den übrigen Dokumenten des Projekts. Halte die YAML‑Metadaten oben immer aktuell, damit der Agent die nötigen Daten maschinell auslesen kann. Jede Rolle ist verpflichtet, nach Abschluss ihrer Arbeit die Felder `current_role`, `last_steps`, `next_steps`, `blockers`, `validation_state`, `decision_log` und `role_prompt` entsprechend anzupassen.
