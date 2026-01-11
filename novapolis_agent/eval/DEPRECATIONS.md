---
stand: 2026-01-11 03:44
update: checks aktualisiert (Basis-Stabilisierung)
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-01-11 03:44); & .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis_agent\analysis_chat_routers.md novapolis_agent\scripts\README.md novapolis_agent\eval\README.md novapolis_agent\eval\DEPRECATIONS.md novapolis_agent\eval\config\context.notes\README.md PASS (2026-01-11 03:44)
---
Deprecations (Eval)
===================

- Datei `eval/eval-21-40_demo_v1.0.json` war ein Duplikat der Version unter `eval/datasets/` und wurde durch `eval/eval-21-40_fantasy_v1.0.*` ersetzt; Top-Level-Duplikate werden via Cleanup entfernt.
- Historische Pfade/Generatoren können zeitweise `eval/*.jsonl` erzeugen. Ergebnisse liegen dauerhaft unter `eval/results/` (gitignored).


