---
stand: 2026-04-14 12:25
update: Das Sim-Board fuehrt den Replay-/Resume-Punkt jetzt als geschlossen; der Hub nutzt den bestehenden Session-/Replay-Vertrag sichtbar und bedienbar.
checks: snapshot-lock 2026-04-14 12:25; get_errors PASS (Main.gd, Main.tscn); verify_sim.gd headless EXITCODE=0; pytest sim replay/session PASS (EXITCODE=0)
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

- `Jetzt`: Live-Spielclient fuer den ersten Slice statt rein statischer Hub-/Log-Anzeige.
- `Als naechstes`: Replay-/Audio-Bridge und Asset-/Bootstrap-Klarheit fuer denselben Slice.
- `Spaeter`: Komfort- und Atmosphaere-Ausbau erst nach stabilem Produktloop.

Offene Aufgaben (Sim)
---------------------

- [x] [Jetzt] Sim-Hub UI von Grund auf als klaren Spiel-/Operations-Hub neu aufsetzen.
  - Ziel: Die aktuelle Godot-Oberflaeche soll nicht weiter als gewachsene Offset-Sammlung gepflegt werden, sondern einen klaren Hub mit Statusband, Live-Spiel-Flaeche, Operations-Spalte und belastbarer Modulzone erhalten.
  - Akzeptanzkriterien:
    1) der Hub trennt Live-Spiel, Steueraktionen, Telemetrie und Modulzugaenge sichtbar statt mehrere Statusinseln lose uebereinander zu legen,
    2) die bestehenden Bedienpfade fuer Live-Chat, Serversteuerung, Checks, RP und Agent bleiben auf denselben Funktionspfaden benutzbar,
    3) der responsive Layoutpfad in `novapolis-sim/scripts/Main.gd` beschreibt den neuen Hub bewusst als wenige Hauptzonen statt als fortgesetzte Einzelrect-Sammlung,
    4) der neue Aufbau bleibt per Godot-Headless-Ladung ohne Scene-Fehler verifizierbar.
  - Evidenz: `novapolis-sim/Main.tscn` fuehrt den Hub derzeit als breite Menge frei platzierter Labels, Panels und Buttons; `novapolis-sim/scripts/Main.gd` verteilt dieselben Knoten in `_apply_editor_hub_layout()`, `_layout_hub_topbar()`, `_layout_hub_actions()` und `_layout_hub_log_and_cards()` weiterhin ueber viele feste Einzelkoordinaten.
  - Ergebnis 2026-04-14 12:03: Der Hub ist visuell und layoutseitig neu aufgebaut. `Main.tscn` fuehrt jetzt eigene Shell-Zonen (`HubTopBandPanel`, `HubStagePanel`, `HubOpsPanel`, `HubTelemetryPanel`) plus neue Panel-Stile; `scripts/Main.gd` schaltet standardmaessig auf den neuen Responsive-Pfad und layoutet den Hub ueber wenige Hauptrechtecke (`_hub_stage_rect()`, `_hub_ops_rect()`, `_layout_hub_shells()`) statt ueber die alte Freihand-Anordnung.
  - Verifikation 2026-04-14 12:03: Die statische Validierung ist gruen (`get_errors` fuer `Main.gd` und `Main.tscn` ohne Befund). Der kanonische Headless-Verifier `res://scripts/verify_sim.gd` laeuft mit der lokal gestarteten Binary `F:/Downloads/Godot/Godot_v4.6.1-stable_win64.exe` jetzt ebenfalls gruen und liefert `SIM_VERIFY: OK` bei `EXITCODE=0`.

- [x] [Als naechstes] Replay-/Resume-Steuerung fuer `Text-RPG Slice 2 Handover v1` im Hub auf den bestehenden Session-Vertrag heben.
  - Ziel: Der Live-Spielclient soll den bereits vorhandenen Session-/Replay-Vertrag operativ nutzbar machen, statt `resume_checkpoint_id` nur als Label zu zeigen.
  - Akzeptanzkriterien:
    1) der Hub nutzt einen klaren Replay-/Resume-Pfad auf Basis des bestehenden Sessionvertrags statt nur `_request_live_session_state()` auf den aktuellen Snapshot,
    2) Resume-Checkpoint oder Replay-Manifest sind im Client sichtbar waehl- oder abrufbar,
    3) die bestehende Epoch-/Audio-Ansicht bleibt an dieselben Session-Artefakte gebunden,
    4) der neue Pfad bleibt fuer Godot-Bedienung und erwartete Resultate dokumentierbar.
  - Evidenz: `novapolis-sim/scripts/Main.gd` liest aktuell `resume_checkpoint_id` in `_apply_live_session_state()` ein und zeigt ihn nur ueber `rp_replay_seed_label` an; derselbe Client nutzt fuer Live-Sync `_request_live_session_state()` auf dem Session-Snapshot, fuehrt aber keinen sichtbaren Replay-/Checkpoint-Requestpfad. `novapolis-dev/docs/process/text-rpg-slice-2-handover-v1.ssot.md` fixiert diesen Resume-Anker jetzt als gemeinsamen Folgevertrag hinter `slot 30`.
  - Arbeitsstand 2026-04-14 12:09: Der Backend-Vertrag ist bereits da. `novapolis_agent/app/api/sim.py` liefert `GET /session/{session_id}` und `GET /session/{session_id}/replay`, inklusive `resume_checkpoint_id`, `checkpoints`, `artifact_paths` und Replay-Zaehlern. Im Sim-Client fehlt aktuell nur der operative Pfad: `scripts/Main.gd` ruft weiterhin lediglich `_request_live_session_state()` und nutzt den Replay-Endpunkt noch nirgends.
  - Ergebnis 2026-04-14 12:21: Der Hub fuehrt jetzt einen eigenen Replay-/Resume-Block. `novapolis-sim/Main.tscn` enthaelt `HubReplayPanel` mit Checkpoint-Auswahl sowie `Replay Sync`- und `Resume-Anker`-Buttons; `novapolis-sim/scripts/Main.gd` ruft den bestehenden Endpunkt `GET /session/{session_id}/replay` jetzt explizit auf, synchronisiert Manifestdaten in denselben Session-/Artefaktpfad und wendet den gewaehlten Resume-Anker ohne Parallelformat auf Slot- und Logansicht an.
  - Verifikation 2026-04-14 12:21: Die statische Pruefung bleibt gruen (`get_errors` fuer `Main.gd` und `Main.tscn` ohne Befund), der kanonische Headless-Verifier `res://scripts/verify_sim.gd` endet mit `EXITCODE=0`, und der gezielte Session-/Replay-Vertragspfad `python -m pytest -q novapolis_agent/tests/test_api_sim_state.py novapolis_agent/tests/tests_sim_api.py` endet ebenfalls mit `EXITCODE=0`.

- [x] [Jetzt] Live-Spielclient fuer den ersten Text-RPG-Slice statt nur Hub-Chat und statischer Epoch-Logs bauen.
  - Akzeptanzkriterium: Die Sim kann eine laufende Spielsession mit aktueller Szene, angebotenen Optionen, Spielereingabe und Rueckmeldung anzeigen, statt nur freie Chat-Nachrichten und vorab gespeicherte Logs zu rendern.
  - Arbeitsstand 2026-04-07: Der bestehende Hub-Chat bleibt bewusst die UI-Basis, wird aber auf den Text-RPG-Pfad gehoben: Der Client sendet Sitzungsrahmen und Orchestrator-Hinweise mit, haelt eine laufende Session-ID und zeigt Szene, Konsequenz, Optionen und Patch-Vorschau als sichtbaren Sessionstand an.
  - Ergebnis 2026-04-07: `novapolis-sim/scripts/Main.gd` sendet den Hub-Chat jetzt mit `orchestrator_enabled`, `campaign_id`, `scene_id`, `slot_id`, `turn_id`, `public_context`, `state_patch_hints` und `retrieval_query` an denselben `/chat`-Pfad; eingehende Antworten werden fuer Szene/Konsequenz/Optionen/State-Patches geparst, im bestehenden Panel als Live-Spielclient gerendert und anschliessend ueber `GET /session/{session_id}` mit dem kanonischen Sessionstand nachgezogen.
  - Evidenz: `_refresh_hub_chat_ui()` in `novapolis-sim/scripts/Main.gd` zeigt Session, Slot/Scene, Szene, Konsequenz, Optionen, State-Patches und das Chat-Protokoll direkt im Hub; `_on_hub_chat_send_pressed()` sendet die laufende Spielereingabe an `/chat`; `_on_hub_chat_request_completed()` und `_on_hub_session_request_completed()` aktualisieren danach denselben sichtbaren Sessionstand.

- [x] [Als naechstes] Replay-/Epoch-Bridge an denselben Agent-Session-Vertrag koppeln.
  - Akzeptanzkriterium: Live-Lauf, gespeicherter Run und Replay nutzen dasselbe Session-/Slot-Modell; `world_log`, `pc_log` und spaetere Audioartefakte lassen sich im Sim-Client ohne Parallelformat laden oder abspielen.
  - Ergebnis 2026-04-07: `novapolis-sim/scripts/Main.gd` zieht den aktuellen Sessionstand jetzt ueber `GET /session/{session_id}` vom Sim-API-Host nach, mappt `world_log`/`pc_log` direkt in dieselbe Epochenansicht, uebernimmt `slot_id`/`slot_index` aus dem Sessionvertrag und markiert `tts_manifest` als live verfuegbaren Audiopfad statt nur `res://data/epochs` zu scannen.
  - Evidenz: `_load_epochs()` in `novapolis-sim/scripts/Main.gd` erwartete zuvor nur lokale Dateien unter `res://data/epochs/<epoch>/world_log.jsonl` und `pc_log.jsonl`, waehrend `novapolis_agent/app/api/sim.py` den kanonischen Session-/Replay-Stand bereits ueber `GET /session/{session_id}` bereitstellt.

- [x] [Als naechstes] Sim-Asset-Warnungen aus `scripts/check_sim_epoch_assets.py` aufloesen oder bewusst kanonisch ausnehmen.
  - Akzeptanzkriterium: Der Check liefert entweder `warn:0` oder die verbleibenden Warnungen sind als absichtliche Ausnahme im Sim-Runbook/Board mit Ursache, Scope und Wiedervorlage dokumentiert.
  - Ergebnis 2026-04-07: `scripts/check_sim_epoch_assets.py` behandelt `--allow-empty` jetzt als kanonisches Clean-Checkout-Profil statt als Warnpfad; fehlende `epochNN`-Ordner und fehlende `.ogg`-Dateien werden in diesem Profil als `INFO` statt `WARN` gewertet, und der Lauf `--repo-root . --allow-empty --check-slot-consistency` endet im aktuellen Repo-Stand mit `summary=fail:0,warn:0`.
  - Evidenz: Derselbe Checker-Lauf meldete zuvor `WARN|no epochNN folders found` und `WARN|audio directory missing`; nach dem Profil-Fix liefert er nur noch `INFO`-Zeilen und `warn:0`.

- [x] [Als naechstes] Minimalen Offline-Bootstrap fuer Epoch- und Audio-Assets definieren, damit der Asset-Check auf Clean-Checkout nicht zwischen Pflicht- und Optionaldaten verschwimmt.
  - Akzeptanzkriterium: Es gibt entweder ein kleines kanonisches Fixture-Set fuer `warn:0` oder eine explizite Profiltrennung `Clean-Checkout` vs. `Vollstand` mit unterschiedlicher Check-Erwartung und dokumentiertem Bootstrap-Pfad.
  - Ergebnis 2026-04-07: Der Offline-Asset-Check kennt jetzt zwei Profile: `Clean-Checkout` mit `--allow-empty` fuer einen warnungsfreien Minimalstand ohne `epochNN`-Ordner oder OGG-Dateien, und `Vollstand` ohne dieses Flag fuer echte Offline-Artefakte. Die Bootstrap-Pfade `novapolis-sim/data/epochs/` und `novapolis-sim/assets/audio/` sind als kanonische Zielorte angelegt und in der Sim-README beschrieben.
  - Evidenz: `scripts/check_sim_epoch_assets.py` dokumentiert `--allow-empty` jetzt explizit als Clean-Checkout-Bootstrap; `novapolis-sim/README.md` trennt denselben Minimalstand vom Vollstand-Pfad.

- [x] [Spaeter] Platzhalterblock aufgeloest: das Sim-Board nutzt keine pauschale Sammelrubrik mehr; Restarbeit wird nur noch als konkrete Einzelpunkte gefuehrt.
  - [x] Headless-Lade-Check `novapolis-sim/project.godot` durchführen; Kurzprotokoll in `novapolis-dev/docs/donelog.md`.
    - Evidenz: `WORKSPACE_STATUS.md` (2025-11-16 04:54, Headless PASS) und `novapolis-dev/docs/donelog.md` (Abschnitt "Godot Headless - Quick Verification").
- [x] [Als naechstes] Hub-Hauptmenue: kleines Chatfenster integriert (Prompt + Antwort + `/chat`-Roundtrip) fuer lokalen Gespraechsmodus direkt im Sim-Hub.
  - Evidenz: `novapolis-sim/Main.tscn` (`HubChatPanel` + Input/Output/Status + `HubChatRequest`) und `novapolis-sim/scripts/Main.gd` (Senden, Endpoint-Aufbau, Response-Handling, Fehlerfall/Status).

Aktiver Kontext (max. 14 Tage)
------------------------------

- 2026-04-14: Der Sim-Hub ist in diesem Lauf layoutseitig neu aufgesetzt und inzwischen auch mit lokaler Godot-4.6.1-Binary headless verifiziert. Der bestehende Live-Spielclient, die Modulpfade und der offene Resume-/Replay-Punkt bleiben funktional erhalten, waehrend der Hub jetzt ueber Top-Band, Stage, Operations-Spalte und Telemetrieband organisiert wird.

- 2026-04-14: Der letzte offene Bedienpfad ist jetzt ebenfalls geschlossen. Der Hub hat einen sichtbaren Replay-/Resume-Block, nutzt `GET /session/{session_id}/replay` explizit neben dem Session-Snapshot und spiegelt den aktiven Resume-Anker in Hub-, Stage- und RP-Ansicht.

- 2026-04-07: Der Sim-Offline-Check kennt jetzt ein kanonisches Clean-Checkout-Profil. `scripts/check_sim_epoch_assets.py --repo-root . --allow-empty --check-slot-consistency` liefert im aktuellen Repo-Stand `summary=fail:0,warn:0`; Vollstand-Laeufe ohne `--allow-empty` pruefen weiter echte Offline-Artefakte.
- 2026-03-27: Wochenabschluss-Refresh. `scripts/check_sim_epoch_assets.py --repo-root . --allow-empty --check-slot-consistency` blieb damals ohne harte Fehler (`summary=fail:0,warn:2`); die Restwarnungen zu fehlenden Epoch-Ordnern und Audio-Assets sind seit 2026-04-07 ueber das Clean-Checkout-Profil geschlossen.
- 2026-03-11: Mikrodrift bereinigt (`offen: 1 -> 0`) und Referenz-Checkbox fuer Scheduler-Spec auf erledigt gesetzt.
- 2026-03-10: Hub-Hauptmenue-Chatfenster abgeschlossen (UI + `/chat`-Roundtrip + robustes Fehlerhandling).

Archivhinweis
-------------

- Aeltere und vollstaendig erledigte Sim-Bloecke liegen in `novapolis-dev/archive/todo.sim.archive.md`.
- Technische Nachweise liegen in `novapolis-dev/docs/donelog.md` (Current-Window) und `DONELOG.md` (Root-Summary).





