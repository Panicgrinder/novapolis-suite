# Copilot-Projektanweisungen (Novapolis Suite)

<!-- markdownlint-disable MD022 MD032 MD036 -->

## Primäre Behaviour-Quellen
- `novapolis-agent/docs/AGENT_BEHAVIOR.md`: maßgeblicher System-Prompt, Sicherheitsrichtlinien, Arbeitsablauf.
- `novapolis-dev/docs/copilot-behavior.md`: redigierte Kopie für den Dokumentations-Hub; folgt denselben Regeln.
- `novapolis-rp/database-rp/00-admin/AI-Behavior-Mapping.{md,json}`: Rollenspiel-spezifische Verhaltenshooks und Rollenmatrix.
- `novapolis-rp/development/docs/` enthält nur Legacy-Stubs; verwende stattdessen die oben genannten Quellen.

## Gemeinsamer Arbeitsstil
- Standard-Antwortsprache ist Deutsch (Erklärungen, Beispiele, Fehlermeldungen).
- Arbeite iterativ, halte Tests und Typprüfungen grün, dokumentiere substanzielle Änderungen im jeweiligen DONELOG (`novapolis-agent/docs/DONELOG.txt`, `novapolis-dev/docs/donelog.md`).
- Prägnanter Output: skimmbar, kurze Sätze/Bullets, keine überladenen Blockzitate; bei großen Aufgaben Plan als Liste führen.
- Sicherheit & Privacy: Keine Secrets, offline bevorzugen, keine harten Pfade zu externen Repositories übernehmen.
- Root-Statusdateien `WORKSPACE_STATUS.md` und `workspace_tree.txt` als globalen Kontext heranziehen und nach größeren Umstrukturierungen oder mindestens monatlich aktualisieren.

## Repositoryweiter Rahmen
- Gemeinsamer Code gehört nach `packages/novapolis_common`; doppelte Module aus den Teilprojekten nach Migration entfernen.
- Konfigurationen bleiben projektspezifisch; Produktions- und API-Code verbleibt im jeweiligen Projektordner, Utilities werden über das Shared-Package re-exportiert.
- Secrets (`.env`) bleiben lokal; ungefilterte Exporte ausschließlich unter `novapolis-rp/database-raw/99-exports/` ablegen.
- Working docs leben in `novapolis-dev/docs/` (todo, donelog, tests, naming-policy, copilot-behavior, index); `novapolis-rp/development/...` sind Redirect-Stubs.

## Prüf- und Release-Checks
- Vor Commits relevante Tests/Skripte ausführen (`novapolis-agent/scripts/run_tests.py`, Validatoren unter `novapolis-rp/coding/tools/validators/`).
- Bei Änderungen an Behaviour- oder Policy-Dokumenten zusätzlich `novapolis-agent/tests/test_content_policy_profiles.py` und Changelogs prüfen.
- PLAN → DRY RUN → APPLY mit klaren Stop-Gates; vor APPLY nach `development/docs` Restreferenzen suchen (nur in Redirect-README und `meta.origin` erlaubt), danach Sidecars (`source`, `origin`, `migrated_at`) kontrollieren.
- Unsichere Anforderungen zuerst rückfragen; Minimal-Delta bewahren, transparente Diffs mit Dateiliste/Diffstat liefern, keine Shell-Kommandos oder History-Rewrites.

## Novapolis Agent (Backend)

### Arbeitskontext
- Repo: `novapolis-agent` (Branch `main`), Stack: FastAPI + Ollama, Kern: `app/main.py`, `app/api/models.py`, `app/core/settings.py`, `app/core/prompts.py`.

### Schnellziele bei Codeänderungen
- CI grün halten: Tests (`pytest`), Typen (Pyright/Mypy). CI prüft `docs/DONELOG.txt`.
- Nicht-triviale Änderungen → DONELOG via `scripts/append_done.py`.
- Nach jedem Edit Tests/Typen sequentiell ausführen und Ergebnisse abwarten (`pytest -q` → `pyright -p pyrightconfig.json` → `mypy -c mypy.ini .`). Keine Vorab-Statusmeldungen.

### PR-/Push-Checks
- Tests lokal: `pytest -q` oder passende Marker.
- Typechecks: `pyright -p pyrightconfig.json`, `mypy -c mypy.ini .`; optional Task „Tests: coverage (fail-under 80%)“.
- Änderungen an `app/`, `scripts/`, `utils/` → DONELOG-Update (Push auf main erfordert Eintrag; PR-Befreiung via Label `skip-donelog`).

### Pytest-Marker & Selektiver Lauf
- Unit: `pytest -q -m unit`.
- API/Streaming: `pytest -q -m "api or streaming"`.
- Selektiv: `pytest -q -k test_rate_limit_headers_on_success`.

### API & Integration
- Endpunkte: `/`, `/health`, `/version`, `POST /chat`, `POST /chat/stream` (SSE).
- Prompts zentral in `app/core/prompts.py`; Kontext-Notizen via ENV `CONTEXT_NOTES_ENABLED=true`, Pfade in Settings.
- Synonyme: Basis `eval/config/synonyms.json`, Overlay `eval/config/synonyms.local.json` (optional, Merge).

### Konventionen
- Modelle ausschließlich über `app/api/models.py` importieren (nicht `app/schemas.py`).
- Middleware setzt `X-Request-ID` auch bei Fehlern; HTTPException-Header werden gemergt.
- Rate-Limit per ENV; Tests nutzen `monkeypatch.setenv(...)` und Module-Reload.

### Häufige Fehlerquellen
- Streaming/SSE: Generator liefert Events; Tests erwarten `event: meta` mit `"policy_post"`, `event: delta` mit `"text"`, `event: done`.
- Rate-Limit-Header: Bei Erfolg `X-RateLimit-{Limit,Remaining,Window}`, bei 429 zusätzlich `Retry-After`.
- CORS-ENV `BACKEND_CORS_ORIGINS` akzeptiert JSON-Liste oder Komma-Liste (Validator in `settings`).

### Workflows & Artefakte
- Lokal starten: `uvicorn app.main:app --reload` (Swagger `/docs`).
- Finetune-Export/Prepare: Tasks „Finetune: export (latest)“ → `scripts/export_finetune.py`, „Finetune: prepare (split)“ → `scripts/prepare_finetune_pack.py` (Outputs `eval/results/finetune/`).

### Nachschlagen & Meta
- CI/Workflows: `.github/workflows/ci.yml`, `.github/workflows/enforce-donelog.yml`.
- Tests siehe `tests/` (u. a. `test_app_*` für Health/Request-ID/Rate-Limit; Streaming-/Policy-Tests definieren Format).
- Skripte: `scripts/` (Eval/Export/Train/Reports) – vorhandene CLI-Optionen nutzen.
- Beim Aktualisieren dieser Datei Hinweise aus `docs/AGENT_BEHAVIOR.md` beachten (Progress-Cadence, DONELOG, Shell-Hinweise); Checks abwarten, ggf. Task „All checks: tests+pyright+mypy“ nutzen.
- Feedbackbedarf (Marker, Tasks, Troubleshooting) kurz melden.

## Novapolis-RP

### Working Rules (Novapolis)
- SSOT: **/Main/novapolis-dev/**.
- PLAN → DRY RUN → APPLY mit harten Stop-Gates.
- Minimal und transparent: Diffs klein halten, betroffene Dateien und Diffstat nennen.
- Keine Shell-Kommandos, keine History-Rewrites.
- Working Docs liegen in `novapolis-dev/docs/` (todo, donelog, tests, naming-policy, copilot-behavior, index).
- `novapolis-rp/development/...` sind Redirect-Stubs – nicht hineinschreiben.
- Vor APPLY nach verbliebenen `development/docs`-Referenzen suchen (nur in Redirect-README und `meta.origin` erlaubt).
- Nach APPLY sicherstellen, dass verschobene Docs Sidecars mit `source`, `origin`, `migrated_at` besitzen.

### Workspace-Instructions (kompakt)

**Primärer Kontext**
- `novapolis-dev/docs/copilot-behavior.md` – Arbeitsweise, Stil, Sicherheit.
- `novapolis-dev/docs/index.md` – Navigation & Prozessreferenz.
- `database-raw/99-exports/README.md` – RAW-Policy (keine ungefilterten Daten nach `database-rp/`).

**Wichtige Regeln**
- Sprache: Deutsch (Erklärungen, Beispiele, Fehlermeldungen).
- RAW-Only: Ungefilterte Exporte ausschließlich unter `database-raw/99-exports/` speichern.
- Curation-Flow: Für RP-Nutzung stets Ingest/Curation verwenden (`coding/tools/curation/`).
- Minimal-Delta: Änderungen klein halten; `novapolis-dev/docs/donelog.md` pflegen.
- Sicherheit & Privacy: Keine Secrets; offline bevorzugen.

**Antworten & Format**
- Prägnant, skimmbar; kurze Sätze, Bullet-Listen ok, keine überladenen Blockzitate.
- Bei Codeänderungen minimaler Patch mit kurzer Begründung und Prüfung.
- Bei größeren Aufgaben ToDo-Liste (Plan) sichtbar führen und aktualisieren.

**Export/Importer**
- Export: `coding/tools/chat-exporter/` (Auto-Scroll, Inaktivitäts-Stop, speicherschonend).
- Ingest: `coding/tools/curation/ingest_jsonl.py` (streamend, chunked, sanftes Cleaning).

**Ziele**
- Stabiles Gedächtnis (Admin: system-prompt/memory-bundle) und reibungsloser Szenenstart.
- Reproduzierbare, nachvollziehbare Schritte (Dokumentation & kleine Commits).
