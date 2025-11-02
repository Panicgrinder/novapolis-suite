---
stand: 2025-11-01 22:31
update: Referenz auf Scheduler‑Spec ergänzt; Tab→Spaces Fix
checks: keine
---

<!-- markdownlint-disable MD022 MD041 -->

TODO (Novapolis-Sim)
====================

Hinweis
-------

- Dieses Dokument bündelt Aufgaben für das Simulations‑Modul (Godot‑Projekt `novapolis-sim`, Visualisierung, API‑Integration, Build/Export).
- Dev‑Aufgaben liegen in `docs/todo.dev.md`. RP‑Aufgaben liegen in `docs/todo.rp.md`. Agent‑Aufgaben liegen in `docs/todo.agent.md`.
- Archivierte, vollständig erledigte Abschnitte (H2/H3, alle [x]) bitte manuell nach `novapolis-dev/archive/todo.sim.archive.md` verschieben (neuester oben), mit `archived_at: YYYY-MM-DD HH:MM` unter der Abschnittsüberschrift.

Offene Aufgaben (Sim)
---------------------

- [ ] (Platzhalter) Sammle Sim‑Aufgaben hier (Godot, Visualisierung, API‑Polling, Exportprofile).

Neue Aufgaben – Epochen & Audio (2025-11-01 22:24)
--------------------------------------------------

- [ ] Epoch‑Loader: 24×1h‑Runden laden (world_log + pc_log) und PC‑zentriert anzeigen (nur Sichtbares abspielen/anzeigen).
- [ ] Audio‑Assets abspielen (OGG): Namensschema `epoch{dd}_slot{hh}_{channel}.ogg` (z. B. `epoch03_slot14_pc.ogg`).
- [ ] Event‑Signals: `on_action_start/end`, `on_visibility_change`, `on_interrupt` (Hook für spätere Mikro‑Turns).
- [ ] Scheduler‑Hook vorbereiten: Min‑Heap‑basierte Event‑Queue (ohne Logik), nur Schnittstellen/Types.
  - [ ] Referenz: `novapolis-dev/docs/specs/scheduler-spec.md`.
- [ ] UI‑Controls: Stundensprung, Auto‑Advance (wenn kein PC‑Event), Replay‑Seed sichtbar machen.
