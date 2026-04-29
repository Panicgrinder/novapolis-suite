---
stand: 2026-04-29 03:56
update: Namespace fuer entity-centric Runtime-Dossiers angelegt.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260429_035444.md
---

Asset Dossiers
==============

Zweck
-----

Dieser Namespace enthaelt aktive Runtime-Dossiers nach dem Muster `entities/<type>/<slug>/`.

Regeln
------

- Nur belegte Arbeitsflaechen anlegen.
- Keine Kanon-Promotion ohne Review oder explizite Freigabe.
- Interne Verweise bevorzugt relativ innerhalb von `entities/` fuehren.
