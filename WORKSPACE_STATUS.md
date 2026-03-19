---
stand: 2026-03-19 11:09
update: Workspace-Status auf den dokumentierten PASS-Lauf vom 2026-03-18 und den aktuellen Board-Stand synchronisiert.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260318_052318.md
---

Workspace-Status
================

Aktuelles Wochenfenster
-----------------------

- 2026-03-18 05:24: Konsolidierter Full-Check erneut dokumentiert und als aktueller Betriebsstand gesetzt. `scripts/run_checks_and_report.py` liefert `overall=PASS`; alle Pflichtchecks sind gruen, Coverage liegt bei `93.69%`. Der Dev-/Root-Status wurde auf diesen Lauf synchronisiert; offener Root-Folgepunkt bleibt nur noch das externe Beta-Installblatt (O11).

- 2026-03-10 15:40: Wochenabschlusslauf nach `novapolis-dev/docs/process/abschluss-routine.ssot.md` durchgefuehrt. Ergebnis `overall=FAIL` wegen `ruff` (1 Finding), `black` (2 Files) und `pytest`-Gate im Full-Check; alle Governance-Gates (`markdownlint`, `frontmatter`, `path-portability`, `namingpolicy`, `todo-index-sync`, `doc-freshness`, `logs-policy`) PASS. Strukturartefakte wurden aktualisiert (`workspace_tree_full.txt`, `workspace_tree.txt`, `workspace_tree_dirs.txt`). Hinweis: VS-Code-Tasks mit `pwsh ... /d /c` waren lokal fehlerhaft (Exit 64), daher wurden die Wochenabschluss-Kommandos direkt per Python/PowerShell ausgefuehrt.

- 2026-03-04 21:29: Optionalpaket O8/O9/O10/O12 nachgezogen. In `scripts/run_checks_and_report.py` sind neue Pflichtchecks aktiv: `todo-index-sync`, `doc-freshness` und `logs-policy`. Zusaetzlich gilt im Beta-SSOT jetzt ein verbindliches Tagging-Schema (`beta-v<MAJOR>.<MINOR>.<PATCH>-r<YYYYMMDD-HHMM>`). Der aktive Dev-Logpfad wurde policy-konform bereinigt (`novapolis-dev/logs/*.tmp.md` verboten; vorhandener Rohlog nach `novapolis-dev/archive/quarantine/logs/` verschoben).

- 2026-03-04 00:43: Standalone-Beta-Referenzlauf erfolgreich abgeschlossen. `scripts/run_checks_and_report.py` liefert `overall=PASS` mit Report `F:\VS-Code-Workspace\Main\.tmp\results\reports\checks_report_20260304_004318.md`; Sim-Offline-Check (`--allow-empty --check-slot-consistency`) bleibt ohne harte Fehler (`summary=fail:0,warn:2`).

- 2026-03-04 00:37: Root-Verzeichnis `TTS/` gemaess Root-Backlog entfernt (B1). Der kanonische TTS-Stand bleibt im Agent-Modul (`novapolis_agent/scripts/tts_coqui_export.py`, Runtime-Endpoints unter `novapolis_agent/app/main.py`). Root-README und WORKSPACE-Index wurden auf den Iststand ohne Root-TTS synchronisiert.

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



