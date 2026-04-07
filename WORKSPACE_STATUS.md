---
stand: 2026-04-07 21:38
update: Workspace-Status dokumentiert jetzt den vollstaendig warnungsfreien kanonischen Agent-Typenlauf; auch die bisherigen Restwarnungen in eval_utils und rag sind geschlossen.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260407_213201.md
---

Workspace-Status
================

Aktuelles Wochenfenster
-----------------------

- 2026-04-07 20:57: Der kanonische Agent-Typenlauf ist jetzt vollstaendig warnungsfrei. Nach den letzten Typverengungen in `novapolis_agent/utils/eval_utils.py` und `novapolis_agent/utils/rag.py` liefert `.tmp/results/reports/checks_types_20260407_205737.log` fuer `pyright -p pyrightconfig.json` jetzt `0 errors, 0 warnings`, und `mypy --config-file mypy.ini app scripts` bleibt ebenfalls gruen. Damit ist der fruehere Restpfad ausserhalb des aktiven Produktpfads ebenfalls geschlossen.

- 2026-04-07 18:35: Der aktive Agent-Produktpfad fuehrt keine offenen Pyright-Warnungen mehr. `app/api/chat.py`, `app/api/sim.py`, `app/main.py` und `app/tts/providers.py` tragen JSON-, Snapshot- und Cache-Payloads jetzt ueber engere Coercion- bzw. TypedDict-Pfade; der erneute `pyright -p pyrightconfig.json` meldet im Produktpfad keine Warnungen mehr, `mypy --config-file mypy.ini app scripts` bleibt gruen, und der gezielte Pytest-Block fuer Chat, Sim und TTS ist PASS. Die verbleibenden Warnungen liegen nur noch in `novapolis_agent/utils/eval_utils.py` und `novapolis_agent/utils/rag.py` und sind damit ein separater Folgepfad ausserhalb des aktuellen Produktpunktes.

- 2026-04-07 17:20: Der offene Dev-Rest zum kanonischen Typenpfad ist wieder geschlossen. `scripts/checks_types.py` bindet Pyright und Mypy jetzt explizit an `novapolis_agent/pyrightconfig.json` und `novapolis_agent/mypy.ini`, fuehrt beide Kommandos mit `cwd=novapolis_agent` aus, und `.vscode/tasks.json` startet denselben Wrapper wieder aus dem Repo-Root; `.tmp/results/reports/checks_types_postflight_20260407_170654.md` zeigt `pyright=0` und `mypy=0`. Nach den direkt betroffenen Portabilitaets- und Formatkorrekturen liefert `.tmp/results/reports/checks_report_20260407_171142.md` den kanonischen Full-Check wieder komplett PASS, und `novapolis-dev/docs/todo.index.md` zeigt alle Modul-Boards erneut auf `offen: 0`.

- 2026-04-07 16:55: Der Text-RPG-Slice selbst bleibt typenstabil, aber der kanonische Workspace-Typenlauf ist erneut als offener Infrastrukturrest aufgetaucht. `scripts/checks_types.py` loest seinen Root auf das Repo und ruft von dort `pyright -p pyrightconfig.json` sowie `mypy --config-file mypy.ini` auf, obwohl `novapolis_agent/pyrightconfig.json` und `novapolis_agent/mypy.ini` die realen Config-Dateien sind; `.tmp/results/reports/checks_types_20260407_165332.log` belegt dazu eine nicht lesbare Pyright-Config am Repo-Root plus `Cannot find config file 'mypy.ini'`. `novapolis-dev/docs/todo.dev.md` fuehrt die Reparatur deshalb wieder als offenen `Jetzt`-Punkt, und `novapolis-dev/docs/todo.index.md` zeigt Dev damit auf `offen: 1` statt alle Boards auf `0`.

- 2026-04-07 16:28: Der suiteweite Root-Metablock fuer `Spielstart Novapolis`, den internen Produktpfad `Slice -> MVP -> Beta` und die Prioritaet `spielbarer Kern vor Komfort` ist jetzt gegen den realen Modul-Iststand geschlossen. `todo.root.md` verweist dafuer nur noch auf `rp-start-chooser.ssot.md`, `text-rpg-session-contract-v1.md`, `text-rpg-product-gate-v1.ssot.md`, `standalone-beta-gates.ssot.md`, `novapolis_agent/docs/runbook.md` und die Modul-Boards; `novapolis-dev/docs/todo.index.md` zeigt alle Modul-Boards auf `offen: 0`.

- 2026-04-07 15:55: Der Sim-Offline-Check trennt jetzt sauber zwischen Clean-Checkout und Vollstand. `scripts/check_sim_epoch_assets.py` behandelt `--allow-empty` nun als kanonisches Clean-Checkout-Profil; der Lauf `--repo-root . --allow-empty --check-slot-consistency` endet im aktuellen Repo-Stand mit `summary=fail:0,warn:0`, waehrend Vollstand-Laeufe ohne dieses Flag weiter echte Offline-Artefakte unter `novapolis-sim/data/epochs/` und `novapolis-sim/assets/audio/` erwarten.

- 2026-03-28 06:32: Der letzte aktive Root-eval-Rest ist final geschlossen. Lokale Kontext-Notizen, Eval-Standardpfade und RAG-Fallbacks laufen jetzt ueber `novapolis_agent/eval/...`; der fruehere Root-Ordner `eval/` wurde nach `novapolis-dev/archive/quarantine/root-cleanup-20260328_0501-root-eval-rest/eval` ueberfuehrt, ein nach den Abschluss-Checks erneut entstandener lokaler Stub `eval/config/context.local.md` zusaetzlich nach `novapolis-dev/archive/quarantine/root-cleanup-20260328_0632-root-eval-rest-postchecks/eval`, und die drei Root-Tree-Artefakte wurden danach erneut neu erzeugt.

- 2026-03-28 03:30: Lokale Editor-/Host-Snapshots aus dem Root entfernt und nach `novapolis-dev/archive/quarantine/root-cleanup-20260328_0330-local-snapshots/` ueberfuehrt. Betroffen waren nur `extensions.installed.txt`, `extensions.status.txt` und `desktop.ini`; die Tree-Artefakte wurden anschliessend direkt per Terminal neu erzeugt, weil die vorhandenen Shell-Tasks `Workspace tree:*` lokal weiter mit dem bekannten `pwsh /d /c`-Fehlpfad (Exit `64`) abbrechen.

- 2026-03-28 03:12: Sichere Root-Altartefakte aus dem aktiven Surface entfernt und nach `novapolis-dev/archive/quarantine/root-cleanup-20260328_0238/` ueberfuehrt. Betroffen waren nur `combined.json`, `lint.out`, `md003_scan.out`, `.tmp-datasets/` und `reports/`; die aktiven Root-Shims `app/__init__.py` und `utils/__init__.py` sowie der noch referenzierte Hinweis `eval/config/context.local.md` blieben absichtlich stehen.

- 2026-03-27 01:16: Wochenabschlusslauf nach `novapolis-dev/docs/process/abschluss-routine.ssot.md` komplett abgeschlossen. Der erste Lauf zeigte nur zwei stale aktive Boards (`novapolis-dev/docs/todo.agent-board.md`, `novapolis-dev/docs/todo.sim.md`) im Freshness-Gate; nach dem Refresh liefert `scripts/run_checks_and_report.py` wieder `overall=PASS`, Coverage bleibt bei `93.69%`, und die Governance-Gates (`todo-index-sync`, `doc-freshness`, `logs-policy`) sind gruen. Der Sim-Offline-/Asset-Check bleibt ohne harte Fehler (`summary=fail:0,warn:2`).

- 2026-03-18 05:24: Konsolidierter Full-Check erneut dokumentiert und als aktueller Betriebsstand gesetzt. `scripts/run_checks_and_report.py` liefert `overall=PASS`; alle Pflichtchecks sind gruen, Coverage liegt bei `93.69%`. Der Dev-/Root-Status wurde auf diesen Lauf synchronisiert; offener Root-Folgepunkt bleibt nur noch das externe Beta-Installblatt (O11).

- 2026-03-10 15:40: Wochenabschlusslauf nach `novapolis-dev/docs/process/abschluss-routine.ssot.md` durchgefuehrt. Ergebnis `overall=FAIL` wegen `ruff` (1 Finding), `black` (2 Files) und `pytest`-Gate im Full-Check; alle Governance-Gates (`markdownlint`, `frontmatter`, `path-portability`, `namingpolicy`, `todo-index-sync`, `doc-freshness`, `logs-policy`) PASS. Strukturartefakte wurden aktualisiert (`workspace_tree_full.txt`, `workspace_tree.txt`, `workspace_tree_dirs.txt`). Hinweis: VS-Code-Tasks mit `pwsh ... /d /c` waren lokal fehlerhaft (Exit 64), daher wurden die Wochenabschluss-Kommandos direkt per Python/PowerShell ausgefuehrt.

- 2026-03-04 21:29: Optionalpaket O8/O9/O10/O12 nachgezogen. In `scripts/run_checks_and_report.py` sind neue Pflichtchecks aktiv: `todo-index-sync`, `doc-freshness` und `logs-policy`. Zusaetzlich gilt im Beta-SSOT jetzt ein verbindliches Tagging-Schema (`beta-v<MAJOR>.<MINOR>.<PATCH>-r<YYYYMMDD-HHMM>`). Der aktive Dev-Logpfad wurde policy-konform bereinigt (`novapolis-dev/logs/*.tmp.md` verboten; vorhandener Rohlog nach `novapolis-dev/archive/quarantine/logs/` verschoben).

- 2026-03-04 00:43: Standalone-Beta-Referenzlauf erfolgreich abgeschlossen. `scripts/run_checks_and_report.py` liefert `overall=PASS` mit Report `.tmp/results/reports/checks_report_20260304_004318.md`; Sim-Offline-Check (`--allow-empty --check-slot-consistency`) bleibt ohne harte Fehler (`summary=fail:0,warn:2`).

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
- Bevorzugte Wrapper: `& .\.venv\Scripts\python.exe scripts/run_checks_and_report.py` und `& .\.venv\Scripts\python.exe scripts/run_pytest_coverage.py --fail-under 80`.
- Governance-SSOT: `.github/copilot-instructions.md`.

Archivhinweise
--------------

- Historischer Root-Status bis vor dem Wochenfenster: `novapolis-dev/archive/docs/others/workspace-status.archive.pre-2026-02-20.md`.
- Vorheriges Dublettenfenster (verlustfrei verschoben): `novapolis-dev/archive/quarantine/archive-window-dedupe-20260227_0018/workspace-status.archive.pre-2026-02-19.md`.
- Historische Postflight-/DoneLog-Artefakte: `novapolis-dev/archive/docs/donelogs/`.



