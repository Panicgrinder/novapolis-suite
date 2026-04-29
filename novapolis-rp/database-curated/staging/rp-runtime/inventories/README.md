---
stand: 2026-04-29 03:56
update: Legacy-Typordner nach entity-centric Runtime-Migration; aktive Daten liegen unter `../entities`.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260429_035444.md
---

Legacy Runtime Folder - inventories
===================================

Status
------

- state: migriert
- active_target: `../entities`
- migration_note: Dieser Typordner bleibt nur als Redirect-Flaeche fuer alte Links. Neue oder aktive Runtime-Daten werden unter `entities/<type>/<slug>/` gepflegt.
