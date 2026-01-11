---
stand: 2026-01-11 03:44
update: checks aktualisiert (Basis-Stabilisierung)
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-01-11 03:44); & .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis-rp\coding\tools\validators\README.md novapolis-rp\coding\tools\metadata\README.md novapolis-rp\coding\tools\chat-exporter\README.md novapolis-rp\coding\tools\curation\README.md PASS (2026-01-11 03:44)
---

Chat-Exporter (Stub)
====================
Details nun im Hub: `novapolis-dev/docs/readme.hub.md` → "Export & Ingest".

Kurz:
- Browser Auto-Scroll Export, speicherschonend (Streaming/Chunks).
- Ziel immer `database-raw/99-exports/`.
- Curation/Ingest danach - siehe Hub.



