---
stand: 2026-04-26 20:40
update: Die Root-Uebersicht fuehrt weiter keine offenen suiteweiten Punkte; der Wochenabschluss ist mit Vollcheck, Sim-Asset-Check und Coverage-Ziellauf gruen belegt.
checks: scripts/run_checks_and_report.py overall=PASS; tests_coverage=PASS (92.19%, 696 passed); sim_epoch_assets=PASS (summary=fail:0,warn:0); report=.tmp\results\reports\checks_report_20260426_203550.md
---

TODO-Uebersicht (Novapolis Suite)
=================================

Kurzstatus
----------

- Der zuletzt abgeschlossene Root-Block ist vollstaendig validiert und unter `novapolis-dev/archive/todo.root.archive.md` archiviert.
- Die aktive Root-Datei ist damit wieder die schlanke Live-Oberflaeche fuer neue suiteweite Querschnittspunkte.
- Die Modul-Boards stehen aktuell bei `Dev=0`, `RP=0`, `Agent=0`, `Sim=0`; Root bleibt bewusst ausserhalb dieser Modul-Open-Counts.
- Der Wochenabschluss vom 2026-04-26 20:40 ist gruen belegt: `Checks: full` PASS, `Checks: sim epoch assets` PASS (`summary=fail:0,warn:0`) und `Tests: coverage (fail-under)` PASS mit `92.19%` bei `696 passed`.
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






