---
stand: 2025-11-09 18:36
update: frontmatter INIT
checks: pending
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

