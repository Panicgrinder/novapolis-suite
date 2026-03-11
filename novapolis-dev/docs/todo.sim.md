---
stand: 2026-03-11 04:45
update: Hub-Hauptmenue-Chatfenster aufgenommen und im selben Lauf als erledigt dokumentiert.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-sim/README.md' 'novapolis-dev/docs/todo.sim.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' PASS (2026-03-10 17:19); .\.venv\Scripts\python.exe scripts/check_frontmatter.py 'novapolis-sim/README.md' 'novapolis-dev/docs/todo.sim.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' PASS (EXITCODE=0, 2026-03-10 17:19)
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

- `Jetzt`: Keine offenen Sim-Blockerpunkte; Stabilitaet ueber Checks/Runbook halten.
- `Als naechstes`: Neue Sim-Pakete nur evidenzbasiert als konkrete Backlogpunkte aufnehmen.
- `Spaeter`: Erweiterungen in separaten, klar begrenzten Sim-Epics planen.

Offene Aufgaben (Sim)
---------------------

- [x] [Spaeter] Platzhalterblock aufgeloest: aktuell keine offenen Sim-Backlogpunkte ausserhalb des Archivs.
  - [x] Headless-Lade-Check `novapolis-sim/project.godot` durchführen; Kurzprotokoll in `novapolis-dev/docs/donelog.md`.
    - Evidenz: `WORKSPACE_STATUS.md` (2025-11-16 04:54, Headless PASS) und `novapolis-dev/docs/donelog.md` (Abschnitt "Godot Headless - Quick Verification").
- [x] [Als naechstes] Hub-Hauptmenue: kleines Chatfenster integriert (Prompt + Antwort + `/chat`-Roundtrip) fuer lokalen Gespraechsmodus direkt im Sim-Hub.
  - Evidenz: `novapolis-sim/Main.tscn` (`HubChatPanel` + Input/Output/Status + `HubChatRequest`) und `novapolis-sim/scripts/Main.gd` (Senden, Endpoint-Aufbau, Response-Handling, Fehlerfall/Status).

Aktiver Kontext (max. 14 Tage)
------------------------------

- 2026-03-11: Mikrodrift bereinigt (`offen: 1 -> 0`) und Referenz-Checkbox fuer Scheduler-Spec auf erledigt gesetzt.
- 2026-03-10: Hub-Hauptmenue-Chatfenster abgeschlossen (UI + `/chat`-Roundtrip + robustes Fehlerhandling).

Archivhinweis
-------------

- Aeltere und vollstaendig erledigte Sim-Bloecke liegen in `novapolis-dev/archive/todo.sim.archive.md`.
- Technische Nachweise liegen in `novapolis-dev/docs/donelog.md` (Current-Window) und `DONELOG.md` (Root-Summary).





