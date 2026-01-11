---
stand: 2026-01-11 03:44
update: checks aktualisiert (Basis-Stabilisierung)
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-01-11 03:44); & .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis-rp\coding\tools\validators\README.md novapolis-rp\coding\tools\metadata\README.md novapolis-rp\coding\tools\chat-exporter\README.md novapolis-rp\coding\tools\curation\README.md PASS (2026-01-11 03:44)
---

Validator-Suite (Stub)
======================
Ausführliche Beschreibung jetzt im Hub: `novapolis-dev/docs/readme.hub.md` → Abschnitt "Validator Tools".

Kurz:
- Validiert Schemata (`manifest`), Markdown-Konventionen & Cross-Refs.
- Behavior-Matrix Check (`behavior_matrix_check.py`).

Siehe Hub für Workflows, CI-Hinweise und Nutzung.


