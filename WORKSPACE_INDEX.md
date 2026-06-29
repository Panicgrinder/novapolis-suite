---
stand: 2026-06-29 16:07
update: Workspace-Landing auf den aktiven Root-/Dev-Status synchronisiert; stale Check-/Board-Summary aus dem 09:17-Stand ist nachgezogen.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp/results/reports/checks_report_20260629_155310.md; snapshot-lock PASS (2026-06-29 16:07)
---

<!-- markdownlint-disable MD013 -->

Novapolis Suite - Workspace Datei-Index
=======================================

Workspace-Landing-Surface
-------------------------

Dieser Index startet als schnelle Arbeitsoberflaeche fuer Root plus die vier Hauptmodule. Der detaillierte Agent-Dateikatalog bleibt darunter als Referenzpfad erhalten, dominiert aber nicht mehr den Einstieg. Fuer den laufenden Iststand ist `WORKSPACE_STATUS.md` fuehrend; fuer gemeinsame Governance und Board-Navigation sind Root- und Dev-Hub-Dokumente der erste Anlaufpunkt.

Root-Steuerflaeche
------------------

- [`README.md`](README.md) - Root-Einstieg fuer Repository-Rahmen, gemeinsame Regeln und Startpfade.
- [`WORKSPACE_STATUS.md`](WORKSPACE_STATUS.md) - laufender Betriebszustand und aktueller Wochenrahmen.
- [`todo.root.md`](todo.root.md) - aktive suiteweite Querschnittspunkte.
- [`DONELOG.md`](DONELOG.md) - Root-Summary fuer Releases und Governance.
- [`novapolis-dev/docs/process/workspace-audit-segmente.ssot.md`](novapolis-dev/docs/process/workspace-audit-segmente.ssot.md) - kanonische Zerlegung des Workspaces in wiederverwendbare Pruefsegmente.
- [`.github/copilot-instructions.md`](.github/copilot-instructions.md) - verbindliche SSOT fuer Arbeitsweise, Gates und Logging.
- [`.vscode/tasks.json`](.vscode/tasks.json) - kanonischer Task-Einstieg fuer Checks, Tests, Produkt-Gates und Tree-Refresh.

Hauptmodule
-----------

- Dev-Hub: [`novapolis-dev/README.md`](novapolis-dev/README.md) fuer Hub-Navigation, [`novapolis-dev/docs/todo.index.md`](novapolis-dev/docs/todo.index.md) fuer die Live-Boards, [`novapolis-dev/docs/donelog.md`](novapolis-dev/docs/donelog.md) fuer operative Beschluesse.
- Agent: [`novapolis_agent/README.md`](novapolis_agent/README.md) fuer Runtime- und Produktpfad, [`novapolis_agent/docs/runbook.md`](novapolis_agent/docs/runbook.md) fuer den operativen Agent-/Gate-Lauf, [`novapolis-dev/docs/todo.agent-board.md`](novapolis-dev/docs/todo.agent-board.md) fuer den aktiven Backend-Backlog.
- RP: [`novapolis-rp/README.md`](novapolis-rp/README.md) fuer Daten- und Workflow-Einstieg, [`novapolis-dev/docs/todo.rp.md`](novapolis-dev/docs/todo.rp.md) fuer den aktiven RP-Backlog.
- Sim: [`novapolis-sim/README.md`](novapolis-sim/README.md) fuer Hub-, API- und Verify-Pfade, [`novapolis-dev/docs/todo.sim.md`](novapolis-dev/docs/todo.sim.md) fuer den aktiven Sim-Backlog.

Arbeits- und Referenzpfade
--------------------------

- [`workspace_tree.txt`](workspace_tree.txt) - aktiver Reader-Baum mit gefilterter Root-Surface fuer Navigation.
- [`workspace_tree_dirs.txt`](workspace_tree_dirs.txt) - aktive Verzeichnis-Summary derselben Reader-Surface.
- [`workspace_tree_full.txt`](workspace_tree_full.txt) - ueberwachter repo-sichtbarer Vollbaum; regenerierbar via Tasks `Workspace tree:*`.
- [`workspace_tree_local.txt`](workspace_tree_local.txt) - expliziter lokaler Maschinenbaum fuer den echten On-Disk-Zustand; bewusst getrennt vom Freshness-Gate der drei kanonischen Trees.
- [`novapolis-dev/docs/active-surface-index.md`](novapolis-dev/docs/active-surface-index.md) - ACTIVE/REFERENCE/HISTORICAL-Klassifikation der Fuehrungsdoku.
- [`novapolis-dev/docs/process/abschluss-routine.ssot.md`](novapolis-dev/docs/process/abschluss-routine.ssot.md) - kanonischer Hygiene- und Abschlussrhythmus.
- [`novapolis-dev/docs/process/workspace-audit-segmente.ssot.md`](novapolis-dev/docs/process/workspace-audit-segmente.ssot.md) - fester Auditrahmen fuer Root, Shared Tooling, Dev, Agent, RP, Sim und forensische Flaechen.
- [`packages/README.md`](packages/README.md) - Einstieg in die gemeinsame Paketlage ausserhalb der vier Hauptmodule.

Reader-Surface-Grenze
---------------------

Die Landing-Surface priorisiert navigationsrelevante, aktive Repo-Inhalte. Private Laufzeitdateien, Caches und generierte Einzelartefakte gehoeren nicht zur primaeren Reader-Surface; sie werden nur als Klassen oder nachgelagerte Referenzpfade dokumentiert. Der folgende Agent-Katalog bleibt bewusst erhalten, dient aber als Tiefeinstieg statt als Workspace-Startpunkt.

Referenzkatalog Agent-Verzeichnis
---------------------------------

Hinweis: Alle Pfade beziehen sich auf den Repo-Root (`Main/`). Sofern nicht anders erwähnt, beginnen sie bei `novapolis_agent/`.
Hinweis (Aktualisierung 2026-02-26): Der Eval-Dataset-Bestand ist kanonisch in `novapolis-dev/docs/dataset-provenance.md` nachzuverfolgen.

### Paket `novapolis_agent/` (Unterordner im Single-Root)

- [`novapolis_agent/.coveragerc`](novapolis_agent/.coveragerc) - Coverage-Konfiguration
- [`novapolis_agent/.env.example`](novapolis_agent/.env.example) - Template für Umgebungsvariablen
- [`novapolis_agent/.gitignore`](novapolis_agent/.gitignore) - Git-Ignorier-Regeln
- [`novapolis_agent/cleanup_recommendations.md`](novapolis_agent/cleanup_recommendations.md) - Aufräum-Empfehlungen
- [`novapolis_agent/docs/CONTEXT_ARCH.md`](novapolis_agent/docs/CONTEXT_ARCH.md) - Kontextfluss Developer ⇄ Copilot ⇄ GPT (Rollen, Beispiele, Privacy)
- [`novapolis_agent/mypy.ini`](novapolis_agent/mypy.ini) - mypy-Konfiguration
- [`novapolis_agent/pyrightconfig.json`](novapolis_agent/pyrightconfig.json) - Python-Typsystem-Konfiguration
- [`novapolis_agent/pytest.ini`](novapolis_agent/pytest.ini) - Pytest-Konfiguration
- [`novapolis_agent/README.md`](novapolis_agent/README.md) - Projekt-Dokumentation
- [`novapolis_agent/LICENSE`](novapolis_agent/LICENSE) - MIT-Lizenz
 - [`novapolis_agent/requirements.txt`](novapolis_agent/requirements.txt) - Python-Abhängigkeiten (Laufzeit)
 - [`novapolis_agent/requirements-dev.txt`](novapolis_agent/requirements-dev.txt) - Dev-Abhängigkeiten (Lint/Tests)
- [`novapolis_agent/run_server.py`](novapolis_agent/run_server.py) - Server-Startskript
- [`novapolis_agent/test_settings.py`](novapolis_agent/test_settings.py) - Einstellungen-Test

### Lokale/generierte Artefaktklassen (nicht Teil der aktiven Reader-Surface)

- Private Laufzeitkonfiguration liegt lokal unter `novapolis_agent/.env`; kanonischer Dokumentations- und Einstiegspunkt bleibt [`novapolis_agent/.env.example`](novapolis_agent/.env.example).
- Generierte Test- und Coverage-Artefakte wie `novapolis_agent/.coverage`, `novapolis_agent/coverage.xml`, `novapolis_agent/__pycache__/`, `novapolis_agent/.mypy_cache/` und `novapolis_agent/.pytest_cache/` gehoeren zum lokalen Arbeitszustand, nicht zur primaeren Navigation.

### VS Code — Agent Workspace (`novapolis_agent/.vscode`)

- [`novapolis_agent/.vscode/extensions.json`](novapolis_agent/.vscode/extensions.json) - VSCode-Erweiterungsempfehlungen
- [`novapolis_agent/.vscode/launch.json`](novapolis_agent/.vscode/launch.json) - Startkonfigurationen
- [`novapolis_agent/.vscode/settings.json`](novapolis_agent/.vscode/settings.json) - Workspace-spezifische Einstellungen
- [`novapolis_agent/.vscode/tasks.json`](novapolis_agent/.vscode/tasks.json) - VSCode-Tasks (z. B. Tests, Eval)
  - Enthält u. a. die Task „Eval: rerun from results“ (profile-aware Reruns aus results_*.jsonl)
### VS Code — Root Workspace (`.vscode`)

- [`.vscode/extensions.json`](.vscode/extensions.json) - VSCode-Erweiterungsempfehlungen
- [`.vscode/launch.json`](.vscode/launch.json) - Startkonfigurationen
- [`.vscode/settings.json`](.vscode/settings.json) - Workspace-spezifische Einstellungen
- [`.vscode/tasks.json`](.vscode/tasks.json) - VSCode-Tasks (z. B. Tests, Eval)
  - Enthält u. a. die Task „Eval: rerun from results“ (profile-aware Reruns aus results_*.jsonl)

### App (`novapolis_agent/app`)

- [`novapolis_agent/app/__init__.py`](novapolis_agent/app/__init__.py) - App-Package-Initialisierung
- [`novapolis_agent/app/main.py`](novapolis_agent/app/main.py) - FastAPI Hauptanwendung mit Chat-/Stream-/Health-Endpunkten

Hinweis (2025-11-17): Teile des `app`-Pakets wurden archiviert und in `novapolis_agent/archive/app/` verschoben. Live-Stubs wurden durch explizite Archiv-/Import-Fehlermarker ersetzt; ein Root-`app/__init__.py`-Shim wurde hinzugefügt, damit Tests vom Repo-Root aus laufen. Commits: `1df7561`, `6191a5d`.

Hinweis Datenmodelle: Quelle ist [`novapolis_agent/app/api/models.py`](novapolis_agent/app/api/models.py).

#### `novapolis_agent/app/api`

- [`novapolis_agent/app/api/__init__.py`](novapolis_agent/app/api/__init__.py) - API-Package-Initialisierung
- [`novapolis_agent/app/api/api.py`](novapolis_agent/app/api/api.py) - API Router-Bündelung
- [`novapolis_agent/app/api/chat.py`](novapolis_agent/app/api/chat.py) - Chat-Request-Processing
- [`novapolis_agent/app/api/models.py`](novapolis_agent/app/api/models.py) - API-Datenmodelle
- [`novapolis_agent/app/api/chat_helpers.py`](novapolis_agent/app/api/chat_helpers.py) - Legacy/Geparkt (historische Helper)

#### `novapolis_agent/app/core`

- [`novapolis_agent/app/core/__init__.py`](novapolis_agent/app/core/__init__.py) - Core-Package-Initialisierung
- [`novapolis_agent/app/core/settings.py`](novapolis_agent/app/core/settings.py) - Konfigurationseinstellungen
- [`novapolis_agent/app/core/prompts.py`](novapolis_agent/app/core/prompts.py) - System-Prompt-Templates (zentral genutzt)
- [`novapolis_agent/app/core/content_management.py`](novapolis_agent/app/core/content_management.py) - Inhaltsfilter & Policy-Hooks (optional)
- [`novapolis_agent/app/core/memory.py`](novapolis_agent/app/core/memory.py) - Speicher-/Gedächtnis-Funktionen (geparkt)

#### `novapolis_agent/app/prompt`

- (entfernt) `novapolis_agent/app/prompt/system.txt` - Altlast gelöscht; zentrale Quelle ist `app/core/prompts.py`.

#### `novapolis_agent/app/routers` (entfernt 2025-11-17)
- Legacy-Router-Verzeichnis gelöscht; aktive Endpunkte liegen ausschließlich unter `app/api`.


#### `novapolis_agent/app/services` (entfernt 2025-11-17)
- Abgebautes Paket (`llm.py` + `__init__`); Chat-Flow nutzt direkt `app/api/chat.py` und Einstellungen unter `app/core`.

#### `novapolis_agent/app/utils`

- [`novapolis_agent/app/utils/convlog.py`](novapolis_agent/app/utils/convlog.py) - Konversations-Logging (geparkt)
- [`novapolis_agent/app/utils/summarize.py`](novapolis_agent/app/utils/summarize.py) - Zusammenfassungs-Tools (geparkt)
- [`novapolis_agent/app/utils/session_memory.py`](novapolis_agent/app/utils/session_memory.py) - Sitzungsbezogene Speicher-Helfer (geparkt)
- [`novapolis_agent/app/utils/examples/`](novapolis_agent/app/utils/examples/) - Beispiele (geparkt)

### Utils (`novapolis_agent/utils`)

- [`novapolis_agent/utils/__init__.py`](novapolis_agent/utils/__init__.py) - Utils-Package-Initialisierung
- [`novapolis_agent/utils/context_notes.py`](novapolis_agent/utils/context_notes.py) - Lokale Kontext-Notizen laden
- [`novapolis_agent/utils/eval_utils.py`](novapolis_agent/utils/eval_utils.py) - Eval-Helfer (truncate, coerce_json_to_jsonl, load_synonyms)
- [`novapolis_agent/utils/eval_cache.py`](novapolis_agent/utils/eval_cache.py) - Einfacher JSONL-Cache für LLM-Summaries
- [`novapolis_agent/utils/message_helpers.py`](novapolis_agent/utils/message_helpers.py) - Message/Historie Utilities
- [`novapolis_agent/utils/time_utils.py`](novapolis_agent/utils/time_utils.py) - Zeit-/Timestamp-Helfer
- [`novapolis_agent/utils/rag.py`](novapolis_agent/utils/rag.py) - Leichtgewichtiger TF-IDF RAG-Retriever (Index/Save/Load/Retrieve)

### Daten (`novapolis_agent/data`)

- [`novapolis_agent/data/logs/`](novapolis_agent/data/logs/) - Laufzeitprotokolle (generiert, gitignored)
  - [`novapolis_agent/data/logs/*.jsonl`](novapolis_agent/data/logs/) - Chat-Protokolle

### Docs (`novapolis_agent/docs`)

- [`novapolis_agent/docs/customization.md`](novapolis_agent/docs/customization.md) - Anpassungs-Dokumentation für private Nutzung
- [`novapolis_agent/docs/ARCHIVE_PLAN.md`](novapolis_agent/docs/ARCHIVE_PLAN.md) - Archiv-/Bereinigungs-Plan (Phasen)
- Zentral: [`novapolis-dev/docs/todo.agent-board.md`](novapolis-dev/docs/todo.agent-board.md) - ToDo & Roadmap (SSOT)
- Zentrale Behaviour-Richtlinien: [`.github/copilot-instructions.md`](.github/copilot-instructions.md) - SSOT für Arbeitsweise/Sicherheit
- [`novapolis_agent/docs/DONELOG.txt`](novapolis_agent/docs/DONELOG.txt) - DONELOG - Abgeschlossene Arbeiten
  (Hinweis: `AGENT_PROMPT.md` und `BEHAVIOR.md` wurden konsolidiert → `AGENT_BEHAVIOR.md`)
- [`novapolis_agent/docs/REPORTS.md`](novapolis_agent/docs/REPORTS.md) - Berichte/Reports Überblick
- [`novapolis_agent/docs/training.md`](novapolis_agent/docs/training.md) - Kurzleitfaden Training/Finetuning (inkl. Reruns)
  - Hinweis: Reruns via `novapolis_agent/scripts/rerun_from_results.py` (Flags: `--all`, `--ids`)
  - Backup/Restore: Separates Backup-Repo mit privaten Releases; MANIFEST (SHA-256) und README mit Restore-Anleitung
- [`novapolis_agent/docs/reports/`](novapolis_agent/docs/reports/) - Sammelordner für generierte/kuratierte Reports

### Eval (`novapolis_agent/eval`)

- [`novapolis_agent/eval/.gitignore`](novapolis_agent/eval/.gitignore) - Eval-spezifische Git-Ignorier-Regeln
- [`novapolis_agent/eval/eval-overview.md`](novapolis_agent/eval/eval-overview.md) - Hinweise zu Eval
- [`novapolis_agent/eval/DEPRECATIONS.md`](novapolis_agent/eval/DEPRECATIONS.md) - Deprecations/Altpfade (Eval)
<!-- Top-Level Duplikat entfernt; maßgeblich sind Dateien unter eval/datasets/ -->

#### `novapolis_agent/eval/datasets`

- [`novapolis_agent/eval/datasets/eval-smoke.jsonl`](novapolis_agent/eval/datasets/eval-smoke.jsonl) - Repo-weites Smoke-Dataset
- [`novapolis_agent/eval/datasets/eval-001-100_technik_erklaerungen_v1.0.zip`](novapolis_agent/eval/datasets/eval-001-100_technik_erklaerungen_v1.0.zip)
  - Historisches Archivpaket
- [`novapolis_agent/eval/datasets/neutral/neutral_01_20_core.v1.jsonl`](novapolis_agent/eval/datasets/neutral/neutral_01_20_core.v1.jsonl) - Neutral Core 01-20
- [`novapolis_agent/eval/datasets/neutral/neutral_81_100_tech.v1.jsonl`](novapolis_agent/eval/datasets/neutral/neutral_81_100_tech.v1.jsonl) - Neutral Tech 81-100
- [`novapolis_agent/eval/datasets/neutral/neutral_smoke.v1.jsonl`](novapolis_agent/eval/datasets/neutral/neutral_smoke.v1.jsonl) - Neutral Smoke
- [`novapolis_agent/eval/datasets/neutral/generated/neutral_101_300_generated.v1.jsonl`](novapolis_agent/eval/datasets/neutral/generated/neutral_101_300_generated.v1.jsonl) - Neutral Generated 101-300
- [`novapolis_agent/eval/datasets/neutral/quality_de_core.v1.jsonl`](novapolis_agent/eval/datasets/neutral/quality_de_core.v1.jsonl) - Quality-DE Core
- [`novapolis_agent/eval/datasets/neutral/quality_de_drift.v1.jsonl`](novapolis_agent/eval/datasets/neutral/quality_de_drift.v1.jsonl) - Quality-DE Drift
- [`novapolis_agent/eval/datasets/neutral/quality_de_canary.v1.jsonl`](novapolis_agent/eval/datasets/neutral/quality_de_canary.v1.jsonl) - Quality-DE Canary
- [`novapolis_agent/eval/datasets/rpg/rpg_21_40_fantasy.v1.jsonl`](novapolis_agent/eval/datasets/rpg/rpg_21_40_fantasy.v1.jsonl) - RPG Fantasy 21-40
- [`novapolis_agent/eval/datasets/rpg/rpg_41_60_dialog.v1.jsonl`](novapolis_agent/eval/datasets/rpg/rpg_41_60_dialog.v1.jsonl) - RPG Dialog 41-60
- [`novapolis_agent/eval/datasets/rpg/rpg_61_80_szenen.v1.jsonl`](novapolis_agent/eval/datasets/rpg/rpg_61_80_szenen.v1.jsonl) - RPG Szenen 61-80

#### `novapolis_agent/eval/config`

- [`novapolis_agent/eval/config/synonyms.json`](novapolis_agent/eval/config/synonyms.json) - Synonym-Mappings für Evaluierung
- [`novapolis_agent/eval/config/profiles.json`](novapolis_agent/eval/config/profiles.json) - Profile/Overrides für Evaluierung (inkl. „chai“)
- [`novapolis_agent/eval/config/policy.sample.json`](novapolis_agent/eval/config/policy.sample.json) - Beispiel-Policy (default + profiles)
- [`novapolis_agent/eval/config/synonyms.local.json`](novapolis_agent/eval/config/synonyms.local.json) - Lokales Synonym-Overlay (freundlich/empathisch/einfühlsam/zuwenden)
- [`novapolis_agent/eval/config/synonyms.local.sample.json`](novapolis_agent/eval/config/synonyms.local.sample.json) - Beispiel für private Synonym-Overlays
- [`novapolis_agent/eval/config/context.local.md`](novapolis_agent/eval/config/context.local.md) - Lokale Kontext-Notizen (privat)
- [`novapolis_agent/eval/config/context.local.sample.md`](novapolis_agent/eval/config/context.local.sample.md) - Muster für lokale Kontext-Notizen
- [`novapolis_agent/eval/config/synonyms.local.sanitized.json`](novapolis_agent/eval/config/synonyms.local.sanitized.json) - Sanitized/abgeleitete Synonyme

#### `novapolis_agent/eval/results`

- [`novapolis_agent/eval/results/results_*.jsonl`](novapolis_agent/eval/results/) - Evaluierungsergebnisse (generiert, gitignored)
- Beispiel: `novapolis_agent/eval/results/results_20251016_0930.jsonl`
- `novapolis_agent/eval/results/summaries/` - Generierte Workspace-Zusammenfassungen (Map-Reduce/LLM)

### Examples (`novapolis_agent/examples`)

- [`novapolis_agent/examples/unrestricted_prompt_example.txt`](novapolis_agent/examples/unrestricted_prompt_example.txt) - Beispiel
  für uneingeschränkten Prompt
- [`novapolis_agent/examples/rpg/models.py`](novapolis_agent/examples/rpg/models.py) - RPG-Modelle (geparkte Features)
- [`novapolis_agent/examples/rpg/state.py`](novapolis_agent/examples/rpg/state.py) - RPG-State-Router (geparkt)
- [`novapolis_agent/examples/rpg/roll.py`](novapolis_agent/examples/rpg/roll.py) - RPG-Roll-Router (geparkt)

### Outputs (`novapolis_agent/outputs`)

- [`novapolis_agent/outputs/`](novapolis_agent/outputs/) - Generierte Artefakte/Exports (gitignored)
- Beispiel: `outputs/lora-chai-mini-0937/` (LoRA-Adapter & Checkpoints)

### Scripts (`novapolis_agent/scripts`)

- [`novapolis_agent/scripts/scripts-overview.md`](novapolis_agent/scripts/scripts-overview.md) - Hinweise zu Skripten
- [`novapolis_agent/scripts/run_eval.py`](novapolis_agent/scripts/run_eval.py) - Hauptevaluierungsskript
- [`novapolis_agent/scripts/quick_eval.py`](novapolis_agent/scripts/quick_eval.py) - Schnelle Eval (ASGI)
- [`novapolis_agent/scripts/eval_ui.py`](novapolis_agent/scripts/eval_ui.py) - Konsolen-UI für Evaluierung
- [`novapolis_agent/scripts/eval_loader.py`](novapolis_agent/scripts/eval_loader.py) - Hilfsfunktionen zum Laden von Evaluationspaketen
- [`novapolis_agent/scripts/audit_workspace.py`](novapolis_agent/scripts/audit_workspace.py) - Einfacher Workspace-Audit
- [`novapolis_agent/scripts/dependency_check.py`](novapolis_agent/scripts/dependency_check.py) - Konsistenz-/Abhängigkeits-Checks (Eval/Config)
- [`novapolis_agent/scripts/curate_dataset_from_latest.py`](novapolis_agent/scripts/curate_dataset_from_latest.py) - Kuratiert Trainingspakete aus results_*.jsonl
- [`novapolis_agent/scripts/export_finetune.py`](novapolis_agent/scripts/export_finetune.py) - Exportiert openai_chat aus Eval-Ergebnissen
- [`novapolis_agent/scripts/prepare_finetune_pack.py`](novapolis_agent/scripts/prepare_finetune_pack.py) - Train/Val-Pack-Erzeugung aus Export
- [`novapolis_agent/scripts/openai_finetune.py`](novapolis_agent/scripts/openai_finetune.py) - Validate-only/Status für OpenAI-Format
- [`novapolis_agent/scripts/openai_ft_status.py`](novapolis_agent/scripts/openai_ft_status.py) - Statusabfrage
- [`novapolis_agent/scripts/train_lora.py`](novapolis_agent/scripts/train_lora.py) - LoRA-Training (TRL/PEFT)
- [`novapolis_agent/scripts/fine_tune_pipeline.py`](novapolis_agent/scripts/fine_tune_pipeline.py) - Mini-Pipeline fürs Fine-Tuning/LoRA
- [`novapolis_agent/scripts/rerun_from_results.py`](novapolis_agent/scripts/rerun_from_results.py) - Profile-aware Reruns auf Basis von results_*.jsonl (Flags: --all, --ids)
- [`novapolis_agent/scripts/rerun_failed.py`](novapolis_agent/scripts/rerun_failed.py) - Reruns fehlgeschlagener Items
- [`novapolis_agent/scripts/map_reduce_summary.py`](novapolis_agent/scripts/map_reduce_summary.py) - Heuristische Workspace-Zusammenfassung
- [`novapolis_agent/scripts/map_reduce_summary_llm.py`](novapolis_agent/scripts/map_reduce_summary_llm.py) - LLM-gestützte Zusammenfassung via /chat
- [`novapolis_agent/scripts/migrate_dataset_schemas.py`](novapolis_agent/scripts/migrate_dataset_schemas.py) - Migration alter Dataset-Schemata
- [`novapolis_agent/scripts/customize_prompts.py`](novapolis_agent/scripts/customize_prompts.py) - Tool zur Prompt-Anpassung
- [`novapolis_agent/scripts/estimate_tokens.py`](novapolis_agent/scripts/estimate_tokens.py) - Token-/Größenschätzung
- [`novapolis_agent/scripts/open_latest_summary.py`](novapolis_agent/scripts/open_latest_summary.py) - Öffnet neueste Gesamtzusammenfassung
- [`novapolis_agent/scripts/open_context_notes.py`](novapolis_agent/scripts/open_context_notes.py) - Öffnet/legt lokale Kontextnotizen an
- [`novapolis_agent/scripts/append_done.py`](novapolis_agent/scripts/append_done.py) - Hängt Eintrag an `docs/DONELOG.txt` an
- [`novapolis_agent/scripts/fix_donelog_times.py`](novapolis_agent/scripts/fix_donelog_times.py) - Korrigiert Zeitstempel im DONELOG
- (archiviert) [`novapolis-dev/archive/scripts/scripts.ps1-scripts/cleanup_phase3.ps1`](novapolis-dev/archive/scripts/scripts.ps1-scripts/cleanup_phase3.ps1) - Cleanup-Skript Phase 3 (ehemals `novapolis_agent/scripts/cleanup_phase3.ps1`)
- (archiviert) [`novapolis-dev/archive/scripts/scripts.ps1-scripts/cleanup_phase4.ps1`](novapolis-dev/archive/scripts/scripts.ps1-scripts/cleanup_phase4.ps1) - Cleanup-Skript Phase 4 (ehemals `novapolis_agent/scripts/cleanup_phase4.ps1`)
- (archiviert) [`novapolis-dev/archive/scripts/scripts.ps1-scripts/history_purge_plan.ps1`](novapolis-dev/archive/scripts/scripts.ps1-scripts/history_purge_plan.ps1) - Historienbereinigung (Plan; ehemals `novapolis_agent/scripts/history_purge_plan.ps1`)
- [`novapolis_agent/scripts/run_tests.py`](novapolis_agent/scripts/run_tests.py) - Test-Launcher/Helper
- [`novapolis_agent/scripts/smoke_asgi.py`](novapolis_agent/scripts/smoke_asgi.py) - Minimaler ASGI-Smoketest
- [`novapolis_agent/scripts/syn_loader.py`](novapolis_agent/scripts/syn_loader.py) - Loader für Synonym-Overlays
- [`novapolis_agent/scripts/summarize_eval_results.py`](novapolis_agent/scripts/summarize_eval_results.py) - Aggregiert Eval-Ergebnisse
- [`novapolis_agent/scripts/rag_indexer.py`](novapolis_agent/scripts/rag_indexer.py) - Baut TF-IDF RAG-Index aus .md/.txt und speichert JSON

### Tests (`novapolis_agent/tests`)

- [`novapolis_agent/tests/`](novapolis_agent/tests/) - Testsuite (Einheiten-/Integrations-Tests)
  - Auszug (nicht vollständig):
    - [`novapolis_agent/tests/test_chai_checks.py`](novapolis_agent/tests/test_chai_checks.py) - Tests für Chai-Checks & Synonyme
    - [`novapolis_agent/tests/test_context_notes.py`](novapolis_agent/tests/test_context_notes.py)
    - [`novapolis_agent/tests/test_utils_context_and_summarize.py`](novapolis_agent/tests/test_utils_context_and_summarize.py)
    - [`novapolis_agent/tests/test_app_chat_post_happy.py`](novapolis_agent/tests/test_app_chat_post_happy.py)
    - [`novapolis_agent/tests/test_streaming_fallback_and_request_id.py`](novapolis_agent/tests/test_streaming_fallback_and_request_id.py)
    - [`novapolis_agent/tests/test_prepare_finetune_pack_extras.py`](novapolis_agent/tests/test_prepare_finetune_pack_extras.py)
    - Weitere Tests siehe Ordnerliste unter `tests/`.

### Git Hooks (aktiv)

- [`githooks/pre-commit`](githooks/pre-commit) - Root-Pre-commit Hook (DONELOG/Lint) fuer das Gesamt-Repo; `git config --get core.hooksPath` zeigt im Workspace auf `githooks`.

### Agent Hooks (workspace)

- [`.github/hooks/rp-runtime-loop-guard.json`](.github/hooks/rp-runtime-loop-guard.json) - Workspace-PreToolUse-Hook fuer RP-Runtime-Mutationen im Agentbetrieb.

Hinweis: Ein modullokaler Pfad `novapolis_agent/.githooks/` ist im aktuellen Workspace nicht mehr vorhanden; fruehere Verweise darauf sind Legacy-Doku, kein aktiver Hook-Ort.

Repository-Hinweis: Standard-Branch ist `main`.

Hinweise:

- Prompts: Zentrale Quelle ist [`novapolis_agent/app/core/prompts.py`](novapolis_agent/app/core/prompts.py).
  `novapolis_agent/app/prompt/system.txt` wurde entfernt (Altlast, nicht produktiv genutzt).
- Eval-Daten bitte ausschließlich unter [`novapolis_agent/eval/datasets/...`](novapolis_agent/eval/datasets/) pflegen. Zusätzliche
  Dateien im Ordner `eval/` sind dokumentiert.




