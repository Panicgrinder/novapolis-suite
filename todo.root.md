---
stand: 2026-06-19 15:17
update: Die Root-Uebersicht fuehrt weiter keine offenen suiteweiten Punkte; der RP-Open-Count in der Kurzstatuszeile ist auf den aktiven Board-Stand (`RP=1`) synchronisiert.
checks: snapshot-lock PASS (2026-06-14 01:54); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc todo.root.md PASS; .\.venv\Scripts\python.exe scripts\check_frontmatter.py todo.root.md PASS (EXITCODE=0); .\.venv\Scripts\python.exe scripts\check_todo_index_sync.py --repo-root . PASS

---

TODO-Uebersicht (Novapolis Suite)
=================================

Kurzstatus
----------

- Der zuletzt abgeschlossene Root-Block ist vollstaendig validiert und unter `novapolis-dev/archive/todo.root.archive.md` archiviert.
- Die aktive Root-Datei ist damit wieder die schlanke Live-Oberflaeche fuer neue suiteweite Querschnittspunkte.
- Die Modul-Boards stehen aktuell bei `Dev=4`, `RP=2`, `Agent=1`, `Sim=1`; Root bleibt bewusst ausserhalb dieser Modul-Open-Counts.
- Der Wochenabschluss vom 2026-05-18 22:32 ist gruen belegt: Der finale Recheck `.tmp/results/reports/checks_report_20260518_222833.md` ist vollstaendig PASS, `Checks: sim epoch assets` bleibt PASS (`summary=fail:0,warn:0`) und `Tests: coverage (fail-under)` bleibt bei `92.19%` mit `709 passed`. Der konsolidierte Wochenstand liegt zusaetzlich in `novapolis-dev/docs/process/wochenbericht-2026-05-18.md` vor.
- Seit dem Abschluss vom 2026-05-11 kam kein neuer Repo-Commit hinzu; der einzige Wochenrest war diesmal reine Hygiene-Drift. Der erste Vollcheck `.tmp/results/reports/checks_report_20260518_222210.md` fiel nur an 23 stale aktiven/Referenzdokus und stale Workspace-Trees, die im selben Lauf zusammen mit `novapolis-dev/docs/todo.index.md` nachgezogen wurden.
- Die suiteweite Hygiene-Cadence fuer KPI- und Boardpflege bleibt ueber `novapolis-dev/docs/process/abschluss-routine.ssot.md` als aktiver 60-Minuten-Takt mit den KPI-Feldern `todo_index_drift`, `active_docs_stale`, `placeholder_conflicts` und `logs_policy_violations` verankert.
- Historische Sammelbasis bleibt `novapolis-dev/archive/todo.root.archive.md`; der fruehere Vollsnapshot unter `novapolis-dev/archive/quarantine/todo-root-snapshot-20260222_1234.md` bleibt zusaetzliche Evidenz.
- Neue Root-Punkte nur anlegen, wenn der Arbeitszuschnitt wirklich suiteweit ist und nicht sauber in Dev, Agent, RP oder Sim gehoert.

Neue Punkte (Backlog)
---------------------

- [ ] [Jetzt] GOV-STRANG-01 bis GOV-STRANG-02 als suiteweite Root-Querschnittsarbeit fuer den beschlossenen Governance-Umbau fuehren.
  - Ziel: Die neun strategischen Arbeitsstraenge werden als expliziter Root/Modul-Planverbund sichtbar und belastbar gehalten, ohne in konkurrierende Parallel-SSOTs zu driften.
  - Akzeptanzkriterien:
    1) Root fuehrt den Querschnittsrahmen und die Modulzuordnung sichtbar,
    2) Modulboards tragen die zugeordneten Umsetzungsstraenge als offene Punkte,
    3) `novapolis-dev/docs/todo.index.md` bleibt mit den Open-Counts synchron,
    4) Root-/Dev-DONELOG fuehren denselben Lauf im selben Change-Set.
  - Evidenz: `.github/copilot-instructions.md`, `novapolis-dev/docs/process/model-credits-optimization-plan.ssot.md`, `novapolis-dev/docs/process/vscode-agent-governance-surface.ssot.md`, `novapolis-dev/docs/process/workspace-audit-segmente.ssot.md`.

- [ ] [Als naechstes] GOV-STRANG-03 als Root-Status-/Evidenzsync zwischen Landing, Status, Boards und DONELOG konsistent schliessen.
  - Ziel: Die aktive Root-Oberflaeche fuehrt keine konkurrierenden Freshness-/Check-Claims gegen Modulboards und Index.
  - Akzeptanzkriterien:
    1) `README.md`, `WORKSPACE_STATUS.md`, `todo.root.md`, `novapolis-dev/docs/todo.index.md` und beide DONELOGs fuehren denselben Stand,
    2) stale Header-/Report-Claims werden nicht still uebernommen,
    3) der Synchronisationspfad bleibt in den bestehenden Governance-Regeln verankert.
  - Evidenz: `novapolis-dev/docs/todo.index.md`, `novapolis-dev/docs/donelog.md`, `DONELOG.md`.

Hinweise
--------

- Abgeschlossene oder historisierte Root-Bloecke in `novapolis-dev/archive/todo.root.archive.md` verschieben.
- Bei neuen Root-Punkten TODO/DONELOG/WORKSPACE_STATUS und `novapolis-dev/docs/todo.index.md` im selben Lauf synchron halten.






