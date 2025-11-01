# TODO-Uebersicht (Novapolis Suite)

Diese Datei dient als zentrale Sammelstelle fuer alle laufenden Aufgaben. Die vollstaendigen Projekt-Listen sind unten eingebettet, damit sie ohne Kontextwechsel eingesehen werden koennen.

## Kurzueberblick

- **novapolis_agent**: Fokus auf Eval-/Tooling-Pflege, RAG-Ausbau, Tool-Use, Policy-Hooks.
- **novapolis-dev / novapolis-rp**: Fokus auf Canvas-Rettung Sprint 1 (Charaktere/Logistik/Systeme) sowie bestehende Datenkurierungs- und Sim-Aufgaben.
- **Root-Übersicht**: `WORKSPACE_STATUS.md` (Stand 2025-11-01) + `workspace_tree*.txt` (Stand 2025-10-31) liefern Gesamtinventar; nächste Aktualisierung idealerweise bis Mitte November oder nach größeren Umstrukturierungen.
  - [ ] Tree-Snapshots (`workspace_tree.txt`, `workspace_tree_dirs.txt`, `workspace_tree_full.txt`) neu erzeugen und ablegen (letzter Lauf 2025-10-31).
- **Archivierung**: `outputs/`- und `Backups/`-Artefakte sukzessive bündeln (ZIP) und Rotation dokumentieren.
  - [ ] Altbestände nach Runs gruppieren (z. B. `outputs/lora-YYYYMMDD_HHMM` → einzelnes ZIP in `Backups/model-runs/`).
  - [ ] Eval-Resultate aus Vor-Umbenennung auf neue Paketpfade prüfen und Meta-Felder ggf. nachziehen (`eval/results/**/*.jsonl`).
  - [ ] README oder `Backups/`-Manifest um Rotationsplan ergänzen (Aufbewahrungsdauer, Löschkriterien).
  - [ ] Automatisierte Aufgabe/Script prüfen (`scripts/cleanup_phase*.ps1`) für regelmäßiges Auslagern.

## Volltexte

<details>
<summary>novapolis_agent/docs/TODO.md</summary>

```markdown
<!-- markdownlint-disable MD013 -->
# Novapolis Agent – ToDo & Roadmap

Kurzfristige Ziele (Heute)

- [x] Eval-Profile festziehen
  - Ziel: Reproduzierbare Läufe via `eval/config/profiles.json` (quiet default, temp, optionale Checks).
  - Status: Done (UI lädt Profile; Meta-Header vollständig; kurzer ASGI-Lauf konsistent).
- [x] Eval-UI: Profile-/Quiet-/ASGI-/Skip-Preflight-Integration
  - Ziel: Läufe steuerbar über Profile, reduzierte Logs, In-Process-ASGI, Preflight optional.
  - Status: Done (Menü integriert, Flags wirksam, Trends/Exports ok).
- [x] Synonym-Overlay (privat) einführen und mergen
  - Ziel: `eval/config/synonyms.local.json` (gitignored) automatisch mit `synonyms.json` mergen.
  - Status: Done (Loader-Merge, Sample-Datei, Doku in README & eval/README, .gitignore ergänzt).
- [x] Eval-Pfade harmonisieren & Meta-Header erweitern
  - Ziel: Nutzung von `eval/datasets|results|config`, Meta mit overrides (model/host/temperature).
  - Status: Done (Runner/UI angepasst, Ergebnisse validiert).
- [x] Altlasten entfernen
  - Ziel: `app/routers/*`, redundante Prompt-Dateien, alte Helpers entfernen; Doku/Index bereinigen.
  - Status: Done (Bereinigt, Referenzen aktualisiert, Smoke-Eval grün).
- [x] Prompt-Schalter robust machen
  - Ziel: Klare Priorität DEFAULT > UNRESTRICTED > EVAL; saubere Systemprompt-Injektion.
  - Status: Done (Unit-Tests für Default/Unrestricted/Eval hinzugefügt und grün).
- [x] HTTP/Client-Reuse & Timeouts
  - Ziel: Wiederverwendbarer AsyncClient auch im HTTP-Modus + zentrale Timeouts.
  - Status: Done (process_chat_request akzeptiert geteilten AsyncClient; zentraler Timeout bleibt aktiv).
- [x] Unit-Tests: Synonym-Overlay-Merge
  - Ziel: Test, dass `synonyms.local.json` korrekt gemerged wird und fehlende Datei still ignoriert wird.
  - Status: Done (zwei Tests hinzugefügt, beide grün).

- [x] Pyright-Upgrade & Typwarnungen bereinigt
  - Status: Done (Pyright 1.1.406; 0 Fehler, 0 Warnungen im App-Bereich; Tests grün; tests/ & scripts/ vorerst aus Pyright-Analyse ausgeschlossen – schrittweise Reaktivierung geplant)

- [x] Markdownlint-Konfiguration & Tasks
  - Status: Done (`.markdownlint.json` hinzugefügt; VS Code Tasks für Lint/Fix; README/TODO/Customization bereinigt)

1–2 Tage

- [x] Qualitäts-Heuristiken fürs RPG (stilistische Checks)
  - Status: Done (rpg_style-Score + Check; Unit-Tests hinzugefügt; per Checks-Liste aktivierbar)
- [x] Parameter-Sweeps (temperature, top_p, max_tokens)
  - Status: Done (Runner unterstützt Sweeps + Overrides; Tagging/Meta;
    Trends zeigt kompakte Aggregation; top_p end-to-end sichtbar)
- [x] Beobachtbarkeit (Korrelation-ID, JSON-Logs, Trunkierung)
  - Status: Done (Request-ID-Middleware; JSON-Logs für Requests/Errors;
    Trunkierung in Chat-Logs; RID-Weitergabe an Modell; strukturierte Model-Logs)
- [x] Rate-Limits/Schutzschalter Feintuning
  - Status: Done (Fenster/Limit/Burst konfigurierbar; Exempt Paths & Trusted IPs; informative Rate-Limit-Header; Tests grün)
- [x] Streaming-Antworten (optional)
  - Status: Done (POST /chat/stream liefert text/event-stream;
    serverseitige Chunk-Ausgabe via Ollama-Stream; Logs & Fehler-Ereignisse;
    kompatibel zu bestehender /chat API)

- [x] DONELOG-Disziplin auch für Agent-Änderungen
  - Ziel: Sicherstellen, dass direkte Pushes auf `main` ebenfalls einen DONELOG-Eintrag erfordern; bequemer Editor-Flow.
  - Status: Done (CI-Workflow prüft jetzt auch Push auf `main`;
    PR-Bypass via Label bleibt; VS Code Task "Append DONELOG entry" hinzugefügt.)

- [x] Mypy-Enforcement für weitere Skripte ausweiten
  - Ziel: Schrittweises Reduzieren von `[mypy-scripts.*] ignore_errors = True`;
    per Datei auf `check_untyped_defs = True` heben.
  - Kandidaten: `scripts/run_eval.py`, `scripts/eval_ui.py`,
    `scripts/curate_dataset_from_latest.py`, `scripts/openai_finetune.py`,
    `scripts/train_lora.py`.
  - Status: Done — Alle genannten Skripte sind jetzt auf `check_untyped_defs=True`
    gestellt und mypy-clean.

  - Ziel: Mehr Edge- und Fehlerpfade testen (Streaming-Fehler, Timeout/Rate-Limit, dependency_check-Sonderfälle, Export/Prepare-Interop).
  - Hinweis: Windows-Pfade beachten (keine Laufwerks-Mismatches; projektwurzelnahe Temp-Verzeichnisse nutzen).
  - Gruppierung: pytest-Marker eingerichtet (unit, api, streaming, eval, scripts);
    VS Code Tasks für "Tests: unit" und "Tests: api+streaming" hinzugefügt.
  - Fortschritt:
    - Neue Tests für Rate-Limit/Timeout, Prompt-/Options-Parsing, Context-Notes,
      Settings-Validatoren, LLM-Service, Summaries.
    - Skript-Smokes erweitert (neu hinzugefügt):
      - `tests/scripts/test_todo_gather_smoke.py` → scripts/todo_gather.py (jetzt ~88%)
      - `tests/scripts/test_customize_prompts_smoke.py` → scripts/customize_prompts.py (jetzt ~48%)
      - `tests/scripts/test_map_reduce_summary_llm_smoke.py` → scripts/map_reduce_summary_llm.py (jetzt ~62%)
      - `tests/scripts/test_open_latest_summary_smoke.py` → scripts/open_latest_summary.py (Happy-Path, Print)
      - `tests/scripts/test_fine_tune_pipeline_smoke.py` → scripts/fine_tune_pipeline.py (Free‑Modell, --no-check, kurzer Pfad)
    - Ergebnis: Scripts-Zeilenabdeckung zuletzt ~67% (vorher ~60–65%);
      weitere Runden erhöht (letzte Messung 69% mit Branch-Coverage,
      erneute Messung steht an).
    - Zusätzlich: Beispiel‑Test `tests/test_chai_checks.py` prüft `check_term_inclusion`
      inkl. Synonym‑Erkennung.
  - Nächste Schritte:
    - [x] Integrationstest: alpaca Export→Prepare
      - Test: `tests/scripts/test_export_and_prepare_pipeline_alpaca.py` (Export alpaca → Prepare-Pack; Train/Val erzeugt)
    - [x] Weitere Edge-Tests ergänzt (export_finetune, open_context_notes, rerun_failed, fine_tune_pipeline)
    - [x] 3+1 Testrunde (customize_prompts, map_reduce_summary, fine_tune_pipeline + /health Header)
      - Resultat: Suite grün; Scripts-Coverage ~75% (Branch-Coverage aktiv)
    - [x] 3+1 Testrunde (map_reduce_summary Python/JSON, rerun_failed JSON-Array, export_finetune Fallback + /404 Header)
      - Resultat: Suite grün; Scripts-Coverage ~78%
    - [x] 3+1 Testrunde (fine_tune_pipeline fp16/KeyboardInterrupt, export_finetune openai_chat include_failures, /chat/stream Fehler-SSE)
      - Resultat: Suite grün; Scripts-Coverage stabil ~78%
    - [x] 3+1 Testrunde (migrate_dataset_schemas Happy-Path, openai_ft_status Snapshot+Follow, [App-Test bereits enthalten])
      - Resultat: Suite grün; Scripts-Coverage ~79%
    - [x] 3+1 Testrunde (audit_workspace Fallback, curate_dataset_from_latest Minimal, open_context_notes Happy, /chat Fehlerpfad)
      - Resultat: Suite grün; Scripts-Coverage stabil ~79%
    - [x] Scripts-Coverage erneut messen und gezielt ≥80% anstreben
      - Erreicht: 80% (Branch-Coverage aktiv)
      - Neu hinzugefügt:
        - tests/scripts/test_curate_dataset_filters_empty.py (Filter führen zu Exit 5)
        - tests/test_audit_workspace_references.py (scan_text_references findet Referenzen)
        - tests/test_app_root_request_id.py (X-Request-ID Header auf /)
      - Messung: vollständige Suite mit --cov=scripts --cov-branch

- [x] Pre-commit-Hook für DONELOG
  - Ziel: Commit verhindern, wenn Code unter `app/|scripts/|utils/` geändert wurde,
    aber kein aktueller DONELOG-Eintrag vorliegt (Jahres-/Datumscheck).
  - Optional: Interaktiv `scripts/append_done.py` aufrufen.
  - Optional (lokal vorbereitet): `.githooks/pre-commit` + VS Code Tasks
    - Installieren: Task "Git hooks: install local pre-commit"
    - Prüfen: Task "Git hooks: verify pre-commit"
    - Manuell ausführen: Task "Pre-commit: run check"
  - Status: Done (Hook aktiv; erweitert um markdownlint-Prüfung mit Auto-Fix für geänderte .md)

- [x] VS Code Tasks normalisieren (Portabilität)
  - Ziel: Harte `F:/`-Pfade durch `${workspaceFolder}` & `${config:python.interpreterPath}` ersetzen; konsistente CWD-Optionen.
  - Bonus: Tasks für `mypy`, `pyright`, `pytest -q`, `scripts/dependency_check.py` hinzufügen.
  - Status: Done (Tasks portabel; Pyright/Mypy ProblemMatcher; Markdownlint
    Lint/Fix Tasks ergänzt; Windows-Optimierungen für Hook-Tasks und
    Markdownlint-Fallback)

## Coverage-Ziele & Tasks

- Ziele (vereinbart):
  - App: ≥85% Zeilen, ≥75–80% Branches (inkrementell anziehen)
  - Scripts: ≥60% Zeilen (Basis, später anheben)
  - Kombiniert: Fail-Under=80 (angezogen)
- VS Code Tasks:
  - "Tests: coverage app (≥85%)"
  - "Tests: coverage scripts (≥60%)"
  - "Tests: coverage (fail-under)" (kombiniert, 80)
  
 Zusätzliche kurzfristige Abschlüsse (2025-10-21)

- [x] CI Stabilisierung (Linux/Windows)
  - `os.startfile` guard + plattformneutrale Open-Logik (webbrowser/open/xdg-open)
  - `rich` optional (Console/Table/Progress Fallbacks in run_eval)
  - `openai` optional in openai_ft_status (Nutzung prüft installierte Lib)
  - `workflow_dispatch` für manuelle CI-Runs

- [x] Synonym-Overlay erweitert (Empathie)
  - `empathisch`: [einfühlsam, zugewandt, mitfühlend, verständnisvoll, empathie]

Zusätzliche kurzfristige Abschlüsse (2025-10-22)

- [x] Docs konsolidiert: `AGENT_PROMPT.md` + `BEHAVIOR.md` → `AGENT_BEHAVIOR.md`
  - Inhalte zusammengeführt (System‑Prompt, Richtlinien, System‑Infos)
  - Verweise aktualisiert (Index, Training, Copilot‑Instructions, VS Code Task)
  - Hinweis aufgenommen, wie das Dokument via `CONTEXT_NOTES_*` in den Agent‑Kontext geladen wird
  - Kontext-Notizen Defaults unverändert belassen; Aktivierung/Erweiterung per ENV dokumentiert

- [x] Kontext-Setup & Logs (heute/gestern)
  - `eval/config/context.local.md`: 2‑Tage‑Digest (heute+gestern) + klare Feststellung (Defaults unverändert; ENV nutzen)
  - Platzhalter-Logs angelegt: `data/logs/2025-10-22.jsonl`, `data/logs/2025-10-21.jsonl` (gitignored)
  - Hinweis in `AGENT_BEHAVIOR.md` Historie präzisiert

Kurz-Update (2025-10-25)

- [x] Kontext‑Notizen: lokale Dateien priorisiert
  - Änderung: `CONTEXT_NOTES_PATHS` so angepasst, dass `context.local.*` vor `context.notes/` eingelesen wird.
  - Ergebnis: Tests wieder grün; Injektion enthält lokale Notizen zuverlässig (vor Trunkierung).
- [x] Pyright‑Konfiguration bereinigt
  - Änderung: Ungültige Keys entfernt; Analysebereich auf `app/` und `utils/` fokussiert.
  - Ergebnis: 0 Fehler/0 Warnungen im App‑Scope; Nacharbeit: tests/ & scripts/ später wieder einbeziehen und Warnungen abbauen.
 - Hinweis: RAG‑Fortschritt siehe Abschnitt „RAG (lokal, optional)“ unten.
  
Hinweise:

- Branch-Coverage ist in `.coveragerc` aktiviert; schwere/interactive Skripte sind ausgeschlossen.
- Zielwerte werden sukzessive angehoben, sobald Teilbereiche stabil darüber liegen.

## Cleanup-Kandidaten (aus Konsistenz-Report 20251021_1446)

Quelle: `eval/results/reports/consistency/20251021_1446/report.md`.

Ziel: Offensichtliche Altlasten/Beispiele sichten, entweder (a) einbinden, (b) nach `examples/` verschieben/archivieren oder (c) entfernen. Bitte jeweils kurz verifizieren (Referenzen/Tests) und mit DONELOG erfassen.

API/Nahbereich:

- [x] `app/schemas.py` — Legacy-Schema entfernt. Modelle liegen zentral unter `app/api/models.py`.
- [x] `app/api/chat_helpers.py` — Geprüft: wird produktiv genutzt (z. B. `normalize_ollama_options` in `app/api/chat.py` und Tests). Behalten.
- [x] `app/core/content_management.py` — Wird aktiv aus `app/api/chat.py` genutzt (optional via Flags, Pre/Post/Prompt‑Modifikationen). Behalten; später gezielt verdrahten/abdecken (Tests vorhanden, z. B. Post‑Hooks via Monkeypatch).
- [x] `app/utils/convlog.py` — Aktuell nur in `app/utils/examples/*` referenziert. Als Beispiel/Utility belassen; ggf. später in `examples/` verschieben.
- [x] `app/utils/summarize.py` — Wird von Tests und Beispielen genutzt; belassen.
- [x] `app/utils/session_memory.py` — Wird in `app/api/chat.py` genutzt (optional via Settings). Belassen; Folgeaufgabe: Basis‑Tests/Trunkierung.
- [x] `app/utils/examples/**` — Beispiele belassen; ggf. später konsolidieren.
- [x] `examples/rpg/*` — Beispiel‑RPG belassen; später separat dokumentieren/archivieren.

Skripte (CLI/Tools – teils „potenziell ungenutzt“ aus App-Perspektive):

- [x] `scripts/customize_prompts.py`, `scripts/estimate_tokens.py`, `scripts/open_context_notes.py` — behalten oder als „optional tools“ markieren; README-Hinweis ergänzen.
  - Status: Done — README-Abschnitt „Optionale CLI-Tools“ ergänzt; Tools aufgeführt; `--help` verfügbar.
- [x] `scripts/openai_finetune.py`, `scripts/openai_ft_status.py`, `scripts/train_lora.py`, `scripts/fine_tune_pipeline.py` — CLI-Only; behalten, aber in Doku referenzieren; ggf. mit `--help`-Tests absichern.
  - Status: Done — In README „Optionale CLI-Tools“ verlinkt; vorhandene Smokes/Tests abdecken Grundpfade (fine_tune_pipeline, openai_ft_status).
- [x] `scripts/reports/generate_*` — jetzt repariert; behalten. Optional: Task/README ergänzen (siehe unten).
  - Status: Done — README „Neuigkeiten“ beschreibt Reports; Generatoren gelistet; CI lädt Artefakte hoch.
- [x] `scripts/audit_workspace.py` — behalten (liefert diese Liste); README-Querverweis setzen.
  - Status: Done — In README „Optionale CLI-Tools“ erwähnt.

Nicht‑Python‑Artefakte (Referenzen vorhanden, aber Pflege prüfen):

- [x] `eval/config/profiles.json` — aktuell; Doku konsolidieren.
  - Status: Done — `eval/README.md` Abschnitt „Profile & Synonyme“ ergänzt.
- [x] `eval/config/synonyms.json` (+ `synonyms.local.json`) — gepflegt; README aktualisieren.
  - Status: Done — `eval/README.md` (Overlay erklärt) und README Synonym-Hinweis vorhanden.
- [x] `app/prompt/system.txt` — Altlast; zentrale Prompts sind `app/core/prompts.py`. Entfernen, wenn nicht mehr referenziert.
  - Status: Done — Datei entfernt; `WORKSPACE_INDEX.md` und `docs/DONELOG.txt` aktualisiert.

Hinweise:

- Die Heuristik meldet auch legitime CLI‑Skripte als „potenziell ungenutzt“, da sie nicht von `app/main.py` referenziert werden. Diese bitte nicht vorschnell löschen, sondern als Tools dokumentieren und ggf. mit leichten Smoke‑Tests abdecken.
- Vollständige Liste siehe Report unter obigem Pfad.

3–7 Tage

- Datensatzkurierung aus Logs (Train/Val-Pack)
  - Status: In Arbeit / Done (Teil 1): Skript `scripts/curate_dataset_from_latest.py` erstellt;
    Export (openai_chat/alpaca), Dedupe & Train/Val-Split;
    VS Code Task "Curate dataset (latest)" hinzugefügt.
  - Robustheit: Export/Kuratierung verbessert
    - `app/core/settings.py`: `EVAL_FILE_PATTERN` auf `eval-*.json*` erweitert (unterstützt .json und .jsonl).
    - `scripts/export_finetune.py`: nutzt zusätzlich `source_file` aus den Results,
      um Dataset‑Items zuverlässig zuzuordnen (auch wenn Dateien nicht mit `eval-*` benannt sind).
- Fine-Tuning/LoRA Mini-Pipeline
- Caching/Memoization für Eval-Reruns
- Rerun-Failed mit Profil/Meta-Rekonstruktion
  - Status: Done (Basis)
    - `scripts/rerun_from_results.py` rekonstruiert Model/Host/Temperature/Checks aus Meta
    - ASGI/HTTP unterstützt
    - Smoke-Test vorhanden

- [x] Mini-Eval → Export → Split → LoRA (Smoke)
  - Ziel: 10–20 Items evaluieren (quiet/ASGI), `openai_chat` exportieren, Split erzeugen,
    kurze LoRA-Trainingsprobe (max 10 Steps) mit `--only-free` oder lokalem Modell.
  - Output: Artefakte in `eval/results/finetune/`, Trainingslogs und Metriken festhalten.
  - Status: Done (chai-Profil)
    - Eval: 15 Items (ASGI/quiet) aus `eval/datasets/chai-ai_small_v1.jsonl` → `eval/results/results_20251016_0930.jsonl`
    - Kuratierung: `openai_chat` Export + Split → Train (13) / Val (2)
    - Validation: `scripts/openai_finetune.py ... --validate-only` → VALIDATION_OK
    - LoRA Mini: 10 Schritte (TinyLlama), Output: `outputs/lora-chai-mini-0937/`
    - Begleitende Verbesserungen: Checks vereinfacht; Synonyms‑Overlay erweitert; Test `tests/test_chai_checks.py` hinzugefügt.

- [x] Eval-Caching (Basis)
  - Status: Done — Optional per `--cache`
    - Speichert Antworten in `eval/results/cache_eval.jsonl`
    - Key: messages+options+model+eval_mode
    - Reruns folgen separat

- [x] Dedupe/Heuristiken für Trainingsdaten schärfen (Basis)
  - Status: Done — `prepare_finetune_pack.py` unterstützt `--near-dup-threshold` (Token‑Jaccard) zusätzlich zur Instruktions‑Dedupe.

- [x] Dokumentation Training/Feinabstimmung
  - Status: Done — `docs/training.md` (Minimalablauf, Optionen, Hinweise).

### Kurzfristig (nächste Iterationen)

- [x] Policy‑Hook & Content‑Management verdrahten
  - Ziel: `core/content_management.py` im Chat‑Flow aktivieren (Pre‑/Post‑Prompt),
    Policies aus ENV/policy.json, Modus‑Schalter (eval/unrestricted/profile).
  - Akzeptanz: Hook in `process_chat_request` und `stream_chat_request`; Log/Audit pro Eingriff;
    Tests: Rewrite/Allow‑All/Block.

- [x] Session‑Memory (Basis)
  - Ziel: `session_id` unterstützen, In‑Memory Store + Trunkierungs‑Heuristik (Token/Chars).
  - Akzeptanz: Einbettung relevanter Turns in Messages; Settings für Limits; Tests: Happy‑Path, Trunkierung, Fallback.

- [x] Erweiterte LLM‑Options
  - Schema/Validierung in `ChatRequest.options` ergänzt (`ChatOptions`), Pass‑Through bis zum Client; Smoke‑Tests hinzugefügt.
  - Ziel: num_ctx, repeat_penalty, presence/frequency_penalty etc. via `ChatRequest.options` validiert durchreichen.
  - Akzeptanz: Pydantic‑Schema/Validation, Payload‑Durchreichung, Smoke‑Tests.

Neu (Backups & Releases)

- [x] Backup-Repo (Release-Assets) erstellen und initial befüllen
  - Status: Done — Neues GitHub-Repo erstellt; `main` enthält README+MANIFEST; kompletter
    Snapshot als Release-Assets hochgeladen (ZIPs, gesplittete .venv-Parts). LFS-Grenzen
    damit umgangen.
- [x] Checksums & Restore-Doku ergänzen
  - Status: Done — Backup-Repo: MANIFEST mit SHA-256 für alle Assets erzeugt; README
    um Restore-Anleitung (Parts zusammenfügen, Verifikation) ergänzt.
  - Hinweis: Optional Verschlüsselung (7‑Zip AES‑256) für sensible Artefakte vorbereiten.

Kurz-Update (2025-10-20)

- [x] Reruns vereinheitlicht (Profile-aware)
  - Skript: [`scripts/rerun_from_results.py`](scripts/rerun_from_results.py)
  - Task: VS Code „Eval: rerun from results“
- [x] Checksums & Restore
  - Skript: [`scripts/generate_checksums.py`](scripts/generate_checksums.py)
  - Doku: [`docs/RESTORE.md`](docs/RESTORE.md)
- [x] Workspace-Index/Tasks konsolidiert
  - Datei: [`WORKSPACE_INDEX.md`](WORKSPACE_INDEX.md)
  - Tasks: normalisiert

Offene Punkte (Kurzfristig)

- [x] Integrationstest „alpaca Export→Prepare“
  - Ziel: End-to-End (Results → Export alpaca → Prepare-Pack)
  - Status: Done — Test vorhanden: [`tests/scripts/test_export_and_prepare_pipeline_alpaca.py`](../tests/scripts/test_export_and_prepare_pipeline_alpaca.py)
    sowie ergänzend: [`tests/scripts/test_export_finetune_more_edges.py`](../tests/scripts/test_export_finetune_more_edges.py),
    [`../tests/test_prepare_finetune_pack_nodedupe.py`](../tests/test_prepare_finetune_pack_nodedupe.py)
- [x] Cleanup: harte Laufwerks-Pfade entfernen
  - Status: Done — [`scripts/cleanup_phase3.ps1`](../scripts/cleanup_phase3.ps1)
    verwendet `Join-Path $ProjectRoot` (keine festen F:\-Pfade mehr)
- [x] Doku-Drift bereinigen
  - Status: Done — `cleanup_recommendations.md` und `README.md` sind konsistent;
    zentrale Endpunkte in [`app/main.py`](../app/main.py): `/`, `/health`, `/version`,
    `POST /chat`, `POST /chat/stream`

Neu: Reports-Standard

- [x] Bericht-Ordner festlegen
  - Struktur: `eval/results/reports/<topic>/<YYYYMMDD_HHMM>/`
  - Inhalte pro Run:
    - `report.md` (Ergebnisse)
    - `params.txt` (Testparameter/Scope)
  - Vorteil: reproduzierbare Audits; klare Trennung von Artefakten

Später

- Narrativspeicher (Session Memory)
- Formale Stil-Guidelines + Tests
- Tooling (pre-commit, ruff/black, pins)

- CI/Qualitätstore
  - Ziel: Optionales Coverage-Minimum in CI (z. B. Zeilen/Branches), Linting (ruff/black)
    und Format-Checks per Pre-commit & CI.

- Packaging & Deployability
  - Ziel: Healthchecks und Produktionshinweise.

### Mittelfristig

- [~] Tool‑Use/Function‑Calling (Basis)
  - Ziel: 2–3 sichere Tools (Rechnen, lokale Datei‑Sandbox, einfache Korpus‑Suche) per ReAct‑Prompting,
    Policy‑basiert freischaltbar; Protokollierung.
  - Fortschritt: Basis‑Scaffold umgesetzt
    - Settings: `TOOLS_ENABLED` (bool), `TOOLS_WHITELIST` (Liste) hinzugefügt.
    - Registry: `app/tools/registry.py` mit `register_tool/list_tools/is_allowed/call_tool`.
    - Built‑in Tool: `calc_add` (Addition mit Float‑Coercion).
    - Tests: `tests/test_tools_basic.py` (unit) prüft Deny by default, Allow per Whitelist, Unknown Tool.
  - Nächste Schritte:
    - Logging/Protokollierung der Tool‑Aufrufe (RID, Dauer, Args‑Redaktion) ergänzen.
    - Optional: Weitere Tools (z. B. `safe_eval_math`, `sandbox_ls` mit strikten Pfaden) + Policy‑Bindung.
    - Chat‑Integration (ReAct‑Stil) hinter Flag verdrahten.

- [ ] RAG (lokal)
  - Ziel: FAISS oder Qdrant; Indexer für Markdown/Text; Query‑Augmentation; konfigurierbar offline.
  - Akzeptanz: Indexer‑Script + Retrieval‑Hook; deterministische Tests (Treffer/Kein‑Treffer).

- [ ] Profile/Personas
  - Ziel: Profile/JSON (Prompts/Policies/Options), Auswahl via Header/Token/Session.
  - Akzeptanz: Validierung + Anwendungslogik; Tests: Profilwechsel wirkt.

- [ ] Evaluierung & Telemetrie
  - Ziel: Policy‑Coverage‑Tests; Metriken (Latenz p50/p95, Länge, RAG‑HitRate); strukturierte Logs.
  - Akzeptanz: Berichte in `eval/results/reports/metrics/` mit Zeitstempel (z. B. `YYYYMMDD_HHMM`); mind. 3 Kennzahlen.

### Langfristig

- [ ] Admin‑UI/Settings
  - Ziel: UI zur Steuerung von Policies/Profilen/Sessions; Live‑Logs/Health; Schutz (AuthN/Z optional).
  - Akzeptanz: Minimal‑UI mit 2–3 Screens; Read/Write Policies; Tests (smoke).

- [ ] Persistenter Memory‑Store & DSGVO‑Löschung
  - Ziel: SQLite/Postgres Speicherung + „Right to be forgotten“‑Routinen; Export/Pruning.
  - Akzeptanz: CRUD + Purge; Tests für Löschpfade.

- [ ] Skalierung/Resilienz
  - Ziel: Worker/Queue, Retry/Timeout‑Policies, Backpressure; Limits observabel.
  - Akzeptanz: Stresstest‑Skript + Metriken.

### Kleine Auffälligkeiten / Verbesserungen

- [x] Einheitliches Message‑Schema
  - Ziel: `ChatRequest.messages` akzeptiert `ChatMessage` und dicts; Validator normalisiert Einträge.
  - Status: Done — Pydantic‑Validator ergänzt; Tests hinzugefügt (`tests/test_messages_schema.py`); Flow bleibt rückwärtskompatibel.

- [x] Streaming‑Meta/Fehler-Modell
  - Ziel: Ersten SSE‑Meta‑Event (Params/Mode/RID) senden; Fehler zusätzlich protokollieren.
  - Status: Done — Erster `event: meta` mit `{params: {mode, request_id, model, options}}` wird zu Beginn des Streams gesendet; bestehendes Policy‑Meta/Delta am Ende bleibt erhalten.
  - Akzeptanz: Tests prüfen Meta‑Event + Error‑Event (neu: `tests/test_streaming_initial_meta.py`; bestehende Error‑/Policy‑Tests grün).

- [ ] Settings/Options erweitern
  - Ziel: Mehr Ollama‑Optionen exponieren, klar dokumentieren; Defaults in Settings.
  - Akzeptanz: Doku + Validation‑Tests.

- [x] AGENT_BEHAVIOR.md: DONELOG Autoren‑Definition präzisieren
  - Ziel: In `AGENT_BEHAVIOR.md` ergänzen, dass der Autor in `docs/DONELOG.txt` die Herkunft des Vorschlags widerspiegelt (z. B. „Panicgrinder“ für Benutzer‑/Owner‑Vorschläge; „Copilot“ für automatisch initiierte/umgesetzte Vorschläge).
  - Akzeptanz: Abschnitt „Regel: Abgeschlossene Arbeiten dokumentieren (DONELOG)“ erweitert; konkrete Beispiele hinzugefügt.

Metriken

- Eval-Erfolgsrate ↑ (gesamt/paketweise)
- Latenz p95 ↓
- 0 RPG-Erkennungen im Eval-Modus; konsistenter RP-Stil im UNRESTRICTED
- Trainingspacks: dedupliziert, ausgewogene Längen
- Logs strukturiert, korrelierbar, ohne sensible Leaks

- Abdeckung: inkrementelle Erhöhung (z. B. +5–10 Prozentpunkte über mehrere Iterationen); Gate optional.

---

Regel: Abgeschlossene Arbeiten dokumentieren (DONELOG)

- Jede nicht-triviale, abgeschlossene Änderung bitte in `docs/DONELOG.txt` erfassen.
- Format je Zeile: `YYYY-MM-DD HH:MM | Author | Kurzbeschreibung` (keine sensiblen Inhalte!).
- Helferskript: `python scripts/append_done.py "Kurzbeschreibung..."` hängt automatisch Zeitstempel und Autor an.
- CI: PRs mit Code-Änderungen (app/, scripts/, utils/) erfordern einen DONELOG-Eintrag; Bypass via Label `skip-donelog` möglich.
- Zusätzlich: Pushes auf `main` werden ebenfalls geprüft. Für Push-Events gibt es keinen
  Label-Bypass. Falls nötig, zuvor `docs/DONELOG.txt` aktualisieren.
- VS Code Task: "Append DONELOG entry" fragt nach einer Kurzbeschreibung und ruft
  `scripts/append_done.py` mit dem aktiven Python-Interpreter auf.

## Roadmap Nächste Schritte (Agent-Funktionen)

- [ ] Session‑Memory (Kurz/Mittelfrist)
  - Ziel: Gesprächskontext je `session_id` persistieren (In‑Memory + optional JSONL/SQLite),
    Fenster/Trunkierung (Token/Chars), konfigurierbar über Settings.
  - Akzeptanzkriterien:
    - `ChatRequest.options.session_id` wird akzeptiert.
    - Vorherige Turns werden geladen und in die Messages eingebettet (Budget‑basiert).
    - Tests: Happy‑Path + Trunkierung + „No Memory“ Fallback.

- [ ] Policy/Rules‑Engine („eigene Regeln statt externer“)
  - Ziel: Pre‑/Post‑Prompt‑Hook mit Policies (ENV/policy.json), Umschaltung per Modus/Profil
    (eval/unrestricted/profile_id).
  - Akzeptanzkriterien:
    - Hook in `process_chat_request`/`stream_chat_request` aktiv.
    - Policies anwendbar (Allow‑All/Rewrite/Verbote); Ereignisse werden geloggt.
    - Tests: Policy wirkt (Rewrite/Block), Protokollierung vorhanden.

- [ ] Tool‑Use/Function‑Calling (Basis)
  - Ziel: 2–3 sichere Tools (z. B. Rechnen, lokale Datei‑Lesen in Sandbox, einfache Suche im Korpus)
    mit ReAct‑Prompting, per Policy freischaltbar.
  - Akzeptanzkriterien:
    - Tool‑Katalog (registriert, Whitelist), Aufrufe werden protokolliert.
    - Tests: mindestens ein Tool End‑to‑End (Stub/Offline), Policy Off/On.

- [ ] RAG (lokal, optional)
  - Ziel: Einfaches Retrieval (zunächst TF‑IDF; perspektivisch FAISS/Qdrant), Indizierung für Markdown/Text, Query‑Augmentation.
  - Aktueller Stand:
    - [x] Leichtgewichtiges TF‑IDF‑Retrieval implementiert (`utils/rag.py`); optional via Settings (`RAG_ENABLED`, `RAG_INDEX_PATH`, `RAG_TOP_K`).
    - [x] Pyright‑Warnungen im RAG‑Code entfernt (strikte Typisierung in `from_dict`; 0 Warnungen).
    - [x] Guards für fehlenden Index getestet (`tests/test_rag_guards.py`) – Stream/Non‑Stream funktionieren ohne Index (fail‑open).
  - Nächste Schritte:
    - [ ] Unit‑Tests für Retrieval/Ranking und Save/Load‑Roundtrip (`retrieve`, `save_index`/`load_index`).
    - [ ] Doku: RAG‑Nutzung & Indexer (Flags, Pfade, CLI `scripts/rag_indexer.py`, empfohlene Tasks).

- [ ] Profile/Personas
  - Ziel: Profile als JSON (Prompts/Policies/Options), Auswahl via Header/Token/Session.
  - Akzeptanzkriterien:
    - Profile werden geladen, validiert und angewandt.
    - Tests: Profilwechsel beeinflusst Prompt/Optionen/Policy.

- [ ] Erweiterte LLM‑Options
  - Ziel: num_ctx, repeat_penalty, presence/frequency_penalty etc. per `ChatRequest.options`
    validiert und weitergereicht.
  - Akzeptanzkriterien:
    - Pydantic‑Schema + Validation‑Tests.
    - Durchreichung an Ollama Payload + Smoke‑Test.
```

</details>

<details>
<summary>novapolis-dev/docs/todo.md</summary>

```markdown
<!-- markdownlint-disable MD022 MD041 -->
last-updated: 2025-11-01T14:40:00+01:00
---
---

TODO (Novapolis-RP)
===================

<!-- Migration: Quelle aus dem frueheren coding-Hub, uebernommen am 2025-10-29 -->
<!-- Relocated aus dem ehemaligen Novapolis-RP Development-Hub nach `novapolis-dev/docs/todo.md` am 2025-10-29 -->

Canvas-Rettung – Sprint 1 (Stand 2025-11-01)
--------------------------------------------

Priorität A – Charaktere & Führung
----------------------------------

- [x] Varek Solun → Canvas `database-rp/02-characters/Varek-Solun.{md,json}` angelegt (2025-11-01T15:45+01:00); Standort H12 harmonisiert, Novapolis-Wissen auf Gerüchte begrenzt.
- [ ] Liora Navesh → neues Canvas `.../Liora-Navesh.*`; RAW 2025-10-16T03:25Z; Sicherstellen, dass Novapolis/D5 unbekannt bleibt; Taxonomie "Arkologie A1" übernehmen.
- [ ] Kora Malenkov → bestehendes Canvas auf Version 1.0 heben; Rollen laut `[CARAVAN-LEADERSHIP]` klarziehen; paranoide Vorsicht + Echo-Notizen übernehmen.
- [ ] Marven Kael → neues Canvas; Flags beachten (Konvoi-/Handelsleitung extern, keine Doppelrolle mit Kora).
- [ ] Arlen Dross → neues Canvas; Rolle als Händler/Vermittler präzisieren; Reflex-Einschätzung aufnehmen.
- [ ] Pahl → neues Canvas; Gesundheitsstatus (Atembeschwerden) verifizieren; Beziehungen/Risiken dokumentieren.
- [ ] Ronja Kerschner → bestehendes Canvas mit RAW-Insights ergänzen; Nachname auf "Kerschner" halten; Drift-Kommentare markieren.
- [ ] Reflex (Primärinstanz) → Canvas + Wissensstand erweitern; Frequenzband 7.3–8.0 Hz und Detachment-Regeln aus RAW übernehmen; `[REFLEX-*]` prüfen.
- [ ] Jonas Merek → Canvas anreichern; Schwester-Status auf "vermisst/unklar" normalisieren; Schuldflag als Kommentar kennzeichnen.

Priorität B – Logistik & Inventar
---------------------------------

- [ ] `inventar_c6_v2` → neues Canvas `database-rp/04-inventory/C6-inventar.*`; Systemlinks auf v2 aktualisieren.
- [ ] `logistik_c6_v2` → Inhalte nach `00-admin/Logistik.md` übernehmen; Mixed-Version-Referenzen bereinigen.
- [ ] `logistik_novapolis_v2` → Lagerstände/Wochenzyklen in Logistik-Canvas einpflegen; Tagesreport ergänzen.
- [ ] `station_d5_v2.1` + Legacy D5 → Standort-Canvas aktualisieren; Lastenaufzug, Grundfläche, Historie kennzeichnen.
- [ ] Inventar-Deltas (`Novapolis-inventar`, `D5-inventar`) synchronisieren; Links zu Missionslog prüfen.

Priorität C – Systeme, Indizes, Ereignisse
------------------------------------------

- [ ] Ereignislog Weltgeschehen → neues Admin-Canvas; Begriff "Allianz" gegen `[SECRECY]` prüfen; H-47 als Ex-Karawane markieren.
- [ ] Relationslog Novapolis → neues Canvas/Project-Canvas; Händlerkontakt "Senn Daru" verlinken; ID-Schema `logistik_novapolis_v2` angleichen.
- [ ] AI-Behavior-Index → `AI-Behavior-Mapping.md` + JSON-Sidecar erweitern; Cluster/Modifikatoren dokumentieren.
- [ ] Meta-Cluster-Index → neues Admin-Canvas; Spannungen/PsyLinks gegen Kanon verifizieren.
- [ ] Missionslog Querverweise aktualisieren (nur falls Rohdaten relevante Ereignisse tragen).

Arbeitsregeln & Referenzen
---------------------------

- Workflow siehe `database-curated/staging/reports/canvas-rescue-plan.md`.
- Quellen + Drift-Notizen in `.../staging/reports/char-block-nord-sources.md` berücksichtigen.
- FACT-Beschlüsse aus `database-curated/staging/reports/resolved.md` vor Promotion prüfen.
- Jede Migration mit JSON-Sidecar und DONELOG-Eintrag dokumentieren (`novapolis-dev/docs/donelog.md`).
- Flags (`vorsichtig_behandeln`, `korrupt`) sichtbar übernehmen, bis Review abgeschlossen ist.

Linkübersicht
-------------

- Plan: `database-curated/staging/reports/canvas-rescue-plan.md`
- Quellen: `database-curated/staging/reports/char-block-nord-sources.md`
- RAW: `database-raw/99-exports/`
- Kanon/Policies: `database-curated/staging/reports/resolved.md`, `novapolis_agent/docs/AGENT_BEHAVIOR.md`

<details>
<summary>Archiviertes Backlog (Stand 2025-10-29)</summary>

Aktive Aufgaben
---------------

- [ ] Relocation Follow-ups
  - [x] Zentrale `.github/copilot-instructions.md` im Monorepo verankert; Duplikate in agent/RP entfernt (2025-10-31)
  - [x] Datenverzeichnisse `database-curated`, `database-raw`, `database-rp` zurück nach `novapolis-rp/` verschoben (2025-10-31)
  - [ ] novapolis-sim/README verweist explizit auf zentrale Copilot-Anweisungen
  - [ ] Externe Skripte/Notizen erneut auf Altpfade prüfen
  - [ ] Set removal date for legacy stubs after downstream confirmation
  - [ ] Post-merge sweep for stragglers
  - [ ] Optional: DevContainer- und CI-Hinweise auf neue Pfade umstellen

- [ ] Sim-API auf WebSockets erweitern (Push-Updates statt Polling)
- [ ] Region-Renderlogik im Godot-Client vorbereiten (Placeholder-Geometrien)
- [ ] Darstellungs-Icons für Akteure entwerfen/ablegen
- [ ] CI-Hooks für Sim/Visualisierung (pytest + Godot Linter) ergänzen

- [ ] Exporte einsortieren
  - [ ] `99-exports/chat-export-complete.txt` hinzufügen
  - [ ] PDF `Chronist von Novapolis - Ronjas Novapolis RP.pdf` ablegen
  - [ ] Kanonische Quelle festlegen: `RAW-chat-export-2025-10-23T03-57-37-172Z.txt` als Quelle A
  - [ ] PDF als Quelle B zur Querprüfung nutzen
  - [ ] Duplikate aus `chat-export.txt` und `chat-export (1).txt` prüfen/entfernen
  - [ ] Normalisierung: `99-exports/chat-export-complete.txt` konsolidiert erzeugen

- [ ] Parsing & Normalisierung
  - [ ] Chat in strukturiertes Format (JSONL) konvertieren (optional – vorerst ausgesetzt)
  - [ ] Extrahate erzeugen: Szenenanker, Kanon-Fakten, Charakter-Fakten, Projekt-/Aufgabenstatus
  - [x] TXT-Normalisierung + Chunking (500 Zeilen) mit Index/Views (staging)

- [ ] Curation-Review (chat-export (1).txt)
  - [x] Chunk part-022 annotieren ([FACT?]/[OPEN], global 10501–10819)
  - [x] Chunk part-021 annotieren ([FACT?]/[OPEN], global 10001–10500)
  - [x] Chunk part-020 annotieren ([FACT?]/[OPEN], global 9501–10000)
  - [x] Chunk part-019 annotieren ([FACT?]/[OPEN], global 9001–9500)
  - [x] Chunk part-018 annotieren ([FACT?]/[OPEN], global 8501–9000)
  - [x] Chunk part-017 annotieren ([FACT?]/[OPEN], global 8001–8500)
  - [x] Chunk part-016 annotieren ([FACT?]/[OPEN], global 7501–8000)
  - [x] Chunk part-015 annotieren ([FACT?]/[OPEN], global 7001–7500)
  - [x] Chunk part-014 annotieren ([FACT?]/[OPEN], global 6501–7000)
  - [x] Chunk part-013 annotieren ([FACT?]/[OPEN], global 6001–6500)
  - [x] Chunk part-012 annotieren ([FACT?]/[OPEN], global 5501–6000)
  - [x] Chunk part-011 annotieren ([FACT?]/[OPEN], global 5001–5500)
  - [x] Chunk part-010 annotieren ([FACT?]/[OPEN], global 4501–5000)
  - [x] Chunk part-009 annotieren ([FACT?]/[OPEN], global 4001–4500)
  - [x] Chunk part-008 annotieren ([FACT?]/[OPEN], global 3501–4000)
  - [x] Chunk part-007 annotieren ([FACT?]/[OPEN], global 3001–3500)
  - [x] Chunk part-006 annotieren ([FACT?]/[OPEN], global 2501–3000)
  - [x] Chunk part-005 annotieren ([FACT?]/[OPEN], global 2001–2500)
  - [x] Chunk part-004 annotieren ([FACT?]/[OPEN], global 1501–2000)
  - [x] Chunk part-003 annotieren ([FACT?]/[OPEN], global 1001–1500)
  - [x] Chunk part-002 annotieren ([FACT?]/[OPEN], global 501–1000)
  - [x] Chunk part-001 annotieren ([FACT?]/[OPEN], global 1–500)
  - [x] Weiter rückwärts bis part-001 (stichprobenweise tiefer, Fokus auf strittige Stellen)

  - [ ] Tagging‑Pipeline (YAML‑getrieben)
    - [x] 019–016: Dry‑Run → Write (Heuristiken: N7→c6‑nord, NOTE/EVENT, MISSION C6‑Nord, Sektor‑Codes)
    - [ ] 015–010: Dry‑Run → Write
    - [ ] 009–001: Dry‑Run → Write
    - [ ] Alias‑Kollisionen prüfen/entscheiden ("C6" → c6 vs c6‑nord; Präferenz festlegen und ggf. Alias entfernen)
    - [ ] Unresolved klären: `Echo`, `Reflex-Wissensstand-Trainingsstand` (MD anlegen/Slug anpassen)
    - [ ] Co‑Occurrence‑Vorschläge prüfen (falls vorhanden) und Alias-Liste gezielt ergänzen

- [ ] Regeln & Verwaltung (Canvas)
  - [ ] Unumstößlich-Canvas finalisieren (Fraktionen, D5/C6-Kernfakten, N7-Entfernung)
  - [x] Day-Switch-Canvas erstellen (Checkliste: alles laden, Validierungen, Teil-Fraktionszug)
  - [ ] A/T/S/D-Metriken definieren (Bedeutung, Anzeigeformat, Zählweise)
  - [ ] Systemmeldung erweitern: Anzahl geladener Canvas + ATSD-String; Persistenz sicherstellen
  - [ ] Canvas-Kategorien A/B/C: Regeln/Workflows und Risiken dokumentieren
  - [ ] Logbuch-Policy festschreiben (stationenweit verfügbar, außer „secret“)
  - [ ] person_index_np – Struktur/Felder (Name, Rolle, Zugehörigkeit, Status, Notizen)
  - [ ] Canvas „Logistik“ – Scope, robuste Verlinkungen (Generator/Energie-Konten), Lazy-Load-Strategie
  - [ ] Canvas „Mission Tunnel“ – Felder/Metriken (Abschnitte, %Fortschritt, Blocker)
  - [ ] Export „alle Canvas“ – Sortierung nach letztem Update (Quelle für Timestamps klären)

- [ ] Memory-Bundle gegen Export prüfen und ggf. verdichten
  - [ ] Welt-/Kanon-Kernpunkte aktualisieren
  - [ ] Charakter-Kompakteinträge (Ronja, Reflex, Jonas) aktualisieren
  - [ ] Orte (D5, C6, Tunnel) und Projekt „Nordlinie 01“ einpflegen
  - [ ] Offene Loops/Blocking-Issues ergänzen

- [ ] Charakter-Canvas prüfen/ergänzen
  - [ ] Gegen Extrahate aus dem Export abgleichen
  - [ ] Ronja – Werte, Skills, Inventar, Ziele
  - [ ] Reflex – Natur/Regeln, Instanzen/Überwachung
  - [ ] Jonas – Herkunft, Rolle, Werkstatt

- [ ] Orte
  - [ ] Gegen Extrahate aus dem Export abgleichen
  - [ ] D5 – Fix-Beschreibung (vom Tunnel aus), Maße je Raum, Lastenaufzug 2t unter Bahnsteig
  - [ ] C6 – Fix-Beschreibung, Beleuchtung (historisch), nutzbare m² je Raum, Liniennetz (D5, F1, verschütteter Trakt, Karawanenlinie) + Wandtunnel; Konflikte zu 4‑Linien-Angaben auflösen
  - [ ] Tunnel D5–C6 – Gesamtlänge fixieren (ggf. aus Reisezeit), Schaden, Materialliste
  - [ ] C6‑Nord (N7) – Sealed Room: Status/Mission-Canvas, Abgrenzung Metro-Kontext dokumentieren

- [ ] Projekte
  - [ ] Gegen Extrahate aus dem Export abgleichen
  - [ ] Nordlinie 01 – Abschnitte, Material, Blocker
  - [ ] Draisine – Spezifikation (Breite≈U-Bahn, Länge ~6 m, ~10 Pers., Antrieb), Baufortschritt dokumentieren
  - [ ] Tunnel-Fortschritt – Methode festlegen (Differenz vs. %/Tag/Person), 40%-Stand verifizieren
  - [ ] Mission C6‑Nord – Ereignisse/Status pflegen; Trigger/Guards verlinken (AI-Behavior-Mapping)

- [ ] Inventar
  - [ ] Gegen Extrahate aus dem Export abgleichen
  - [ ] Fehlteile: Schweißgerät, Adapter DN60, Hydrofilter-Behälter-Plan

- [ ] Energie & Logistik
  - [ ] Energieformel/Saldo finalisieren (D5/C6), Generator-Verlinkung im Logistik-Canvas sicherstellen
  - [ ] Lazy-Load vs. dauerhaft aktive Canvas: Policy definieren (damit Verlinkungen zuverlässig ziehen)
  - [ ] Algen-/Pilz-Kapazitäten und Vorratsreichweiten modellieren; Skalierung mit Bevölkerungszahl
  - [ ] D5↔C6 Datenaustausch-Prozess (Jonas) definieren und verlinken (Logistik/Inventar)

- [ ] Szenen-Backfill & Timeline
  - [ ] `06-scenes/` füllen: letzte 3–5 Szenen rückwärts aus Export
  - [ ] Szenen-Kacheln: Datum, Kernentscheidungen, offene Fäden
  - [ ] Optional: Timeline-Index anlegen

- [ ] Nächste Spielsitzung vorbereiten
  - [ ] Szenen-Kachel 1: Status-Ping D5/C6/Nordlinie
  - [ ] Szenen-Kachel 2: Pahl/Jonas Versorgung
  - [ ] Szenen-Kachel 3: Exo-Prototyp erste Iteration

- [ ] Qualitätssicherung
  - [ ] Konsistenzcheck: Memory-Bundle vs. Einzeldateien
  - [ ] Benennungskonventionen vereinheitlichen
  - [x] Markdown-Lint/CI prüfen
  - [x] Daten-Validierungen in CI verankern (Schema + Cross-Refs)
  - [x] Szenen-Front-Matter etabliert (README + erste Szene aktualisiert)
  - [ ] Szenen-Backfill mit Front-Matter (letzte 3–5 Szenen)
  - [x] Benennung vereinheitlichen (database-rp)
  - [x] Policy dokumentieren (`novapolis-dev/docs/naming-policy.md`)
    - [x] Name-Linter hinzufügen (Dry-Run in CI)
    - [x] Dry-Run lokal ausführen (Task: "lint:names (auto)") – 0 Verstöße
    - [x] Renames: aktuell nicht erforderlich

Abgeschlossene Basisaufgaben
----------------------------

- [x] Workspace auf F:\Novapolis-RP anlegen (Ordnerstruktur)
- [x] Admin-Setup: README, Memory-Bundle, System-Prompt, Donelog

Hintergrund & Notizen
---------------------

- Vorschläge nur auf Anfrage; Kontinuität strikt wahren.
- Nach jedem Post interne 200-Token-Zusammenfassung (vom SL) einfordern.

</details>
```

</details>
