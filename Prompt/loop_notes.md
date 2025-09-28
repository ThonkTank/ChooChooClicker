---
current_role: implementation
last_steps:
  - "Backlog in tasks/backlog.jsonl strukturiert und erweitert"
  - "Aufgabenabhängigkeiten in tasks/dag.json dokumentiert"
  - "SPARC-Task-Map in tasks/task_map.json erstellt"
  - "Planungssession in memory/session_2025-09-29_planner.md protokolliert"
next_steps:
  - "Vite-React-TypeScript-Projektgerüst aufsetzen und Grundlayout anlegen"
  - "State-Management für Grid, Gleise, Zug und Momentum definieren"
  - "Momentum-Steuerung, Schienenbau und Zugbewegung iterativ implementieren"
role_prompt: "Prompt/implementation_prompt.md"
---

# Loop‑Notizen

Diese Datei muss **nach jedem Arbeitsschritt von der jeweils aktiven Rolle** aktualisiert werden. Nur wenn die Loop‑Notizen gepflegt sind, weiß der nächste Agent, welche Rolle auszuführen ist und wo der zugehörige Prompt zu finden ist. Sie dient ausschließlich dazu, dem Agent mitzuteilen:

1. **Welche Rolle als Nächstes auszuführen ist** (`current_role`).
2. **Was in den letzten Schritten erledigt wurde** (`last_steps`), als kurze Liste.
3. **Was als Nächstes zu tun ist** (`next_steps`), ebenfalls als Liste.
4. **Wo sich der entsprechende Rollen‑Prompt befindet** (`role_prompt`), damit der Agent die detaillierten Anweisungen nachlesen kann.

Planner > Implementation > Documentation > Supervisor > Planner

Alle anderen Informationen finden sich in den jeweiligen Rollen‑Prompts oder den übrigen Dokumenten des Projekts. Halte die YAML‑Metadaten oben immer aktuell, damit der Agent die nötigen Daten maschinell auslesen kann. Jede Rolle ist verpflichtet, nach Abschluss ihrer Arbeit die Felder `current_role`, `last_steps`, `next_steps` und `role_prompt` entsprechend anzupassen.
