---
stand: 2026-02-27 06:06
update: Datensatz-/Training-Tasklabels mit Board/README synchronisiert.
checks: npx --yes markdownlint-cli2 --config F:/VS-Code-Workspace/Main/.markdownlint-cli2.jsonc "F:/VS-Code-Workspace/Main/novapolis-dev/docs/todo.agent-board.md" "F:/VS-Code-Workspace/Main/novapolis-dev/docs/todo.index.md" "F:/VS-Code-Workspace/Main/novapolis-dev/docs/donelog.md" "F:/VS-Code-Workspace/Main/novapolis_agent/docs/DONELOG.txt" "F:/VS-Code-Workspace/Main/novapolis_agent/README.md" "F:/VS-Code-Workspace/Main/novapolis_agent/docs/runbook.md" PASS (2026-02-27 05:31); F:/VS-Code-Workspace/Main/.venv/Scripts/python.exe F:/VS-Code-Workspace/Main/scripts/check_frontmatter.py "F:/VS-Code-Workspace/Main/novapolis-dev/docs/todo.agent-board.md" "F:/VS-Code-Workspace/Main/novapolis-dev/docs/todo.index.md" "F:/VS-Code-Workspace/Main/novapolis-dev/docs/donelog.md" "F:/VS-Code-Workspace/Main/novapolis_agent/docs/DONELOG.txt" "F:/VS-Code-Workspace/Main/novapolis_agent/README.md" "F:/VS-Code-Workspace/Main/novapolis_agent/docs/runbook.md" PASS (EXITCODE=0, 2026-02-27 05:31)
---

Novapolis Agent Runbook (Ist-Stand)
===================================

Ziel
----

- Betriebsanleitung fuer lokalen Betrieb und Qualitaetsgates auf Basis des aktuell umgesetzten Stands.
- Keine Produktivzusagen ohne Evidenz; alle Aussagen orientieren sich an verifizierbaren Laufartefakten.

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

VS Code Task-Labels (Datensatz & Training)
------------------------------------------

- `Data: curate from latest (train pack)`
- `Data: export+pack (latest results)`
- `Train: baseline LoRA (tiny-gpt2, 1-step)`

TTS Runtime-Status (wahrheitsgetreu)
------------------------------------

- Endpunkte vorhanden: `/tts/health`, `/tts/voices`, `/tts/synthesize`, `/tts/cache/stats`, `/tts/cache/cleanup`.
- Produktiver Runtime-Provider aktiv: `coqui` (HTTP-Endpunktaufruf + lokaler Artefaktpfad bei erfolgreicher Synthese).
- Weitere Provider verbleiben als Adapter-Scaffolds: `ollama`, `openai`; Testanker: `dummy`, `null`.
- Fallback-Verhalten: bei nicht verfuegbarem Runtime-Provider liefert `/tts/synthesize` kontrolliert `503` (kein Silent-Fail).
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
.\.venv\Scripts\python.exe -m scripts.agent.run_eval --asgi --profile eval --limit 20 --quiet --packages novapolis_agent/eval/datasets/neutral/neutral_01_20_core.v1.jsonl --packages novapolis_agent/eval/datasets/neutral/neutral_81_100_tech.v1.jsonl --packages novapolis_agent/eval/datasets/neutral/neutral_smoke.v1.jsonl --packages novapolis_agent/eval/datasets/neutral/generated/neutral_101_300_generated.v1.jsonl
```

Direkte CLI-Variante (rpg):

```powershell
.\.venv\Scripts\python.exe -m scripts.agent.run_eval --asgi --profile unrestricted --limit 20 --quiet --packages novapolis_agent/eval/datasets/rpg/rpg_21_40_fantasy.v1.jsonl --packages novapolis_agent/eval/datasets/rpg/rpg_41_60_dialog.v1.jsonl --packages novapolis_agent/eval/datasets/rpg/rpg_61_80_szenen.v1.jsonl
```

Interpretation:

- `neutral` bewertet primär neutrale Hilfsantworten (rpg_style sollte niedrig sein).
- `rpg` bewertet rollenspielnahe/szenische Antworten; der Lauf ist nicht direkt mit neutralen Keyword-Anforderungen vergleichbar.
- Fuer die RPG-Suite ist `rpg_style` bewusst aus den Checks entfernt, damit kein neutraler Stil-Malus den RPG-Lauf verfälscht.

Quality-Track `quality_de` (operativ)
-------------------------------------

Ziel:

- Deutsches Antwortniveau als reproduzierbaren Zusatz-Gate im neutralen Eval-Betrieb fahren.
- `quality_de` ist ein Check-Alias und expandiert in `languagetool_quality` + `sts_relevance`.

Verpflichtung (Suite-Zuordnung):

- Suite `neutral`: enthält `quality_de` als verpflichtenden Check.
- Suite `quality_de`: dedizierte Qualitäts-Suite für fokussierte Läufe und Triage.

Schwellwerte und Begründung:

- `languagetool_quality`: PASS bei `issue_count <= 2` und `score >= 0.65`.
- `sts_relevance`: PASS bei `score >= 0.09`.
- Begründung: Die Schwellen sind absichtlich moderat gewählt, damit fachlich korrekte Kurzantworten nicht übermäßig blockiert werden, gleichzeitig aber klare Qualitäts-/Relevanz-Ausreißer zuverlässig sichtbar werden.

Tasks:

- `Eval: suite neutral (20, asgi)` (inkl. `quality_de`).
- `Eval: suite quality_de (20, asgi)` (fokussierter Qualitätslauf).

CLI-Beispiel (`quality_de`):

```powershell
.\.venv\Scripts\python.exe -m scripts.agent.run_eval --asgi --profile eval --limit 20 --quiet --tag quality_de --checks must_include,keywords_any,keywords_at_least,not_include,regex,quality_de --packages novapolis_agent/eval/datasets/neutral/neutral_01_20_core.v1.jsonl --packages novapolis_agent/eval/datasets/neutral/neutral_81_100_tech.v1.jsonl --packages novapolis_agent/eval/datasets/neutral/neutral_smoke.v1.jsonl
.\.venv\Scripts\python.exe -m scripts.agent.run_eval --asgi --profile eval --limit 20 --quiet --tag quality_de --checks must_include,keywords_any,keywords_at_least,not_include,regex,quality_de --packages novapolis_agent/eval/datasets/neutral/quality_de_core.v1.jsonl --packages novapolis_agent/eval/datasets/neutral/quality_de_drift.v1.jsonl --packages novapolis_agent/eval/datasets/neutral/quality_de_canary.v1.jsonl
```

Laufartefakte:

- Ergebnisse landen unter `novapolis_agent/eval/results/results_<timestamp>_quality_de*.jsonl`.
- Die erste Zeile (`_meta`) dokumentiert aktive Checks (`enabled_checks`) und Overrides als technische SSOT.
- Aktueller verifizierter Stand: `quality_de_round7b` mit `20/20` sowie drei Wiederholungsläufe (`quality_de_round7b_repeat1..3`) ebenfalls `20/20`.

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
