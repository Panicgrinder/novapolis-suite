---
stand: 2026-02-27 06:06
update: Agent-Open-Count nach Abschluss des letzten offenen Task-Set-Punkts synchronisiert.
checks: npx --yes markdownlint-cli2 --config F:/VS-Code-Workspace/Main/.markdownlint-cli2.jsonc "F:/VS-Code-Workspace/Main/novapolis-dev/docs/todo.agent-board.md" "F:/VS-Code-Workspace/Main/novapolis-dev/docs/todo.index.md" "F:/VS-Code-Workspace/Main/novapolis-dev/docs/donelog.md" "F:/VS-Code-Workspace/Main/novapolis_agent/docs/DONELOG.txt" "F:/VS-Code-Workspace/Main/novapolis_agent/README.md" "F:/VS-Code-Workspace/Main/novapolis_agent/docs/runbook.md" PASS (2026-02-27 05:31); F:/VS-Code-Workspace/Main/.venv/Scripts/python.exe F:/VS-Code-Workspace/Main/scripts/check_frontmatter.py "F:/VS-Code-Workspace/Main/novapolis-dev/docs/todo.agent-board.md" "F:/VS-Code-Workspace/Main/novapolis-dev/docs/todo.index.md" "F:/VS-Code-Workspace/Main/novapolis-dev/docs/donelog.md" "F:/VS-Code-Workspace/Main/novapolis_agent/docs/DONELOG.txt" "F:/VS-Code-Workspace/Main/novapolis_agent/README.md" "F:/VS-Code-Workspace/Main/novapolis_agent/docs/runbook.md" PASS (EXITCODE=0, 2026-02-27 05:31)
---

<!-- markdownlint-disable MD022 MD041 -->

TODO-Index (Novapolis-Dev)
==========================

Übersicht
---------

- RP-Module: `docs/todo.rp.md` — Aufgaben, Kanon-/Canvas-Arbeit, Logs (offen: 3)
- Dev-Module: `docs/todo.dev.md` — Tooling, Lint/CI, Validatoren, Doku-Infra (offen: 7)
- Agent-Module: `docs/todo.agent-board.md` — Backend (FastAPI/Ollama), Tests/Typing, Scripts (offen: 0)
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


