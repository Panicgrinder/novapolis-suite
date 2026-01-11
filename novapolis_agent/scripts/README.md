---
stand: 2026-01-11 03:44
update: checks aktualisiert (Basis-Stabilisierung)
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-01-11 03:44); & .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis_agent\analysis_chat_routers.md novapolis_agent\scripts\README.md novapolis_agent\eval\README.md novapolis_agent\eval\DEPRECATIONS.md novapolis_agent\eval\config\context.notes\README.md PASS (2026-01-11 03:44)
---
Novapolis Agent Evaluierungsskripte
===================================

Dieses Verzeichnis enthält Skripte zum Testen und Evaluieren des Novapolis Agents.

Skripte
-------

### run_eval.py

Ein Skript zur automatisierten Evaluierung des Chat-Endpunkts:

```bash
python run_eval.py [prompts_datei] [api_url]
```

Parameter:

- `prompts_datei`: Pfad zur JSON/JSONL-Datei mit Testfällen (Standard: `eval/datasets/eval-*.json`)
- `api_url`: URL des Chat-Endpunkts (Standard: `http://localhost:8000/chat`)

Hinweis: Für OpenAI-Finetuning steht `openai_finetune.py` bereit.

Beispiel:

- OpenAI FT: `openai_finetune.py`
  - Voraussetzungen: `pip install openai`; `OPENAI_API_KEY` gesetzt
  - Datensätze: openai_chat `*_train.jsonl` und `*_val.jsonl`
  - Aufruf: `python scripts/openai_finetune.py eval/datasets/xxx_train.jsonl eval/datasets/xxx_val.jsonl --model gpt-4o-mini`

```bash
python scripts/run_eval.py --packages eval/datasets/eval-*.json http://localhost:8000/chat
```

### Abhängigkeiten

Das Skript benötigt die folgenden Python-Pakete:

- httpx
- rich

Installation:

```bash
pip install httpx rich
```

