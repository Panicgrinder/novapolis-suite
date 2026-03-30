---
stand: 2026-03-30 05:08
update: Phase-2-Konsistenzlauf zieht das Scripts-README auf aktuellen PASS-Kontext, PowerShell-Beispiele und Root-Wrapper.
checks: snapshot-lock PASS; markdownlint PASS; frontmatter PASS; todo-index PASS; naming-policy PASS; path-portability PASS; logs-policy PASS; doc-freshness PASS; scan-links PASS; validate-rp PASS (2026-03-30 05:08)
---
Novapolis Agent Evaluierungsskripte
===================================

Dieses Verzeichnis enthält Skripte zum Testen und Evaluieren des Novapolis Agents.

Skripte
-------

### run_eval.py

Ein Skript zur automatisierten Evaluierung des Chat-Endpunkts:

```powershell
& .\.venv\Scripts\python.exe novapolis_agent\scripts\run_eval.py [prompts_datei] [api_url]
```

Parameter:

- `prompts_datei`: Pfad zur JSON/JSONL-Datei mit Testfällen (Standard: `eval/datasets/eval-*.json`)
- `api_url`: URL des Chat-Endpunkts (Standard: `http://localhost:8000/chat`)

Hinweis: Für OpenAI-Finetuning steht `openai_finetune.py` bereit.

Beispiel:

- OpenAI FT: `openai_finetune.py`
  - Voraussetzungen: `& .\.venv\Scripts\python.exe -m pip install openai`; `OPENAI_API_KEY` gesetzt
  - Datensätze: openai_chat `*_train.jsonl` und `*_val.jsonl`
  - Aufruf: `& .\.venv\Scripts\python.exe novapolis_agent\scripts\openai_finetune.py novapolis_agent\eval\datasets\xxx_train.jsonl novapolis_agent\eval\datasets\xxx_val.jsonl --model gpt-4o-mini`

```powershell
& .\.venv\Scripts\python.exe novapolis_agent\scripts\run_eval.py --packages novapolis_agent\eval\datasets\eval-*.json http://127.0.0.1:8000/chat
```

### Abhängigkeiten

Das Skript benötigt die folgenden Python-Pakete:

- httpx
- rich

Installation:

```powershell
& .\.venv\Scripts\python.exe -m pip install httpx rich
```

