---
stand: 2026-03-03 23:13
update: Hub-Dashboard-Bereiche nachgeschaerft (Bereichsmarken, Runtime-Sync, Klick-Hotfix) und TODO-Index/Dev-DONELOG im selben Lauf synchronisiert.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-dev/docs/todo.sim.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' PASS (2026-03-03 23:13); .\.venv\Scripts\python.exe scripts\check_frontmatter.py 'novapolis-dev/docs/todo.sim.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' PASS (EXITCODE=0, 2026-03-03 23:13)
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

- `Jetzt`: Hub-Kern stabil halten und offene Punkte nach Modulgrenzen umsetzen.
- `Als naechstes`: Agent-Modul im Hub integrieren (Eval, Datasets, Synonyms, Finetuning, Profile, KI-Stand).
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
- [x] [Jetzt] Event-Signals: `on_action_start/end`, `on_visibility_change`, `on_interrupt` (Hook für spätere Mikro-Turns).
  - Evidenz: `novapolis-sim/scripts/Main.gd` (Signal-Definitionen + Emission + Runtime-Event-Log in `PcLogLabel`), Headless-Start `res://Main.tscn` ohne Fehler.
- [x] [Jetzt] Scheduler-Hook vorbereiten: Min-Heap-basierte Event-Queue (ohne Logik), nur Schnittstellen/Types.
  - Evidenz: `novapolis-sim/scripts/scheduler_hook.gd` (Min-Heap API: `enqueue/peek_next/pop_next/pop_due`), `novapolis-sim/scripts/Main.gd` (`SCHEDULER_READY` Runtime-Event).
  - [ ] Referenz: `novapolis-dev/docs/specs/scheduler-spec.md`.
- [ ] [Als naechstes] RP-Panel-Controls: Stundensprung, Auto-Advance (wenn kein PC-Event), Replay-Seed sichtbar machen (nicht im allgemeinen Hub).
  - Hinweis: Im allgemeinen Hub bewusst entfernt; Umsetzung folgt in einem separaten RP-spezifischen Panel/Flow.

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

- [ ] Dashboard: Gesamtstatus, letzte Events, Schnellaktionen (Start/Stop/Reload/Checks).
  - Fortschritt 2026-03-03: Bereiche `bereich-01..04` in `novapolis-sim/Main.tscn` zur visuellen Slot-Abgrenzung angelegt; Runtime-Layout in `novapolis-sim/scripts/Main.gd` auf die aktuellen Bereichszuschnitte nachgezogen; Input-Hotfix gesetzt (`mouse_filter=2`), damit die Markierungsflaechen keine Schaltflaechen blockieren.
- [ ] Sim: Tick/Zeit, Scheduler-Queue, Runtime-Events, Slot-/Epoch-Navigation.
- [ ] Agent/API: Health, Port/Host, Response-Latenz, letzte Fehler, Retry-Status.
- [ ] Eval/Training: letzter Lauf, pass_rate, Datensatzquelle, Artefaktstatus.
- [ ] RP/Content: aktive Quelle/Modul, Sichtbarkeitsstatus, letzte Content-Events.

Statusinformationen (Hub-Topbar + Modul-Karten)

- [ ] Verbindung: `API reachable`, `polling active/paused`, `last_ok_age_s`.
- [ ] Laufzeit: `tick`, `sim_time_s`, `event_rate`, `queue_size` (Scheduler-Hook).
- [ ] Qualitaet: `tests_last`, `types_last`, `coverage_last` (wenn verfuegbar).
- [ ] Daten: `epoch_data_present`, `audio_assets_present`, `dataset_tag`.
- [ ] Fehlerbild: `last_error_code`, `error_duration_s`, `consecutive_failures`.

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
- [ ] Datasets erstellen/verwalten: Quelle waehlen, Kurationslauf starten, Version/Tag setzen, Active Dataset markieren.
  - Vorstufe erweitert: Source-Auswahl ist jetzt separater Control (`Source: clean/with_failures`), waehrend `Datasets` in `Operate` und `Author` wieder konsistent `Run/Stop` fuer reale Kurationslaeufe (`curate_dataset_from_latest.py`) anbietet.
  - Vorstufe erweitert: Im unteren Agent-Bereich oeffnet `Datasets` (Author) jetzt eine gefuehrte Maske mit Modus/Target/Name und JSON-Vorlage; Entwuerfe werden als Datei unter `user://agent_forms/` gespeichert.
  - Schritt 2: `Apply` schreibt jetzt direkt in User-Assets (`user://agent_user_data/datasets/*.jsonl`) mit Validierung und `new`/`append_user`-Semantik.
  - Schritt 3: `Apply` verarbeitet jetzt `dataset_tag` + `set_active` und pflegt eine Registry (`user://agent_user_data/datasets/_registry.json`) mit aktivem Dataset (`name@tag`).
- [ ] Synonyms erstellen/verwalten: Begriffspaare pflegen, Import/Export, Delta-Ansicht, letzter Validator-Status.
  - Vorstufe erweitert: Im unteren Agent-Bereich oeffnet `Synonyms` (Author) jetzt eine gefuehrte Maske mit Modus/Target/Name und editierbarer JSON-Vorlage.
  - Schritt 2: `Apply` schreibt jetzt direkt in User-Assets (`user://agent_user_data/synonyms/*.json`) mit Validierung und `new`/`append_user`-Semantik.
  - Schritt 3: `Apply` verarbeitet jetzt `synonym_tag` + `set_active` und pflegt eine Registry (`user://agent_user_data/synonyms/_registry.json`) mit aktivem Set (`name@tag`).
- [ ] Finetuning starten: Profil waehlen, Basismodel/Artefaktpfad setzen, Lauf starten/abbrechen, Trainingsmetriken anzeigen.
  - Schritt 1: `Finetune` oeffnet jetzt im `Author`-Modus eine Form mit Profil/Basismodell/Train-File/Output/Hyperparametern; `Apply` startet reale Runs via `scripts/agent/fine_tune_pipeline.py`.
  - Schritt 1: Lauf kann ueber denselben Button gestoppt werden (`Finetune Stop`); Statuszeile zeigt Running/Done/Failed inkl. Profil und Output.
- [ ] Entwicklungsstand der KI auswerten: kompakte Trendkarte (Pass-Rate, Fehlerschwerpunkte, letzte Regression, Drift-Status).
  - Vorstufe erweitert: `AI Status` triggert jetzt sofortige Metrik-Aktualisierung (CPU/RAM/GPU/Temp) mit laufender Anzeige im Agent-Studio.
  - Nachschaerfung: Anzeige nutzt jetzt GPU-VRAM (`gpu_vram_percent`, `used/total`) statt GPU-Load-Prozent.

- [x] [Jetzt] Runtime-Log im Hub fuer Bedienung nachgeschaerft: Ping-Noise (`state_update`) unterdrueckt, Historie vergroessert und Scrollbarkeit explizit aktiviert.
- [ ] Profile anlegen/verwalten: Prompt-/Verhaltensprofile, Zuweisung zu Eval/Finetune-Laeufen, Aktiv/Archiv-Status.
  - Schritt 1: `Profiles` oeffnet jetzt im `Author`-Modus eine Form mit Profilname, Modus, Prompt/Notes und Assignment (`eval`/`finetune`).
  - Schritt 1: `Apply` persistiert Profile unter `user://agent_user_data/profiles/*.json` und pflegt Active/Archive-Status in `user://agent_user_data/profiles/_registry.json`.
- [ ] `Advanced Settings` einfuehren: Leitplanken, Systemverhalten, Safety-/Policy-Profile, Debug-/Strictness-Level.
  - Schritt 1: `AI Status` oeffnet im `Author`-Modus jetzt eine `Advanced Settings`-Form; `Apply` persistiert die Konfiguration unter `user://agent_user_data/settings/advanced.json`.
  - Schritt 1: Agent-Statusblock zeigt den aktuellen Advanced-Status (`Advanced: <mode> | policy=<...> | strict=<...>`) in den Latest-Runs-Infos.
- [ ] Menuepunkt `Jobs`: zentrale Queue/Laufverwaltung fuer Eval, Finetune und Datenjobs inklusive Retry/Cancel.
  - Schritt 1: `Eval Run` oeffnet im `Author`-Modus jetzt eine `Jobs`-Form; `Apply` reiht Jobs (`eval`/`finetune`/`datasets`) in `user://agent_user_data/jobs/queue.json` ein.
  - Schritt 1: Agent-Statusblock zeigt Queue-Status (`Jobs: queued=<n> | latest=<name> (<type>)`) in den Latest-Runs-Infos.
- [x] UI-Standard: Single-Select-Steuerungen im Agent-/Hub-Bereich auf Dropdowns (`OptionButton`) vereinheitlicht.
  - Umsetzung: `Eval-Suite`, `Dataset-Quelle`, Form-`Modus`/`Ziel` sowie Hub-Config `Default-Panel`/`Refresh` nutzen jetzt konsistent Dropdowns statt Klick-Zyklen.
- [ ] Menuepunkt `Artifacts`: Versionen fuer Datasets, Synonym-Sets, Modelle, Reports (Tagging, Aktivstand, Herkunft).
- [ ] Menuepunkt `Experiments`: Vergleichsansichten zwischen Laeufen (A/B, Regression, Drift, KPI-Diff).
- [ ] Menuepunkt `Policy Sandbox`: Leitplanken-/Prompt-Profile testweise gegen Checks fahren, bevor Aktivschaltung erfolgt.
- [ ] Menuepunkt `Release Gate`: Go/No-Go Uebersicht mit Mindestkriterien (z. B. pass_rate, drift, safety).
- [ ] Menuepunkt `Audit Trail`: nachvollziehbare Historie fuer Starts, Aenderungen, Profile-Switches und Policy-Edits.
- [ ] Rechte-/Sicherheitsmodell fuer Agent-Aktionen definieren (z. B. destructive actions nur mit Explizitfreigabe).

D) Qualitaet, Governance, Nachweis

- Archiviert: `novapolis-dev/archive/todo.sim.archive.md` (Block `Neuordnung: D) Qualitaet, Governance, Nachweis`, `archived_at: 2026-03-03 00:38`).

Phase 3 - Qualitaet und Nachweisfuehrung (Als naechstes)

- Archiviert: `novapolis-dev/archive/todo.sim.archive.md` (Block `Phase 3 - Qualitaet und Nachweisfuehrung (Als naechstes)`, `archived_at: 2026-03-03 00:38`).

Abschlusskriterien (Definition of Done)

- [x] Ein lokaler Durchlauf deckt API-smoke, Godot-headless und Offline-Asset-Check in fester Reihenfolge ab.
  - Nachweis: API-smoke (`pytest ...::test_get_world_state_initial_values`) PASS, Godot-headless-Load ausgefuehrt, `check_sim_epoch_assets.py --allow-empty --check-slot-consistency` mit `fail:0`.
- [ ] Die offenen Sim-Todo-Punkte sind mit Evidenzpfaden im Dev-DONELOG nachweisbar abgeschlossen.



