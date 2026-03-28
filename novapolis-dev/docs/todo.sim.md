---
stand: 2026-03-28 06:51
update: Modulreview trennt den Sim-Restpunkt jetzt in Warnungsentscheidung und Clean-Checkout-Bootstrap fuer Asset-Checks.
checks: markdownlint PASS; frontmatter PASS; todo-index PASS; logs-policy PASS (2026-03-28 00:22)
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

- `Jetzt`: Keine Sim-Blocker; nur ein dokumentierter Hygiene-Punkt aus dem Asset-Check ist offen.
- `Als naechstes`: Asset-Warnungen entscheiden und neue Sim-Pakete nur evidenzbasiert als konkrete Backlogpunkte aufnehmen.
- `Spaeter`: Erweiterungen in separaten, klar begrenzten Sim-Epics planen.

Offene Aufgaben (Sim)
---------------------

- [ ] [Als naechstes] Sim-Asset-Warnungen aus `scripts/check_sim_epoch_assets.py` aufloesen oder bewusst kanonisch ausnehmen.
  - Akzeptanzkriterium: Der Check liefert entweder `warn:0` oder die verbleibenden Warnungen sind als absichtliche Ausnahme im Sim-Runbook/Board mit Ursache, Scope und Wiedervorlage dokumentiert.
  - Evidenz: Wochenabschluss 2026-03-27 meldet weiter `summary=fail:0,warn:2`; der aktive Kontext nennt fehlende Epoch-Ordner und Audio-Assets als bekannte Restwarnungen.

- [ ] [Als naechstes] Minimalen Offline-Bootstrap fuer Epoch- und Audio-Assets definieren, damit der Asset-Check auf Clean-Checkout nicht zwischen Pflicht- und Optionaldaten verschwimmt.
  - Akzeptanzkriterium: Es gibt entweder ein kleines kanonisches Fixture-Set fuer `warn:0` oder eine explizite Profiltrennung `Clean-Checkout` vs. `Vollstand` mit unterschiedlicher Check-Erwartung und dokumentiertem Bootstrap-Pfad.
  - Evidenz: `novapolis-sim/README.md` sagt weiter, dass keine weiteren Assets oder Artefakte benoetigt werden, waehrend `WORKSPACE_STATUS.md` und dieses Board im Wochenabschluss weiter `summary=fail:0,warn:2` wegen fehlender Epoch-Ordner und Audio-Assets fuehren.

- [x] [Spaeter] Platzhalterblock aufgeloest: das Sim-Board nutzt keine pauschale Sammelrubrik mehr; Restarbeit wird nur noch als konkrete Einzelpunkte gefuehrt.
  - [x] Headless-Lade-Check `novapolis-sim/project.godot` durchführen; Kurzprotokoll in `novapolis-dev/docs/donelog.md`.
    - Evidenz: `WORKSPACE_STATUS.md` (2025-11-16 04:54, Headless PASS) und `novapolis-dev/docs/donelog.md` (Abschnitt "Godot Headless - Quick Verification").
- [x] [Als naechstes] Hub-Hauptmenue: kleines Chatfenster integriert (Prompt + Antwort + `/chat`-Roundtrip) fuer lokalen Gespraechsmodus direkt im Sim-Hub.
  - Evidenz: `novapolis-sim/Main.tscn` (`HubChatPanel` + Input/Output/Status + `HubChatRequest`) und `novapolis-sim/scripts/Main.gd` (Senden, Endpoint-Aufbau, Response-Handling, Fehlerfall/Status).

Aktiver Kontext (max. 14 Tage)
------------------------------

- 2026-03-27: Wochenabschluss-Refresh. `scripts/check_sim_epoch_assets.py --repo-root . --allow-empty --check-slot-consistency` bleibt ohne harte Fehler (`summary=fail:0,warn:2`); offen sind nur die bekannten Warnungen zu fehlenden Epoch-Ordnern und Audio-Assets.
- 2026-03-11: Mikrodrift bereinigt (`offen: 1 -> 0`) und Referenz-Checkbox fuer Scheduler-Spec auf erledigt gesetzt.
- 2026-03-10: Hub-Hauptmenue-Chatfenster abgeschlossen (UI + `/chat`-Roundtrip + robustes Fehlerhandling).

Archivhinweis
-------------

- Aeltere und vollstaendig erledigte Sim-Bloecke liegen in `novapolis-dev/archive/todo.sim.archive.md`.
- Technische Nachweise liegen in `novapolis-dev/docs/donelog.md` (Current-Window) und `DONELOG.md` (Root-Summary).





