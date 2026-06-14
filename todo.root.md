---
stand: 2026-06-14 03:15
update: Die Root-Uebersicht fuehrt weiter keine offenen suiteweiten Punkte; der RP-Open-Count in der Kurzstatuszeile ist auf den aktiven Board-Stand (`RP=1`) synchronisiert.
checks: snapshot-lock PASS (2026-06-14 01:54); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc todo.root.md PASS; .\.venv\Scripts\python.exe scripts\check_frontmatter.py todo.root.md PASS (EXITCODE=0); .\.venv\Scripts\python.exe scripts\check_todo_index_sync.py --repo-root . PASS
---

TODO-Uebersicht (Novapolis Suite)
=================================

Kurzstatus
----------

- Der zuletzt abgeschlossene Root-Block ist vollstaendig validiert und unter `novapolis-dev/archive/todo.root.archive.md` archiviert.
- Die aktive Root-Datei ist damit wieder die schlanke Live-Oberflaeche fuer neue suiteweite Querschnittspunkte.
- Die Modul-Boards stehen aktuell bei `Dev=0`, `RP=1`, `Agent=0`, `Sim=0`; Root bleibt bewusst ausserhalb dieser Modul-Open-Counts.
- Der Wochenabschluss vom 2026-05-18 22:32 ist gruen belegt: Der finale Recheck `.tmp/results/reports/checks_report_20260518_222833.md` ist vollstaendig PASS, `Checks: sim epoch assets` bleibt PASS (`summary=fail:0,warn:0`) und `Tests: coverage (fail-under)` bleibt bei `92.19%` mit `709 passed`. Der konsolidierte Wochenstand liegt zusaetzlich in `novapolis-dev/docs/process/wochenbericht-2026-05-18.md` vor.
- Seit dem Abschluss vom 2026-05-11 kam kein neuer Repo-Commit hinzu; der einzige Wochenrest war diesmal reine Hygiene-Drift. Der erste Vollcheck `.tmp/results/reports/checks_report_20260518_222210.md` fiel nur an 23 stale aktiven/Referenzdokus und stale Workspace-Trees, die im selben Lauf zusammen mit `novapolis-dev/docs/todo.index.md` nachgezogen wurden.
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






