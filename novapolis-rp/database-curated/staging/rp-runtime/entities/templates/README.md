---
stand: 2026-06-13 09:17
update: Template-Sammlung fuer entity-centric Runtime-Dossiers angelegt.
checks: scripts/run_checks_and_report.py overall=FAIL; markdownlint=PASS; frontmatter=PASS; path-portability=FAIL; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=FAIL; logs-policy=PASS; ruff=FAIL; black=FAIL; pytest=FAIL; pyright=SKIP; mypy=PASS; report=.tmp\results\reports\checks_report_20260613_091615.md
---

Runtime Entity Templates
========================

Zweck
-----

Knappe Vorlagen fuer neue Dossierdateien unter `entities/<type>/<slug>/`.

Regeln
------

- Nur verwenden, wenn die jeweilige Arbeitsflaeche belegt oder action-relevant ist.
- Offene Werte als `offen`, `tbd` oder `review_required` markieren statt zu erfinden.
