---
stand: 2026-02-23 09:19
update: Sim-Epoch-Asset-Task abgeschlossen; verbleibenden Dev-Punkt priorisiert.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'README.md' 'todo.root.md' 'novapolis-dev/docs/todo.dev.md' 'novapolis-dev/docs/todo.agent-board.md' 'novapolis-dev/docs/todo.sim.md' 'novapolis-dev/docs/todo.rp.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' 'DONELOG.md' 'WORKSPACE_STATUS.md' PASS (2026-02-23 08:39); .\.venv\Scripts\python.exe scripts\check_frontmatter.py 'README.md' 'todo.root.md' 'novapolis-dev/docs/todo.dev.md' 'novapolis-dev/docs/todo.agent-board.md' 'novapolis-dev/docs/todo.sim.md' 'novapolis-dev/docs/todo.rp.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' 'DONELOG.md' 'WORKSPACE_STATUS.md' PASS (EXITCODE=0, 2026-02-23 08:40)
---

<!-- markdownlint-disable MD022 MD041 -->

TODO (Novapolis-Dev)
====================

Hinweis
-------

- Dieses Dokument buendelt Aufgaben fuer das Dev-Modul (Tooling, Lint/CI, Validatoren, Doku-Infra).
- RP-Aufgaben liegen in `docs/todo.rp.md`. Agent-Aufgaben liegen in `docs/todo.agent-board.md`.
- Vollstaendig erledigte Bloecke werden nach `novapolis-dev/archive/todo.dev.archive.md` verschoben.

Offene Aufgaben (Dev)
---------------------

- [x] VS-Code-Task für `scripts/check_sim_epoch_assets.py` hinzufügen und kurz in Doku verlinken.
- [ ] [Als naechstes] `scripts/run_checks_and_report.py` um optionalen Sim-Offline-Assetcheck (`--with-sim-assets`) erweitern.
