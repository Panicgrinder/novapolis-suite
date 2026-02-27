---
stand: 2026-02-27 06:06
update: Archivfenster auf kanonisches pre-2026-02-20 konsolidiert; pre-2026-02-19 verlustfrei nach Quarantaene verschoben.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc "WORKSPACE_STATUS.md" "DONELOG.md" "novapolis-dev/docs/donelog.md" "novapolis-dev/archive/quarantine/archive-window-dedupe-20260227_0018/README.md" "novapolis-dev/archive/docs/others/workspace-status.archive.pre-2026-02-20.md" "novapolis-dev/archive/docs/donelogs/donelog_dev.window-archive.pre-2026-02-20.md" PASS (2026-02-27 00:20); f:/VS-Code-Workspace/Main/.venv/Scripts/python.exe scripts/check_frontmatter.py "WORKSPACE_STATUS.md" "DONELOG.md" "novapolis-dev/docs/donelog.md" "novapolis-dev/archive/quarantine/archive-window-dedupe-20260227_0018/README.md" "novapolis-dev/archive/docs/others/workspace-status.archive.pre-2026-02-20.md" "novapolis-dev/archive/docs/donelogs/donelog_dev.window-archive.pre-2026-02-20.md" PASS (EXITCODE=0, 2026-02-27 00:20)
---

Workspace-Status
================

Aktuelles Wochenfenster
-----------------------

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
