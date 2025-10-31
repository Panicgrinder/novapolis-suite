# DONELOG-Uebersicht (Novapolis Suite)

Schneller Blick auf alle dokumentierten Abschluesse. Die Projekt-Logbuecher bleiben weiterhin die fuehrenden Quellen; diese Datei spiegelt ihren Inhalt fuer eine zentrale Sicht wider.

## Kurzueberblick

- **novapolis_agent/docs/DONELOG.txt** protokolliert jede nicht-triviale Codeaenderung im Agent-Backend (Pflicht fuer CI).
- **novapolis-dev/docs/donelog.md** haelt migrations-, daten- und policy-bezogene Arbeiten fest.

## Volltexte

<details>
<summary>novapolis_agent/docs/DONELOG.txt</summary>

```text
# DONELOG – Abgeschlossene Arbeiten

Hinweis:
- Bitte jede abgeschlossene, nicht-triviale Änderung hier kurz dokumentieren.
- Format: YYYY-MM-DD HH:MM | Author | Kurzbeschreibung
- Keine sensiblen Inhalte eintragen.

Beispiel:
2025-10-15 12:34 | username | Eval-Pipeline stabilisiert; map_reduce_summary_llm typisiert; Doku aktualisiert.
2025-10-15 14:10 | Copilot | CI erweitert: DONELOG-Prüfung auch bei Push auf main; VS Code Task zum schnellen Eintrag hinzugefügt.
2025-10-15 14:22 | Copilot | Optionale Absicherung: lokaler pre-commit Hook (.githooks) + VS Code Tasks zum Installieren/Prüfen; Tasks portabilisiert.
2025-10-15 14:27 | Copilot | Neuer System-Prompt: docs/AGENT_PROMPT.md; VS Code Task zum Kopieren in die Zwischenablage.
2025-10-15 16:05 | Copilot | Pyright auf 1.1.406 aktualisiert; 0 Fehler/0 Warnungen; mypy/pytest grün.
2025-10-15 16:12 | Copilot | VS Code Tasks portabilisiert; ProblemMatcher für pyright/mypy hinzugefügt; schema warnings behoben.
2025-10-15 16:18 | Copilot | Markdownlint eingeführt (.markdownlint.json); Lint/Fix Tasks; Pre-commit Hook um Markdownlint mit Auto-Fix erweitert.
2025-10-15 16:26 | Copilot | README/TODO/Customization nach markdownlint (MD031/MD032/MD012/MD009/MD007) bereinigt.
2025-10-15 16:41 | Copilot | VS Code Tasks: Git-Hook-Verify/Run auf PowerShell umgestellt; doppelte Ad-hoc-Tasks entfernt; JSON-Syntaxfehler behoben.
2025-10-15 16:44 | Copilot | Markdownlint: npx-basierte Tasks ergänzt und PowerShell-Fallback-Task hinzugefügt (npx oder globales markdownlint).
2025-10-15 16:58 | Copilot | mypy: `scripts/run_eval.py` auf check_untyped_defs=True gestellt; ungenutzte ignores entfernt; Typen/Casts ergänzt; Tests grün.
2025-10-15 17:06 | Copilot | mypy: `scripts/eval_ui.py` auf check_untyped_defs=True gestellt; unused ignores entfernt; Variable umbenannt; Tests grün.
2025-10-15 17:34 | Copilot | mypy: Enforcement abgeschlossen für curate_dataset_from_latest.py, openai_finetune.py, train_lora.py; unnötige ignores entfernt; kleinere Typanpassungen; pytest grün.
2025-10-15 17:55 | Copilot | Tests: Marker-Gruppierung (unit/api/streaming/eval/scripts) eingeführt; Streaming-Fehlerpfad, dependency_check und Export→Prepare-Pipeline als offline-Tests ergänzt; Tasks für Marker-Läufe.
2025-10-15 17:48 | Copilot | Tests gruppiert: pytest-Marker (unit, api, streaming, eval, scripts) eingeführt; VS Code Tasks für gruppierte Läufe hinzugefügt; Marker auf repräsentative Tests angewendet.
2025-10-15 17:18 | Copilot | mypy-Enforcement bestätigt: `scripts/eval_ui.py` clean; pytest erneut grün; TODO/DONELOG aktualisiert.
2025-10-15 18:05 | Copilot | Rate-Limit/Timeout-Tests ergänzt; Middleware wandelt HTTPException in JSONResponse um und setzt X-Request-ID auch bei Fehlern; Header dokumentiert.
2025-10-15 18:22 | Copilot | Coverage erweitert: Prompt-/Options-Parsing, Context-Notes-Injektion, Settings-Validatoren, LLM-Service Success/Fail, Summary-Kantenfälle; .coveragerc mit Branch-Coverage; VS Code Coverage-Tasks; kombiniertes Fail-Under auf 80 angehoben.
2025-10-15 18:47 | Copilot | ID-Normalisierung vereinheitlicht ("eval-" Präfix) in export_finetune/rerun_failed/eval_ui; Utils: strip_eval_prefix/ensure_eval_prefix; Test für gemischte IDs; Cross-Drive relpath-Fixes in audit_workspace/rerun_failed/map_reduce_summary.
2025-10-15 19:02 | Copilot | Script-Smokes hinzugefügt (audit_workspace, smoke_asgi, fine_tune_pipeline, openai_ft_status, open_latest_summary, map_reduce_summary); OpenAI-Client im Test stubbed; minimale Script-Abdeckung >5% erreicht; Teil-Suites grün.
2025-10-15 19:18 | Copilot | Datensatzkurierung aus Logs: VS Code Task "Curate dataset (latest)" ergänzt; Smoke-Test für `scripts/curate_dataset_from_latest.py` hinzugefügt (Export/Prepare gepatcht, stdout-Report geprüft).
2025-10-16 09:40 | Copilot | Chai-Datensatz vereinfacht (must_include reduziert), Synonyms-Overlay erweitert (freundlich/empathisch/einfühlsam/zuwenden), Beispiel-Test `tests/test_chai_checks.py` hinzugefügt.
2025-10-16 09:41 | Copilot | Export/Kuratierung robuster: `EVAL_FILE_PATTERN` auf `eval-*.json*` erweitert; `export_finetune` nutzt `source_file` aus Results für zuverlässige Zuordnung; Mini-LoRA-Lauf (10 Schritte) auf chai-Pack durchgeführt.
2025-10-16 09:45 | Copilot | Docs aktualisiert: AGENT_PROMPT.md um Pipeline/PowerShell‑Shortcuts/Artefakte erweitert; ARCHIVE_PLAN.md mit Status & Prüfkommandos ergänzt; TODO.md Fortschritte/Robustheit dokumentiert.
2025-10-17 10:10 | Copilot | Eval: optionaler Response-Cache in `scripts/run_eval.py` (`--cache`), Near-Dedupe in `prepare_finetune_pack.py` (`--near-dup-threshold`), neue Tests hinzugefügt; VS Code Test-Explorer konfiguriert (pytest), Run-&-Debug-Profile für Marker.
2025-10-18 09:15 | Copilot | Reruns: `scripts/rerun_from_results.py` (profile-aware, liest Meta/Overrides/Patterns), Pattern-Normalisierung implementiert; Smoke-Test hinzugefügt.
2025-10-19 12:12 | Copilot | Backup: Separates Backup-Repo finalisiert (origin auf neues Repo), orphan main mit README+MANIFEST; GitHub Release erstellt und alle Snapshot-Dateien als Assets hochgeladen (um LFS-Grenzen zu vermeiden).
2025-10-19 12:14 | Copilot | VS Code: Task "Eval: rerun from results" hinzugefügt; docs/TODO.md und docs/DONELOG.txt aktualisiert.
2025-10-19 12:28 | Copilot | Backup-Härtung: cvn-root-files ZIP sanitized (ohne .env) und im Release ersetzt; MANIFEST mit SHA-256 für alle Assets aktualisiert; README mit Restore-Anleitung ergänzt.
2025-10-19 13:05 | Copilot | Tests: Neue Script-Smokes (todo_gather, customize_prompts, map_reduce_summary_llm, open_latest_summary, fine_tune_pipeline) hinzugefügt; Scripts-Abdeckung auf ~67% erhöht.
2025-10-19 14:25 | Copilot | Tests: Integration "alpaca Export→Prepare" ergänzt; Edge-Tests für export_finetune, open_context_notes, rerun_failed, fine_tune_pipeline und App-Header auf 400; Suite grün, erneute Scripts-Coverage-Messung anstehend.
2025-10-19 15:10 | Copilot | Tests: 3+1-Runde durchgeführt (customize_prompts EOF/KeyboardInterrupt, map_reduce_summary Markdown+Excludes, fine_tune_pipeline Happy-Path, /health Header). Suite grün, Scripts-Coverage ~75%.
2025-10-19 15:30 | Copilot | Tests: 3+1-Runde II (map_reduce_summary Python/JSON-Zweige, rerun_failed JSON-Array, export_finetune Outdir-Fallback, /404 Header). Suite grün, Scripts-Coverage ~78%.
2025-10-19 15:50 | Copilot | Tests: 3+1-Runde III (fine_tune_pipeline fp16 & KeyboardInterrupt, export_finetune openai_chat include_failures, /chat/stream Fehler als SSE). Suite grün, Scripts-Coverage ~78%.
2025-10-19 16:10 | Copilot | Tests: 3+1-Runde IV (migrate_dataset_schemas Happy-Path, openai_ft_status Snapshot & Follow). Suite grün, Scripts-Coverage ~79%.
2025-10-19 16:28 | Copilot | Tests: 3+1-Runde V (audit_workspace Fallback, curate_dataset_from_latest Minimal-Flow, open_context_notes Happy, /chat Fehlerpfad). Suite grün, Scripts-Coverage ~79%.
2025-10-19 17:05 | Copilot | Tests: 3+1-Runde VI (curate_dataset_from_latest Filter-Exit-5; audit_workspace Referenzsuche; / Root Request-ID Header). Suite grün; Scripts-Coverage jetzt 80% (Branch-Coverage aktiv).
2025-10-20 09:10 | Copilot | Tests: 3+1-Runde VII (curate positive Filterpfad, audit Reachability-Graph, open_latest_summary open-Path, App Rate-Limit-Header). Neue Pfade abgedeckt; Schnelllauf grün.
2025-10-20 10:00 | Copilot | TODO/DONELOG aktualisiert; Konsistenzprüfung Runde 1 durchgeführt; Reports-Standard vorgeschlagen (eval/results/reports/<topic>/<ts> mit report.md und params.txt).
2025-10-20 10:20 | Copilot | Re-Check Konsistenz nach Löschungen: cleanup_recommendations.md aktualisiert; cleanup_phase3.ps1 portabel gemacht; REPORTS.md erstellt; Report abgelegt unter eval/results/reports/consistency/20251020_1015/.
2025-10-20 20:45 | Copilot | Demo→Fantasy-Umstellung konsolidiert (Code/Tests/Docs); Reporting-Skripte (Dependencies/Coverage/Consistency) ergänzt; CI-Workflow für Reports hinzugefügt; Legacy-Bereinigung: doppelten Re-Import in app/services/__init__.py entfernt, Rerun-Failed-Status in todo_gather vereinheitlicht, WORKSPACE_INDEX um Top-Level-Duplikat bereinigt.
2025-10-20 21:10 | Copilot | Endpoints final bereinigt (app/api/endpoints/* entfernt), README/WORKSPACE_INDEX aktualisiert, TODO-Drift korrigiert; Reports-Skripte lokal erfolgreich ausgeführt (dependencies/coverage placeholder/consistency).
2025-10-21 09:25 | Copilot | Pyright Linux-Fix: `scripts/open_context_notes.py` und `scripts/open_latest_summary.py` plattformneutral (webbrowser/open/xdg-open), `os.startfile` nur noch guarded; ungenutzte type: ignore entfernt.
2025-10-21 09:28 | Copilot | `scripts/run_eval.py`: `rich` optional gemacht (Console/Table/Progress Fallbacks) und Typen für `progress.update` bereinigt; mypy/pyright grün.
2025-10-21 09:31 | Copilot | `scripts/openai_ft_status.py`: Import von `openai` optional; Fehlerausgabe nur bei tatsächlicher Nutzung, Tests können `OpenAI` stubben.
2025-10-21 09:34 | Copilot | Synonyme erweitert: Eintrag für „empathisch“ (einfühlsam, zugewandt, mitfühlend, verständnisvoll, empathie) ergänzt; `tests/test_chai_checks.py` besteht.
2025-10-21 09:38 | Copilot | CI: `workflow_dispatch` zur CI hinzugefügt (manuelle Runs möglich); alle Checks grün (CI/build-test, Enforce DONELOG, Consistency & Reports).
2025-10-21 12:00 | Copilot | Chat-Options zentral normalisiert (normalize_ollama_options) und in Stream/Non-Stream verdrahtet; Policy-Stream-Tests (Pyright) stabilisiert; Copilot-Anleitung (PR-Checkliste/Marker/Pitfalls) geschärft.
2025-10-21 12:15 | Copilot | .gitignore: Kontext-Notizen konsolidiert (eval/config/context.local.* statt Einzellisten); keine weiteren Änderungen.
2025-10-21 13:29 | Copilot | Zeitstempel vereinheitlicht: utils/time_utils.py eingeführt; convlog nutzt now_iso(); append_done nutzt now_human(); schnelle Tests grün.
2025-10-21 13:35 | Copilot | Kompakte Timestamps zentralisiert: Scripts auf now_compact() umgestellt (export_finetune, map_reduce_summary[_llm], run_eval, rerun_from_results, reports/*, eval_ui, fine_tune_pipeline, todo_gather); Scripts-Tests grün.
2025-10-21 12:47 | Panicgrinder | Reports: Konsistenz/Dependencies/Coverage Generatoren repariert (sys.path + now_compact); Reports erzeugt.
2025-10-21 12:54 | Panicgrinder | TODO: Cleanup-Kandidaten-Sektion basierend auf Konsistenz-Report ergänzt; CLI-Tools markiert.
2025-10-21 20:53 | Panicgrinder | Docs: removed remaining Compose mention in TODO (superproject and submodule). Also restored VS Code settings from backup to undo catch-all auto-approve.
2025-10-21 20:57 | Panicgrinder | Tests: add pytest norecursedirs to ignore nested submodule; fix import mismatch and restore stable test runs (api, streaming, unit passing).
2025-10-21 22:00 | Panicgrinder | Docs: add docs-only history purge plan and helper script; wording cleanup in DONELOG.
2025-10-21 22:50 | Panicgrinder | Types: fix mypy errors in chat.py, content_management.py, and run_eval.py; no runtime behavior change.
2025-10-21 23:36 | Panicgrinder | Docs: add BEHAVIOR.md (Projektverhalten) und WORKSPACE_INDEX.md aktualisiert.
2025-10-22 00:41 | Panicgrinder | Eval: start overnight run (ASGI) tag=overnight-20251022; results will be summarized after completion.
2025-10-22 00:53 | Panicgrinder | Eval: Teilrun 50/136 (ASGI) saved to results_20251022_0042_overnight-20251022.jsonl; report at docs/reports/overnight-20251022.md.
2025-10-22 01:01 | Panicgrinder | Automation: add summarize_eval_results.py and VS Code task for overnight eval + auto report.
2025-10-22 01:11 | Panicgrinder | Add generator script for new eval items and create dataset eval-101-300_generated_v1.0.jsonl (200 items)
2025-10-22 13:54 | Panicgrinder | Docs konsolidiert: AGENT_BEHAVIOR.md erstellt (Merge aus AGENT_PROMPT.md + BEHAVIOR.md); Settings CONTEXT_NOTES_PATHS um AGENT_BEHAVIOR/TODO/DONELOG erweitert; Referenzen & VS Code Task aktualisiert.
2025-10-22 14:17 | Panicgrinder | Kontext: Digest in eval/config/context.local.md; Platzhalter-Logs für heute/gestern (data/logs/YYYY-MM-DD.jsonl) erstellt; Historie in docs/AGENT_BEHAVIOR.md präzisiert; TODO aktualisiert.
2025-10-22 16:50 | Panicgrinder | Docs/Tasks: Referenzen nach Entfernen der verschachtelten Kopie geprueft; keine verbleibenden  enter cvn-agent/-Hinweise; VS Code Task auf AGENT_BEHAVIOR.md umgestellt; Tests gruen; Typechecks: Pyright 1 Fehler (Test named arg), Mypy weist bestehende unused-ignore in Tests aus.
2025-10-22 17:30 | Panicgrinder | Typechecks gruen: Pyright Warnungen nur; Mypy konfiguriert (warn_unused_ignores in tests deaktiviert); Test-Fix: eval_mode aus ChatRequest() entfernt; tzinfo-Typ fix in time_utils.
2025-10-22 18:56 | Panicgrinder | docs/prompts: Sprache dauerhaft auf Deutsch gesetzt (AGENT_BEHAVIOR.md, DEFAULT_SYSTEM_PROMPT, context.local.md). Tests/Typen grün.
2025-10-22 19:19 | Panicgrinder | lint: Pyright-Warnungen reduziert  unbenutzte Imports in Scripts entfernt (curate_dataset_from_latest, eval_ui, export_finetune, fine_tune_pipeline, generate_eval_dataset, map_reduce_summary(_llm), reports/*, rerun_from_results, todo_gather). Tests/Typen grün.
2025-10-22 23:52 | Panicgrinder | Context notes: directory + .ref support; added eval/config/context.notes with 5 pinned refs; updated AGENT_BEHAVIOR.md
2025-10-23 00:22 | Panicgrinder | Context notes: directory order via ORDER file; ignore README/ORDER meta; collapse excessive blank lines in loader; docs+tests updated
2025-10-23 01:13 | Panicgrinder | Tests: docs obsolete absent  AGENT_PROMPT.md darf fehlen; Mypy: unused ignore in app/core/mode.py entfernt
2025-10-23 10:00 | Copilot | Kontext-Notizen Defaults erweitert (eval/config/context.notes in CONTEXT_NOTES_PATHS); eval_loader Diagnostics um schema_issues ergänzt; Tests/Typen unverändert.
2025-10-23 10:00 | Copilot | Kontext-Notizen Budget erhöht (CONTEXT_NOTES_MAX_CHARS=12000); Standard-Pfade für pinned Notes aktiv; schnelle Tests grün.
2025-10-23 10:20 | Copilot | Cleanup: `app/schemas.py` als Deprecation-Weiterleitung auf `app/api/models.py` umgestellt (keine direkten Importe gefunden); sichere Migration ohne Bruch.
2025-10-23 10:35 | Copilot | Cleanup: `app/schemas.py` endgültig entfernt; Modelle liegen zentral in `app/api/models.py`. Kurzer Testlauf grün.
2025-10-23 10:42 | Copilot | Cleanup-Review: `content_management` aktiv genutzt (behalten), `convlog` nur Beispiele (belassen), `summarize` in Tests/Beispielen (belassen), `session_memory` genutzt (belassen); TODO entsprechend aktualisiert.
2025-10-23 10:50 | Copilot | Lizenz hinzugefügt: MIT-Lizenz-Datei (`LICENSE`) und Hinweis in README.
2025-10-23 11:05 | Copilot | Policy-Hooks: Datei-basierte Minimal-Tests für forbidden_terms/rewrite_map hinzugefügt; Nutzung über SETTINGS.POLICY_FILE verifiziert; schneller Teil-Lauf grün.
2025-10-23 11:08 | Copilot | Doku: Abschnitt „Inhalts‑Policy & Hooks (optional)“ in AGENT_BEHAVIOR.md ergänzt (Aktivierung, POLICY_FILE, Struktur, Verweise auf Implementierung/Tests).
2025-10-23 11:30 | Copilot | Policy-Profile: Merge von default + profiles.<id> in content_management implementiert; Tests für Allow/Rewrite/Block/Profile-Merge/Bypass hinzugefügt; policy.sample.json erweitert.
2025-10-23 11:34 | Copilot | Memory: Tests für Fenster/Trunkierung (InMemory/JSONL) ergänzt; Append-Fehler schlagen Stream nicht mehr fehl (WARN statt Crash).
2025-10-23 11:36 | Copilot | LLM-Options: Smoke-Tests für erweiterte Optionen (num_ctx/stop/penalties) hinzugefügt; Pass-Through verifiziert.
2025-10-23 11:38 | Copilot | Doku: Profiles & Merge Order in AGENT_BEHAVIOR.md ergänzt; WORKSPACE_INDEX aktualisiert (LICENSE, policy.sample.json, Beschreibungen).
2025-10-23 11:40 | Copilot | DONELOG: Autorenschafts-Hinweis in AGENT_BEHAVIOR.md ergänzt (Quelle kann Mensch oder Tool sein; Format dokumentiert).
2025-10-23 11:46 | Copilot | ChatOptions: Pydantic-Optionschema eingeführt; ChatRequest.options akzeptiert Dict oder ChatOptions; chat.py passt Mapping/Dump an; Tests hinzugefügt.
2025-10-24 11:20 | Panicgrinder | Cleanup: app/prompt/system.txt (Altlast) entfernt; WORKSPACE_INDEX und README geprüft.
2025-10-24 11:28 | Copilot | Pyright-Warnungen im App-Code bereinigt (casts/Typen in chat_helpers, content_management, mode, main); Pyright-Config auf app+utils fokussiert.
2025-10-25 09:10 | Copilot | Mittelfristig: Tool‑Use Basis angelegt (Settings: TOOLS_ENABLED/WHITELIST; Registry; calc_add Tool; Unit‑Tests). TODO.md aktualisiert.
2025-10-25 14:02 | Panicgrinder | Kontext-Notizen: Priorität auf lokale Dateien (context.local.*) vor angehefteten Refs (context.notes) gesetzt; Pyright-Konfiguration bereinigt (ungueltige Keys entfernt, Tests/Scripts vorerst ausgeschlossen). Tests & Typen grün.
2025-10-25 14:22 | Panicgrinder | Streaming: Initiales Meta-Event (params: mode, request_id, model, options) am Stream-Beginn hinzugefügt; Test ergänzt (tests/test_streaming_initial_meta.py); TODO.md aktualisiert. Suite & Typen grün.
2025-10-25 18:51 | Panicgrinder | API: Einheitliches Message-Schema  ChatRequest.messages akzeptiert ChatMessage oder dict; Validator hinzugefügt; Tests ergänzt (tests/test_messages_schema.py). CI-Gates grün.
2025-10-25 19:52 | Panicgrinder | Typfehler in app/main.py behoben: Messages-Längenprüfung für ChatMessage|dict; request.json typisiert; Pyright/Mypy grün; Tests unverändert grün.
2025-10-25 20:12 | Panicgrinder | Refactor: _get_content_from_message() eingeführt; Union-Attributzugriff eliminiert; Pyright/Mypy/Tests grün.
2025-10-25 21:10 | Copilot | RAG (leichtgewichtig) integriert: TF‑IDF‑Retriever injiziert Top‑K Snippets als System‑Nachricht (optional via SETTINGS.RAG_*); CLI `scripts/rag_indexer.py` hinzugefügt; bestehende Tests unverändert.
2025-10-25 21:18 | Copilot | Bugfix: utils/rag.py save_index Einrückung korrigiert (payload/json.dump innerhalb des with‑Blocks); Tests/Typen erneut grün.
2025-10-25 21:13 | Panicgrinder | Kleine Korrekturen
2025-10-25 22:07 | Panicgrinder | Pyright-Warnungen in utils/rag.py entfernt: explizite Typisierungen in from_dict (Dict[str, object], Mapping-Casts); keine Verhaltensänderung.
2025-10-25 22:16 | Panicgrinder | Tests ergänzt: RAG-Guards (stream/non-stream) sichern None-Index-Pfade ab; chat.py Typisierungen für RAG-Imports/idx präzisiert; Pyright jetzt 0 Warnungen; Verhalten unverändert.
2025-10-25 22:20 | Panicgrinder | Outstanding Änderungen synchronisiert (Tasks, AGENT_BEHAVIOR, Settings, WORKSPACE_INDEX); rag_indexer Script hinzugefügt. Keine Verhaltensänderung.
2025-10-25 22:31 | Panicgrinder | TODO um RAG-Sektion konsolidiert (Fortschritt+Next Steps an passender Stelle); Unit-Tests für TF-IDF (retrieve Ranking, save/load Roundtrip) ergänzt; Gates grün.
2025-10-25 22:37 | Panicgrinder | README: kurzer Abschnitt 'Lokales RAG' ergänzt (Flags, Indexer-CLI, Beispiel, Task-Hinweise); keine Codeänderungen; Gates grün.
2025-10-25 23:20 | Panicgrinder | chat.py: SSE streaming now emits 'event: delta' with JSON {text} per chunk; keeps meta/done and post-policy meta; tests+pyright+mypy PASS.
2025-10-25 23:59 | Copilot | Streaming: SSE-Chunks als Plain "data: <chunk>" + Fallback bei invalid JSON; "event: delta" nur bei Post-Rewrite; Tests/Pyright/Mypy PASS.
2025-10-25 23:59 | Copilot | LLM-Optionen erweitert: ChatOptions & Normalisierung (top_k, min_p, typical_p, tfs_z, mirostat*, penalize_newline); Settings-Defaults ergänzt; README dokumentiert; Validation-Tests hinzugefügt; Gates PASS.
2025-10-26 00:05 | Copilot | Doku: customization.md um Abschnitt zu LLM-Optionen (Defaults via .env, Pro-Request-Overrides, Beispiele curl/PowerShell) erweitert; Gates PASS.
2025-10-25 23:58 | Panicgrinder | eval_ui: profiles support top_p/num_predict; added sample profile policies; updated eval README; tests+types PASS
2025-10-26 00:10 | Panicgrinder | eval_ui: robust multi-select (comma/space/semicolon, ranges); search datasets+eval for packages; gates PASS
2025-10-31 13:22 | Panicgrinder | Markdownlint-Workflow geprüft; offene Funde aus novapolis-rp erfasst
2025-10-31 14:05 | Copilot | Dokumentation auf Novapolis-Agent umgestellt (AGENT_BEHAVIOR, README, TODO, customization, Index, Eval-Doku, Kontextsample aktualisiert).
2025-10-31 15:10 | Copilot | Root-Dokumente (Copilot-Anleitung, README, TODO, DONELOG) an Novapolis-Agent Branding angepasst.
2025-10-31 23:40 | Copilot | Agent-Workspace in `novapolis_agent` umbenannt, Mypy-Flow angepasst und Statusdateien bereinigt.
```

</details>

<details>
<summary>novapolis-dev/docs/donelog.md</summary>

```markdown
<!-- markdownlint-disable MD005 MD007 MD032 MD041 -->
<!-- Migration: Quelle aus dem frueheren coding-Hub, uebernommen am 2025-10-29 -->
<!-- Relocated aus dem ehemaligen Novapolis-RP Development-Hub nach `novapolis-dev/docs/donelog.md` am 2025-10-29 -->
Dev Hub Konsolidierung (2025-10-29)

- Dev Hub vom ehemaligen RP-Development-Hub nach `novapolis-dev/docs` verlegt; Referenzen aktualisiert und Meta-Sidecars harmonisiert.
- Legacy `development/docs` bereinigt; Meta-Sidecars geprüft; `.github/copilot-instructions.md` im RP-Repo ergänzt.
- 2025-10-29: Meta sidecars normalized: origin → full legacy path; migrated_at added.
- 2025-10-29: Dev Hub polish (README/index), VS Code Copilot instructions verlinkt; Residual-Sweep ohne Treffer.

VS Code Launch-Konfigurationen (2025-10-28)

- `.vscode/launch.json` hinzugefügt:
  - PowerShell-Runner: `validate:data (ps1)`, `lint:names (ps1)`, `lint:markdown (ps1)`, `system:check (windows)`.
  - Node-Varianten: `validate:data (node/npm)`, `lint:names (node)`, `lint:markdown (npx)`, `validate:data (status)`.
  - Ziel: Checks direkt per Startmenü (Run and Debug) nutzbar; identische Pfade wie Tasks/Wrapper.

Dokumentation/Tasks aktualisiert (2025-10-27T20:06:30+01:00)

- `novapolis-dev/docs/index.md` (vormals Coding-Index): Abschnitt "Validierung & Tasks" ergänzt (Validatoren, Lint, Systemcheck); Verweise auf `tools/validators/` und Devcontainer; `last-updated` angepasst.
- `novapolis-dev/docs/copilot-behavior.md` (vormals Coding-Copilot-Policy): Prozessregeln präzisiert – vor Push lokale Tasks ausführen (validate/data, lint/markdown, optional lint/names); Szenen‑Front‑Matter und Co‑Occurrence beachten.
- `novapolis-dev/docs/todo.md` (vormals Coding-TODO): Status synchronisiert – Rückwärts‑Review bis part‑001 abgehakt; Day‑Switch‑Canvas abgehakt; QA‑Punkt zu Szenen‑Front‑Matter in "etabliert" (✓) und "Backfill" (offen) aufgeteilt; `last-updated` angepasst.

Canvas-Verbesserungen (2025-10-27)
Linter-Wrapper (2025-10-27T20:12:30+01:00)

- `coding/tools/validators/run_check_names.ps1` hinzugefügt: stabiler Aufruf des Name-Linters ohne PowerShell `-Command`‑Quoting; nutzt Docker (falls vorhanden) oder Node/npm, sonst Exit 1 mit klarer Meldung.
- `coding/tools/validators/README.md` ergänzt (Wrapper‑Hinweis); `novapolis-dev/docs/index.md` mit Fallback‑Befehl verlinkt.

PS1-Tasks ergänzt (2025-10-27T20:18:30+01:00)

- `.vscode/tasks.json`: zusätzliche Tasks ohne Inline‑`-Command` aufgenommen:
  - `lint:names (ps1)` → `run_check_names.ps1`
  - `validate:data (ps1)` → `run_validate_all.ps1`
  - `lint:markdown (ps1)` → `run_lint_markdown.ps1`
- Neue Wrapper: `run_validate_all.ps1`, `run_lint_markdown.ps1` (Docker bevorzugt; sonst lokal; klare Fehlermeldung bei fehlenden Voraussetzungen).

CI erweitert (2025-10-27T22:40:00+01:00)

- `.github/workflows/validate.yml` aufgeteilt:
  - Linux-Job (Node 20) mit npm cache; führt Validatoren, Name‑Check, Markdown‑Lint aus.
  - Windows-Job (PS1‑Wrapper) – führt `run_validate_all.ps1`, `run_check_names.ps1`, `run_lint_markdown.ps1` aus, um PowerShell‑Skripte in CI mitzuprüfen.
- Validator-Fixes:
  - Ajv 2020‑12 für kuratiertes Manifest (`validate-curated.js`).
  - Front‑Matter‑Validator (`validate-rp.js`): `last-updated` tolerant (String/Date), H1‑Allowlist für `00-admin/system-prompt.md`.

Markdown‑Lint Wrapper gefixt (2025-10-27T22:55:00+01:00)

- `coding/tools/validators/run_lint_markdown.ps1`: Fallbacks ergänzt
  - absolute `node.exe` Erkennung; direkter Aufruf von `npx-cli.js` via `node.exe` (unabhängig von PATH)
  - Reihenfolge: Docker → node+npx-cli.js → npx.cmd → Fehlermeldung
  - Behebt Fehler "'node' is not recognized" bei fehlendem PATH.
- `00-admin/Canvas-Admin-Day-Switch-Debug.md`: ATSD-Definition ergänzt, Systemmeldungs-Template aufgenommen, Fehlerfälle/Recovery ergänzt.
- `00-admin/Canvas-T+0-Timeline.md`: Marker-Raster (Beginn/Ereignisse/Ende) und Delta-Log ergänzt.
- `00-admin/canon-canvas.draft.md`: Front-Matter (last-updated, status) hinzugefügt; Tippfehler "Akologie"→"Arkologie" korrigiert; Revision vermerkt.
- `06-scenes/scene-2025-10-27-a.md`: Erste Szenen-Kachel mit Front-Matter (characters/locations/inventoryRefs) und Cross-Links angelegt; Timeline T+0 verlinkt.
- RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T03-25-20-000Z.txt` (Quelle: Canvas; Entität Reflex – Wurzelgewebe D5 v1; TIMESTAMP: 2025-10-16_03:25).
- Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T03-25-20-000Z.flags.txt` (vorsichtig_behandeln; Grund: Regeln [REFLEX-*] abgleichen; "Entfernen möglich" vs [REFLEX-DETACH] klären; Frequenzband/Terminologie synchronisieren).
- RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T03-25-10-000Z.txt` (Quelle: Canvas; Charakter Dr. Liora Navesh v1; TIMESTAMP: 2025-10-16_03:25).
- Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T03-25-10-000Z.flags.txt` (vorsichtig_behandeln; Grund: [FR-KNOWLEDGE] wahren; H‑47/SÜDFRAGMENT gegen [EVENT-TIMELINE] prüfen; Arkologie_A1 Taxonomie mit Cluster/Relations harmonisieren).
- RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T03-25-00-000Z.txt` (Quelle: Canvas; Charakter Varek Solun v1; TIMESTAMP: 2025-10-16_03:25).
- Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T03-25-00-000Z.flags.txt` (vorsichtig_behandeln; Grund: [FR-KNOWLEDGE] wahren; H‑47-Routenstatus prüfen; Standort-Taxonomie H12 vs "Sektor_H3" harmonisieren vor Promotion).
 - RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T08-07-00-000Z.txt` (Quelle: Canvas; Relationslog Novapolis v1; TIMESTAMP: 2025-10-16_08:07).
 - Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T08-07-00-000Z.flags.txt` (vorsichtig_behandeln; Grund: Namens-/ID-Drift – System „novapolis_logistik_v1“ vs. Schema `logistik_novapolis_v*`; Händlerkontakt „Senn Daru“ unbekannt; gegen Händlergilde-Kanon prüfen/normalisieren).
 - RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T11-05-00-000Z.txt` (Quelle: Canvas; AI Behavior Index v2; TIMESTAMP: 2025-10-16_11:05).
 - Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T11-05-00-000Z.flags.txt` (vorsichtig_behandeln; Grund: Globales Matrix-Canvas – Versionsabgleich mit [BEHAVIOR-VERSION] und `ai_psymatrix_index_v1`; Modifikatoren-/Code-Format vereinheitlichen, Mappings dokumentieren).
 - RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T05-34-00-000Z.txt` (Quelle: Canvas; Ereignislog Weltgeschehen v1; TIMESTAMP: 2025-10-16_05:34).
 - Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T05-34-00-000Z.flags.txt` (vorsichtig_behandeln; Grund: Timeline/Namensabgleich – H-47 Identität offen; "Allianz" gegen [SECRECY]/[FR-KNOWLEDGE] prüfen; mit Missionslog/Sim-Woche synchronisieren).
 - RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T13-05-00-000Z.txt` (Quelle: Canvas; Logistik Novapolis v2; TIMESTAMP: 2025-10-16_13:05).
 - Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T13-05-00-000Z.flags.txt` (vorsichtig_behandeln; Grund: Konsistenzprüfung Link-Graph v2; Curation vormerken).
 - RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T12-55-00-000Z.txt` (Quelle: Canvas; Logistik C6 v2; TIMESTAMP: 2025-10-16_12:55).
 - Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T12-55-00-000Z.flags.txt` (vorsichtig_behandeln; Grund: Verknüpfungen referenzieren `logistik_novapolis_v1` trotz v2; vor Promotion angleichen/begründen).
 - RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T12-30-00-000Z.txt` (Quelle: Canvas; Inventar C6 v2; TIMESTAMP: 2025-10-16_12:30).
 - Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T12-30-00-000Z.flags.txt` (vorsichtig_behandeln; Grund: Systemverknüpfungen referenzieren `logistik_novapolis_v1`; v2-Set angleichen oder begründen).
 - RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T12-00-00-000Z.txt` (Quelle: Canvas; Station D5 – Basis (legacy)); TIMESTAMP: 2025-10-16_12:00).
 - Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T12-00-00-000Z.flags.txt` (vorsichtig_behandeln; Grund: Legacy-Snapshot; mit D5 v2.1/Kanon abgleichen, erst danach promoten).
 - RAW-Canvas abgelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T14-12-00-000Z.txt` (Quelle: Canvas; Charakter Jonas v2; TIMESTAMP: 2025-10-16_14:12).
- Sidecar-Flag erstellt: `database-raw/99-exports/RAW-canvas-2025-10-16T14-12-00-000Z.flags.txt` (vorsichtig_behandeln, korrupt; Grund: Konflikt m

```
