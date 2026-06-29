---
stand: 2026-06-29 16:07
update: Wochenbericht fuer den Abschlusslauf 2026-06-29 angelegt.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp/results/reports/checks_report_20260629_155310.md; snapshot-lock PASS (2026-06-29 16:07)
---

Wochenbericht 2026-06-29
========================

Zeitraum
--------

- Berichtswoche: 2026-06-22 bis 2026-06-29.
- Abschlusskontext: Wochenabschluss gemaess `novapolis-dev/docs/process/abschluss-routine.ssot.md`.

Kurzfazit
---------

- Der Wochenabschluss ist technisch gruen geschlossen: Full-Check, Sim-Asset-Check und Coverage-Gate sind belegt PASS.
- Der einzige Laufrest war diesmal reine Freshness-Drift: Der initiale Vollcheck `.tmp/results/reports/checks_report_20260629_153748.md` fiel nur an `doc-freshness` mit `74` stale Dokumenten. Nach gezieltem Freshness-Repair ist der Recheck `.tmp/results/reports/checks_report_20260629_155005.md` vollstaendig PASS.

Wesentliche Befunde
-------------------

- Full-Check Recheck: `.tmp/results/reports/checks_report_20260629_155005.md` meldet `overall=PASS` mit allen Kern-Gates auf PASS.
- Sim-Assets: `scripts/check_sim_epoch_assets.py --repo-root . --allow-empty` bleibt bei `summary=fail:0,warn:0`.
- Coverage: `scripts/run_pytest_coverage.py` bestaetigt `709 passed` und `92.19%` (Hard Gate `>=80%` und Qualitaetsziel `>=90%` gehalten).
- Hygiene/KPI: `todo_index_drift=0`, `active_docs_stale=74 -> 0 im selben Lauf`, `placeholder_conflicts=0`, `logs_policy_violations=0`.

Belegte Wochenanker
-------------------

- 2026-06-29: Initialer Vollcheck mit einzigem Rest in `doc-freshness` (`74` stale).
- 2026-06-29: Freshness-Repair fuer stale Frontmatter-/mtime-Pfade, danach gruener Recheck.
- 2026-06-29: Sim-Assets und Coverage separat nachgezogen und PASS bestaetigt.

Offener Stand zum Wochenwechsel
-------------------------------

- Die Modul-Open-Counts bleiben unveraendert bei `Dev=6`, `RP=2`, `Agent=1`, `Sim=1`.
- Der Root-Querschnitt bleibt unveraendert bei zwei offenen Governance-Umbaupunkten und ist in `todo.root.md` dokumentiert.
