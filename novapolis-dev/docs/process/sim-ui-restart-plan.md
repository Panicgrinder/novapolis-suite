---
stand: 2026-06-12 08:32
update: Initial plan created for Sim UI restart and scaffolding
checks: frontmatter=manual
author: Novapolis Workspace Navigator
---

Sim UI Neustart — Plan (schlank)
================================

Zweck
-----
Klarer, prüfbarer Fahrplan für den Neuanfang der Sim-Oberfläche (Hub/Stage/Ops/Telemetry), mit minimalen, rückwärtskompatiblen Diffs und CI-Checks.

Kurzplan (hoch)
----------------
1. SSOT & Snapshot: Sicherstellen, dass `novapolis-dev/docs/process/sim-ui-menue-ia.ssot.md` und `novapolis-sim/Main.tscn` die Ausgangsbasis sind; frischen Snapshot/Stand aufnehmen.
2. Design-Dokument: Detaillierte Ziel-IA (Zonen, Interaktionen, Zustandsbesitz, Recovery-Lesart) präzisieren — dieses Dokument ist das aktuelle Artefakt.
3. Scaffolding: Neue, simplere Node-Struktur in `novapolis-sim/Main.tscn` und begleitende Aufräum-/Fassade in `novapolis-sim/scripts/Main.gd` implementieren (kleine, sichtbare Schritte).
4. Controller-Abgrenzung: Sicherstellen, dass bestehende Controller-Refs (`hub_layout_controller.gd`, `hub_chat_controller.gd`, `session_replay_*`) unberührt bleiben; nur Fassade anpassen.
5. Tests & Verify: `Checks: sim headless verify`, `Checks: sim hub prefs contract`, `Checks: sim export smoke` lokal laufen lassen; ziel: Headless-Verify passt.
6. DONELOG & Board: Abschluss-Eintrag im Modul-DONELOG `novapolis-dev/docs/donelog.md` plus Update `novapolis-dev/docs/todo.sim.md` wenn offene Folgeschritte entstehen.

Akzeptanzkriterien
-------------------
- Headless-Verify (`scripts/run_sim_headless_verify.py`) läuft nach Änderungen ohne `SIM_VERIFY: FAIL`.
- Keine Änderungen an API-/Session-Verträgen.
- Änderungen rückwärtskompatibel: bestehende Module/Controller arbeiten weiter.
- Neue Main-Scene ist klar in Zonen (TopBand, Stage, Ops, Telemetry) aufgebaut.

Erste, kleine Implementations-Schritte (konkret)
-----------------------------------------------
A. Erzeuge `novapolis-dev/docs/process/sim-ui-restart-plan.md` (dieses File).
B. Lege Branch/Commit-Kontext (lokal): `feature/sim-ui-restart` — (auf Wunsch automatisch erstellen).
C. Patch 1: Extrahiere alte Layout-Hardcoords aus `Main.gd` in `_layout_hub_shells()` und ersetze durch rechtecksbasierte Zonen mit `anchors_preset`-freundlichen Einstellungen.
D. Patch 2: Entferne keine Controller-Preloads; nur Umbau der Panel-Parents/Containers und sichtbare Panel-IDs belassen.
E. Verifikation: Headless-Verify + `pytest -q novapolis_agent/tests/tests_sim_api.py::test_get_world_state_initial_values`.

Tests
-----
- `.\.venv\Scripts\python.exe scripts/run_sim_headless_verify.py`
- `.\.venv\Scripts\python.exe scripts/check_sim_hub_prefs_contract.py --repo-root .`
- `.\.venv\Scripts\python.exe -m pytest -q novapolis_agent/tests/tests_sim_api.py`

Nächste Schritte (wenn genehmigt)
--------------------------------
- Umsetzung der Scaffolding-Patches im kleinen, commitbaren Schritten (1-3 PRs maximal).
- Headless-Verify iterativ nach jedem Patch.
- Abschluss-DONELOG-Eintrag + kurzes Postflight-Receipt.

