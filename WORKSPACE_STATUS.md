---
stand: 2026-03-03 14:32
update: Tagesabschlusslauf ausgefuehrt; Qualitaetsstatus aktualisiert und Launcher-Fehler der zwei Einzel-Tasks als known issue dokumentiert.
checks: .\.venv\Scripts\python.exe scripts\snapshot_write_lock.py PASS (2026-03-03 03:43); process: Checks: full FAIL (2026-03-03 03:39); .\.venv\Scripts\python.exe scripts\run_pytest_coverage.py FAIL (EXITCODE=1, 2026-03-03 03:40); .\.venv\Scripts\python.exe scripts\check_sim_epoch_assets.py --repo-root . --allow-empty PASS (summary=fail:0,warn:2, 2026-03-03 03:40); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'todo.root.md' 'WORKSPACE_STATUS.md' 'DONELOG.md' 'novapolis-dev/docs/donelog.md' PASS (2026-03-03 03:45); .\.venv\Scripts\python.exe scripts\check_frontmatter.py 'todo.root.md' 'WORKSPACE_STATUS.md' 'DONELOG.md' 'novapolis-dev/docs/donelog.md' PASS (EXITCODE=0, 2026-03-03 03:45)
---

Workspace-Status
================

Aktuelles Wochenfenster
-----------------------

- 2026-03-03 03:43: Tagesabschlusslauf vorbereitet und ausgefuehrt. `Checks: full` erneut gelaufen mit aktuellem Status: `markdownlint FAIL (419)`, `path-portability FAIL (60)`, `ruff FAIL (26)`, `black FAIL (4)`, `pytest/coverage FAIL`, waehrend `frontmatter`, `namingpolicy`, `pyright` und `mypy` PASS blieben. Zusatzlaeufe `Tests: coverage (fail-under)` und `Checks: sim epoch assets` schlugen im VS-Code-Task-Launcher technisch fehl (`pwsh ... /d /c`, Exit 64), daher direkt per Python ausgefuehrt; Sim-Check meldet weiterhin `fail:0,warn:2`.

- 2026-03-03 02:42: Repo-weite Naming-Policy im aktiven Scope umgesetzt (`novapolis-dev/docs/naming-policy.md`) und neues Gate `scripts/check_naming_policy.py` eingefuehrt; Check ist in `scripts/run_checks_and_report.py` als Pflichtcheck `namingpolicy` verdrahtet, zusaetzlich Task `Checks: naming policy` in `.vscode/tasks.json`.

- 2026-03-03 02:21: Mind-Cluster-SSOT-Paket abgeschlossen. Normierungen fuer `relation_status`-Enum, `confidence/volatility`-Range, `event_id`-Schema sowie registrierte `applied_rules`/`reason_codes` in Template + Instructions umgesetzt; RP-Validator um Mind-Cluster-Checks erweitert und bestehende `reason_codes` auf `RC-*` migriert.

- 2026-03-02 23:29: SSOT fuer Wochen-/Monatsabschluss eingefuehrt (`novapolis-dev/docs/process/abschluss-routine.ssot.md`) und Root-README darauf umgestellt.
- 2026-03-02 23:23: Abschlusslauf fuer den 1. Montag im Maerz gestartet (`scripts/run_checks_and_report.py`): aktuell nicht gruen (`markdownlint`, `path-portability`, `ruff`, `black`, `pytest/coverage` FAIL); Sim-Offline-Check lief ohne harte Fehler (`fail:0,warn:2`).
- 2026-02-26 21:59: Doku-Drift-Audit abgeschlossen; obsolete Referenzen in `WORKSPACE_INDEX.md` und `novapolis-dev/docs/tests.md` korrigiert.
- 2026-02-23 08:37: Root-Folgepunkte 1-3 abgeschlossen (`Checks: sim epoch assets`, Prioritaetstags harmonisiert, Wochenabschluss-Routine dokumentiert).
- 2026-02-22 23:58: Root-/Dev-Archivierung und TODO-Index-Sync abgeschlossen; kompletter Testblock (`pytest` + Marker + Coverage) gruen.
- 2026-02-22 21:48: `scripts/check_sim_epoch_assets.py` eingefuehrt und Bootstrap-Lauf erfolgreich.
- 2026-02-22 21:45: Sim-Epoch-Loader inkl. PC-zentrierter Anzeige/OGG-Playback in `novapolis-sim` umgesetzt.

Betriebsstatus (aktiv)
----------------------

- Workspace-Modell: Single-Root (`Main/`).
- Qualitaetsablauf: Lint -> Typen -> Tests -> Coverage.
- Bevorzugte Wrapper: `python scripts/run_checks_and_report.py` und `python scripts/run_pytest_coverage.py --fail-under 80`.
- Governance-SSOT: `.github/copilot-instructions.md`.

Archivhinweise
--------------

- Historischer Root-Status bis vor dem Wochenfenster: `novapolis-dev/archive/docs/others/workspace-status.archive.pre-2026-02-20.md`.
- Vorheriges Dublettenfenster (verlustfrei verschoben): `novapolis-dev/archive/quarantine/archive-window-dedupe-20260227_0018/workspace-status.archive.pre-2026-02-19.md`.
- Historische Postflight-/DoneLog-Artefakte: `novapolis-dev/archive/docs/donelogs/`.

