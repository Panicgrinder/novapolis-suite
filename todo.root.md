---
stand: 2026-05-04 09:36
update: Die Root-Uebersicht fuehrt weiter keine offenen suiteweiten Punkte; der aktuelle Wochenabschluss ist inklusive Wochenbericht gruen belegt.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp/results/reports/checks_report_20260504_083908.md; snapshot-lock PASS (2026-05-04 09:36)
---

TODO-Uebersicht (Novapolis Suite)
=================================

Kurzstatus
----------

- Der zuletzt abgeschlossene Root-Block ist vollstaendig validiert und unter `novapolis-dev/archive/todo.root.archive.md` archiviert.
- Die aktive Root-Datei ist damit wieder die schlanke Live-Oberflaeche fuer neue suiteweite Querschnittspunkte.
- Die Modul-Boards stehen aktuell bei `Dev=0`, `RP=0`, `Agent=0`, `Sim=0`; Root bleibt bewusst ausserhalb dieser Modul-Open-Counts.
- Der Wochenabschluss vom 2026-05-04 08:42 ist gruen belegt: `Checks: full` PASS gegen `.tmp/results/reports/checks_report_20260504_083908.md`, `Checks: sim epoch assets` PASS (`summary=fail:0,warn:0`) und `Tests: coverage (fail-under)` PASS mit `92.19%` bei `709 passed`. Der konsolidierte Wochenstand liegt zusaetzlich in `novapolis-dev/docs/process/wochenbericht-2026-05-04.md` vor.
- Die suiteweite Hygiene-Cadence fuer KPI- und Boardpflege bleibt ueber `novapolis-dev/docs/process/abschluss-routine.ssot.md` als aktiver 60-Minuten-Takt mit den KPI-Feldern `todo_index_drift`, `active_docs_stale`, `placeholder_conflicts` und `logs_policy_violations` verankert.
- Historische Sammelbasis bleibt `novapolis-dev/archive/todo.root.archive.md`; der fruehere Vollsnapshot unter `novapolis-dev/archive/quarantine/todo-root-snapshot-20260222_1234.md` bleibt zusaetzliche Evidenz.
- Neue Root-Punkte nur anlegen, wenn der Arbeitszuschnitt wirklich suiteweit ist und nicht sauber in Dev, Agent, RP oder Sim gehoert.

Neue Punkte (Backlog)
---------------------

- Aktuell keine offenen Root-Punkte.
- Neue suiteweite Querschnittspunkte nur mit belegter Evidenz anlegen und im selben Lauf mit `WORKSPACE_STATUS.md`, `DONELOG.md`, `novapolis-dev/docs/donelog.md` und `novapolis-dev/docs/todo.index.md` synchronisieren.

Hinweise
--------

- Abgeschlossene oder historisierte Root-Bloecke in `novapolis-dev/archive/todo.root.archive.md` verschieben.
- Bei neuen Root-Punkten TODO/DONELOG/WORKSPACE_STATUS und `novapolis-dev/docs/todo.index.md` im selben Lauf synchron halten.






