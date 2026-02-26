---
stand: 2026-02-26 05:17
update: Agent-Open-Count nach Abschluss des README/Runbook-Truthfulness-Drift-Punkts synchronisiert.
checks: Snapshot-Lock gesetzt (2026-02-26 04:27); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis_agent/README.md' 'novapolis_agent/docs/runbook.md' 'novapolis-dev/docs/todo.agent-board.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' 'novapolis_agent/docs/DONELOG.txt' PASS (2026-02-26 04:28); .\.venv\Scripts\python.exe scripts/check_frontmatter.py 'novapolis_agent/README.md' 'novapolis_agent/docs/runbook.md' 'novapolis-dev/docs/todo.agent-board.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' 'novapolis_agent/docs/DONELOG.txt' PASS (2026-02-26 04:28)
---

<!-- markdownlint-disable MD022 MD041 -->

TODO-Index (Novapolis-Dev)
==========================

Übersicht
---------

- RP-Module: `docs/todo.rp.md` — Aufgaben, Kanon-/Canvas-Arbeit, Logs (offen: 3)
- Dev-Module: `docs/todo.dev.md` — Tooling, Lint/CI, Validatoren, Doku-Infra (offen: 8)
- Agent-Module: `docs/todo.agent-board.md` — Backend (FastAPI/Ollama), Tests/Typing, Scripts (offen: 6)
- Sim-Module: `docs/todo.sim.md` — Godot/Visualisierung, API-Polling, Exportprofile (offen: 4)

- Statushinweis Dev: `docs/todo.dev.md` enthaelt jetzt einen priorisierten Hygiene-Sprint (Truthfulness, Donelog-/Log-Hygiene, Freshness-SLA, Guardrails).

Hinweise (Index)
----------------

- Vollständig erledigte Abschnitte (H2/H3, alle [x]) bitte manuell in `novapolis-dev/archive/todo.<modul>.archive.md` verschieben; unter der Abschnittsüberschrift `archived_at: YYYY-MM-DD HH:MM` ergänzen. Übersicht aller Archive: `novapolis-dev/archive/README.md`.
- Validierung bei Änderungen: markdownlint via `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc` und Frontmatter-Check via `scripts/check_frontmatter.py`.

Verweise
--------

- Root-Übersicht: `todo.root.md` (Kurzüberblick, Meta-Aufgaben, Links)
- DONELOG-Zentralstruktur: `novapolis-dev/archive/docs/donelogs/INDEX.md`


