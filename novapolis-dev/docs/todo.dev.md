---
stand: 2026-02-23 00:04
update: Vollständig erledigten Dev-Punkt archiviert und neue aktive Dev-Folgeaufgaben vorbereitet.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-dev/docs/todo.dev.md' 'novapolis-dev/archive/todo.dev.archive.md' PASS (2026-02-23 00:00); .\.venv\Scripts\python.exe scripts\check_frontmatter.py 'novapolis-dev/docs/todo.dev.md' 'novapolis-dev/archive/todo.dev.archive.md' PASS (2026-02-23 00:00)
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

- [ ] VS-Code-Task für `scripts/check_sim_epoch_assets.py` hinzufügen und kurz in Doku verlinken.
- [ ] `scripts/run_checks_and_report.py` um optionalen Sim-Offline-Assetcheck (`--with-sim-assets`) erweitern.
