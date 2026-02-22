---
stand: 2026-02-23 00:04
update: Sim-MVP umgesetzt: Epoch-Loader (world_log/pc_log) + OGG-Playback im Main-UI integriert.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-dev/docs/todo.sim.md' 'DONELOG.md' 'WORKSPACE_STATUS.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-22 21:46); .\.venv\Scripts\python.exe scripts\check_frontmatter.py 'novapolis-dev/docs/todo.sim.md' 'DONELOG.md' 'WORKSPACE_STATUS.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-22 21:46)
---

<!-- markdownlint-disable MD022 MD041 -->

TODO (Novapolis-Sim)
====================

Hinweis
-------

- Dieses Dokument bündelt Aufgaben für das Simulations-Modul (Godot-Projekt `novapolis-sim`, Visualisierung, API-Integration, Build/Export).
- Dev-Aufgaben liegen in `docs/todo.dev.md`. RP-Aufgaben liegen in `docs/todo.rp.md`. Agent-Aufgaben liegen in `docs/todo.agent-board.md`.
- Archivierte, vollständig erledigte Abschnitte (H2/H3, alle [x]) bitte manuell nach `novapolis-dev/archive/todo.sim.archive.md` verschieben (neuester oben), mit `archived_at: YYYY-MM-DD HH:MM` unter der Abschnittsüberschrift.

Offene Aufgaben (Sim)
---------------------

- [ ] (Platzhalter) Sammle Sim-Aufgaben hier (Godot, Visualisierung, API-Polling, Exportprofile).
 - [x] Headless-Lade-Check `novapolis-sim/project.godot` durchführen; Kurzprotokoll in `novapolis-dev/docs/donelog.md`.
   - Evidenz: `WORKSPACE_STATUS.md` (2025-11-16 04:54, Headless PASS) und `novapolis-dev/docs/donelog.md` (Abschnitt "Godot Headless - Quick Verification").

Neue Aufgaben - Epochen & Audio (2025-11-01 22:24)
--------------------------------------------------

- [x] Epoch-Loader: 24×1h-Runden laden (world_log + pc_log) und PC-zentriert anzeigen (nur Sichtbares abspielen/anzeigen).
- [x] Audio-Assets abspielen (OGG): Namensschema `epoch{dd}_slot{hh}_{channel}.ogg` (z. B. `epoch03_slot14_pc.ogg`).
  - Evidenz: `novapolis-sim/scripts/Main.gd` (Loader/Parser/PC-View/Playback) und `novapolis-sim/Main.tscn` (UI-Controls + Log-Ausgabe).
- [ ] Event-Signals: `on_action_start/end`, `on_visibility_change`, `on_interrupt` (Hook für spätere Mikro-Turns).
- [ ] Scheduler-Hook vorbereiten: Min-Heap-basierte Event-Queue (ohne Logik), nur Schnittstellen/Types.
  - [ ] Referenz: `novapolis-dev/docs/specs/scheduler-spec.md`.
- [ ] UI-Controls: Stundensprung, Auto-Advance (wenn kein PC-Event), Replay-Seed sichtbar machen.



