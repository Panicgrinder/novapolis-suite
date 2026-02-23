---
stand: 2026-02-23 09:19
update: Prioritaetstags (Jetzt/Als naechstes/Spaeter) fuer aktive Sim-Punkte harmonisiert.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'README.md' 'todo.root.md' 'novapolis-dev/docs/todo.dev.md' 'novapolis-dev/docs/todo.agent-board.md' 'novapolis-dev/docs/todo.sim.md' 'novapolis-dev/docs/todo.rp.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' 'DONELOG.md' 'WORKSPACE_STATUS.md' PASS (2026-02-23 08:39); .\.venv\Scripts\python.exe scripts\check_frontmatter.py 'README.md' 'todo.root.md' 'novapolis-dev/docs/todo.dev.md' 'novapolis-dev/docs/todo.agent-board.md' 'novapolis-dev/docs/todo.sim.md' 'novapolis-dev/docs/todo.rp.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' 'DONELOG.md' 'WORKSPACE_STATUS.md' PASS (EXITCODE=0, 2026-02-23 08:40)
---

<!-- markdownlint-disable MD022 MD041 -->

TODO (Novapolis-Sim)
====================

Hinweis
-------

- Dieses Dokument bündelt Aufgaben für das Simulations-Modul (Godot-Projekt `novapolis-sim`, Visualisierung, API-Integration, Build/Export).
- Dev-Aufgaben liegen in `docs/todo.dev.md`. RP-Aufgaben liegen in `docs/todo.rp.md`. Agent-Aufgaben liegen in `docs/todo.agent-board.md`.
- Archivierte, vollständig erledigte Abschnitte (H2/H3, alle [x]) bitte manuell nach `novapolis-dev/archive/todo.sim.archive.md` verschieben (neuester oben), mit `archived_at: YYYY-MM-DD HH:MM` unter der Abschnittsüberschrift.

Prioritaetstags (aktiv)
-----------------------

- `Jetzt`: Event-Signals und Scheduler-Hook fuer Mikro-Turns vorbereiten.
- `Als naechstes`: UI-Controls fuer Stundensprung/Auto-Advance/Replay-Seed ergänzen.
- `Spaeter`: Platzhalterblock durch konkrete Sim-Backlogpunkte ersetzen.

Offene Aufgaben (Sim)
---------------------

- [ ] [Spaeter] (Platzhalter) Sammle Sim-Aufgaben hier (Godot, Visualisierung, API-Polling, Exportprofile).
 - [x] Headless-Lade-Check `novapolis-sim/project.godot` durchführen; Kurzprotokoll in `novapolis-dev/docs/donelog.md`.
   - Evidenz: `WORKSPACE_STATUS.md` (2025-11-16 04:54, Headless PASS) und `novapolis-dev/docs/donelog.md` (Abschnitt "Godot Headless - Quick Verification").

Neue Aufgaben - Epochen & Audio (2025-11-01 22:24)
--------------------------------------------------

- [x] Epoch-Loader: 24×1h-Runden laden (world_log + pc_log) und PC-zentriert anzeigen (nur Sichtbares abspielen/anzeigen).
- [x] Audio-Assets abspielen (OGG): Namensschema `epoch{dd}_slot{hh}_{channel}.ogg` (z. B. `epoch03_slot14_pc.ogg`).
  - Evidenz: `novapolis-sim/scripts/Main.gd` (Loader/Parser/PC-View/Playback) und `novapolis-sim/Main.tscn` (UI-Controls + Log-Ausgabe).
- [ ] [Jetzt] Event-Signals: `on_action_start/end`, `on_visibility_change`, `on_interrupt` (Hook für spätere Mikro-Turns).
- [ ] [Jetzt] Scheduler-Hook vorbereiten: Min-Heap-basierte Event-Queue (ohne Logik), nur Schnittstellen/Types.
  - [ ] Referenz: `novapolis-dev/docs/specs/scheduler-spec.md`.
- [ ] [Als naechstes] UI-Controls: Stundensprung, Auto-Advance (wenn kein PC-Event), Replay-Seed sichtbar machen.



