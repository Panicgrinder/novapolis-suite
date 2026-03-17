---
stand: 2026-03-17 16:58
update: Sim-Modulscan um Restverzeichnis-Drift des alten Nested-Aufbaus erweitert.
checks: scripts/run_checks_and_report.py overall=FAIL; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=FAIL; logs-policy=PASS; ruff=FAIL; black=FAIL; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260317_064114.md
---

<!-- markdownlint-disable MD022 MD041 -->

TODO (Novapolis-Sim)
====================

Hinweis
-------

- Arbeitsmodus (User-Praeferenz): Alles, was nicht direkt in VS Code ausgefuehrt wird (insbesondere Godot-Editor-Schritte), immer als explizite Schritt-fuer-Schritt-Anleitung mit klaren Klickpfaden und erwarteten Ergebnissen liefern.
- Dieses Dokument bündelt Aufgaben für das Simulations-Modul (Godot-Projekt `novapolis-sim`, Visualisierung, API-Integration, Build/Export).
- Dev-Aufgaben liegen in `docs/todo.dev.md`. RP-Aufgaben liegen in `docs/todo.rp.md`. Agent-Aufgaben liegen in `docs/todo.agent-board.md`.
- Aktive Oberflaeche bleibt absichtlich kurz: nur offene Punkte plus max. 14 Tage Kontext.
- Vollstaendig erledigte und aeltere Bloecke liegen in `novapolis-dev/archive/todo.sim.archive.md`.

Prioritaetstags (aktiv)
-----------------------

- `Jetzt`: Keine Sim-Blockerpunkte mit Sofortmassnahme; Stabilitaet ueber Checks/Runbook halten.
- `Jetzt`: Keine Sim-Blockerpunkte mit Sofortmassnahme; Stabilitaet ueber Checks/Runbook halten.
- `Als naechstes`: Neue Sim-Pakete nur evidenzbasiert als konkrete Backlogpunkte aufnehmen.
- `Spaeter`: Erweiterungen in separaten, klar begrenzten Sim-Epics planen.

Offene Aufgaben (Sim)
---------------------

- [ ] [Als naechstes] Sim-README auf den portablen Start-/Verify-Pfad ohne lokal eingebettete Godot-Binary synchronisieren.
  - Akzeptanzkriterium: `novapolis-sim/README.md` nutzt fuer Godot denselben portablen Ansatz wie der kanonische Sim-Pruefablauf (`GODOT_BIN` oder `godot4`) und vermeidet hart verdrahtete lokale Binary-Pfade.
  - Evidenz: `novapolis-sim/README.md` enthaelt weiterhin direkte Aufrufe auf `${workspaceFolder}/novapolis-sim/Godot_v4.5.1-stable_win64.exe` sowie eine lokale `uvicorn app.api.sim:app`-Anleitung, waehrend der kanonische Ablauf im Workspace auf portable Godot-Aufrufe und den zentralen Checkpfad abstellt.
- [ ] [Als naechstes] Hub-interne Sim-Checks auf den kanonischen Asset-Check mit `--allow-empty --check-slot-consistency` angleichen.
  - Akzeptanzkriterium: die von `novapolis-sim/scripts/Main.gd` generierten Sim-Check-Kommandos liefern denselben Mindestpruefpfad wie README/Runbook und unterschlagen keine harten Slot-Konsistenzpruefungen.
  - Evidenz: `_build_check_command(..., "lint")` und `_build_check_command(..., "full")` in `novapolis-sim/scripts/Main.gd` rufen aktuell nur `scripts/check_sim_epoch_assets.py` ohne `--allow-empty --check-slot-consistency` auf, waehrend der dokumentierte kanonische Ablauf diese Flags explizit fordert.
- [ ] [Als naechstes] Leeres Restverzeichnis des alten Nested-Sim-Aufbaus aufraeumen oder bewusst markieren.
  - Akzeptanzkriterium: `novapolis-sim/novapolis-sim/` bleibt nicht kommentarlos als leerer Rest des frueheren verschachtelten Projekts im aktiven Baum stehen; entweder Entfernung, klare Markierung oder dokumentierte technische Notwendigkeit.
  - Evidenz: `novapolis-sim/README.md` erklaert den frueheren verschachtelten Aufbau bereits als nach `Backups/novapolis-sim-archived-20251104/` verschoben, waehrend im aktiven Modulpfad `novapolis-sim/novapolis-sim/` weiterhin ein leeres Restverzeichnis vorhanden ist.

- [x] [Spaeter] Platzhalterblock historisch aufgeloest; frueherer Null-Backlog-Zustand ist archiviert und abgeschlossen.
  - [x] Headless-Lade-Check `novapolis-sim/project.godot` durchführen; Kurzprotokoll in `novapolis-dev/docs/donelog.md`.
    - Evidenz: `WORKSPACE_STATUS.md` (2025-11-16 04:54, Headless PASS) und `novapolis-dev/docs/donelog.md` (Abschnitt "Godot Headless - Quick Verification").
- [x] [Als naechstes] Hub-Hauptmenue: kleines Chatfenster integriert (Prompt + Antwort + `/chat`-Roundtrip) fuer lokalen Gespraechsmodus direkt im Sim-Hub.
  - Evidenz: `novapolis-sim/Main.tscn` (`HubChatPanel` + Input/Output/Status + `HubChatRequest`) und `novapolis-sim/scripts/Main.gd` (Senden, Endpoint-Aufbau, Response-Handling, Fehlerfall/Status).

Aktiver Kontext (max. 14 Tage)
------------------------------

- 2026-03-13: Modulscan hat drei neue Driftpunkte geoeffnet (`offen: 0 -> 3`): portable README-Startwege, Hub-Check-Kommandos gegen den kanonischen Sim-Asset-Check und ein leeres Restverzeichnis des alten Nested-Aufbaus.
- 2026-03-11: Mikrodrift bereinigt (`offen: 1 -> 0`) und Referenz-Checkbox fuer Scheduler-Spec auf erledigt gesetzt.
- 2026-03-10: Hub-Hauptmenue-Chatfenster abgeschlossen (UI + `/chat`-Roundtrip + robustes Fehlerhandling).

Archivhinweis
-------------

- Aeltere und vollstaendig erledigte Sim-Bloecke liegen in `novapolis-dev/archive/todo.sim.archive.md`.
- Technische Nachweise liegen in `novapolis-dev/docs/donelog.md` (Current-Window) und `DONELOG.md` (Root-Summary).





