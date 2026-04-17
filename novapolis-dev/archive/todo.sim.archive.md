---
stand: 2026-04-17 04:39
update: Der zuletzt geschlossene Sim-Abschlussschnitt ist jetzt aus dem Live-Board ins Sim-Archiv uebernommen und mit archived_at dokumentiert.
checks: snapshot-lock PASS (2026-04-17 04:27); markdownlint=PASS; frontmatter=PASS; todo-index-sync=PASS
---

TODO-Archiv - Sim
=================

Zweck: Vollständig abgeschlossene TODO-Abschnitte aus `novapolis-sim/**` Aufgaben aufnehmen.

Regeln (kurz)
- Nur vollständig abgehakte Abschnitte ([x] überall) verschieben.
- Inhalt unverändert übernehmen; unter der Abschnitts-Überschrift `archived_at: YYYY-MM-DD HH:MM` ergänzen.
- Headings in diesem Archiv: Setext (MD003 konform, H1/H2).
- Präsentation: Lint-Läufe mit PRESENTATION=SHARED.

Ablage
- Neueste Einträge oben einfügen.

<!-- Hier unterhalb neue, vollständig erledigte Blöcke einfügen (neu zuerst). -->

Offene Aufgaben (Sim) - Abschlussschnitt 2026-04-17
---------------------------------------------------

archived_at: 2026-04-17 04:27

Quelle: `novapolis-dev/docs/todo.sim.md` (Abschnitt `Offene Aufgaben (Sim)`, Stand 2026-04-17 04:24).

- [x] [Jetzt] Sim-Hub nach dem Layout-Reset in modulare Controller und Runtime-Dienste zerlegen.
  - Ziel: `novapolis-sim/scripts/Main.gd` soll nicht dauerhaft zugleich Layout-Manager, Session-Client, Replay-Steuerung, Audio-Bridge, Agent-/Checks-/RP-Menue und Prozess-Orchestrator bleiben.
  - Akzeptanzkriterien:
    1) Hub-Layout, Session-/Replay-Lebenszyklus, Runtime-/Process-Steuerung und Modulnavigation liegen in getrennten Scripts oder klar abgegrenzten Controller-Komponenten,
    2) `Main.gd` bleibt sichtbarer Einstieg, verliert aber den All-in-One-Charakter als zentrale Sammelstelle fuer nahezu jeden Sim-Pfad,
    3) bestehende Node-Pfade und Bedienwege fuer Hub, Agent, Checks und RP bleiben kompatibel oder der Migrationspfad ist im selben Lauf dokumentiert,
    4) der Headless-Start bleibt ohne neue Scene-Fehler verifizierbar.
  - Evidenz: Unter `novapolis-sim/scripts/` liegen mittlerweile bereits eigene Controller fuer Hub-Layout, Hub-Config, Hub-Chat, Session-/Replay-Helper, Session-/Replay-Requests, Session-/Replay-State, Checks/RP, Agent-Studio-UI, Agent-Form-UI, Agent-Runtime, Agent-Authoring-Payloads, Agent-Authoring-Persistenz, Registry-/State-Lader, Restpoint-Summaries, Server-Ops, Runtime-Audit und jetzt auch Runtime-Telemetrie. Offen bleiben in `Main.gd` nach diesem Schnitt praktisch nur noch kleinere Cleanup-Altlasten wie unreferenzierte Runtime-Helfer und harmlose Format-/Textbausteine statt eines weiteren grossen Verantwortungsblocks.
  - Arbeitsstand 2026-04-14 13:29: Der erste Refactor-Schnitt bleibt bewusst klein und kompatibel. Zuerst wandern Session-/Replay-Normalisierung, Checkpoint-/Slot-Helfer und das Laden/Speichern der Hub-Prefs in eigene Runtime-Helfer, waehrend `Main.gd` die Node-Anbindung und sichtbaren Bedienpfade unveraendert behaelt.
  - Ergebnis 2026-04-14 13:29: `novapolis-sim/scripts/hub_preferences_store.gd` und `novapolis-sim/scripts/session_replay_helpers.gd` sind neu. `novapolis-sim/scripts/Main.gd` delegiert das Laden/Speichern der Hub-Prefs, die Session-/Replay-Normalisierung, Endpoint-Bildung sowie Checkpoint-/Slot-Helfer jetzt an diese Runtime-Helfer, behaelt aber vorerst die sichtbare Node- und UI-Orchestrierung als kompatible Fassade.
  - Verifikation 2026-04-14 13:29: `get_errors` bleibt fuer `novapolis-sim/scripts/Main.gd`, `novapolis-sim/scripts/hub_preferences_store.gd` und `novapolis-sim/scripts/session_replay_helpers.gd` ohne Befund. Ein erneuter Godot-Headless-Lauf war in diesem Terminal-Kontext nicht belegbar, weil keine lokal aufloesbare Godot-Binary im PATH gemeldet wurde.
  - Arbeitsstand 2026-04-14 13:49: Der zweite Schnitt zieht nicht mehr nur Daten-Helfer aus `Main.gd`, sondern die eigentliche Session-/Replay-Request-Statemaschine. In-Flight-Status, Request-Guards und Response-Auswertung fuer Session- und Replay-HTTP-Laeufe sollen in einen eigenen Controller wandern, waehrend `Main.gd` nur noch Resultate auf Epochen-, Replay- und UI-Zustand abbildet.
  - Ergebnis 2026-04-14 13:49: `novapolis-sim/scripts/session_replay_request_controller.gd` ist neu. `novapolis-sim/scripts/Main.gd` delegiert Startbedingungen, In-Flight-Status und Response-Auswertung fuer Session- und Replay-Requests jetzt an diesen Controller; `Main.gd` behaelt fuer diese Pfade nur noch Host/Port-Aufloesung sowie die Abbildung erfolgreicher Resultate auf Sim-Zustand und UI.
  - Verifikation 2026-04-14 13:49: `get_errors` bleibt fuer `novapolis-sim/scripts/Main.gd`, `novapolis-sim/scripts/session_replay_request_controller.gd`, `novapolis-sim/scripts/session_replay_helpers.gd` und `novapolis-sim/scripts/hub_preferences_store.gd` ohne Befund. Ein erneuter Godot-Headless-Lauf bleibt weiter offen, solange keine lokal aufloesbare Godot-Binary fuer den Terminalkontext verfuegbar ist.
  - Naechster Schnitt 2026-04-14 13:57: Nach den Helper- und Request-Controllern soll als naechste Entflechtung die Session-/Replay-Zustandsanwendung selbst in einen eigenen State-Controller wandern, damit `Main.gd` in diesen Pfaden nur noch UI-Komposition statt Zustandsmutation traegt.
  - Arbeitsstand 2026-04-14 14:02: Dieser dritte Schnitt zieht jetzt die eigentlichen State-Transitionen aus `Main.gd`: Live-Session-Anwendung, Replay-Manifest-Uebernahme und Resume-/Checkpoint-Anwendung sollen in einen eigenen Controller wandern, waehrend `Main.gd` nur noch die daraus resultierenden Zustands-Snapshots auf bestehende Member spiegelt und UI-Refreshes ausloest.
  - Ergebnis 2026-04-14 14:02: `novapolis-sim/scripts/session_replay_state_controller.gd` ist neu. `novapolis-sim/scripts/Main.gd` delegiert die Live-Session-Anwendung, die Replay-Manifest-Uebernahme und die Resume-/Checkpoint-State-Transition jetzt an diesen Controller und spiegelt nur noch die resultierenden Snapshot-Updates auf bestehende Member, bevor UI-Refreshes laufen.
  - Verifikation 2026-04-14 14:02: `get_errors` bleibt fuer `novapolis-sim/scripts/Main.gd`, `novapolis-sim/scripts/session_replay_state_controller.gd`, `novapolis-sim/scripts/session_replay_request_controller.gd` und `novapolis-sim/scripts/session_replay_helpers.gd` ohne Befund. Ein echter Godot-Headless-Lauf bleibt fuer diesen Refactor weiterhin nur mit lokaler Binary moeglich.
  - Arbeitsstand 2026-04-14 14:10: Als naechster kleiner Schnitt folgt jetzt der Hub-Chat-Pfad. Prompt-Aufbau, Retrieval-Query, Antwort-Parsing und Chat-State-Anwendung sind bislang noch direkt in `Main.gd` verdrahtet, obwohl dieser Pfad inhaltlich bereits wie ein eigener Runtime-Controller funktioniert.
  - Ergebnis 2026-04-14 14:10: `novapolis-sim/scripts/hub_chat_controller.gd` ist neu. `novapolis-sim/scripts/Main.gd` delegiert Slot-/Context-Aufbau, Request-Start, Response-Auswertung und Chat-State-Anwendung fuer den Live-Spielclient jetzt an diesen Controller und behaelt fuer den Chat-Pfad nur noch Widget-Status, Logzeilen und die anschliessenden UI-/Session-Refreshes.
  - Verifikation 2026-04-14 14:10: `get_errors` bleibt fuer `novapolis-sim/scripts/Main.gd` und `novapolis-sim/scripts/hub_chat_controller.gd` ohne Befund. Ein echter Godot-Headless-Lauf bleibt auch fuer diesen Schnitt weiter von einer lokal verfuegbaren Binary abhaengig.
  - Arbeitsstand 2026-04-14 14:25: Nach Session-/Replay und Hub-Chat folgen in diesem Sammellauf die letzten klar abgegrenzten Controller-Schnitte fuer `Main.gd`: der Responsive-/Hub-Layoutpfad, der Hub-Config-/Prefs-Bedienpfad sowie der Checks-/RP-Modulpfad. Der deutlich breitere Agent-Studio-Block bleibt bewusst ausserhalb dieses Laufs, weil er aktuell noch Form-State, Scriptstarts, Registry-Lader und Runtime-Refreshs zu eng koppelt, um als kleiner sicherer Controller-Schnitt zu gelten.
  - Ergebnis 2026-04-14 14:36: `novapolis-sim/scripts/hub_layout_controller.gd`, `hub_config_controller.gd` und `checks_rp_controller.gd` sind neu. `novapolis-sim/scripts/Main.gd` delegiert damit jetzt auch den Responsive-/Hub-Layoutpfad, die Hub-Config-/Prefs-Bedienlogik sowie die Checks-/RP-Modul-UI in eigene Controller und behaelt fuer diese Bereiche nur noch Zustandsfluss, Node-Fassade und die verbleibend eng gekoppelte Agent-Studio-Orchestrierung.
  - Verifikation 2026-04-14 14:36: `get_errors` bleibt fuer `novapolis-sim/scripts/Main.gd`, `novapolis-sim/scripts/hub_layout_controller.gd`, `novapolis-sim/scripts/hub_config_controller.gd` und `novapolis-sim/scripts/checks_rp_controller.gd` ohne Befund. Ein echter Godot-Headless-Lauf bleibt fuer diesen Sammelschnitt weiter offen, solange im aktuellen Terminalkontext keine lokal aufloesbare Godot-Binary belegbar ist.
  - Ergebnis 2026-04-14 14:49: `novapolis-sim/scripts/agent_studio_controller.gd` ist neu. `novapolis-sim/scripts/Main.gd` delegiert damit jetzt auch Agent-Studio-UI-Exklusivschaltung, Agent-Studio-Layout und den zentralen Studio-UI-Refresh in einen eigenen Controller; zusaetzlich sind die versehentlich doppelt angehaengten Dateihälften in `hub_config_controller.gd` und `checks_rp_controller.gd` im selben Lauf bereinigt.
  - Verifikation 2026-04-14 14:49: `get_errors` bleibt fuer `novapolis-sim/scripts/Main.gd`, `novapolis-sim/scripts/agent_studio_controller.gd`, `novapolis-sim/scripts/hub_config_controller.gd` und `novapolis-sim/scripts/checks_rp_controller.gd` ohne Befund. Ein echter Godot-Headless-Lauf bleibt fuer diesen Agent-Schnitt weiter offen, solange im aktuellen Terminalkontext keine lokal aufloesbare Godot-Binary belegbar ist.
  - Ergebnis 2026-04-14 15:01: `novapolis-sim/scripts/hub_layout_controller.gd` ist nach einem Runtime-Befund auf Datei-Integritaet nachgezogen. Die angehaengte zweite Klassenhaelfte wurde entfernt; damit entfaellt der Parserfehler beim `preload("res://scripts/hub_layout_controller.gd")` in `Main.gd`.
  - Verifikation 2026-04-14 15:01: Der Doppelbezeichner `class_name HubLayoutController` liegt in `hub_layout_controller.gd` wieder nur einmal vor, und `get_errors` bleibt fuer `novapolis-sim/scripts/Main.gd` sowie `novapolis-sim/scripts/hub_layout_controller.gd` ohne Befund.
  - Arbeitsstand 2026-04-15 03:00: Der heutige Lauf schliesst bewusst nicht kuenstlich den Architekturrest, sondern grenzt ihn schaerfer ein. Die Sim fuehrt jetzt Persistenz-, Export- und IA-SSOTs kanonisch, aber `Main.gd` bleibt im Agent-Studio-Pfad weiter der Ort fuer Form-State-Aufbau und mehrere Runtime-Aktionshandler. Genau dieser Rest bleibt als letzter offener Sim-Punkt stehen.
  - Ergebnis 2026-04-15 04:39: `novapolis-sim/scripts/agent_form_controller.gd` ist neu. `novapolis-sim/scripts/Main.gd` delegiert damit jetzt auch Oeffnen, Dropdown-Normalisierung, Platzhalter, Layout und dynamischen Feldaufbau der Agent-Formulare an einen eigenen Controller; die ungenutzten `_build_*_form_template()`-Helfer sind aus `Main.gd` entfernt.
  - Verifikation 2026-04-15 04:39: `get_errors` bleibt fuer `novapolis-sim/scripts/Main.gd`, `novapolis-sim/scripts/agent_form_controller.gd` und `novapolis-sim/scripts/agent_studio_controller.gd` ohne Befund. Ein echter Godot-Headless-Lauf bleibt fuer diesen Refactor weiterhin offen, solange im aktuellen Terminalkontext keine lokal aufloesbare Godot-Binary belegbar ist.
  - Ergebnis 2026-04-15 04:56: Der Modulwechsel blendet das Hub jetzt ohne Zwischenzustand aus. `Main.gd` fuehrt fuer Agent/Checks/RP einen `defer_hub_refresh`-Pfad ein und setzt die Hub-Sichtbarkeit erst einmal zentral ueber `_apply_hub_visibility_for_modules()`. Dadurch verschwindet das kurzzeitige Wieder-Einblenden des Hubs beim Wechsel zwischen zwei exklusiven Modulen.
  - Verifikation 2026-04-15 04:56: `get_errors` bleibt fuer `novapolis-sim/scripts/Main.gd`, `novapolis-sim/scripts/agent_form_controller.gd` und `novapolis-sim/scripts/agent_studio_controller.gd` ohne Befund. Ein echter Godot-Headless-Lauf bleibt fuer diesen UI-Fix weiterhin offen, solange im aktuellen Terminalkontext keine lokal aufloesbare Godot-Binary belegbar ist.
  - Arbeitsstand 2026-04-15 05:02: Der aktuelle Bildbefund zeigt weiterhin sichtbare Hub-Topbar-Elemente im Agent-Modul (`HubTitle/API/Polling/Queue/Errors`) sowie zwei JSON-Parsefehler im Session-/Replay-Request-Controller. Der Lauf adressiert beides als kleinen kompatiblen Debug-Schnitt.
  - Ergebnis 2026-04-15 05:02: `novapolis-sim/scripts/Main.gd` blendet beim exklusiven Modulmodus jetzt auch die separaten Topbar-Labels (`hub_title_label`, `hub_api_label`, `hub_polling_label`, `hub_queue_label`, `hub_errors_label`) aus. `novapolis-sim/scripts/session_replay_request_controller.gd` verwendet in `complete_live_session()` und `complete_live_replay()` jetzt robustes JSON-Parsing via `JSON.new().parse(...)` mit kontrollierter `parse_error`-Rueckgabe statt harter `JSON.parse_string`-Fehler.
  - Verifikation 2026-04-15 05:02: `get_errors` bleibt fuer `novapolis-sim/scripts/Main.gd` und `novapolis-sim/scripts/session_replay_request_controller.gd` ohne Befund. Ein echter Godot-Headless-Lauf bleibt fuer diesen Debug-Fix weiterhin offen, solange im aktuellen Terminalkontext keine lokal aufloesbare Godot-Binary belegbar ist.
  - Arbeitsstand 2026-04-17 00:33: Der verbliebene Architekturrest ist gegen den aktuellen Codezustand nachgeschaerft. Die offenen Zustaendigkeiten liegen nicht mehr bei Form-UI oder Layout, sondern in drei klaren Restbloecken: Form-Payload-Building mit lokaler Validation, Datei-/Registry-Persistenz fuer Authoring-Aktionen und Runtime-/Prozesssteuerung fuer Eval, Finetune und Jobs.
  - Naechster Schnitt 2026-04-17 00:33: 1) Payload-/Validation-Building aus `Main.gd` in einen eigenen Agent-Authoring-Service ziehen, 2) Dataset-/Synonym-/Profile-/Advanced-/Jobs-Persistenz samt Registry-Updates in einen getrennten IO-Service ziehen, 3) Eval-/Finetune-/Job-Runtime inklusive Start/Stop-/Confirm-Logik in einen eigenen Runtime-Controller ziehen, 4) `Main.gd` danach auf UI-Wiring, Status-Refresh und Controller-Fassade begrenzen.
  - Arbeitsstand 2026-04-17 00:39: Der aktuelle Lauf zieht jetzt zuerst Punkt 3 vor. Betroffen sind im bestehenden Iststand vor allem `_on_agent_eval_run_pressed()`, `_apply_finetune_form_payload()`, `_apply_jobs_form_payload()`, `_refresh_eval_runtime_state()`, `_refresh_finetune_runtime_state()` sowie die zugehoerigen Job-/Finetune-Helfer in `Main.gd`.
  - Ergebnis 2026-04-17 00:50: `novapolis-sim/scripts/agent_runtime_controller.gd` ist neu. `novapolis-sim/scripts/Main.gd` delegiert Eval-Start/Stop, Finetune-Start/Stop, Jobs-Queue-Mutationen, Destructive-Guard und die Eval-/Finetune-Runtime-Refreshes jetzt an diesen Controller; `Main.gd` behaelt in diesem Restblock nur noch Zustandsspiegelung, UI-Refresh und die bereits bestehenden Persistenz-/Payload-Pfade.
  - Verifikation 2026-04-17 00:50: `get_errors` bleibt fuer `novapolis-sim/scripts/Main.gd` und `novapolis-sim/scripts/agent_runtime_controller.gd` ohne Befund. Ein echter Godot-Headless-Lauf bleibt fuer diesen Schnitt weiterhin offen, solange im aktuellen Terminalkontext keine lokal aufloesbare Godot-Binary belegbar ist.
  - Arbeitsstand 2026-04-17 00:58: Der verbleibende Rest ist jetzt dokumentarisch bis auf Controller-Ebene vorbereitet. `novapolis-dev/docs/process/sim-controller-roadmap.ssot.md` fuehrt als direkte Folge nach dem Runtime-Schnitt die Kandidaten `AgentAuthoringPayloadController`, `AgentAuthoringPersistenceController`, `AgentRegistryStateController`, `AgentRestpointSummaryController`, `HubServerOpsController` und `RuntimeAuditController` mit Evidenzfunktionen, Prioritaet und Abgrenzung.
  - Naechster Schnitt 2026-04-17 00:58: Direkt sinnvoll bleiben weiterhin zuerst 1) `AgentAuthoringPayloadController` fuer `_build_agent_form_payload_from_controls()` samt `_form_control_*()` und 2) `AgentAuthoringPersistenceController` fuer `_apply_dataset_form_payload()`, `_apply_synonym_form_payload()`, `_apply_profile_form_payload()` und `_apply_advanced_settings_form_payload()`. Registry-/Summary-/Server-/Audit-Controller sind als nachgelagerte, aber dokumentierte Folgepfade vorbereitet.
  - Arbeitsstand 2026-04-17 01:10: Der aktuelle Codeschnitt zieht jetzt Punkt 1 aus der Roadmap vor. Betroffen sind im belegten Iststand `_build_agent_form_payload_from_controls()`, `_form_control_text()`, `_form_control_int()`, `_form_control_float()`, `_form_control_bool()` und `_form_control_csv_array()`; `Main.gd` soll diesen Block danach nur noch fuer Form-Dispatch und Statusanwendung nutzen.
  - Ergebnis 2026-04-17 01:16: `novapolis-sim/scripts/agent_authoring_payload_controller.gd` ist neu. `novapolis-sim/scripts/Main.gd` delegiert das Form-Control-Lesen, lokale Pflichtfeldpruefung und die kanonische Payload-Normalisierung fuer Datasets, Synonyms, Finetune, Profiles, Advanced und Jobs jetzt an diesen Controller; `Main.gd` behaelt in diesem Pfad nur noch Form-Dispatch und Statusanwendung.
  - Verifikation 2026-04-17 01:16: `get_errors` bleibt fuer `novapolis-sim/scripts/Main.gd` und `novapolis-sim/scripts/agent_authoring_payload_controller.gd` ohne Befund. Ein echter Godot-Headless-Lauf bleibt fuer diesen Refactor weiterhin offen, solange im aktuellen Terminalkontext keine lokal aufloesbare Godot-Binary belegbar ist.
  - Ergebnis 2026-04-17 01:24: `novapolis-sim/scripts/agent_authoring_persistence_controller.gd` ist neu. `novapolis-sim/scripts/Main.gd` delegiert Dataset-/Synonym-/Profile-/Advanced-Persistenz, Synonym-Import/Export, lokale Persistenz-Validation und die zugehoerigen Registry-Schreibpfade jetzt an diesen Controller; `Main.gd` behaelt in diesem Restblock nur noch Resultat-Anwendung und Runtime-Event-Weitergabe.
  - Verifikation 2026-04-17 01:24: `get_errors` bleibt fuer `novapolis-sim/scripts/Main.gd` und `novapolis-sim/scripts/agent_authoring_persistence_controller.gd` ohne Befund. Ein echter Godot-Headless-Lauf bleibt fuer diesen Refactor weiterhin offen, solange im aktuellen Terminalkontext keine lokal aufloesbare Godot-Binary belegbar ist.
  - Ergebnis 2026-04-17 01:32: `novapolis-sim/scripts/agent_registry_state_controller.gd` ist neu. `novapolis-sim/scripts/Main.gd` delegiert Dataset-/Synonym-/Profile-/Advanced-State-Laden sowie das Security-Model-Laden und dessen Default-Persistenz jetzt an diesen Controller; `Main.gd` behaelt in diesem Restblock nur noch die Anwendung der geladenen Zustandswerte.
  - Verifikation 2026-04-17 01:32: `get_errors` bleibt fuer `novapolis-sim/scripts/Main.gd` und `novapolis-sim/scripts/agent_registry_state_controller.gd` ohne Befund. Ein echter Godot-Headless-Lauf bleibt fuer diesen Refactor weiterhin offen, solange im aktuellen Terminalkontext keine lokal aufloesbare Godot-Binary belegbar ist.
  - Ergebnis 2026-04-17 02:00: `novapolis-sim/scripts/agent_restpoint_summary_controller.gd`, `hub_server_ops_controller.gd` und `runtime_audit_controller.gd` sind neu. `novapolis-sim/scripts/Main.gd` delegiert damit jetzt auch Restpoint-Summary-Bildung, lokale Serversteuerung sowie Runtime-Event-/Audit-Trail-Persistenz an eigene Controller; `Main.gd` behaelt in diesem Restblock nur noch Zustandsanwendung, Health-Ableitung und einige gemeinsame Runtime-Helfer.
  - Verifikation 2026-04-17 02:00: `get_errors` bleibt fuer `novapolis-sim/scripts/Main.gd`, `novapolis-sim/scripts/agent_restpoint_summary_controller.gd`, `novapolis-sim/scripts/hub_server_ops_controller.gd` und `novapolis-sim/scripts/runtime_audit_controller.gd` ohne Befund. Ein echter Godot-Headless-Lauf bleibt fuer diesen Refactor weiterhin offen, solange im aktuellen Terminalkontext keine lokal aufloesbare Godot-Binary belegbar ist.
  - Ergebnis 2026-04-17 02:07: `novapolis-sim/scripts/runtime_telemetry_controller.gd` ist neu. `novapolis-sim/scripts/Main.gd` delegiert damit jetzt auch Eval-Summary-Refresh, Trendbildung, System-Metrik-Refresh, Python-Aufloesung sowie Health-/Reachability-Ableitung an einen eigenen Telemetrie-Controller; `Main.gd` behaelt in diesem Restblock nur noch wenige harmlose Wrapper und verbleibende Cleanup-Altlasten.
  - Verifikation 2026-04-17 02:07: `get_errors` bleibt fuer `novapolis-sim/scripts/Main.gd` und `novapolis-sim/scripts/runtime_telemetry_controller.gd` ohne Befund. Ein echter Godot-Headless-Lauf bleibt fuer diesen Refactor weiterhin offen, solange im aktuellen Terminalkontext keine lokal aufloesbare Godot-Binary belegbar ist.
  - Naechster Schnitt 2026-04-17 02:07: Direkt anschliessend bleiben nur noch kleinere Cleanup-Altlasten wie unreferenzierte Runtime-Helfer (`_resolve_finetune_train_file()`, `_start_finetune_run()`) und vereinzelte harmlose Format-/Texthelfer. Das ist eher Bereinigung als weiterer Architektur-Umbau.
  - Arbeitsstand 2026-04-17 04:20: Der offene Architekturpunkt ist jetzt am Codezustand nachgemessen. `novapolis-sim/scripts/Main.gd` fuehrt `_resolve_finetune_train_file()` und `_start_finetune_run()` noch lokal, obwohl die Finetune-Runtime bereits in `novapolis-sim/scripts/agent_runtime_controller.gd` lebt; fuer `res://scripts/verify_sim.gd` gibt es ausser README-Text und internen Checks-Bausteinen noch keinen kanonischen Workspace-Task oder Python-Wrapper.
  - Naechster Schnitt 2026-04-17 04:20: 1) lokale Finetune-Altlasten aus `Main.gd` entfernen, 2) einen Root-Wrapper fuer `verify_sim.gd` mit `GODOT_BIN`/PATH-Fallback einziehen, 3) denselben Smoke-Pfad in `.vscode/tasks.json`, `novapolis-sim/README.md` und den relevanten Sim-SSOTs angleichen.
  - Ergebnis 2026-04-17 04:24: `novapolis-sim/scripts/Main.gd` fuehrt die doppelten lokalen Finetune-Helfer nicht mehr; die Runtime-Verantwortung bleibt konsistent im bestehenden `agent_runtime_controller.gd`. Zusaetzlich fuehren `scripts/run_sim_headless_verify.py`, der neue Task `Checks: sim headless verify`, `novapolis-sim/README.md` sowie die Sim-SSOTs jetzt denselben kanonischen Godot-CLI-Smoke fuer `res://scripts/verify_sim.gd`.
  - Verifikation 2026-04-17 04:24: `get_errors` bleibt fuer `Main.gd`, `verify_sim.gd`, den neuen Wrapper, `.vscode/tasks.json` und die betroffenen Sim-Dokus ohne Befund. Der echte Headless-Lauf `scripts/run_sim_headless_verify.py --godot-bin 'F:/Downloads/Godot/Godot_v4.6.1-stable_win64.exe'` endet nach Cleanup in `verify_sim.gd` mit `SIM_VERIFY: OK` und `EXITCODE=0`.

- [x] [Als naechstes] Verbleibende `Main.gd`-Altlasten und den reproduzierbaren Godot-CLI-Smoke auf einen kleinen Abschlussschnitt ziehen.
  - Ziel: Nach der Controller-Welle soll der Sim-Rest nicht bei vereinzelten Alt-Helfern und nur situativ belegbaren Headless-Laeufen stehen bleiben.
  - Akzeptanzkriterien:
    1) unreferenzierte oder doppelt vorhandene Runtime-Helfer wie `_resolve_finetune_train_file()` und `_start_finetune_run()` werden entfernt, in Controller gezogen oder als bewusster Rest sauber dokumentiert,
    2) fuer `res://scripts/verify_sim.gd` existiert ein kanonischer CLI-Pfad ueber Task, Wrapper oder dokumentierten `GODOT_BIN`-/Binary-Pfad,
    3) derselbe Smoke-Pfad prueft `Main.tscn` ohne neue Scene-, Preload- oder Parserfehler,
    4) `novapolis-sim/README.md`, dieses Board und die Export-/IA-SSOT fuehren denselben Verifier-/Smoke-Pfad.
  - Evidenz: `novapolis-sim/scripts/Main.gd` fuehrt `_resolve_finetune_train_file()` und `_start_finetune_run()` weiterhin lokal, waehrend `novapolis-sim/scripts/agent_runtime_controller.gd` denselben Themenbereich bereits teilweise uebernommen hat; zugleich vermerkt dieses Board in mehreren Verifikationsbloecken, dass echte Headless-Laeufe im aktuellen Terminalkontext nur mit lokal aufloesbarer Godot-Binary belegbar waren.
  - Ergebnis 2026-04-17 04:24: Der Abschlussschnitt ist jetzt materialisiert. `scripts/run_sim_headless_verify.py` loest Godot ueber `--godot-bin`, `GODOT_BIN` oder PATH auf und startet den bestehenden Verifier headless; `.vscode/tasks.json`, `novapolis-sim/README.md`, `novapolis-dev/docs/process/sim-export-release-path.ssot.md` und `novapolis-dev/docs/process/sim-ui-menue-ia.ssot.md` fuehren denselben Einstieg. Die lokale Cleanup-Korrektur in `verify_sim.gd` gibt die instanzierte Main-Scene wieder frei, sodass der kanonische Smoke-Lauf nicht mehr mit RID-/Resource-Leaks endet.
  - Verifikation 2026-04-17 04:24: Der echte Lauf `scripts/run_sim_headless_verify.py --godot-bin 'F:/Downloads/Godot/Godot_v4.6.1-stable_win64.exe'` prueft `Main.tscn` ueber `res://scripts/verify_sim.gd` erfolgreich, meldet `SIM_VERIFY: OK` und endet mit `EXITCODE=0` ohne neue Scene-, Preload-, Parser- oder Exit-Leak-Fehler.

Neuordnung: C) Agent-Modul im Hub (neu)
---------------------------------------

archived_at: 2026-03-04 00:20

Quelle: `novapolis-dev/docs/todo.sim.md` (Abschnitt `Neuordnung offener Punkte nach Zugehoerigkeit (Stand 2026-03-02)`).

- [x] Agent-Menuepunkt im Hub anlegen (`Agent Studio`) als eigener Bereich neben Sim/API/Eval.
  - Evidenz: `novapolis-sim/Main.tscn` (`AgentStudioPanel`) und `novapolis-sim/scripts/Main.gd` (UI-Bindings + Refresh).
- [x] Agent Studio in zwei Subbereiche teilen: `Operate` (Runs/Monitoring) und `Author` (Daten/Leitplanken/Profile), um Ueberladung zu vermeiden.
  - Evidenz: `novapolis-sim/Main.tscn` (`AgentOperateButton`, `AgentAuthorButton`), `novapolis-sim/scripts/Main.gd` (`_on_agent_operate_pressed`, `_on_agent_author_pressed`, `_refresh_agent_studio_ui`).
- [x] Agent-Bereich als Untermenue schaltbar gemacht (statt separatem Dauerpanel): Trigger auf dem ehemaligen `Play PC OGG`-Slot.
  - Evidenz: `novapolis-sim/Main.tscn` (`PlayPcAudioButton` Text -> `Agent Menu`), `novapolis-sim/scripts/Main.gd` (`_on_play_pc_audio_pressed` toggelt `AgentStudioPanel.visible`).
- [x] Agent-Modul als exklusiver Submenu-View umgesetzt (nicht nur kleines Panel): eigener Vollbereich mit Rueckweg zum Hub.
  - Evidenz: `novapolis-sim/Main.tscn` (`AgentBackButton`), `novapolis-sim/scripts/Main.gd` (`_set_agent_module_exclusive`, dynamische Panel-Groesse + Hub-Content-Visibility).
- [x] Eval-Runs starten: Suite-Auswahl (`neutral`, `rpg`, `quality_de`), Start/Stop, Laufstatus, letzte KPIs.
  - Vorstufe erweitert: `Eval Run (quick)` startet jetzt real `novapolis_agent/scripts/quick_eval.py` als Hintergrundprozess, inklusive Laufstatus und Prozentanzeige (zeitbasiert/approximativ).
  - Nachschaerfung: `quick_eval.py` akzeptiert nun `--limit`; Hub startet standardmaessig mit hoeherem Quick-Limit (`eval_quick_limit=30`) fuer belastbarere Kurzlaeufe.
  - Nachschaerfung: letzte Runs werden als Success-Rate-Prozent live eingeblendet (`latest_eval_summary.py` -> `AgentLatestRunsLabel`).
  - Umsetzung v2: Suite-Button im Agent-Modul (`neutral/rpg/quality_de`) + `Eval Start`/`Eval Stop`; Starts laufen jetzt ueber `scripts/agent/run_eval.py` mit suite-spezifischen Paketlisten analog Workspace-Tasks.
- [x] Datasets erstellen/verwalten: Quelle waehlen, Kurationslauf starten, Version/Tag setzen, Active Dataset markieren.
  - Vorstufe erweitert: Source-Auswahl ist jetzt separater Control (`Source: clean/with_failures`), waehrend `Datasets` in `Operate` und `Author` wieder konsistent `Run/Stop` fuer reale Kurationslaeufe (`curate_dataset_from_latest.py`) anbietet.
  - Vorstufe erweitert: Im unteren Agent-Bereich oeffnet `Datasets` (Author) jetzt eine gefuehrte Maske mit Modus/Target/Name und JSON-Vorlage; Entwuerfe werden als Datei unter `user://agent_forms/` gespeichert.
  - Schritt 2: `Apply` schreibt jetzt direkt in User-Assets (`user://agent_user_data/datasets/*.jsonl`) mit Validierung und `new`/`append_user`-Semantik.
  - Schritt 3: `Apply` verarbeitet jetzt `dataset_tag` + `set_active` und pflegt eine Registry (`user://agent_user_data/datasets/_registry.json`) mit aktivem Dataset (`name@tag`).
  - Evidenz: `novapolis-sim/scripts/Main.gd` (`_start_dataset_curation`, `_apply_dataset_form_payload`, `_update_dataset_registry`, `_load_dataset_registry_state`) plus Source-Dropdown/Controls in `novapolis-sim/Main.tscn` (`AgentDatasetSourceButton`, `AgentDatasetsButton`).
- [x] Synonyms erstellen/verwalten: Begriffspaare pflegen, Import/Export, Delta-Ansicht, letzter Validator-Status.
  - Vorstufe erweitert: Im unteren Agent-Bereich oeffnet `Synonyms` (Author) jetzt eine gefuehrte Maske mit Modus/Target/Name und editierbarer JSON-Vorlage.
  - Schritt 2: `Apply` schreibt jetzt direkt in User-Assets (`user://agent_user_data/synonyms/*.json`) mit Validierung und `new`/`append_user`-Semantik.
  - Schritt 3: `Apply` verarbeitet jetzt `synonym_tag` + `set_active` und pflegt eine Registry (`user://agent_user_data/synonyms/_registry.json`) mit aktivem Set (`name@tag`).
  - Schritt 4: Import/Export-Pfade sind im Formpayload verfuegbar; Delta (`+terms/+syns`) und Validatorstatus (`ok|warn`) werden nach `Apply` in Status und Runtime-Event ausgewiesen.
  - Evidenz: `novapolis-sim/scripts/Main.gd` (`_apply_synonym_form_payload`, `_load_synonym_entries_from_path`, `_write_json_to_path`, `_build_synonym_delta`, `_validate_synonym_entries`).
- [x] Finetuning starten: Profil waehlen, Basismodel/Artefaktpfad setzen, Lauf starten/abbrechen, Trainingsmetriken anzeigen.
  - Schritt 1: `Finetune` oeffnet jetzt im `Author`-Modus eine Form mit Profil/Basismodell/Train-File/Output/Hyperparametern; `Apply` startet reale Runs via `scripts/agent/fine_tune_pipeline.py`.
  - Schritt 1: Lauf kann ueber denselben Button gestoppt werden (`Finetune Stop`); Statuszeile zeigt Running/Done/Failed inkl. Profil und Output.
  - Schritt 2: Statuszeile enthaelt jetzt Laufzeit- und Trainingsmetriken (`epochs`, `max_steps`, `batch_size`, `lr`) in Running/Done/Failed.
  - Evidenz: `novapolis-sim/scripts/Main.gd` (`_start_finetune_run`, `_refresh_finetune_runtime_state`, `_finetune_epochs/_finetune_max_steps/_finetune_batch_size/_finetune_lr`).
- [x] Entwicklungsstand der KI auswerten: kompakte Trendkarte (Pass-Rate, Fehlerschwerpunkte, letzte Regression, Drift-Status).
  - Vorstufe erweitert: `AI Status` triggert jetzt sofortige Metrik-Aktualisierung (CPU/RAM/GPU/Temp) mit laufender Anzeige im Agent-Studio.
  - Nachschaerfung: Anzeige nutzt jetzt GPU-VRAM (`gpu_vram_percent`, `used/total`) statt GPU-Load-Prozent.
  - Schritt 2: Trendkarte aus den letzten Eval-Runs wird aus `success_rate_percent`/`avg_duration_ms` berechnet (`pass`, `delta`, `regress`, `drift`, `avg_ms`) und in der Zusammenfassung angezeigt.
  - Evidenz: `novapolis-sim/scripts/Main.gd` (`_refresh_latest_eval_summary`, `_build_ai_trend_summary`).
- [x] [Jetzt] Runtime-Log im Hub fuer Bedienung nachgeschaerft: Ping-Noise (`state_update`) unterdrueckt, Historie vergroessert und Scrollbarkeit explizit aktiviert.
- [x] Profile anlegen/verwalten: Prompt-/Verhaltensprofile, Zuweisung zu Eval/Finetune-Laeufen, Aktiv/Archiv-Status.
  - Schritt 1: `Profiles` oeffnet jetzt im `Author`-Modus eine Form mit Profilname, Modus, Prompt/Notes und Assignment (`eval`/`finetune`).
  - Schritt 1: `Apply` persistiert Profile unter `user://agent_user_data/profiles/*.json` und pflegt Active/Archive-Status in `user://agent_user_data/profiles/_registry.json`.
  - Evidenz: `novapolis-sim/scripts/Main.gd` (`_open_agent_form("profiles")`, `_apply_profile_form_payload`, `_update_profile_registry`, `_load_profile_registry_state`) und `AgentProfilesButton` in `novapolis-sim/Main.tscn`.
- [x] `Advanced Settings` einfuehren: Leitplanken, Systemverhalten, Safety-/Policy-Profile, Debug-/Strictness-Level.
  - Schritt 1: `AI Status` oeffnet im `Author`-Modus jetzt eine `Advanced Settings`-Form; `Apply` persistiert die Konfiguration unter `user://agent_user_data/settings/advanced.json`.
  - Schritt 1: Agent-Statusblock zeigt den aktuellen Advanced-Status (`Advanced: <mode> | policy=<...> | strict=<...>`) in den Latest-Runs-Infos.
  - Evidenz: `novapolis-sim/scripts/Main.gd` (`_open_agent_form("advanced")`, `_apply_advanced_settings_form_payload`, `_load_advanced_settings_state`, `_refresh_agent_studio_ui`) und `AgentAiStatusButton` in `novapolis-sim/Main.tscn`.
- [x] Menuepunkt `Jobs`: zentrale Queue/Laufverwaltung fuer Eval, Finetune und Datenjobs inklusive Retry/Cancel.
  - Schritt 1: `Eval Run` oeffnet im `Author`-Modus jetzt eine `Jobs`-Form; `Apply` reiht Jobs (`eval`/`finetune`/`datasets`) in `user://agent_user_data/jobs/queue.json` ein.
  - Schritt 1: Agent-Statusblock zeigt Queue-Status in den Latest-Runs-Infos.
  - Schritt 2: Jobs-Target unterstuetzt jetzt `retry_latest` (letzten `failed/cancelled` Job neu einreihen) und `cancel_latest` (letzten `queued/running` Job abbrechen) inklusive Runtime-Events.
  - Evidenz: `novapolis-sim/scripts/Main.gd` (`_apply_jobs_form_payload`, `_agent_form_target_options_for_kind`, `_load_jobs_queue_payload`, `_write_jobs_queue_payload`, `_find_latest_job_index_by_status`, `_refresh_jobs_status_text`) mit Queue unter `user://agent_user_data/jobs/queue.json`.
- [x] UI-Standard: Single-Select-Steuerungen im Agent-/Hub-Bereich auf Dropdowns (`OptionButton`) vereinheitlicht.
  - Umsetzung: `Eval-Suite`, `Dataset-Quelle`, Form-`Modus`/`Ziel` sowie Hub-Config `Default-Panel`/`Refresh` nutzen jetzt konsistent Dropdowns statt Klick-Zyklen.
- [x] Menuepunkt `Artifacts`: Versionen fuer Datasets, Synonym-Sets, Modelle, Reports (Tagging, Aktivstand, Herkunft).
  - Umsetzung: Aggregierte Artefakt-Summary zeigt aktives Dataset/Synonym-Set, Modellreferenz und Reportstatus im Agent-Studio.
  - Evidenz: `novapolis-sim/scripts/Main.gd` (`_build_artifacts_summary`, `_refresh_agent_restpoint_summaries`).
- [x] Menuepunkt `Experiments`: Vergleichsansichten zwischen Laeufen (A/B, Regression, Drift, KPI-Diff).
  - Umsetzung: A/B-Delta aus den letzten zwei Eval-Runs inkl. Tag (`A>B`, `A<B`, `stable`) im Agent-Studio-Status.
  - Evidenz: `novapolis-sim/scripts/Main.gd` (`_latest_eval_runs`, `_build_experiments_summary`, `_refresh_latest_eval_summary`).
- [x] Menuepunkt `Policy Sandbox`: Leitplanken-/Prompt-Profile testweise gegen Checks fahren, bevor Aktivschaltung erfolgt.
  - Umsetzung: Policy-Sandbox-Status wird aus Advanced-Settings + Quality-Gate (`tests/types`) als `ready|hold` abgeleitet.
  - Evidenz: `novapolis-sim/scripts/Main.gd` (`_build_policy_sandbox_summary`, `_load_advanced_settings_state`).
- [x] Menuepunkt `Release Gate`: Go/No-Go Uebersicht mit Mindestkriterien (z. B. pass_rate, drift, safety).
  - Umsetzung: Gate-Entscheid als `GO|NO-GO` aus `tests`, `types`, `coverage>=80`, Regression und Security-Guard.
  - Evidenz: `novapolis-sim/scripts/Main.gd` (`_build_release_gate_summary`).
- [x] Menuepunkt `Audit Trail`: nachvollziehbare Historie fuer Starts, Aenderungen, Profile-Switches und Policy-Edits.
  - Umsetzung: Runtime-Events werden persistent nach `user://agent_user_data/audit/trail.jsonl` geschrieben und als Summary angezeigt.
  - Evidenz: `novapolis-sim/scripts/Main.gd` (`_append_audit_event`, `_build_audit_trail_summary`, `_append_runtime_event`).
- [x] Rechte-/Sicherheitsmodell fuer Agent-Aktionen definieren (z. B. destructive actions nur mit Explizitfreigabe).
  - Umsetzung: Destructive-Guard mit Zwei-Schritt-Bestaetigung fuer `Eval Stop`, `Datasets Stop`, `Finetune Stop`; Security-State wird unter `user://agent_user_data/security/model.json` persistiert.
  - Evidenz: `novapolis-sim/scripts/Main.gd` (`_confirm_destructive_action`, `_load_security_model_state`, `_persist_security_model_state`).

Arbeitsplan Sim-Modul: Phase 1 - Stabilisierung der Laufzeitkopplung (Jetzt)
--------------------------------------------------------------------------

archived_at: 2026-03-03 00:38

Quelle: `novapolis-dev/docs/todo.sim.md` (Abschnitt `Arbeitsplan Sim-Modul (Analyse 2026-03-02)`).

- [x] Verbindungszustand im UI klarer machen (`novapolis-sim/scripts/Main.gd`): letzte erfolgreiche Aktualisierung + Fehlerdauer anzeigen.
- [x] Polling robuster machen (`novapolis-sim/autoload/SimClient.gd`): explizite Request-Timeout/Retry-Status im Label und optionale Pause bei Dauerfehlern.
- [x] Sim-API-Payload minimal erweitern (`novapolis_agent/app/api/sim.py`): neben `tick/time/events` optionalen `sim_meta`-Block (z. B. `seed`, `mode`) vorbereiten.

Arbeitsplan Sim-Modul: Phase 2 - Interaktions- und Scheduler-Vorbereitung (Als naechstes)
-------------------------------------------------------------------------------------------

archived_at: 2026-03-03 00:38

Quelle: `novapolis-dev/docs/todo.sim.md` (Abschnitt `Arbeitsplan Sim-Modul (Analyse 2026-03-02)`).

- [x] Event-Signals in Godot konkretisieren (`on_action_start/end`, `on_visibility_change`, `on_interrupt`) und in `Main.gd` an UI/Log binden.
- [x] Scheduler-Hook als reine Schnittstelle anlegen (ohne Business-Logik), referenziert von `novapolis-dev/docs/specs/scheduler-spec.md`.
- [x] UI-Controls erweitern: Stundensprung, Auto-Advance bei leerem PC-Slot, sichtbarer Replay-Seed.

Hub-v1: Priorisierung fuer Umsetzung
------------------------------------

archived_at: 2026-03-03 00:38

Quelle: `novapolis-dev/docs/todo.sim.md` (Abschnitt `Hub-v1 fuer Framework-Betrieb (konkretisiert 2026-03-02)`).

- [x] [Jetzt] Hub-Topbar v1 (Verbindung + Laufzeit + Fehlerbild) in `Main.tscn/Main.gd` einziehen.
  - [x] Umsetzung erfolgt: Labels `HubTitle/Api/Polling/Queue/Errors` in `Main.tscn`; Live-Refresh in `Main.gd` mit SimClient-Runtime-Snapshot.
  - [x] Revalidiert am 2026-03-02 16:06: Godot Headless-Load (`res://Main.tscn`, Exitcode 0) und Diagnostics fuer `Main.gd`/`Main.tscn` ohne Fehler.
- [x] [Als naechstes] Modul-Karten v1 fuer `Sim`, `Agent/API`, `Eval/Training` (zunaechst read-only).
  - Evidenz: `novapolis-sim/Main.tscn` (Panels + Label-Struktur) und `novapolis-sim/scripts/Main.gd` (`_refresh_module_cards()` mit Runtime-Snapshot, sim_meta, Queue-/Artefaktstatus).
- [x] [Als naechstes] Dashboard-Schnellaktionen als Platzhalter-Buttons mit Runtime-Events verdrahten.
  - Evidenz: `novapolis-sim/Main.tscn` (`ServerToggleButton`, `HubReloadButton`, `HubChecksButton`) und `novapolis-sim/scripts/Main.gd` (`_on_server_toggle_pressed`, `_on_hub_reload_pressed`, `_on_hub_checks_pressed`).
- [x] [Spaeter] Persistente Hub-Konfiguration (sichtbare Module, Refresh-Raten, Default-Panel).
  - Evidenz: `novapolis-sim/Main.tscn` (`HubConfigPanel`) und `novapolis-sim/scripts/Main.gd` (`_load_hub_preferences`, `_save_hub_preferences`, `_apply_hub_preferences`, `_open_default_panel_if_configured`).
  - Persistenz: `user://hub_prefs.cfg` (ConfigFile) fuer sichtbare Cards, Refresh-Profil, Default-Panel.
  - Verifikation: Diagnostics fuer `Main.gd`/`Main.tscn` ohne Fehler; Godot Headless-Load `res://Main.tscn` mit `EXITCODE=0`.

Neuordnung: A) Hub-Core (frameworkweit, allgemein)
---------------------------------------------------

archived_at: 2026-03-03 00:38

Quelle: `novapolis-dev/docs/todo.sim.md` (Abschnitt `Neuordnung offener Punkte nach Zugehoerigkeit (Stand 2026-03-02)`).

- [x] Persistente Hub-Konfiguration umsetzen (sichtbare Module, Refresh-Rate, Default-Panel je Nutzerprofil).
  - Umsetzung in `HubConfigPanel`: Karten-Sichtbarkeit (Sim/API/Eval), Refresh-Profile (`fast/normal/slow`), Default-Panel (`hub/agent/checks`) und Save.
- [x] Dashboard-Punkt `Run Checks` von Placeholder auf echte Task-Ausfuehrung mit Ergebnisstatus umstellen.
  - Evidenz: `novapolis-sim/Main.tscn` (`ChecksStudioPanel` mit 2-Spalten-Baukasten + read-only Output) und `novapolis-sim/scripts/Main.gd` (exklusiver Checks-Subview, Command-Builder, Ausfuehrung via PowerShell, Modul-/Typ-Selektion).
  - Verifikation: Godot Headless-Load `res://Main.tscn` mit `EXITCODE=0`; Diagnostics fuer `Main.gd`/`Main.tscn` ohne Fehler.
- [x] Health-Panel standardisieren: klarer Status fuer `local`, `external`, `offline`, `degraded` inkl. letzter Ursache.
  - Evidenz: `novapolis-sim/scripts/Main.gd` (`_derive_health_state`) und Einbindung in `hub_api_label`, `api_card_health_label`, `server_status_label`.
  - Verifikation: Diagnostics fuer `Main.gd` ohne Fehler; Godot Headless-Load `res://Main.tscn` mit `EXITCODE=0`.

Neuordnung: B) RP-spezifische Bedienebene (nicht allgemeiner Hub)
------------------------------------------------------------------

archived_at: 2026-03-03 00:38

Quelle: `novapolis-dev/docs/todo.sim.md` (Abschnitt `Neuordnung offener Punkte nach Zugehoerigkeit (Stand 2026-03-02)`).

- [x] RP-Panel einfuehren: `Hour +1`, `Auto-Advance`, `Replay-Seed` ausschließlich dort darstellen.
- [x] RP-Panel mit Slot-/Epoch-Navigation koppeln, ohne Hub-Core zu vermischen.
- [x] RP-Panel-Ereignisse separat im Runtime-Log taggen (z. B. `RP_*`) fuer bessere Nachvollziehbarkeit.
- [x] RP-Einstieg am ehemaligen zweiten Audio-Slot vorbereitet: Buttontext auf `RP Modul` gesetzt und Runtime-Event `RP_MODULE` angebunden.

Neuordnung: D) Qualitaet, Governance, Nachweis
----------------------------------------------

archived_at: 2026-03-03 00:38

Quelle: `novapolis-dev/docs/todo.sim.md` (Abschnitt `Neuordnung offener Punkte nach Zugehoerigkeit (Stand 2026-03-02)`).

- [x] API-Tests erweitern (ungueltiges `dt`, Event-Cap, Reset-Invarianten, Fehlerpfad-Resilienz).
  - Evidenz: `novapolis_agent/tests/test_api_sim_state.py` und `novapolis_agent/tests/tests_sim_api.py` decken jetzt Invalid-`dt`-Faelle (`422`/ValidationError), Event-Cap-Truncation und Reset-Invarianten explizit ab.
- [x] Offline-Asset-Check vertiefen (Slot-Konsistenz world_log vs. pc_log, klare Abbruchkriterien).
  - Evidenz: `scripts/check_sim_epoch_assets.py` um `--check-slot-consistency` erweitert (FAIL bei Slot-Mismatch, Slotwerten ausserhalb `0..23`, oder nicht detektierbaren Slots bei vorhandenen Eintraegen).
- [x] Sim-Runbook aktualisieren (kanonischer Ablauf: API-smoke -> Godot-headless -> Asset-check -> optionale Eval-Checks).
  - Evidenz: `novapolis_agent/docs/runbook.md` enthaelt jetzt den Abschnitt `Kanonischer Sim-Pruefablauf (kurz, in Reihenfolge)` mit festen Kommandos.

Phase 3 - Qualitaet und Nachweisfuehrung (Als naechstes)
---------------------------------------------------------

archived_at: 2026-03-03 00:38

Quelle: `novapolis-dev/docs/todo.sim.md`.

- [x] API-Tests ausbauen (`novapolis_agent/tests/test_api_sim_state.py`, `novapolis_agent/tests/tests_sim_api.py`): Fehlerpfade fuer ungueltiges `dt`, Event-Cap und Reset-Invarianten absichern.
  - Verifikation: `pytest -q novapolis_agent/tests/test_api_sim_state.py novapolis_agent/tests/tests_sim_api.py` PASS (5/5), `pyright` PASS, `mypy` PASS.
- [x] Sim-Offline-Check staerken (`scripts/check_sim_epoch_assets.py`): optional Slot-Konsistenz zwischen `world_log` und `pc_log` validieren.
  - Verifikation: `pytest -q novapolis_agent/tests/scripts/test_check_sim_epoch_assets.py` PASS (4/4), Checker-Lauf `--allow-empty --check-slot-consistency` mit `fail:0`.
- [x] Runbook/README nachziehen (`novapolis-sim/README.md`): neuer Testablauf (headless + API-smoke + epoch-assets-check) als kanonischer Kurzablauf.
  - Evidenz: `novapolis-sim/README.md` Abschnitt `Kanonischer Testablauf (lokal)` hinzugefuegt und mit identischer Reihenfolge dokumentiert.

Root-Uebernahme: novapolis-sim Block aus todo.root
-------------------------------------------------

archived_at: 2026-02-21 04:52

Quelle: `todo.root.md` (Abschnitt `novapolis-sim`).

- [x] Headless-Lade-Check als abgeschlossen archiviert.
- [x] Sim-Detailhistorie aus Root entfernt; aktiver Sim-Backlog bleibt in Sim-/Dev-Boards.


