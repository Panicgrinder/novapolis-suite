---
stand: 2026-06-13 09:17
update: Namespace fuer entity-centric Runtime-Dossiers angelegt.
checks: scripts/run_checks_and_report.py overall=FAIL; markdownlint=PASS; frontmatter=PASS; path-portability=FAIL; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=FAIL; logs-policy=PASS; ruff=FAIL; black=FAIL; pytest=FAIL; pyright=SKIP; mypy=PASS; report=.tmp\results\reports\checks_report_20260613_091615.md
---

Project Dossiers
================

Zweck
-----

Dieser Namespace enthaelt aktive Runtime-Dossiers nach dem Muster `entities/<type>/<slug>/`.

Regeln
------

- Nur belegte Arbeitsflaechen anlegen.
- Keine Kanon-Promotion ohne Review oder explizite Freigabe.
- Interne Verweise bevorzugt relativ innerhalb von `entities/` fuehren.
