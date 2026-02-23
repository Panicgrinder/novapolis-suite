---
stand: 2026-02-23 15:52
update: Agent-Open-Count nach Abschluss von Schritt 10 (Betriebsdoku-Truthfulness) synchronisiert.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-dev/docs/todo.agent-board.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-23 13:52); .\.venv\Scripts\python.exe scripts/check_frontmatter.py 'novapolis-dev/docs/todo.agent-board.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' PASS (EXITCODE=0, 2026-02-23 13:52)
---

<!-- markdownlint-disable MD022 MD041 -->

TODO-Index (Novapolis-Dev)
==========================

Übersicht
---------

- RP-Module: `docs/todo.rp.md` — Aufgaben, Kanon-/Canvas-Arbeit, Logs (offen: 7)
- Dev-Module: `docs/todo.dev.md` — Tooling, Lint/CI, Validatoren, Doku-Infra (offen: 1)
- Agent-Module: `docs/todo.agent-board.md` — Backend (FastAPI/Ollama), Tests/Typing, Scripts (offen: 2)
- Sim-Module: `docs/todo.sim.md` — Godot/Visualisierung, API-Polling, Exportprofile (offen: 5)

Hinweise (Index)
----------------

- Vollständig erledigte Abschnitte (H2/H3, alle [x]) bitte manuell in `novapolis-dev/archive/todo.<modul>.archive.md` verschieben; unter der Abschnittsüberschrift `archived_at: YYYY-MM-DD HH:MM` ergänzen. Übersicht aller Archive: `novapolis-dev/archive/README.md`.
- Validierung bei Änderungen: markdownlint via `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc` und Frontmatter-Check via `scripts/check_frontmatter.py`.

Verweise
--------

- Root-Übersicht: `todo.root.md` (Kurzüberblick, Meta-Aufgaben, Links)
- DONELOG-Zentralstruktur: `novapolis-dev/archive/docs/donelogs/INDEX.md`


