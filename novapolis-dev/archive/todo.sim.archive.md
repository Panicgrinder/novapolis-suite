---
stand: 2026-03-04 00:20
update: Vollstaendig erledigten Abschnitt Neuordnung C) Agent-Modul im Hub aus dem aktiven Sim-Board archiviert (neuester oben).
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'DONELOG.md' 'novapolis-dev/docs/todo.sim.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' 'novapolis-dev/archive/todo.sim.archive.md' PASS (2026-03-04 00:22); .\.venv\Scripts\python.exe scripts\check_frontmatter.py 'DONELOG.md' 'novapolis-dev/docs/todo.sim.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' 'novapolis-dev/archive/todo.sim.archive.md' PASS (EXITCODE=0, 2026-03-04 00:22)
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


