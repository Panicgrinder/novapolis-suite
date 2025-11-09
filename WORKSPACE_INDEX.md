---
stand: 2025-11-09 22:11
update: Datei vom Agent-Verzeichnis ins Repo-Root verschoben; Links auf `novapolis_agent/` angepasst
checks: markdownlint PASS (scoped)
---

<!-- markdownlint-disable MD013 -->

Novapolis Agent - Workspace Datei-Index
=======================================

Vollständiger Index aller Dateien im Agent-Verzeichnis
------------------------------------------------------

Hinweis: Alle Pfade beginnen bei `novapolis_agent/`, sofern nicht anders angegeben.

### Agent-Verzeichnis (`novapolis_agent/`)

- [`novapolis_agent/.coverage`](novapolis_agent/.coverage) - Coverage-Report (generiert)
- [`novapolis_agent/.coveragerc`](novapolis_agent/.coveragerc) - Coverage-Konfiguration
- [`novapolis_agent/.env`](novapolis_agent/.env) - Umgebungsvariablen (private Konfiguration)
- [`novapolis_agent/.env.example`](novapolis_agent/.env.example) - Template für Umgebungsvariablen
- [`novapolis_agent/.gitignore`](novapolis_agent/.gitignore) - Git-Ignorier-Regeln
- [`novapolis_agent/coverage.xml`](novapolis_agent/coverage.xml) - Coverage-Report (XML, generiert)
- [`novapolis_agent/analysis_chat_routers.md`](novapolis_agent/analysis_chat_routers.md) - Analyse der Chat-Router
- [`novapolis_agent/cleanup_recommendations.md`](novapolis_agent/cleanup_recommendations.md) - Aufräum-Empfehlungen
- [`novapolis_agent/docs/CONTEXT_ARCH.md`](novapolis_agent/docs/CONTEXT_ARCH.md) – Kontextfluss Developer ⇄ Copilot ⇄ GPT (Rollen, Beispiele, Privacy)
- [`novapolis_agent/mypy.ini`](novapolis_agent/mypy.ini) - mypy-Konfiguration
- [`novapolis_agent/pyrightconfig.json`](novapolis_agent/pyrightconfig.json) - Python-Typsystem-Konfiguration
- [`novapolis_agent/pytest.ini`](novapolis_agent/pytest.ini) - Pytest-Konfiguration
- [`novapolis_agent/README.md`](novapolis_agent/README.md) - Projekt-Dokumentation
- [`novapolis_agent/LICENSE`](novapolis_agent/LICENSE) - MIT-Lizenz
- [`novapolis_agent/requirements.txt`](novapolis_agent/requirements.txt) - Python-Abhängigkeiten (Laufzeit)
- [`novapolis_agent/requirements-dev.txt`](novapolis_agent/requirements-dev.txt) - Dev-Abhängigkeiten (Lint/Tests)
- [`novapolis_agent/requirements-train.txt`](novapolis_agent/requirements-train.txt) - Zusatzabhängigkeiten (Training)
- [`novapolis_agent/run_server.py`](novapolis_agent/run_server.py) - Server-Startskript
- [`novapolis_agent/test_settings.py`](novapolis_agent/test_settings.py) - Einstellungen-Test
- [`novapolis_agent/__pycache__/`](novapolis_agent/__pycache__/) - Python-Bytecode-Cache (generiert)
- [`novapolis_agent/.mypy_cache/`](novapolis_agent/.mypy_cache/) - mypy-Cache (generiert)
- [`novapolis_agent/.pytest_cache/`](novapolis_agent/.pytest_cache/) - Pytest-Cache (generiert)

### VS Code (`novapolis_agent/.vscode`)

- [`novapolis_agent/.vscode/extensions.json`](novapolis_agent/.vscode/extensions.json) - VSCode-Erweiterungsempfehlungen
- [`novapolis_agent/.vscode/launch.json`](novapolis_agent/.vscode/launch.json) - Startkonfigurationen
- [`novapolis_agent/.vscode/settings.json`](novapolis_agent/.vscode/settings.json) - Workspace-spezifische Einstellungen
- [`novapolis_agent/.vscode/tasks.json`](novapolis_agent/.vscode/tasks.json) - VSCode-Tasks (z. B. Tests, Eval)
  - Enthält u. a. die Task „Eval: rerun from results“ (profile-aware Reruns aus results_*.jsonl)

### App (`novapolis_agent/app`)

- [`novapolis_agent/app/__init__.py`](novapolis_agent/app/__init__.py) - App-Package-Initialisierung
- [`novapolis_agent/app/main.py`](novapolis_agent/app/main.py) - FastAPI Hauptanwendung mit Chat-/Stream-/Health-Endpunkten

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

- (entfernt) `novapolis_agent/app/prompt/system.txt` – Altlast gelöscht; zentrale Quelle ist `app/core/prompts.py`.

#### `novapolis_agent/app/routers` (legacy/geparkt)

- [`novapolis_agent/app/routers/README.md`](novapolis_agent/app/routers/README.md) - Hinweisdatei (Ordner nicht produktiv eingebunden)

#### `novapolis_agent/app/services`

- [`novapolis_agent/app/services/__init__.py`](novapolis_agent/app/services/__init__.py) - Services-Package
- [`novapolis_agent/app/services/llm.py`](novapolis_agent/app/services/llm.py) - LLM-Service (geparkt)

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
- [`novapolis_agent/utils/rag.py`](novapolis_agent/utils/rag.py) - Leichtgewichtiger TF‑IDF RAG‑Retriever (Index/Save/Load/Retrieve)

### Daten (`novapolis_agent/data`)

- [`novapolis_agent/data/logs/`](novapolis_agent/data/logs/) - Laufzeitprotokolle (generiert, gitignored)
  - [`novapolis_agent/data/logs/*.jsonl`](novapolis_agent/data/logs/) - Chat-Protokolle

### Docs (`novapolis_agent/docs`)

- [`novapolis_agent/docs/customization.md`](novapolis_agent/docs/customization.md) - Anpassungs-Dokumentation für private Nutzung
- [`novapolis_agent/docs/ARCHIVE_PLAN.md`](novapolis_agent/docs/ARCHIVE_PLAN.md) - Archiv-/Bereinigungs-Plan (Phasen)
- Zentral: [`novapolis-dev/docs/todo.agent.md`](novapolis-dev/docs/todo.agent.md) – ToDo & Roadmap (SSOT)
- Zentrale Behaviour‑Richtlinien: [`.github/copilot-instructions.md`](.github/copilot-instructions.md) – SSOT für Arbeitsweise/Sicherheit
- [`novapolis_agent/docs/DONELOG.txt`](novapolis_agent/docs/DONELOG.txt) - DONELOG – Abgeschlossene Arbeiten
  (Hinweis: `AGENT_PROMPT.md` und `BEHAVIOR.md` wurden konsolidiert → `AGENT_BEHAVIOR.md`)
- [`novapolis_agent/docs/REPORTS.md`](novapolis_agent/docs/REPORTS.md) - Berichte/Reports Überblick
- [`novapolis_agent/docs/training.md`](novapolis_agent/docs/training.md) - Kurzleitfaden Training/Finetuning (inkl. Reruns)
  - Hinweis: Reruns via `novapolis_agent/scripts/rerun_from_results.py` (Flags: `--all`, `--ids`)
  - Backup/Restore: Separates Backup-Repo mit privaten Releases; MANIFEST (SHA-256) und README mit Restore-Anleitung
- [`novapolis_agent/docs/reports/`](novapolis_agent/docs/reports/) - Sammelordner für generierte/kuratierte Reports

### Eval (`novapolis_agent/eval`)

- [`novapolis_agent/eval/.gitignore`](novapolis_agent/eval/.gitignore) - Eval-spezifische Git-Ignorier-Regeln
- [`novapolis_agent/eval/README.md`](novapolis_agent/eval/README.md) - Hinweise zu Eval
- [`novapolis_agent/eval/DEPRECATIONS.md`](novapolis_agent/eval/DEPRECATIONS.md) - Deprecations/Altpfade (Eval)
<!-- Top-Level Duplikat entfernt; maßgeblich sind Dateien unter eval/datasets/ -->

#### `novapolis_agent/eval/datasets`

- [`novapolis_agent/eval/datasets/eval-01-20_prompts_v1.0.json`](novapolis_agent/eval/datasets/eval-01-20_prompts_v1.0.json) -
  Sachliche Prompts (eval-001 bis eval-020)
- [`novapolis_agent/eval/datasets/eval-21-40_fantasy_v1.0.json`](novapolis_agent/eval/datasets/eval-21-40_fantasy_v1.0.json) -
  Fantasy-Prompts (eval-021 bis eval-040)
- [`novapolis_agent/eval/datasets/eval-41-60_dialog_prompts_v1.0.json`](novapolis_agent/eval/datasets/eval-41-60_dialog_prompts_v1.0.json)
  - Dialog-Prompts (eval-041 bis eval-060)
- [`novapolis_agent/eval/datasets/eval-61-80_szenen_prompts_v1.0.json`](novapolis_agent/eval/datasets/eval-61-80_szenen_prompts_v1.0.json)
  - Szenen-Prompts (eval-061 bis eval-080)
- [`novapolis_agent/eval/datasets/eval-81-100_technik_erklaerungen_v1.0.json`](novapolis_agent/eval/datasets/eval-81-100_technik_erklaerungen_v1.0.json)
  - Technische Erklärungen (eval-081 bis eval-100)
- [`novapolis_agent/eval/datasets/chai-ai_small_v1.jsonl`](novapolis_agent/eval/datasets/chai-ai_small_v1.jsonl) - Chai-Smalltalk/Empathie-Dataset (aktuell)
- [`novapolis_agent/eval/datasets/eval-001-100_technik_erklaerungen_v1.0.zip`](novapolis_agent/eval/datasets/eval-001-100_technik_erklaerungen_v1.0.zip)
  - Archiv (optional)
- [`novapolis_agent/eval/datasets/combined_eval_001-100.jsonl`](novapolis_agent/eval/datasets/combined_eval_001-100.jsonl) - Kombiniertes 001-100 JSONL
- [`novapolis_agent/eval/datasets/eval-101-300_generated_v1.0.jsonl`](novapolis_agent/eval/datasets/eval-101-300_generated_v1.0.jsonl) - Generierte Zusatzdaten
- [`novapolis_agent/eval/datasets/eval-smoke.jsonl`](novapolis_agent/eval/datasets/eval-smoke.jsonl) - Smoke-Test Dataset
- [`novapolis_agent/eval/datasets/gpt_samples.de.jsonl`](novapolis_agent/eval/datasets/gpt_samples.de.jsonl) - Beispielantworten (Deutsch)

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

- [`novapolis_agent/scripts/README.md`](novapolis_agent/scripts/README.md) - Hinweise zu Skripten
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
- [`novapolis_agent/scripts/cleanup_phase3.ps1`](novapolis_agent/scripts/cleanup_phase3.ps1) - Cleanup-Skript Phase 3
- [`novapolis_agent/scripts/cleanup_phase4.ps1`](novapolis_agent/scripts/cleanup_phase4.ps1) - Cleanup-Skript Phase 4
- [`novapolis_agent/scripts/history_purge_plan.ps1`](novapolis_agent/scripts/history_purge_plan.ps1) - Historienbereinigung (Plan)
- [`novapolis_agent/scripts/run_tests.py`](novapolis_agent/scripts/run_tests.py) - Test-Launcher/Helper
- [`novapolis_agent/scripts/smoke_asgi.py`](novapolis_agent/scripts/smoke_asgi.py) - Minimaler ASGI-Smoketest
- [`novapolis_agent/scripts/syn_loader.py`](novapolis_agent/scripts/syn_loader.py) - Loader für Synonym-Overlays
- [`novapolis_agent/scripts/summarize_eval_results.py`](novapolis_agent/scripts/summarize_eval_results.py) - Aggregiert Eval-Ergebnisse
- [`novapolis_agent/scripts/rag_indexer.py`](novapolis_agent/scripts/rag_indexer.py) - Baut TF‑IDF RAG‑Index aus .md/.txt und speichert JSON

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

### Git Hooks (optional)

- [`novapolis_agent/.githooks/pre-commit`](novapolis_agent/.githooks/pre-commit) - Lokaler Pre-commit Hook (DONELOG/Lint)

Repository-Hinweis: Standard-Branch ist `main`.

Hinweise:

- Prompts: Zentrale Quelle ist [`novapolis_agent/app/core/prompts.py`](novapolis_agent/app/core/prompts.py).
  `novapolis_agent/app/prompt/system.txt` wurde entfernt (Altlast, nicht produktiv genutzt).
- Eval-Daten bitte ausschließlich unter [`novapolis_agent/eval/datasets/...`](novapolis_agent/eval/datasets/) pflegen. Zusätzliche
  Dateien im Ordner `eval/` sind dokumentiert.
