---
stand: 2026-02-23 15:53
update: Eval-Laufpfade auf neue Unterordnerpakete (`datasets/neutral`, `datasets/rpg`) umgestellt; ersetzte Altpakete in Quarantäne verschoben.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis_agent/docs/runbook.md' PASS (2026-02-23 15:23); .\.venv\Scripts\python.exe scripts/check_frontmatter.py 'novapolis_agent/docs/runbook.md' PASS (EXITCODE=0, 2026-02-23 15:23)
---

Novapolis Agent Runbook (Ist-Stand)
===================================

Ziel
----

- Betriebsanleitung fuer lokalen Betrieb und Qualitaetsgates auf Basis des aktuell umgesetzten Stands.
- Keine Produktivzusagen ohne Evidenz; TTS bleibt Runtime-seitig aktuell ein Contract-First-Placeholder.

Runtime-Start
-------------

1. Python-Umgebung aktivieren:

```powershell
.\.venv\Scripts\activate
```

2. API starten (Agent-Modul-CWD):

```powershell
Set-Location .\novapolis_agent
..\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

3. Health/Docs pruefen:

```text
http://127.0.0.1:8000/health
http://127.0.0.1:8000/docs
```

Qualitaetsgates (verbindliche Reihenfolge)
------------------------------------------

Im CWD `novapolis_agent`:

1. Lint:

```powershell
..\.venv\Scripts\python.exe -m ruff check .
..\.venv\Scripts\python.exe -m black --check .
```

2. Typen:

```powershell
..\.venv\Scripts\python.exe -m pyright -p pyrightconfig.json
..\.venv\Scripts\python.exe -m mypy --config-file mypy.ini app scripts
```

3. Tests:

```powershell
..\.venv\Scripts\python.exe -m pytest -q
```

4. Coverage (Repo-Root):

```powershell
Set-Location ..
.\.venv\Scripts\python.exe scripts/run_pytest_coverage.py --fail-under 80
```

TTS Runtime-Status (wahrheitsgetreu)
------------------------------------

- Endpunkte vorhanden: `/tts/health`, `/tts/voices`, `/tts/synthesize`, `/tts/cache/stats`, `/tts/cache/cleanup`.
- Provider-Abstraktion vorhanden: `dummy`, `null`, sowie Adapter-Scaffolds fuer `coqui`, `ollama`, `openai`.
- Aktuell keine echte Audio-Synthese-Engine verdrahtet; Antworten sind Contract-First/Placeholder.
- Sicherheit und Stabilitaet aktiv: TTS-Auth, TTS-Rate-Limit, TTS-Cache (TTL/Size/Cleanup/Telemetry).

TTS Build-Time-Exporter
-----------------------

- Entrypoint: `novapolis_agent/scripts/tts_export_coqui.py` (Wrapper auf `tts_coqui_export.py`).
- Beispielaufruf (`--dry-run`):

```powershell
.\.venv\Scripts\python.exe novapolis_agent\scripts\tts_export_coqui.py --input <pfad> --voice-map <pfad> --model-id <id> --dry-run
```

- Compliance-Gate aktiv: Model-Allowlist und lokale Lizenzkopie werden geprüft.

Eval-Betrieb (Suite-Trennung)
-----------------------------

Ziel: neutrale Assistenz-Evaluation und RPG-Evaluation getrennt fahren, damit Metriken nicht durch Moduskonflikte verfälscht werden.

Suite-Definition:

- `novapolis_agent/eval/config/suites.json`

Tasks:

- `Eval: suite neutral (20, asgi)`
- `Eval: suite rpg (20, asgi)`

Direkte CLI-Variante (neutral):

```powershell
.\.venv\Scripts\python.exe -m scripts.agent.run_eval --asgi --profile eval --limit 20 --quiet --packages novapolis_agent/eval/datasets/neutral/neutral_01_20_core.v1.jsonl --packages novapolis_agent/eval/datasets/neutral/neutral_81_100_tech.v1.jsonl --packages novapolis_agent/eval/datasets/neutral/neutral_gpt_samples.de.v1.jsonl --packages novapolis_agent/eval/datasets/neutral/neutral_smoke.v1.jsonl
```

Direkte CLI-Variante (rpg):

```powershell
.\.venv\Scripts\python.exe -m scripts.agent.run_eval --asgi --profile unrestricted --limit 20 --quiet --packages novapolis_agent/eval/datasets/rpg/rpg_21_40_fantasy.v1.jsonl --packages novapolis_agent/eval/datasets/rpg/rpg_41_60_dialog.v1.jsonl --packages novapolis_agent/eval/datasets/rpg/rpg_61_80_szenen.v1.jsonl
```

Interpretation:

- `neutral` bewertet primär neutrale Hilfsantworten (rpg_style sollte niedrig sein).
- `rpg` bewertet rollenspielnahe/szenische Antworten; der Lauf ist nicht direkt mit neutralen Keyword-Anforderungen vergleichbar.
- Fuer die RPG-Suite ist `rpg_style` bewusst aus den Checks entfernt, damit kein neutraler Stil-Malus den RPG-Lauf verfälscht.

Dataset-Metadaten (slug/tags, YAML)
-----------------------------------

- Eval-Datasets koennen jetzt neben JSON/JSONL auch YAML (`.yaml`, `.yml`) nutzen.
- Feld `slug` wird als stabiler Identifier unterstuetzt; fehlt `id`, wird `id` aus `slug` abgeleitet (`eval-<slug>`).
- Feld `tags` (Liste von Strings) wird fuer Routing-/Heuristik-Logik verwendet.

Validator-Gate:

- Task: `Eval: validate datasets (slug+tags)`
- Strikter Suite-Lauf (nur Pakete aus `suites.json`): `Eval: validate suite datasets (strict)`
- CLI:

```powershell
.\.venv\Scripts\python.exe novapolis_agent\scripts\validate_eval_datasets.py
```

Strict nur auf Suiten:

```powershell
.\.venv\Scripts\python.exe novapolis_agent\scripts\validate_eval_datasets.py --strict --suite-config novapolis_agent/eval/config/suites.json --suite neutral --suite rpg
```

Hinweis:

- Aggregierte Dateien wie `combined_*` sind im Validator als Duplicate-Allowlist hinterlegt und blockieren damit den allgemeinen Lauf nicht.
