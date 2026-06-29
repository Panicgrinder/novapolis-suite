---
stand: 2026-06-29 16:07
update: README trennt jetzt den belegten Python-Interpreter, Standard-Chat, Support-A-B und Judge-Pfad sauber in einer operativen Profilmatrix.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp/results/reports/checks_report_20260629_155310.md; snapshot-lock PASS (2026-06-29 16:07)
---

Novapolis Agent
===============

Ein FastAPI-Backend für einen Conversational Agent innerhalb der Novapolis Suite, der Ollama als LLM-Runtime verwendet.
Der Agent tritt unter dem Namen "Chronistin von Novapolis" auf.

Lokale Runtime-Baseline (2026-04-06): `Ollama + qwen2.5:7b` ist das bevorzugte Standardprofil fuer 8-GB-VRAM-Systeme. `llama3.1:8b` bleibt ein moeglicher Vergleichs- oder Fallback-Kandidat, ist aber nicht mehr der Default.

Ist-Stand (Betriebsfaehigkeit)
------------------------------

- Runtime-Betrieb erfolgt stabil über `.venv` und `app.main` (FastAPI).
- Belegter Workspace-Interpreter fuer den aktuellen Gate-Stand ist die Root-`.venv` mit Python 3.12.x; der zuletzt dokumentierte gruene Sammellauf lief mit Python 3.12.10. Solange kein eigener Migrationslauf dokumentiert ist, bleibt diese 3.12.x-Umgebung der reproduzierbare Referenzpfad fuer Tests, Typen und Sammelchecks.
- Betriebsname: "Chronistin von Novapolis".
- Qualitaetsgates sind in Reihenfolge `Lint -> Typen -> Tests -> Coverage` dokumentiert und lauffaehig.
- TTS-Runtime ist produktiv über `coqui`: API, Auth, Rate-Limit, Cache und Provider-Abstraktion sind aktiv; `coqui` erzeugt reale Artefakte (`status=ok`, `artifact_path`), `ollama`/`openai` bleiben Adapter-Scaffolds.
- `quality_de` ist operativ: dedizierte Suite auf Core/Drift/Canary (10/10/6), dokumentierter Laufstand bis `20/20` inkl. 3-facher Wiederholung zur Reproduzierbarkeit.
- Operatives Runbook: `novapolis_agent/docs/runbook.md`.

Profilmatrix (Chat/Runtime)
---------------------------

| Pfad | Zweck | Standardmodell(e) | Hinweis |
| --- | --- | --- | --- |
| Standard-Chat | allgemeiner Produkt- und API-Betrieb | `qwen2.5:7b` | aktuelle lokale Runtime-Baseline fuer 8-GB-VRAM-Systeme |
| Support A/B | neutrale Support-Antworten ueber `profile_id=support_de_ab` | `llama3.1:8b`, `qwen3.5:4b` | heuristische Kandidatenwertung, optional mit Modell-Judge |
| Support-Judge | opt-in Tie-Break oder erzwungene Zweitentscheidung | typischerweise `qwen2.5:7b` | nur wenn `support_judge_model` gesetzt ist |
| Vergleich/Fallback | manueller oder operativer Vergleichspfad | `llama3.1:8b` | nicht die Default-Baseline des Standard-Chats |

VS Code Task-Labels (Datensatz & Training)
------------------------------------------

- `Data: curate from latest (train pack)`
- `Data: export+pack (latest results)`
- `Eval: session promotions review (10, asgi)`
- `Data: export+pack (session promotions review)`
- `Train: baseline LoRA (tiny-gpt2, 1-step)`

Hinweis: Diese Labels sind bewusst identisch in `novapolis-dev/docs/todo.agent-board.md` und `novapolis_agent/docs/runbook.md` gehalten, um Doku-Drift zu vermeiden.

Release-Gate-Hinweis:

- `Data: export+pack (latest results)` und `Train: baseline LoRA (tiny-gpt2, 1-step)` laufen jetzt beide ueber `novapolis_agent/scripts/training_release_gate.py`.
- Der Guard blockiert hart, wenn `validate_eval_datasets --strict`, ein grüner `rp_content`-Beleg oder die notwendige Dataset-Provenienz fehlen.

Lizenz
------

Dieses Projekt steht unter der MIT-Lizenz. Siehe die Datei `LICENSE` im Repository-Wurzelverzeichnis.

Neuigkeiten (2025-10-20)
------------------------

- Demo→Fantasy: Datensatz-Bezeichnungen vereinheitlicht (`eval-21-40_fantasy_v1.0.*`).
   Maßgeblich sind die Dateien unter `novapolis_agent/eval/datasets/`.
- Reports: Drei Skripte erzeugen reproduzierbare Berichte unter
   `novapolis_agent/eval/results/reports/<topic>/<timestamp>/`:
   - `scripts/reports/generate_dependencies_report.py`
   - `scripts/reports/generate_coverage_report.py`
   - `scripts/reports/generate_consistency_report.py`
- CI: Ein Workflow erzeugt die Reports automatisch bei Push und lädt sie als
   Artefakte hoch.
- Legacy-Bereinigung: Unbenutzte Legacy-Endpunkte unter `app/api/endpoints/`
   entfernt; doppelte Exporte in `app/services/__init__.py` bereinigt.

Repository-Info
---------------

- Standard-Branch: `main`
- Optional: Zusätzliche Pyright-Konfig für Skripte: `pyrightconfig.scripts.json`

Einrichtung
----------

1. Fuer reproduzierbare Checks und lokale Nachstellung die aktuell verifizierte Root-`.venv` mit Python 3.12.x verwenden; der zuletzt belegte gruene Sammellauf lief mit Python 3.12.10.
2. Im Repo-Root die Root-`.venv` aktivieren:

```powershell
& .\.venv\Scripts\activate
```

3. Abhängigkeiten installieren (eine der beiden Varianten):

- Aus dem Repo-Root (empfohlen, bündelt alles):

```powershell
& .\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

- Direkt im Modul `novapolis_agent` (granular):

```powershell
# Basis-Laufzeit
& .\.venv\Scripts\python.exe -m pip install -r novapolis_agent\requirements\base.txt
# Dev-Extras (Tests, Lint)
& .\.venv\Scripts\python.exe -m pip install -r novapolis_agent\requirements\dev.txt
# Optional: Trainings-Extras
& .\.venv\Scripts\python.exe -m pip install -r novapolis_agent\requirements\train.txt
# Optional: CLI-Tools (OpenAI/Rich/PDF)
& .\.venv\Scripts\python.exe -m pip install -r novapolis_agent\requirements\optional-tools.txt
```

Abhaengigkeitsprofile (kanonisch)
---------------------------------

- `runtime`: `requirements/base.txt` (API-Betrieb)
- `dev`: `requirements/dev.txt` (Tests/Typen/Lint)
- `train`: `requirements/train.txt` (LoRA/Training)
- `optional-tools`: `requirements/optional-tools.txt` (nur Spezial-CLIs, z. B. OpenAI-FT-Status, Rich-CLI-Output, PDF-Extraction)

Profil-Check (leichtgewichtig):

```powershell
& .\.venv\Scripts\python.exe novapolis_agent\scripts\check_dependency_profiles.py
```

Oder manuell im Repo-Root:

```powershell
& .\.venv\Scripts\python.exe -m pip install fastapi uvicorn httpx python-dotenv
```

4. Ollama installieren und starten:

```text
Windows-Installer: https://ollama.com/download/windows
Nach der Installation: ollama serve
```

5. LLM-Modell herunterladen:

```powershell
   ollama pull qwen2.5:7b
   ```

Anwendung starten
-----------------

```powershell
& .\.venv\Scripts\python.exe -m uvicorn novapolis_agent.app.main:app --reload
```

API-Endpunkte
-------------

- `GET /`: Basis-Endpunkt für Gesundheitsprüfung
- `POST /chat`: Chat-Endpunkt zum Senden von Nachrichten an das LLM

### Chat-Endpunkt verwenden

```text
curl -X POST http://127.0.0.1:8000/chat -H "Content-Type: application/json" -d "{\"messages\":[{\"role\":\"user\",\"content\":\"Du bist die Chronistin von Novapolis. Stell dich kurz vor.\"}]}"
```

Oder mit PowerShell:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/chat" -Method Post -Body '{"messages":[{"role":"user","content":"Du bist die Chronistin von Novapolis. Stell dich kurz vor."}]}' -ContentType "application/json"
```

Swagger-Dokumentation
---------------------

Zugriff auf die API-Dokumentation unter:

```text
http://127.0.0.1:8000/docs
```

Simulation API
--------------

Eine kompakte Simulation steckt in `app/api/sim.py` und stellt einen stetig
fortschreibbaren Weltzustand bereit. Die Endpunkte dienen als leichtgewichtige
Quelle für Visualisierungen oder externe Clients.

### Endpunkte

- `GET /world/state` - liefert `{tick, time, regions, actors, events}` als aktuellen Snapshot.
- `POST /world/step` - erwartet `{dt: float}`, erhöht Tick sowie Zeit und gibt den aktualisierten Zustand zurück.

Der Server liest `AGENT_PORT` (Standard `8765`) aus der Umgebung.

### Start (Windows PowerShell)

1. `.env.example` nach `.env` kopieren oder `AGENT_PORT` manuell setzen.
2. Server direkt starten:

```powershell
$port = $env:AGENT_PORT
if (-not $port) { $port = 8765 }
& .\.venv\Scripts\python.exe -m uvicorn novapolis_agent.app.api.sim:app --host 127.0.0.1 --port $port --reload
```

3. Probeaufruf:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:$port/world/state" -Method Get
```

### Start (Dev Container)

1. Dev-Container öffnen (`Reopen in Container`).
2. Post-Create installiert `requirements.txt` und `requirements-dev.txt` automatisch.
3. Im Dev-Container denselben Uvicorn-Aufruf nutzen; der Port 8765 wird an den Host weitergeleitet.

Einstellungen/Umgebung
----------------------

Konfiguration per `.env` (siehe Beispiele in `app/core/settings.py`). Wichtige Felder:

Hinweis: Bei aktiviertem Rate Limiting wird pro IP innerhalb eines 60s-Fensters begrenzt (in-memory, best-effort).

Empfohlene lokale Modellbasis:

- Runtime: `Ollama`
- Baseline-Modell (Standard-Chat): `qwen2.5:7b`
- Support-A-B-Kandidaten: `llama3.1:8b`, `qwen3.5:4b`
- Typischer Judge fuer Support-A-B: `qwen2.5:7b`
- Vergleich/Fallback ausserhalb des Standard-Chats: `llama3.1:8b`

### Konfigurationsvertrag (Masterplan Schritt 2)

- Vertragsversion: `CONFIG_CONTRACT_VERSION=2026-02-23`
- Pflichtwerte fuer Runtime: `OLLAMA_HOST`, `MODEL_NAME`
- Optionale Runtime-Werte: `BACKEND_CORS_ORIGINS`, `REQUEST_TIMEOUT`, `REQUEST_MAX_INPUT_CHARS`, `REQUEST_MAX_TOKENS`, `RATE_LIMIT_*`
- Safe-Fallbacks bei ungueltigen numerischen Werten (z. B. `REQUEST_TIMEOUT<=0`) greifen automatisch auf konservative Defaults zurueck.
- Keine stillen Ausfaelle: Korrekturen werden in `SETTINGS_CONTRACT_ISSUES` gesammelt.
- Strikter Modus: `STRICT_CONFIG=true` erzwingt Fehler statt Fallback, wenn der Vertrag verletzt wird.

### LLM-Optionen (Ollama) - Defaults & Overrides

Der Agent unterstützt eine Reihe von Sampling-/Decoding-Optionen. Defaults sind zentral in `app/core/settings.py` hinterlegt und können via `.env` überschrieben werden. Pro Request lassen sich Optionen in `ChatRequest.options` setzen; diese überschreiben die Defaults.

Unterstützte Optionen (Auswahl):

- Temperatur/Sampling: `temperature`, `top_p`, `top_k`, `min_p`, `typical_p`, `tfs_z`
- Länge/Kontext: `num_predict` (Alias: `max_tokens`), `num_ctx`
- Penalties: `repeat_penalty`, `repeat_last_n`, `presence_penalty`, `frequency_penalty`, `penalize_newline`
- Steuerung/Seed: `seed`, `stop` (String oder Liste), `host` (Ollama Base-URL)
- Mirostat: `mirostat` (0/1/2), `mirostat_tau`, `mirostat_eta`

Zentrale Defaults (aus Settings; Beispielwerte):

```ini
TEMPERATURE=0.7
TOP_P=0.9
TOP_K=40
MIN_P=0.0
TYPICAL_P=1.0
TFS_Z=1.0
MIROSTAT=0
MIROSTAT_TAU=5.0
MIROSTAT_ETA=0.1
PENALIZE_NEWLINE=false
REPEAT_PENALTY=1.1
REPEAT_LAST_N=64
REQUEST_MAX_TOKENS=512
# Optional: NUM_CTX_DEFAULT (wenn gesetzt, wird übernommen)
# NUM_CTX_DEFAULT=4096
```

Hinweise:

- `eval_mode` deckelt `temperature` automatisch auf maximal 0.25.
- `stop` akzeptiert entweder eine Liste von Strings oder einen einzelnen String (wird intern zu einer Liste gewandelt).
- Wertebereiche werden konservativ geprüft/geklammert (z. B. `top_p`, `min_p`, `typical_p`, `tfs_z` in [0,1]; `mirostat` ∈ {0,1,2}).

### Policies aktivieren (optional)

Die Inhalts-Policies sind standardmäßig aus. Zur Aktivierung in `.env` oder Umgebungsvariablen setzen:

```ini
POLICIES_ENABLED=true
POLICY_FILE="novapolis_agent/eval/config/policy.sample.json"
# Im "unrestricted"-Modus strikt alle Policies umgehen:
POLICY_STRICT_UNRESTRICTED_BYPASS=true
```

Hinweise:

- Policy-Datei kann „default“ und „profiles“ enthalten. Merge-Reihenfolge: `default` → `profiles[profile_id]`;
   `forbidden_terms` werden vereinigt, `rewrite_map` überlagert die Schlüssel.
- `mode=eval` mappt implizit auf `profile_id="eval"`.
- Details und Tests siehe `../.github/copilot-instructions.md` und `tests/test_content_policy_profiles.py`.

Optionale CLI-Tools
-------------------

Für erweiterte Workflows stehen optionale Skripte zur Verfügung (nicht Teil des API-Pflichtpfads):

- `scripts/customize_prompts.py` - Prompts/Policies/Profiles zusammenstellen; Export in Dateien
- `scripts/estimate_tokens.py` - Grobe Token-/Längenabschätzung für Eingaben
- `scripts/open_context_notes.py` - Kontextnotizen aus `settings` öffnen (lokal)
- `scripts/audit_workspace.py` - Konsistenz-/Altlasten-Scan; Hinweise und Pfadprüfungen
- `scripts/openai_finetune.py` - OpenAI-kompatible Finetune-Packs validieren/Triggern
- `scripts/openai_ft_status.py` - Finetune-Status abfragen
- `scripts/train_lora.py` - LoRA-Miniläufe (TinyLlama etc.)
- `scripts/fine_tune_pipeline.py` - End-to-End Pipeline (Export→Prepare→Train)

Tipps:

- Viele Schritte sind als VS Code Tasks vorhanden (Suche nach „Finetune“, „Eval“, „Summary“).
- Alle Skripte akzeptieren `--help` mit Kurzbeschreibung und Argumenten.

Templates (knowledge/actions)
-----------------------------

- Beispielvorlage fuer Agent-Konfigurationen: `novapolis_agent/docs/templates/knowledge-actions.example.yaml`.
- Fachliche Leitplanken zum TTS-Track: `novapolis_agent/docs/tts-model-track.md`.

Lokales RAG (optional)
----------------------

Der Agent kann optional Kontext-Snippets aus einem lokalen Text-Korpus (Markdown/TXT) via leichtgewichtigem TF-IDF-Retriever injizieren.

- Flags (in `.env` oder als Umgebungsvariablen):
   - `RAG_ENABLED=true` - RAG aktivieren
   - `RAG_INDEX_PATH=novapolis_agent/eval/results/rag/index.json` - Pfad zur Index-Datei
   - `RAG_TOP_K=3` - Anzahl der Snippets

- Indexer-CLI: `scripts/rag_indexer.py`
   - Baut einen JSON-Index über `.md`/`.txt` Dateien (nicht rekursiv für Ordner-Top-Level)
   - Beispiel (PowerShell):

```powershell
& .\.venv\Scripts\python.exe novapolis_agent\scripts\rag_indexer.py --input novapolis_agent\docs novapolis_agent\eval\config --out novapolis_agent\eval\results\rag\index.json
```

- Verwendung im Server:
   - Server liest `RAG_INDEX_PATH` beim Request ein (best-effort). Wenn der Index fehlt, läuft der Chat normal weiter (fail-open).
   - Snippets werden als zusätzliche System-Nachricht `[RAG]` injiziert.

- Task-Hinweise:
   - Es gibt aktuell keinen dedizierten VS Code Task für den Indexer; der obige Aufruf funktioniert plattformneutral über den aktiven Interpreter.
   - Optional kann ein eigener Task ergänzt werden, der `scripts/rag_indexer.py` mit gewünschten `--input`/`--out` Werten ausführt.

Datenmodelle (Quelle)
---------------------

Die zentralen Pydantic-Modelle für Requests/Responses liegen in `app/api/models.py`.
Historische `app/schemas.py` wurde entfernt. Bitte nur `app/api/models.py` importieren.

Workspace-Zusammenfassung
--------------------------

- Neueste Gesamt-Zusammenfassung (LLM+Heuristik):
   - novapolis_agent/eval/results/summaries/summary_ALL_20250824_0306_MIXED.md

Datensatz-Kurierung (3-7 Tage)
------------------------------

Aus Eval-Ergebnissen Trainingspakete erzeugen:

- Skript: `scripts/curate_dataset_from_latest.py`
- Ablauf: nimmt die neueste `results_*.jsonl`, exportiert in `openai_chat` oder `alpaca`, erzeugt deduplizierte Train/Val-Dateien.
- Zusatz fuer getrennte Review-Pfade: ueber `--results-glob` kann die Kandidatenauswahl gezielt auf einen getaggten Results-Strom wie `results_*_session_promotions*.jsonl` eingegrenzt werden.
- Ausgabe liegt unter `novapolis_agent/eval/results/finetune/`.

Finetune workflow
-----------------

Schneller Export und Vorbereitung von Trainingspaketen auf Basis der neuesten
Evaluations-Ergebnisse (`novapolis_agent/eval/results/results_*.jsonl`). Zwei VS Code Tasks sind vorhanden:

- Finetune: export (latest)
   - Ermittelt die neueste `results_*.jsonl` und exportiert nach OpenAI-Chat-Format.
   - Ausgabe: `${workspaceFolder}/novapolis_agent/eval/results/finetune/exports/openai_chat.jsonl`
   - OS-spezifisch (Windows PowerShell vs. Linux/macOS Bash) hinterlegt.

- Finetune: prepare (split)
   - Erzeugt deduplizierte Splits:
   - Train: `${workspaceFolder}/novapolis_agent/eval/results/finetune/train.jsonl`
   - Val: `${workspaceFolder}/novapolis_agent/eval/results/finetune/val.jsonl`
   - Schwellwert für Near-Duplicates: `0.92`

Akzeptanz: Das Ausführen beider Tasks erzeugt valide JSONL-Dateien für Train/Val ohne JSON-Fehler.

Fine-Tuning / LoRA Mini-Pipeline (3-7 Tage)
------------------------------------------

- Skript: `scripts/fine_tune_pipeline.py`
- Voraussetzungen: passende PyTorch-Installation und optionale Pakete aus `requirements-train.txt`.
- Beispiel (CPU/GPU abhängig):
   - python scripts/fine_tune_pipeline.py \
   --finetune-dir novapolis_agent/eval/results/finetune \
      --epochs 1 \
      --per-device-train-batch-size 1 \
      --bf16

Eval: Synonyme mit privatem Overlay
----------------------------------

Für die Keyword-Checks in der Evaluierung können Synonyme aus `novapolis_agent/eval/config/synonyms.json` geladen werden.
Zusätzlich können lokale, private Ergänzungen in
`novapolis_agent/eval/config/synonyms.local.json` abgelegt werden.
Diese Datei ist git-ignoriert und wird automatisch mit der Basisdatei gemerged.

- Beispiel: `novapolis_agent/eval/config/synonyms.local.sample.json` kopieren zu `synonyms.local.json` und anpassen.

Eval-Suites (neutral vs rpg)
----------------------------

Zur sauberen Trennung der Zielverhalten sind zwei Suiten definiert:

- `neutral`: neutral-assistive Evaluierung (kein RPG-Fokus), Profil `eval`.
- `rpg`: szenisch/rollenspielorientierte Evaluierung, Profil `unrestricted`.

Suite-Quelle:

- `novapolis_agent/eval/config/suites.json`

VS-Code-Tasks:

- `Eval: suite neutral (20, asgi)`
- `Eval: suite rpg (20, asgi)`

Check-Matrix:

- `neutral` nutzt den `rpg_style`-Check, um RPG-Drift sichtbar zu machen.
- `rpg` läuft ohne `rpg_style`, damit rollenspielnahe Antworten nicht am neutralen Stilkriterium scheitern.

Dataset-Metadaten:

- Eval-Datasets unterstuetzen `tags` und `slug`.
- Wenn `id` fehlt, wird sie aus `slug` abgeleitet (`eval-<slug>`).
- Neben JSON/JSONL sind auch YAML-Dateien (`.yaml`/`.yml`) fuer Eval-Datasets moeglich.

Validierung:

- Task: `Eval: validate datasets (slug+tags)`
- Task: `Eval: validate suite datasets (strict)`
- CLI: `.\.venv\Scripts\python.exe novapolis_agent\scripts\validate_eval_datasets.py`
- Strict nur fuer Suiten: `.\.venv\Scripts\python.exe novapolis_agent\scripts\validate_eval_datasets.py --strict --suite-config novapolis_agent/eval/config/suites.json --suite neutral --suite rpg`
- `combined_*`-Dateien gelten als aggregierte Artefakte und sind bei Duplicate-Pruefungen erlaubt.

Manuell (Beispiel neutral):

```powershell
.\.venv\Scripts\python.exe -m scripts.agent.run_eval --asgi --profile eval --limit 20 --quiet --packages novapolis_agent/eval/datasets/neutral/neutral_01_20_core.v1.jsonl --packages novapolis_agent/eval/datasets/neutral/neutral_81_100_tech.v1.jsonl --packages novapolis_agent/eval/datasets/neutral/neutral_gpt_samples.de.v1.jsonl --packages novapolis_agent/eval/datasets/neutral/neutral_smoke.v1.jsonl
```

Lokale Kontext-Notizen (optional)
----------------------------------

Der Server kann optionale, lokale Kontext-Notizen als zusätzliche
System-Nachricht injizieren. Das ist nützlich für projektspezifisches Wissen
oder interne Begriffe.

- Beispieldatei: `novapolis_agent/eval/config/context.local.sample.md` → kopieren zu `context.local.md` und Inhalte ergänzen.
- Aktivierung via Settings/ENV:
   - `CONTEXT_NOTES_ENABLED=true`
   - Optional Pfade anpassen:
      `CONTEXT_NOTES_PATHS=["novapolis_agent/eval/config/context.local.md", "novapolis_agent/eval/config/context.local.jsonl", ...]`
   - Optional Größe begrenzen: `CONTEXT_NOTES_MAX_CHARS=4000`
- Die Notizen werden als zweite System-Nachricht eingefügt (nach dem gewählten
   System-Prompt), sowohl im normalen als auch im Streaming-Endpunkt.
- Fehlende Overlay-Datei wird stillschweigend ignoriert.

Eval-Style-Guard (Post-Hook im eval_mode)
----------------------------------------

Der Streaming-Post-Hook normalisiert im `eval_mode` die finale
Assistenten-Antwort heuristisch: neutral, kurz, ohne Rollenspiel/Emoji/
Storytelling. Die Normalisierung greift nur, wenn `eval_mode` aktiv ist und
kann über Settings deaktiviert werden. Der umgeschriebene Text wird in der
Sitzungshistorie persistiert.

- Flags in `app/core/settings.py` (auch per ENV setzbar):
   - `EVAL_POST_REWRITE_ENABLED` (default: `True`)
   - `EVAL_POST_MAX_SENTENCES` (default: `2`)
   - `EVAL_POST_MAX_CHARS` (default: `240`)
   - Heuristiken: Neutralisierung und Kompaktierung
      (Pronomen/Rollenspiel/Emojis/! entfernen, Duplikate/Punktuation
      normalisieren)

- Beispiel: SSE-Tail beim Streaming (eval_mode)

```text
   event: delta
   data: {"text":"..."}
   event: meta
   data: {"policy_post":"rewritten","request_id":"<RID>","delta_len":42}
   event: done
   ```

- Eval-Runner Preset: `--profile eval`
   - Setzt konservative Sampling-Defaults (nur wenn nicht manuell
      überschrieben):
      - `temperature=0.2`, `top_p=0.1`, `max_tokens=128`
   - Checks lassen sich fokussieren, z. B.:
      `--checks rpg_style,term_inclusion`
   - Ruhige Ausgabe: `--quiet`

### Schnelle Rezepte (copy/paste)

- CHAI (ASGI, eval-Profil, fokussierte Checks):

```powershell
& .\.venv\Scripts\python.exe -m scripts.agent.run_eval --asgi --packages novapolis_agent/eval/datasets/chai-ai_small_v1.jsonl --profile eval --checks rpg_style,term_inclusion --quiet
```

- Combined 001-100 (ASGI, eval-Profil, fokussierte Checks):

```powershell
& .\.venv\Scripts\python.exe -m scripts.agent.run_eval --asgi --packages novapolis_agent/eval/datasets/combined_eval_001-100.jsonl --profile eval --checks rpg_style,term_inclusion --quiet
```

Copilot @workspace / #codebase (Code-Suche)
-------------------------------------------

- Empfehlung: Remote-Index nutzen (Repo liegt auf GitHub). Lokaler Index dient als Fallback.
- Push regelmäßig, damit der Remote-Index aktuell bleibt.
- Nutzung in Prompts: `@workspace` oder `#codebase` hinzufügen, optional Code markieren/auswählen.
- Status und Index-Build über die Copilot-Statusleiste; bei Bedarf "Build Remote Workspace Index" ausführen.



