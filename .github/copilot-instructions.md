# Copilot-Projektanweisungen (Novapolis Suite)

Stand: 2025-11-02 02:15 – Task-Panel-Policy & Zuständigkeiten geschärft.

<!-- markdownlint-disable MD022 MD032 MD036 -->

## Primäre Behaviour-Quellen
- `novapolis_agent/docs/AGENT_BEHAVIOR.md`: maßgeblicher System-Prompt, Sicherheitsrichtlinien, Arbeitsablauf.
- `novapolis-dev/docs/copilot-behavior.md`: redigierte Kopie für den Dokumentations-Hub; folgt denselben Regeln.
- `novapolis-rp/database-rp/00-admin/AI-Behavior-Mapping.{md,json}`: Rollenspiel-spezifische Verhaltenshooks und Rollenmatrix.
- `novapolis-rp/development/docs/` enthält nur Legacy-Stubs; verwende stattdessen die oben genannten Quellen.

## Gemeinsamer Arbeitsstil
- Standard-Antwortsprache ist Deutsch (Erklärungen, Beispiele, Fehlermeldungen).
- Arbeite iterativ, halte Tests und Typprüfungen grün, dokumentiere substanzielle Änderungen im jeweiligen DONELOG (`novapolis_agent/docs/DONELOG.txt`, `novapolis-dev/docs/donelog.md`).
- Prägnanter Output: skimmbar, keine überladenen Blockzitate; bei großen Aufgaben Plan in betreffende todo eintragen.
- Sicherheit & Privacy: Keine Secrets, offline bevorzugen, keine harten Pfade zu externen Repositories übernehmen.
- Root-Statusdateien `WORKSPACE_STATUS.md`, `workspace_tree_full.txt` und `workspace_tree_dirs.txt` als globalen Kontext heranziehen und nach größeren Umstrukturierungen oder mindestens monatlich aktualisieren.

### Tippfehler-/Benennungshygiene

- Proaktiv auf offensichtliche Tippfehler und inkonsistente Benennungen hinweisen (z. B. „archiv“ → „archive“ bei Ordnernamen/Dateien).
- Bei Korrekturen mit Minimal‑Delta vorgehen: Redirects/Stubs belassen bis alle Verweise umverdrahtet sind, dann aufräumen.
- Vor dem Entfernen von Redirect-/Mirror‑Stubs eingehende Links per Suche prüfen und erst danach löschen.

### Checkliste: Task-Läufe

- Automation-Konsole auf Idle prüfen.
- Benötigten Task im Tasks-Panel starten.
- Exit-Code und vollständigen Output abwarten.
- 2–3 s Cooldown einhalten, dann erst den nächsten Task starten.

### Copilot vs. Mensch (Verantwortungsmatrix)

- Copilot: startet und überwacht Tasks im gemeinsamen Panel.
- Copilot: dokumentiert PASS/FAIL-Ergebnisse und aktualisiert `checks` nach realen Läufen.
- Copilot: pflegt Task-Definitionen und fordert bei fehlenden Tasks Freigabe ein.
- Mensch: nutzt das User-Terminal für ad-hoc Shell-Kommandos und Explorationsläufe.
- Mensch: bestätigt Moduswechsel (Stop-Gate) und gibt neue Tasks oder Anpassungen frei.
- Mensch: sorgt dafür, dass das User-Terminal frei ist, wenn Copilot Tasks starten soll.

### Kanonische Tasks (Referenz)

- Checks: *lint+pytest* (Task ruft zuerst `Lint: markdownlint-cli2 (all md)` und danach `Tests: pytest (-q)` sequenziell auf).
- Git: *commit+push* (Commit-Message per Prompt, dann Push).
- Lint: *markdownlint-cli2 (all md)*.
- Snapshot: *now (timestamp)*.
- Hinweis: Labels müssen exakt den Einträgen in `.vscode/tasks.json` entsprechen; bei Abweichung **nicht starten**, sondern Rückfrage.

### Kanonische Task-Labels

- `Tests: pytest (-q)`
- `Tests: coverage (fail-under)`
- `DONELOG: append entry`
- `Snapshot: now (timestamp)`
- `TTS: export (Coqui→OGG)`
- `Git: commit+push`
- `Checks: lint+pytest`
- `Lint: markdownlint-cli2 (all md)`
- `Lint: markdownlint-cli2 (docs focused)`
- `Workspace tree: full`
- `Workspace tree: directories`
- `Workspace tree: summary (dirs)`

### Update-Logistik (Snapshot)

- Timestamp: Änderungen mit `YYYY-MM-DD HH:mm` (lokale Zeit) vermerken – gilt für Kopfzeilen („Stand“, „Letzte Aktualisierung“), DONELOG-Einträge und kurze Statusnotizen.
- Systemzeit vor Updates per Task `Snapshot: now (timestamp)` oder `Get-Date -Format 'yyyy-MM-dd HH:mm'` abrufen und übernehmen.
- Kurznotiz: 1–2 Sätze oder Bullet, was angepasst wurde (analog zu `novapolis-rp/database-rp/02-*`). Bei komplexeren Tasks optional Primärpfad referenzieren (`app/...`, `scripts/...`).
- Prüfungen: Relevante Checks nennen (z. B. `pytest -q`, `pyright`, `markdownlint-cli2`) inkl. Ergebnis/Exit-Status; bei Bedarf Link/Dateipfad zur Ausgabe ergänzen.
- Markdownlint-Läufe protokollieren: Lauf/Command + PASS/FAIL direkt nach dem Lauf im Status erwähnen.
- Dokumentpflege: Betroffene Artefakte synchron halten (`TODO.md`, `novapolis_agent/docs/TODO.md`, DONELOGs, `WORKSPACE_INDEX.md`, `WORKSPACE_STATUS.md`, README/Index-Seiten). Strukturänderungen → zusätzlich Tree-Snapshots aktualisieren; Behaviour-Änderungen → `AGENT_BEHAVIOR.md` & Kopien prüfen.
- Referenzen: Wenn vorhanden Issue-/PR-Links, Commit-Hash oder Kontextnotizen angeben (Inline oder als Fußnote). Für wiederkehrende Schritte Templates/Tasks im Root `.vscode/` ergänzen.

#### YAML-Frontmatter (kompakt & LLM-freundlich)

- Ab sofort bevorzugt jede Datei mit Snapshot-Kopfzeile eine YAML-Frontmatter am Dokumentanfang.
- Übergangsphase: Legacy-Kopfzeilen mit `Stand:`/`Letzte Aktualisierung:` bleiben gültig; neue Änderungen bevorzugt als YAML einpflegen. Mischbetrieb kurzfristig erlaubt; Ziel ist vollständige Migration.
- Empfohlene Schlüssel (kurz und stabil):
  - `stand`: `YYYY-MM-DD HH:mm` (lokale Zeit)
  - `update`: 1–2 Stichpunkte zur Änderung
  - `checks`: kurz zu den relevanten Prüfungen/Ergebnissen (z. B. „pytest -q PASS“)
  - Optional: `refs` (Issue/PR/Commit), `affected` (betroffene Dateien/Pfade)

Beispiel:

```markdown
---
stand: 2025-11-01 09:05
update: Task „DONELOG: append entry“ ergänzt.
checks: keine
---
```

- Hinweise:
 - Tokens sparsam halten (kurze Schlüssel, 1–2 Stichpunkte).
 - Bei jedem Schreibvorgang Frontmatter-Zeitstempel und `update`/`checks` aktualisieren.
 - Für Tools/Parsing ist YAML robuster als Freitext-Kopfzeilen.
 - Ausnahme: Für dieses Dokument (`.github/copilot-instructions.md`) keine YAML-Frontmatter verwenden (Parser-Einschränkung). Snapshot hier weiterhin per `Stand:`-Zeile pflegen.
 - Fallback (allgemein): Wenn YAML-Frontmatter technisch nicht einsetzbar ist (Parser/Format-Einschränkung), nutze am Dokumentanfang eine kompakte Kopfzeile im Klartext:
  - Erste Zeile: `Stand: YYYY-MM-DD HH:mm – <Kurznotiz>`
  - Optional darunter: `Checks: <kurz>`
  - Beispiel:
    - `Stand: 2025-11-01 09:28 – Abschnitt X präzisiert.`
    - `Checks: pytest -q PASS`

Hinweis für OpenAI Custom Instructions

- Für Kontexte mit striktem Tokenbudget (z. B. Chat‑Assistenten außerhalb des Editors) existiert eine kompakte „Min“-Variante der Arbeitsregeln: `novapolis-dev/docs/copilot-behavior.min.md`. Diese ist für das Feld „Custom Instructions“ geeignet (LLM‑freundlich, ≤1k Tokens).

### Modell-Profile & Moduswechsel (GPT‑5 ↔ GPT‑5 Codex)

- Standardmodus: GPT‑5 (General) für redaktionelle Arbeiten, Kanon-/Quellenabgleich, `[FACT]`↔`[FACT?]`‑Revalidierung, Policy-/Prozess‑Checks und Textkurierung.
- Codex-Modus (umschalten bei Bedarf): Für Code‑schwere Aufgaben wie Skripte/Validatoren, Tests/CI, API‑/Service‑Änderungen, Parser/RegEx, Datentransformationen.
- Heuristische Trigger für Wechselvorschlag (nicht automatisch, nur Hinweis):
  - Edits in Quellcodepfaden: `novapolis_agent/app/**`, `novapolis_agent/scripts/**`, `novapolis_agent/utils/**`, `novapolis_agent/tests/**`, `packages/**`, `novapolis-rp/coding/**`.
  - Anforderung: „Bitte Skript/Validator/Test bauen“, „API anpassen“, „Pytest/Typing fixen“.
  - Geplante Ausführung technischer Tasks: Pytest/Mypy/Pyright, Linter-/Build‑Themen.
- Erinnerung/Prompting‑Policy:
  - Wenn aktueller Modus = GPT‑5 und ein Trigger erkannt wird, freundlich hinweisen: „Hinweis: Für Code‑Änderungen ist Codex sinnvoll. Jetzt auf GPT‑5 Codex wechseln?“
  - Nutzerentscheid respektieren; bei „nein“ weiter im aktuellen Modus arbeiten. Auf Wunsch „Bitte nicht erinnern“ stelle ich Erinnerungen ein, bis du wieder grünes Licht gibst.
  - Explizite Nutzerwahl überschreibt Heuristik: „Modus Codex“/„Modus General“ setzt sofort um.
- Transparenz: Den aktiven Modus im nächsten Status‑Update kurz erwähnen (z. B. „Modus: General“), wenn ein Wechsel stattfand oder Code‑Arbeit ansteht.
- Optional: In `WORKSPACE_STATUS.md` im Abschnitt „Aktueller Arbeitsmodus“ die letzte Wahl notieren (nur wenn erwünscht).

#### STOP‑Gate vor Code‑Aktionen

- Vor potenziell code‑schweren Aktionen (Dateiedits unter Codepfaden, Skript-/Validator‑Neubau, Test-/Typecheck‑Runs, API/Service‑Änderungen) wird ein hartes Stop‑Gate gesetzt.
- Ablauf:
  1) Ausgabe „STOP: Moduswechsel empfohlen. Bitte Modus wählen.“
  2) Warten auf explizite Bestätigung:
    - „Wechsel: Modus Codex“ → sofort auf Codex wechseln und fortfahren.
    - „Weiter: Modus General“ → im General‑Modus fortfahren.
  3) Ohne Bestätigung keine Code‑Änderungen/startenden Läufe durchführen.
- Hinweise:
  - Das STOP‑Gate gilt nur für Code‑Aktionen; reine Redaktions-/Kanonarbeiten laufen ohne Unterbrechung weiter.
  - Du kannst das Gate jederzeit durch die Formulierung „Stop‑Gate aus (Session)“ deaktivieren und mit „Stop‑Gate an“ wieder aktivieren.

## Repositoryweiter Rahmen
- Gemeinsamer Code gehört nach `packages/novapolis_common`; doppelte Module aus den Teilprojekten nach Migration entfernen.
- Konfigurationen bleiben projektspezifisch; Produktions- und API-Code verbleibt im jeweiligen Projektordner, Utilities werden über das Shared-Package re-exportiert.
- Secrets (`.env`) bleiben lokal; ungefilterte Exporte ausschließlich unter `novapolis-rp/database-raw/99-exports/` ablegen.
- Working docs leben in `novapolis-dev/docs/` (todo, donelog, tests, naming-policy, copilot-behavior, index); `novapolis-rp/development/...` sind Redirect-Stubs.

## Prüf- und Release-Checks
- Vor Commits relevante Tests/Skripte ausführen (`novapolis_agent/scripts/run_tests.py`, Validatoren unter `novapolis-rp/coding/tools/validators/`).
- Bei Änderungen an Behaviour- oder Policy-Dokumenten zusätzlich `novapolis_agent/tests/test_content_policy_profiles.py` und Changelogs prüfen.
- PLAN → DRY RUN → APPLY mit klaren Stop-Gates; vor APPLY nach `development/docs` Restreferenzen suchen (nur in Redirect-README und `meta.origin` erlaubt), danach Sidecars (`source`, `origin`, `migrated_at`) kontrollieren.
- Unsichere Anforderungen zuerst rückfragen; Minimal-Delta bewahren, transparente Diffs mit Dateiliste/Diffstat liefern, keine Shell-Kommandos oder History-Rewrites.

## Novapolis Agent (Backend)

### Arbeitskontext
- Repo: `novapolis_agent` (Branch `main`), Stack: FastAPI + Ollama, Kern: `app/main.py`, `app/api/models.py`, `app/core/settings.py`, `app/core/prompts.py`.

### Schnellziele bei Codeänderungen
- CI grün halten: Tests (`pytest`), Typen (Pyright/Mypy). CI prüft `docs/DONELOG.txt`.
- Nicht-triviale Änderungen → DONELOG via `scripts/append_done.py`.
- Nach jedem Edit Tests/Typen sequentiell ausführen und Ergebnisse abwarten (`pytest -q` → `pyright -p pyrightconfig.json` → `python -m mypy --config-file mypy.ini app scripts`). Keine Vorab-Statusmeldungen.

### PR-/Push-Checks
- Tests lokal: `pytest -q` oder passende Marker.
- Typechecks: `pyright -p pyrightconfig.json`, `python -m mypy --config-file mypy.ini app scripts`; optional Task „Tests: coverage (fail-under 80%)“.
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

### Markdownlint (zentral)

- Zentrale Konfiguration: `.markdownlint-cli2.jsonc` im Root.
  - MD003 = `consistent` (pro Datei einheitlicher Heading‑Stil; gemischte ATX/Setext in derselben Datei → FAIL). Empfehlung: ATX verwenden und Inhalte vereinheitlichen.
  - `ignores` in der CLI2‑Config decken generierte/kuratierte Bereiche ab (u. a. `novapolis_agent/eval/results/**`, `novapolis_agent/outputs/**`, `outputs/**`, `novapolis-rp/.pytest_cache/**`).
- Lokaler Lauf (nur im bestehenden Terminal): `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc "**/*.md"`.
- Auto‑Fix optional: `npx --yes markdownlint-cli2-fix --config .markdownlint-cli2.jsonc "**/*.md"`.
- Wrapper/Tasks: Entfernt bzw. als Hinweis‑Stub belassen (`novapolis-rp/coding/tools/validators/run_lint_markdown.ps1`).

### Mirrors/Redirect‑Stubs

- Unter `novapolis-rp/Main/novapolis-dev/docs/` liegen nur noch Redirect‑Stubs; Single Source of Truth ist `novapolis-dev/docs/**`.
- Änderungen an Arbeitsregeln/Dokumentation ausschließlich in den Live‑Quellen vornehmen; Stubs nicht bearbeiten.

**Export/Importer**
- Export: `coding/tools/chat-exporter/` (Auto-Scroll, Inaktivitäts-Stop, speicherschonend).
- Ingest: `coding/tools/curation/ingest_jsonl.py` (streamend, chunked, sanftes Cleaning).

**Ziele**
- Stabiles Gedächtnis (Admin: system-prompt/memory-bundle) und reibungsloser Szenenstart.
- Reproduzierbare, nachvollziehbare Schritte (Dokumentation & kleine Commits).
