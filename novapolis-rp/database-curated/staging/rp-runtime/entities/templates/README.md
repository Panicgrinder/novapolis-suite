---
stand: 2026-04-29 03:56
update: Template-Sammlung fuer entity-centric Runtime-Dossiers angelegt.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260429_035444.md
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
