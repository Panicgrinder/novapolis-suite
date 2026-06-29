---
stand: 2026-06-29 16:07
update: Wochenabschluss 2026-06-29 ist technisch gruen geschlossen; Full-Check, Sim-Assets und Coverage sind belegt PASS.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp/results/reports/checks_report_20260629_155310.md; snapshot-lock PASS (2026-06-29 16:07)

---

TODO-Uebersicht (Novapolis Suite)
=================================

Kurzstatus
----------

- Der zuletzt abgeschlossene Root-Block ist vollstaendig validiert und unter `novapolis-dev/archive/todo.root.archive.md` archiviert.
- Die aktive Root-Datei ist damit wieder die schlanke Live-Oberflaeche fuer neue suiteweite Querschnittspunkte.
- Die Modul-Boards stehen aktuell bei `Dev=6`, `RP=2`, `Agent=1`, `Sim=1`; Root bleibt bewusst ausserhalb dieser Modul-Open-Counts.
- Der Wochenabschluss vom 2026-06-29 ist gruen belegt: Der finale Recheck `.tmp/results/reports/checks_report_20260629_155005.md` ist vollstaendig PASS, `Checks: sim epoch assets` bleibt PASS (`summary=fail:0,warn:0`) und `Tests: coverage (fail-under)` bleibt bei `92.19%` mit `709 passed`.
- Der initiale Vollcheck `.tmp/results/reports/checks_report_20260629_153748.md` fiel nur an `doc-freshness` (`74` stale Dokus). Nach gezieltem Freshness-Sync der stale Frontmatter-/mtime-Pfade ist der Recheck wieder gruen (`findings=0`).
- Der Wochenabschluss vom 2026-05-18 22:32 ist gruen belegt: Der finale Recheck `.tmp/results/reports/checks_report_20260518_222833.md` ist vollstaendig PASS, `Checks: sim epoch assets` bleibt PASS (`summary=fail:0,warn:0`) und `Tests: coverage (fail-under)` bleibt bei `92.19%` mit `709 passed`. Der konsolidierte Wochenstand liegt zusaetzlich in `novapolis-dev/docs/process/wochenbericht-2026-05-18.md` vor.
- Seit dem Abschluss vom 2026-05-11 kam kein neuer Repo-Commit hinzu; der einzige Wochenrest war diesmal reine Hygiene-Drift. Der erste Vollcheck `.tmp/results/reports/checks_report_20260518_222210.md` fiel nur an 23 stale aktiven/Referenzdokus und stale Workspace-Trees, die im selben Lauf zusammen mit `novapolis-dev/docs/todo.index.md` nachgezogen wurden.
- Die suiteweite Hygiene-Cadence fuer KPI- und Boardpflege bleibt ueber `novapolis-dev/docs/process/abschluss-routine.ssot.md` als aktiver 60-Minuten-Takt mit den KPI-Feldern `todo_index_drift`, `active_docs_stale`, `placeholder_conflicts` und `logs_policy_violations` verankert.
- Historische Sammelbasis bleibt `novapolis-dev/archive/todo.root.archive.md`; der fruehere Vollsnapshot unter `novapolis-dev/archive/quarantine/todo-root-snapshot-20260222_1234.md` bleibt zusaetzliche Evidenz.
- Neue Root-Punkte nur anlegen, wenn der Arbeitszuschnitt wirklich suiteweit ist und nicht sauber in Dev, Agent, RP oder Sim gehoert.

Neue Punkte (Backlog)
---------------------

- [ ] [Jetzt] Korrektur-Planlauf fuer den Governance-Umbau als Root-Querschnitt verbindlich abschliessen.
  - Ziel: Der Umbau wird nicht mehr als kuenstlich nummeriertes Paket gefuehrt, sondern als vollstaendiger Problemraum mit klarer Rollenableitung fuer Root, Dev, Agent, RP und Sim.
  - Akzeptanzkriterien:
    1) Root fuehrt nur echte Querschnittsarbeit; Module fuehren ihre jeweiligen Arbeitsanteile,
    2) strategische Kernarbeit ist von technischen Folgearbeiten sichtbar getrennt,
    3) kuenstliche GOV-Nummerierung ist aus dem aktiven Planlauf entfernt,
    4) `novapolis-dev/docs/todo.index.md` und beide DONELOGs fuehren denselben Stand.
  - Evidenz: `.github/copilot-instructions.md`, `novapolis-dev/docs/process/model-credits-optimization-plan.ssot.md`, `novapolis-dev/docs/process/vscode-agent-governance-surface.ssot.md`, `novapolis-dev/docs/process/workspace-audit-segmente.ssot.md`, `novapolis-dev/docs/process/abschluss-routine.ssot.md`.

- [ ] [Als naechstes] Formale Konsistenz zwischen Header, Open-Counts, Snapshot-Claims und Board-Body dauerhaft stabilisieren.
  - Ziel: Keine widerspruechlichen Aussagen mehr zwischen Frontmatter, Kurzstatus, Offenen Aufgaben und Index.
  - Akzeptanzkriterien:
    1) Headeraussagen zu offenen Punkten spiegeln den Body exakt,
    2) Open-Counts in Boards und `novapolis-dev/docs/todo.index.md` sind synchron,
    3) Snapshot-/Check-Claims bleiben zeitlich und inhaltlich nachvollziehbar.
  - Evidenz: `todo.root.md`, `novapolis-dev/docs/todo.index.md`, `novapolis-dev/docs/todo.dev.md`, `novapolis-dev/docs/todo.agent-board.md`, `novapolis-dev/docs/todo.rp.md`, `novapolis-dev/docs/todo.sim.md`, `novapolis-dev/docs/donelog.md`, `DONELOG.md`.

Hinweise
--------

- Abgeschlossene oder historisierte Root-Bloecke in `novapolis-dev/archive/todo.root.archive.md` verschieben.
- Bei neuen Root-Punkten TODO/DONELOG/WORKSPACE_STATUS und `novapolis-dev/docs/todo.index.md` im selben Lauf synchron halten.






