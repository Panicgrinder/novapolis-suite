---
stand: 2026-03-11 03:57
update: Sim-Index fuer Hub-Chatfenster-Aufnahme und Abschlussstatus synchronisiert.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-sim/README.md' 'novapolis-dev/docs/todo.sim.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' PASS (2026-03-10 17:19); .\.venv\Scripts\python.exe scripts/check_frontmatter.py 'novapolis-sim/README.md' 'novapolis-dev/docs/todo.sim.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' PASS (EXITCODE=0, 2026-03-10 17:19)
---

<!-- markdownlint-disable MD022 MD041 -->

TODO-Index (Novapolis-Dev)
==========================

Übersicht
---------

- RP-Module: `docs/todo.rp.md` — Aufgaben, Kanon-/Canvas-Arbeit, Logs (offen: 5)
- Dev-Module: `docs/todo.dev.md` — Tooling, Lint/CI, Validatoren, Doku-Infra (offen: 1)
- Agent-Module: `docs/todo.agent-board.md` — Backend (FastAPI/Ollama), Tests/Typing, Scripts (offen: 0)
- Sim-Module: `docs/todo.sim.md` — Godot/Visualisierung, API-Polling, Exportprofile (offen: 1)

- Statushinweis Index v1.2: Open-Count-Drift bereinigt - RP `1 -> 5` und Sim `0 -> 1` anhand aktiver Checkboxen in den Modul-Boards synchronisiert.
- Statushinweis Index v1.3: Agent-Backlog nach Tiefenanalyse ergänzt - Open-Count Agent `0 -> 6` (Portabilitaet, Abhaengigkeiten, Legacy, Testdeterminismus, Artefakt-Lifecycle, Marathon-KPI-Automation).
- Statushinweis Index v1.4: Erster Agent-Analysepunkt abgeschlossen - Runbook-Portabilitaet umgesetzt, Open-Count Agent `6 -> 5`.
- Statushinweis Index v1.5: Zweiter Agent-Analysepunkt abgeschlossen - Dependency-Profil formalisiert, Open-Count Agent `5 -> 4`.
- Statushinweis Index v1.6: Dritter Agent-Analysepunkt abgeschlossen - Legacy-Shim-Inventar/Guard plus technische Entkopplung von `novapolis_agent.app.utils.examples`, Open-Count Agent `4 -> 3`.
- Statushinweis Index v1.7: Vierter Agent-Analysepunkt abgeschlossen - test_prepare_pack-SMoke deterministisch ohne Vorartefakte, Open-Count Agent `3 -> 2`.
- Statushinweis Index v1.8: Artefakt-Lifecycle automatisiert - Cleanup-Skript+Task+Dry-Run-Report eingefuehrt, Open-Count Agent `2 -> 1`.
- Statushinweis Index v1.9: RP->Eval-Builder und Synonym-Overlay-Ausbau umgesetzt (Script+Task+Tests+RP-Set), Open-Count Agent bleibt `1`.
- Statushinweis Index v1.10: Marathon-KPI-Rueckkopplung automatisiert (Parser+Severity+board-ready Report), Open-Count Agent `1 -> 0`.
- Statushinweis Index v1.11: RP-Content-Eval nahtlos integriert (Suite `rp_content`, Task, strict-Validator, Runbook, Provenance), Open-Count Agent bleibt `0`.

- Statushinweis Dev: `docs/todo.dev.md` enthaelt jetzt einen priorisierten Hygiene-Sprint (Truthfulness, Donelog-/Log-Hygiene, Freshness-SLA, Guardrails).
- Statushinweis Sim: `docs/todo.sim.md` fuehrt offene Punkte jetzt kanonisch nach Zugehoerigkeit (Hub-Core, RP-Panel, Agent Studio, Qualitaet/Nachweis).
- Statushinweis Agent-Studio: In `docs/todo.sim.md` ist fuer den Hub ein klarer `Operate`/`Author`-Zuschnitt mit erweiterten Menuepunkten (`Jobs`, `Artifacts`, `Experiments`, `Policy Sandbox`, `Release Gate`, `Audit Trail`) hinterlegt.
- Statushinweis Agent-Studio v1.2: Runtime-Log ist fuer Bedienerevents entlastet (kein `state_update`-Spam), Historie vergroessert und scrollbar; Metrikzeile zeigt GPU-VRAM statt GPU-Load.
- Statushinweis Agent-Studio v1.3: Agent-Flaeche ist jetzt als Untermenue ueber `Agent-Modul` (ehemals `Play PC OGG`) toggelbar; `RP Modul` ersetzt den zweiten Audio-Schnellbutton als RP-Einstieg.
- Statushinweis Agent-Studio v1.4: Agent-Modul oeffnet als exklusiver Submenu-View mit Rueck-Button; letzte Eval-Laeufe inkl. Success-Rate (%) werden im Modul eingeblendet.
- Statushinweis Sim v1.5: Hub-Topbar-Punkt in `docs/todo.sim.md` final auf erledigt gesetzt; Headless-Load und Diagnostics wurden erneut ohne Befund verifiziert.
- Statushinweis Sim v1.6: `Run Checks` oeffnet jetzt ein exklusives Checks-Modul mit Baukasten-Logik (Spalte 1: Modul, Spalte 2: Check-Typ) und read-only Output-Fenster.
- Statushinweis Sim v1.7: Health-Anzeige im Hub ist jetzt vereinheitlicht (`local`, `external`, `offline`, `degraded`) inkl. klarer Ursachen in Topbar, API-Card und Server-Statuszeile.
- Statushinweis Sim v1.8: Hub-Konfiguration ist persistent (Cards sichtbar/unsichtbar, Refresh-Profil, Default-Panel) via `user://hub_prefs.cfg`.
- Statushinweis Sim v1.9: RP-Panel ist jetzt als exklusiver Submenu-View verfuegbar (`Hour +1`, `Auto-Advance`, `Replay-Seed`) und taggt Runtime-Ereignisse separat mit `RP_*`.
- Statushinweis Sim v2.0: Agent-Eval-Runs im Hub bieten jetzt Suite-Auswahl (`neutral/rpg/quality_de`) sowie `Eval Start`/`Eval Stop`; Run-Start nutzt suite-spezifische Paketsets analog den Eval-Tasks.
- Statushinweis Sim v2.1: `Datasets` im Agent-Modul bietet Source-Modus (`clean/with_failures`) und Start/Stop fuer reale Kurationslaeufe, inklusive Laufstatus im Modul.
- Statushinweis Sim v2.2: Datasets-Regression behoben: Source-Umschaltung ist eigener Button, waehrend `Datasets` in `Operate` und `Author` wieder konsistent `Run/Stop` ausfuehrt.
- Statushinweis Sim v2.3: Im unteren Agent-Bereich oeffnen `Datasets`/`Synonyms` (Author) jetzt gefuehrte Form-Masken mit Modus/Target/Name und editierbarer Vorlage, damit Nutzer nur die Maske ausfuellen muessen.
- Statushinweis Sim v2.4: Schritt 2 umgesetzt - `Apply` persistiert Datasets/Synonyms direkt als User-Assets mit Validierung und `new`/`append_user`-Semantik.
- Statushinweis Sim v2.5: Datasets Schritt 3 umgesetzt - `Apply` verarbeitet jetzt `dataset_tag` + `set_active` und pflegt den Active-Status in `user://agent_user_data/datasets/_registry.json`.
- Statushinweis Sim v2.6: Synonyms Schritt 3 umgesetzt - `Apply` verarbeitet jetzt `synonym_tag` + `set_active` und pflegt den Active-Status in `user://agent_user_data/synonyms/_registry.json`.
- Statushinweis Sim v2.7: Finetune Schritt 1 umgesetzt - `Finetune` oeffnet im Author-Bereich eine Startmaske und steuert reale Start/Stop-Laeufe via `scripts/agent/fine_tune_pipeline.py`.
- Statushinweis Sim v2.8: Profiles Schritt 1 umgesetzt - `Profiles` oeffnet im Author-Bereich eine Form und verwaltet Active/Archive-Status via `user://agent_user_data/profiles/_registry.json`.
- Statushinweis Sim v2.9: Advanced Settings Schritt 1 umgesetzt - `AI Status` oeffnet im Author-Bereich eine Form und persistiert Leitplanken/Systemverhalten in `user://agent_user_data/settings/advanced.json`.
- Statushinweis Sim v3.0: Jobs Schritt 1 umgesetzt - `Eval Run` oeffnet im Author-Bereich eine Jobs-Form und persistiert Queue-Eintraege in `user://agent_user_data/jobs/queue.json`.
- Statushinweis Sim v3.1: Dropdown-Standard umgesetzt - `Eval-Suite`, `Dataset-Quelle`, Form-`Modus`/`Ziel` und Hub-Config `Default/Refresh` sind jetzt konsistent als `OptionButton` ausgefuehrt.
- Statushinweis Sim v3.2: Sim-API-Testabdeckung erweitert - Invalid-`dt`, Event-Cap und Reset-Invarianten sind jetzt als Unit- und API-Tests abgesichert (`pytest`, `pyright`, `mypy` gruen auf den geaenderten Dateien).
- Statushinweis Sim v3.3: Sim-Runbook/README auf kanonischen Verifikationsablauf synchronisiert (`API-smoke -> Godot-headless -> Asset-check -> optional Eval`).
- Statushinweis Sim v3.4: Offline-Asset-Check gehaertet - `check_sim_epoch_assets.py` validiert optional Slot-Konsistenz (`--check-slot-consistency`) mit klaren FAIL-Kriterien und Unit-Tests.
- Statushinweis Sim v3.5: Vollstaendig erledigte Sim-Bloecke (Arbeitsplan-Phasen, Hub-Priorisierung, Neuordnung A/B/D, Phase 3) aus `docs/todo.sim.md` in `novapolis-dev/archive/todo.sim.archive.md` ueberfuehrt.
- Statushinweis Ops 2026-03-03: Qualitaetsstabilisierung 1-5 abgeschlossen (`checks_report_20260303_141251.md`): `path-portability`, `ruff`, `black`, `pytest/coverage` und `markdownlint` im Full-Check gruen.
- Statushinweis Sim v3.6: Dashboard-Bereichsfeinschliff umgesetzt - visuelle Marken `bereich-01..04`, Runtime-Layout auf aktuellen Zuschnitt synchronisiert und Klick-Blockade durch Marker via `mouse_filter=2` behoben.
- Statushinweis Sim v3.7: Hub-Statusblock evidenzbasiert nachgezogen - `Verbindung` auf erledigt gesetzt; bei `Laufzeit`, `Daten` und `Fehlerbild` Teilfortschritt dokumentiert (jeweils mit offenem Restpunkt).
- Statushinweis Sim v3.8: Restpunkte im Hub-Statusblock umgesetzt - `event_rate` in Queue-Labels, `dataset_tag` in Artifact-Status und `last_error_code` in Error-Label integriert; damit sind `Laufzeit`, `Daten` und `Fehlerbild` auf erledigt gehoben.
- Statushinweis Sim v3.9: Qualitaetsanzeige im Hub nachgezogen - `tests_last`, `types_last`, `coverage_last` werden aus dem neuesten `checks_report_*.json` gelesen und in der Eval-Karte angezeigt.
- Statushinweis Sim v4.0: Navigationsblock evidenzbasiert nachgezogen - `Dashboard`, `Sim`, `Agent/API` und `Eval/Training` auf erledigt; `RP/Content` bleibt mit offener Content-Quellenanzeige als Restpunkt.
- Statushinweis Sim v4.1: `RP/Content` abgeschlossen - Hub zeigt jetzt Modul/Sichtbarkeit/Quelle/letztes RP-Event direkt in der Event-Karte.
- Statushinweis Sim v4.2: Agent-Studio-Backlog nachgezogen - `Datasets`, `Profiles` und `Advanced Settings` sind auf erledigt gehoben (Operate/Author-Flow, Persistenz und Active-Status belegt).
- Statushinweis Sim v4.3: Jobs-Flow nachgezogen - Queue-Verwaltung deckt jetzt `retry_latest`/`cancel_latest` ab; Statuszeile zeigt aggregierte Job-Zustaende plus neuesten Job.
- Statushinweis Sim v4.4: Agent-Studio-Restpunkte nachgezogen - `Synonyms` (Import/Export + Delta/Validator), `Finetuning` (Trainingsmetriken in Laufstatus) und `KI-Stand` (Trendkarte aus letzten Eval-Runs) sind abgeschlossen.
- Statushinweis Sim v4.5: Agent-Studio vervollstaendigt - `Artifacts`, `Experiments`, `Policy Sandbox`, `Release Gate`, `Audit Trail` sowie ein explizites Destructive-Sicherheitsmodell sind im Status-/Event-Flow implementiert.
- Statushinweis Sim v4.6: RP-Panel-Restpunkt abgeschlossen - RP-Submenu steuert `Hour +1`, `Auto-Advance`, `Replay-Seed` inkl. eigener `RP_*`-Runtime-Events.
- Statushinweis Sim v4.7: Vollstaendig erledigter Block `Neuordnung: C) Agent-Modul im Hub (neu)` aus `docs/todo.sim.md` nach `novapolis-dev/archive/todo.sim.archive.md` ueberfuehrt (`archived_at: 2026-03-04 00:20`).
- Statushinweis Sim v4.8: Neuer Hub-Punkt aufgenommen: kleines Chatfenster im Hauptmenue mit `/chat`-Roundtrip als lokaler Gespraechsmodus.
- Statushinweis Sim v4.9: Hub-Chatfenster abgeschlossen - kleines Chatpanel im Hauptmenue sendet an `/chat` und zeigt Antworten/Fehler robust im UI an.
- Statushinweis Root/Beta v0: `todo.root.md` enthaelt jetzt eine geordnete Standalone-Beta-Exit-Checkliste mit Blockern [1]-[7] und Optionalpunkten [8]-[12].
- Statushinweis Beta v0.1: Blockerpakete Dev/RP/Sim strukturell nachgezogen (`todo.dev` Jetzt-Block abgeschlossen, `todo.rp` P0-Jetzt abgeschlossen, `todo.sim` auf `offen:0`).
- Statushinweis Beta v1.0: Root-Blocker B1-B7 und `Definition of Ready` in `todo.root.md` auf erledigt gesetzt; Referenzlauf `checks_report_20260304_004318.md` ist gruen.
- Statushinweis Beta v1.1: Optional-Guardrails O8/O9/O10/O12 umgesetzt (`todo-index-sync`, `doc-freshness`, `logs-policy`, Beta-Tagging-Konvention) und in `Checks: full` verdrahtet.

Hinweise (Index)
----------------

- Vollständig erledigte Abschnitte (H2/H3, alle [x]) bitte manuell in `novapolis-dev/archive/todo.<modul>.archive.md` verschieben; unter der Abschnittsüberschrift `archived_at: YYYY-MM-DD HH:MM` ergänzen. Übersicht aller Archive: `novapolis-dev/archive/README.md`.
- Validierung bei Änderungen: markdownlint via `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc` und Frontmatter-Check via `scripts/check_frontmatter.py`.

Verweise
--------

- Root-Übersicht: `todo.root.md` (Kurzüberblick, Meta-Aufgaben, Links)
- DONELOG-Zentralstruktur: `novapolis-dev/archive/docs/donelogs/INDEX.md`





