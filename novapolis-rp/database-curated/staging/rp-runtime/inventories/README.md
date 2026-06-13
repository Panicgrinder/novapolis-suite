---
stand: 2026-06-13 09:17
update: Legacy-Typordner nach entity-centric Runtime-Migration; aktive Daten liegen unter `../entities`.
checks: scripts/run_checks_and_report.py overall=FAIL; markdownlint=PASS; frontmatter=PASS; path-portability=FAIL; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=FAIL; logs-policy=PASS; ruff=FAIL; black=FAIL; pytest=FAIL; pyright=SKIP; mypy=PASS; report=.tmp\results\reports\checks_report_20260613_091615.md
---

Legacy Runtime Folder - inventories
===================================

Status
------

- state: migriert
- active_target: `../entities`
- migration_note: Dieser Typordner bleibt nur als Redirect-Flaeche fuer alte Links. Neue oder aktive Runtime-Daten werden unter `entities/<type>/<slug>/` gepflegt.
