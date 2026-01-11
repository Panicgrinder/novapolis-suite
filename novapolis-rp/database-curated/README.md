---
stand: 2026-01-11 03:44
update: checks aktualisiert (Basis-Stabilisierung)
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-01-11 03:44); & .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis-rp\database-curated\README.md novapolis-rp\database-curated\final\README.md PASS (2026-01-11 03:44)
---

Database Curated (Stub)
=======================
Workflow jetzt zentral dokumentiert im Hub: `novapolis-dev/docs/readme.hub.md` → "Curation Workflow".

Kurz:
- staging/: Aufbereitung & Review
- final/: Geplant für abgenommene Artefakte
- RAW bleibt in `database-raw/99-exports/`


