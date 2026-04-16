---
stand: 2026-04-17 01:04
update: Diese SSOT dokumentiert die verbleibenden sinnvollen Controller-Schnitte im Sim-Architekturrest nach dem AgentRuntimeController.
checks: snapshot-lock PASS (2026-04-17 01:04); Main.gd-Evidenz PASS; markdownlint=PASS; frontmatter=PASS; todo-index-sync=PASS
---

Sim Controller Roadmap (SSOT)
=============================

Zweck
-----

Diese SSOT dokumentiert die verbleibenden sinnvollen Controller-Schnitte fuer den offenen Sim-Architekturrest nach der Auslagerung von Hub-, Session-/Replay-, Checks-/RP-, Agent-Form- und Agent-Runtime-Pfaden.

Scope
-----

- belastbare Abgrenzung der noch sinnvollen Controller-Kandidaten in [novapolis-sim/scripts/Main.gd](novapolis-sim/scripts/Main.gd)
- pragmatische Priorisierung fuer weitere kleine Refactor-Schnitte
- Abgrenzung zwischen sofort sinnvollen Controllern und bewusst verbleibenden Hilfsfunktionen

Nicht-Ziele
-----------

- keine sofortige Code-Auslagerung in diesem Doku-Lauf
- keine kuenstliche Controller-Zerlegung fuer triviale String- oder Format-Helfer
- keine Aenderung an Node-Pfaden, UI-Bedienwegen oder Session-Vertrag

Iststand nach dem Runtime-Schnitt
---------------------------------

- Bereits ausgelagert sind Hub-Layout, Hub-Config, Hub-Chat, Session-/Replay-Helper, Session-/Replay-Requests, Session-/Replay-State, Checks/RP, Agent-Studio-UI, Agent-Form-UI und Agent-Runtime.
- In [novapolis-sim/scripts/Main.gd](novapolis-sim/scripts/Main.gd) verbleiben danach vor allem noch Agent-Authoring-Payloads, Persistenz-/Registry-IO, Security-/Summary-State sowie Server-/Audit-Steuerung.
- Die frueheren Runtime-Helfer `_resolve_finetune_train_file()`, `_start_finetune_run()`, `_load_jobs_queue_payload()` und `_write_jobs_queue_payload()` stehen in [novapolis-sim/scripts/Main.gd](novapolis-sim/scripts/Main.gd) aktuell nur noch als Altlasten- oder Cleanup-Kandidaten ohne belegten Call-Site-Rest im verbleibenden Pfad.

Pragmatische Leitlinien
-----------------------

- Ein neuer Controller ist nur dann sinnvoll, wenn er einen klaren Verantwortungsblock mit eigener Eingabe-/Ausgabegrenze traegt.
- [novapolis-sim/scripts/Main.gd](novapolis-sim/scripts/Main.gd) bleibt sichtbare Fassade fuer Node-Wiring, Statusspiegelung und UI-Refresh.
- Bereits in [novapolis-sim/scripts/agent_runtime_controller.gd](novapolis-sim/scripts/agent_runtime_controller.gd) liegende Jobs-Queue- und Start/Stop-Logik wird nicht wieder aufgespalten.
- Kleinere Format-Helfer wie `_format_percent()` oder `_format_temperature()` rechtfertigen allein keinen eigenen Controller.

Controller-Kandidaten
---------------------

### 1. AgentAuthoringPayloadController

- Prioritaet: sofort sinnvoll
- Ziel: Form-Payload-Building, lokale Validation und Normalisierung aus [novapolis-sim/scripts/Main.gd](novapolis-sim/scripts/Main.gd) herausziehen.
- Evidenzfunktionen:
  - `_build_agent_form_payload_from_controls()`
  - `_form_control_text()`
  - `_form_control_int()`
  - `_form_control_float()`
  - `_form_control_bool()`
  - `_form_control_csv_array()`
- Verantwortung:
  - UI-nahe Form-Control-Werte in kanonische Payloads fuer datasets, synonyms, finetune, profiles, advanced und jobs uebersetzen
  - lokale Pflichtfeld- und Typnormalisierung kapseln, ohne selbst Datei-IO oder Prozessstarts zu uebernehmen
- Ergebnisgrenze:
  - Input: Form-State plus Controls
  - Output: normalisierte Payloads oder strukturierte Validation-Fehler

### 2. AgentAuthoringPersistenceController

- Prioritaet: sofort sinnvoll
- Ziel: Authoring-Schreibpfade fuer Dataset-, Synonym-, Profil- und Advanced-Settings aus [novapolis-sim/scripts/Main.gd](novapolis-sim/scripts/Main.gd) entfernen.
- Evidenzfunktionen:
  - `_apply_dataset_form_payload()`
  - `_apply_synonym_form_payload()`
  - `_load_synonym_entries_from_path()`
  - `_build_synonym_delta()`
  - `_validate_synonym_entries()`
  - `_write_json_to_path()`
  - `_apply_profile_form_payload()`
  - `_apply_advanced_settings_form_payload()`
- Verantwortung:
  - Dateischreiben, Import/Export, Persistenzvalidation und Event-Payloads fuer Authoring-Aktionen kapseln
  - keine UI-Layout- oder Runtime-Prozesslogik tragen
- Ergebnisgrenze:
  - Input: normalisierte Payloads aus dem Payload-Controller
  - Output: Updates fuer Statusfelder, aktive Artefakte und Runtime-Events

### 3. AgentRegistryStateController

- Prioritaet: sinnvoll nach Payload/Persistenz
- Ziel: aktive Registry- und Sicherheitsmodell-Zustaende von Authoring-IO und UI-Fassade trennen.
- Evidenzfunktionen:
  - `_load_dataset_registry_state()`
  - `_load_synonym_registry_state()`
  - `_load_profile_registry_state()`
  - `_load_advanced_settings_state()`
  - `_load_security_model_state()`
  - `_persist_security_model_state()`
  - `_update_dataset_registry()`
  - `_update_synonym_registry()`
  - `_update_profile_registry()`
- Verantwortung:
  - aktive Dataset-/Synonym-/Profil-Referenzen sowie Security-Guard-Settings laden, schreiben und auf UI-lesbare State-Snapshots abbilden
  - Registry-Metadaten von den groesseren Authoring-Schreibpfaden entkoppeln
- Hinweis:
  - Falls der verbleibende Codeblock klein genug wird, kann dieser Controller auch als Untermodul des Persistence-Controllers enden; die Trennung ist nur dann sinnvoll, wenn Registry-State weiter eigenstaendig waechst.

### 4. AgentRestpointSummaryController

- Prioritaet: sinnvoll, aber nachrangig
- Ziel: die verbleibende Summary- und Gate-Bildung aus [novapolis-sim/scripts/Main.gd](novapolis-sim/scripts/Main.gd) herausziehen.
- Evidenzfunktionen:
  - `_refresh_agent_restpoint_summaries()`
  - `_build_artifacts_summary()`
  - `_build_experiments_summary()`
  - `_build_policy_sandbox_summary()`
  - `_build_release_gate_summary()`
  - `_build_audit_trail_summary()`
- Verantwortung:
  - aus Registry-, Eval-, Security- und Audit-Zustaenden konsistente Summary-Strings erzeugen
  - Gate-Lesart an einem Ort halten, statt sie ueber [novapolis-sim/scripts/Main.gd](novapolis-sim/scripts/Main.gd) zu verteilen

### 5. HubServerOpsController

- Prioritaet: optional sinnvoll nach dem Agent-Studio-Rest
- Ziel: lokale Serverprozess-Steuerung von der Sim-Fassade trennen.
- Evidenzfunktionen:
  - `_resolve_python_executable()`
  - `_start_local_server()`
  - `_stop_local_server()`
  - `_update_server_control_ui()`
  - `_refresh_server_runtime_state()`
  - `_is_external_server_reachable()`
- Verantwortung:
  - lokalen API-Server starten/stoppen, Reachability abbilden und UI-Status dafuer erzeugen
  - keine Agent-Authoring- oder Session-/Replay-Logik tragen
- Hinweis:
  - Dieser Controller ist fachlich sinnvoll, gehoert aber nicht mehr in den unmittelbaren Agent-Studio-Rest. Er ist eher ein separater Hub-Ops-Schnitt.

### 6. RuntimeAuditController

- Prioritaet: optional sinnvoll nach den fachlichen Kernschnitten
- Ziel: Runtime-Event-Puffer und Audit-Trail-Persistenz entkoppeln.
- Evidenzfunktionen:
  - `_append_runtime_event()`
  - `_append_audit_event()`
  - `_runtime_event_rate_per_second()`
  - `_trim_runtime_event_rate_window()`
  - `_extract_error_code()`
- Verantwortung:
  - Runtime-Ereignisse, Rate-Fenster und Audit-Trail-Datei zentral kapseln
  - [novapolis-sim/scripts/Main.gd](novapolis-sim/scripts/Main.gd) nur noch fertige Event-Updates liefern lassen
- Hinweis:
  - Dieser Schnitt ist vor allem dann sinnvoll, wenn Event- und Audit-Logik weiter fuer mehrere Module waechst.

Bewusst keine eigenen Controller
--------------------------------

- `_dataset_source_mode_label()`, `_active_dataset_label()`, `_active_synonym_label()` und `_active_profile_label()` bleiben vorerst harmlose UI-Helfer.
- `_format_percent()`, `_format_temperature()`, `_format_vram()` und `_effective_temperature_c()` rechtfertigen aktuell keinen eigenen Controller.
- Unreferenzierte Runtime-Reste in [novapolis-sim/scripts/Main.gd](novapolis-sim/scripts/Main.gd) sollen im naechsten Codeschnitt eher bereinigt als als neue Controller promoted werden.

Empfohlene Reihenfolge
----------------------

1. AgentAuthoringPayloadController
2. AgentAuthoringPersistenceController
3. AgentRegistryStateController
4. AgentRestpointSummaryController
5. HubServerOpsController
6. RuntimeAuditController

Definition of Done
------------------

- Die verbleibenden sinnvollen Controller-Kandidaten sind evidenzbasiert aus [novapolis-sim/scripts/Main.gd](novapolis-sim/scripts/Main.gd) abgeleitet.
- Die direkte Restarbeit hinter dem AgentRuntimeController ist klar von optionalen Folge-Schnitten getrennt.
- Der naechste Codeschnitt kann ohne neue Repo-Exploration direkt auf Payload- und Persistenz-Controller gehen.