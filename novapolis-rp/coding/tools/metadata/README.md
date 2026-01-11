---
stand: 2026-01-11 03:44
update: checks aktualisiert (Basis-Stabilisierung)
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-01-11 03:44); & .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis-rp\coding\tools\validators\README.md novapolis-rp\coding\tools\metadata\README.md novapolis-rp\coding\tools\chat-exporter\README.md novapolis-rp\coding\tools\curation\README.md PASS (2026-01-11 03:44)
---

Metadata Tool (Stub)
====================
Details & JSON-Shape jetzt im Hub: `novapolis-dev/docs/readme.hub.md` → "Metadata Layer".

Kurz:
- Erzeugt Companion JSON neben Markdown (Struktur/Tags, kein Text-Eingriff).
- Dry-Run / Overwrite Flags.
- Siehe Hub für Beispiele & Integrationshinweise.


