---
stand: 2026-03-11 04:17
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
- Archivierte, vollständig erledigte Abschnitte (H2/H3, alle [x]) bitte manuell nach `novapolis-dev/archive/todo.sim.archive.md` verschieben (neuester oben), mit `archived_at: YYYY-MM-DD HH:MM` unter der Abschnittsüberschrift.

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

Neue Aufgaben - Epochen & Audio (2025-11-01 22:24)
--------------------------------------------------

- [x] Epoch-Loader: 24×1h-Runden laden (world_log + pc_log) und PC-zentriert anzeigen (nur Sichtbares abspielen/anzeigen).
- [x] Audio-Assets abspielen (OGG): Namensschema `epoch{dd}_slot{hh}_{channel}.ogg` (z. B. `epoch03_slot14_pc.ogg`).
  - Evidenz: `novapolis-sim/scripts/Main.gd` (Loader/Parser/PC-View/Playback) und `novapolis-sim/Main.tscn` (UI-Controls + Log-Ausgabe).
- [x] [Jetzt] Event-Signals: `on_action_start/end`, `on_visibility_change`, `on_interrupt` (Hook für spätere Mikro-Turns).
  - Evidenz: `novapolis-sim/scripts/Main.gd` (Signal-Definitionen + Emission + Runtime-Event-Log in `PcLogLabel`), Headless-Start `res://Main.tscn` ohne Fehler.
- [x] [Jetzt] Scheduler-Hook vorbereiten: Min-Heap-basierte Event-Queue (ohne Logik), nur Schnittstellen/Types.
  - Evidenz: `novapolis-sim/scripts/scheduler_hook.gd` (Min-Heap API: `enqueue/peek_next/pop_next/pop_due`), `novapolis-sim/scripts/Main.gd` (`SCHEDULER_READY` Runtime-Event).
  - [x] Referenz: `novapolis-dev/docs/specs/scheduler-spec.md`.
- [x] [Als naechstes] RP-Panel-Controls: Stundensprung, Auto-Advance (wenn kein PC-Event), Replay-Seed sichtbar machen (nicht im allgemeinen Hub).
  - Evidenz: `novapolis-sim/scripts/Main.gd` (`_set_rp_module_exclusive`, `_on_rp_hour_plus_pressed`, `_on_rp_auto_advance_pressed`, `_run_rp_auto_advance`, `_refresh_rp_studio_ui`) mit `RP_HOUR_JUMP`/`RP_AUTO_ADVANCE`-Events und `rp_replay_seed_label`.

Arbeitsplan Sim-Modul (Analyse 2026-03-02)
------------------------------------------

Ziel: Sim als robusten, nachvollziehbaren End-to-End-Loop zwischen Godot-Client (`novapolis-sim`) und Sim-API (`novapolis_agent/app/api/sim.py`) aufsetzen, inklusive verlässlicher Checks.

Phase 1 - Stabilisierung der Laufzeitkopplung (Jetzt)

- Archiviert: `novapolis-dev/archive/todo.sim.archive.md` (Block `Arbeitsplan Sim-Modul: Phase 1 - Stabilisierung der Laufzeitkopplung (Jetzt)`, `archived_at: 2026-03-03 00:38`).

Phase 2 - Interaktions- und Scheduler-Vorbereitung (Als naechstes)

- Archiviert: `novapolis-dev/archive/todo.sim.archive.md` (Block `Arbeitsplan Sim-Modul: Phase 2 - Interaktions- und Scheduler-Vorbereitung (Als naechstes)`, `archived_at: 2026-03-03 00:38`).

Hub-v1 fuer Framework-Betrieb (konkretisiert 2026-03-02)
--------------------------------------------------------

Zielbild: Das Sim-UI dient als Hub fuer das gesamte Framework (Sim/Agent/Eval/RP) und nicht nur als RPG-Ansicht.

Menuepunkte (Hub-Navigation)

- [x] Dashboard: Gesamtstatus, letzte Events, Schnellaktionen (Start/Stop/Reload/Checks).
  - Fortschritt 2026-03-03: Bereiche `bereich-01..04` in `novapolis-sim/Main.tscn` zur visuellen Slot-Abgrenzung angelegt; Runtime-Layout in `novapolis-sim/scripts/Main.gd` auf die aktuellen Bereichszuschnitte nachgezogen; Input-Hotfix gesetzt (`mouse_filter=2`), damit die Markierungsflaechen keine Schaltflaechen blockieren.
  - Evidenz: `novapolis-sim/scripts/Main.gd` (`_refresh_hub_topbar`, `_refresh_module_cards`, `_on_server_toggle_pressed`, `_on_hub_reload_pressed`, `_on_hub_checks_pressed`) sowie Runtime-Events in `PcLogLabel`.
- [x] Sim: Tick/Zeit, Scheduler-Queue, Runtime-Events, Slot-/Epoch-Navigation.
  - Evidenz: `novapolis-sim/scripts/Main.gd` (`sim_card_tick_label`, `sim_card_queue_label`, `_render_pc_centric_view`, `_on_rp_hour_plus_pressed`) und Scheduler-Hook-Anbindung (`_scheduler_hook.size()`).
- [x] Agent/API: Health, Port/Host, Response-Latenz, letzte Fehler, Retry-Status.
  - Evidenz: `novapolis-sim/scripts/Main.gd` (`api_card_health_label`, `api_card_runtime_label`, `api_card_backoff_label`, `api_card_endpoint_label`, `_derive_health_state`).
- [x] Eval/Training: letzter Lauf, pass_rate, Datensatzquelle, Artefaktstatus.
  - Evidenz: `novapolis-sim/scripts/Main.gd` (`_refresh_latest_eval_summary`, `eval_card_profile_label`, `eval_card_artifacts_label`, `eval_card_notes_label`).
- [x] RP/Content: aktive Quelle/Modul, Sichtbarkeitsstatus, letzte Content-Events.
  - Evidenz: `novapolis-sim/scripts/Main.gd` (`_rp_content_summary`) zeigt im Hub `module=rp`, `vis=...`, `src=<epoch/pc_log@slot>` und `last=<RP_*>` in `eval_card_events_label`.

Statusinformationen (Hub-Topbar + Modul-Karten)

- [x] Verbindung: `API reachable`, `polling active/paused`, `last_ok_age_s`.
  - Evidenz: `novapolis-sim/scripts/Main.gd` (`_refresh_hub_topbar`, `_derive_health_state`) setzt `hub_api_label` mit API-State/Reason/`last_ok` und `hub_polling_label` mit `active|paused`, `fail`, `backoff`.
- [x] Laufzeit: `tick`, `sim_time_s`, `event_rate`, `queue_size` (Scheduler-Hook).
  - Evidenz: `novapolis-sim/scripts/Main.gd` (`_refresh_module_cards`, `_runtime_event_rate_per_second`) setzt `sim_card_tick_label` (`tick/time`) sowie `sim_card_queue_label`/`hub_queue_label` inkl. `rate=.../s` und Queue-Groesse.
- [x] Qualitaet: `tests_last`, `types_last`, `coverage_last` (wenn verfuegbar).
  - Evidenz: `novapolis-sim/scripts/Main.gd` (`_refresh_quality_status`) liest den neuesten `.tmp/results/reports/checks_report_*.json` und setzt `eval_card_notes_label` auf `Quality: tests=... | types=... | cov=...`.
- [x] Daten: `epoch_data_present`, `audio_assets_present`, `dataset_tag`.
  - Evidenz: `novapolis-sim/scripts/Main.gd` (`_refresh_module_cards`) setzt `sim_card_data_label` (`epochs/audio`) und `eval_card_artifacts_label` inkl. aktivem `dataset=<name@tag|n/a>`.
- [x] Fehlerbild: `last_error_code`, `error_duration_s`, `consecutive_failures`.
  - Evidenz: `novapolis-sim/scripts/Main.gd` (`_refresh_hub_topbar`, `_extract_error_code`) zeigt `Errors ... | code=...` in `hub_errors_label`; `consecutive_failures` bleibt in `hub_polling_label` sichtbar.

Priorisierung fuer Umsetzung

- Archiviert: `novapolis-dev/archive/todo.sim.archive.md` (Block `Hub-v1: Priorisierung fuer Umsetzung`, `archived_at: 2026-03-03 00:38`).

Neuordnung offener Punkte nach Zugehoerigkeit (Stand 2026-03-02)
----------------------------------------------------------------

Kanonischer Arbeitsmodus fuer offene Punkte

- Dieser Abschnitt ist ab jetzt die kanonische Sortierung der offenen Sim-/Hub-Aufgaben nach Verantwortungsbereich.
- RP-spezifische Bedienlogik bleibt aus dem allgemeinen Hub herausgetrennt und wird separat im RP-Panel umgesetzt.

A) Hub-Core (frameworkweit, allgemein)

- Archiviert: `novapolis-dev/archive/todo.sim.archive.md` (Block `Neuordnung: A) Hub-Core (frameworkweit, allgemein)`, `archived_at: 2026-03-03 00:38`).

B) RP-spezifische Bedienebene (nicht allgemeiner Hub)

- Archiviert: `novapolis-dev/archive/todo.sim.archive.md` (Block `Neuordnung: B) RP-spezifische Bedienebene (nicht allgemeiner Hub)`, `archived_at: 2026-03-03 00:38`).

C) Agent-Modul im Hub (neu)

- Archiviert: `novapolis-dev/archive/todo.sim.archive.md` (Block `Neuordnung: C) Agent-Modul im Hub (neu)`, `archived_at: 2026-03-04 00:20`).

D) Qualitaet, Governance, Nachweis

- Archiviert: `novapolis-dev/archive/todo.sim.archive.md` (Block `Neuordnung: D) Qualitaet, Governance, Nachweis`, `archived_at: 2026-03-03 00:38`).

Phase 3 - Qualitaet und Nachweisfuehrung (Als naechstes)

- Archiviert: `novapolis-dev/archive/todo.sim.archive.md` (Block `Phase 3 - Qualitaet und Nachweisfuehrung (Als naechstes)`, `archived_at: 2026-03-03 00:38`).

Abschlusskriterien (Definition of Done)

- [x] Ein lokaler Durchlauf deckt API-smoke, Godot-headless und Offline-Asset-Check in fester Reihenfolge ab.
  - Nachweis: API-smoke (`pytest ...::test_get_world_state_initial_values`) PASS, Godot-headless-Load ausgefuehrt, `check_sim_epoch_assets.py --allow-empty --check-slot-consistency` mit `fail:0`.
- [x] Die offenen Sim-Todo-Punkte sind mit Evidenzpfaden im Dev-DONELOG nachweisbar abgeschlossen.
  - Nachweis: `novapolis-dev/docs/donelog.md` (Current-Window Eintraege `Dev/Sim:*` inkl. Archivlauf, RP-Panel-Abschluss und Agent-Studio-Restpunktpakete).





