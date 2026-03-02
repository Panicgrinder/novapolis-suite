---
stand: 2026-03-02 23:30
update: Sim v3.3 aufgenommen: Runbook/README auf festen Verifikationsablauf (API-smoke, headless, Asset-check) synchronisiert.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis_agent/docs/runbook.md' 'novapolis-sim/README.md' 'novapolis-dev/docs/todo.sim.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' 'novapolis_agent/docs/DONELOG.txt' PASS (2026-03-02 23:06); .\.venv\Scripts\python.exe scripts\check_frontmatter.py 'novapolis_agent/docs/runbook.md' 'novapolis-sim/README.md' 'novapolis-dev/docs/todo.sim.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' 'novapolis_agent/docs/DONELOG.txt' PASS (EXITCODE=0, 2026-03-02 23:06)
---

<!-- markdownlint-disable MD022 MD041 -->

TODO-Index (Novapolis-Dev)
==========================

Übersicht
---------

- RP-Module: `docs/todo.rp.md` — Aufgaben, Kanon-/Canvas-Arbeit, Logs (offen: 3)
- Dev-Module: `docs/todo.dev.md` — Tooling, Lint/CI, Validatoren, Doku-Infra (offen: 7)
- Agent-Module: `docs/todo.agent-board.md` — Backend (FastAPI/Ollama), Tests/Typing, Scripts (offen: 0)
- Sim-Module: `docs/todo.sim.md` — Godot/Visualisierung, API-Polling, Exportprofile (offen: 3)

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

Hinweise (Index)
----------------

- Vollständig erledigte Abschnitte (H2/H3, alle [x]) bitte manuell in `novapolis-dev/archive/todo.<modul>.archive.md` verschieben; unter der Abschnittsüberschrift `archived_at: YYYY-MM-DD HH:MM` ergänzen. Übersicht aller Archive: `novapolis-dev/archive/README.md`.
- Validierung bei Änderungen: markdownlint via `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc` und Frontmatter-Check via `scripts/check_frontmatter.py`.

Verweise
--------

- Root-Übersicht: `todo.root.md` (Kurzüberblick, Meta-Aufgaben, Links)
- DONELOG-Zentralstruktur: `novapolis-dev/archive/docs/donelogs/INDEX.md`


