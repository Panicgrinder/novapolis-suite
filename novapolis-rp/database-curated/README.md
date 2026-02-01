---
stand: 2026-02-01 14:14
update: FinalGate-Records (staging) als Standard-Link/Pattern ergänzt.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-02-01 14:14); & .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis-rp\database-curated PASS (2026-02-01 14:14); npm --prefix novapolis-rp/coding/tools/validators run validate:rp PASS (2026-02-01 14:14)
---

Database Curated (Stub)
=======================
Workflow jetzt zentral dokumentiert im Hub: `novapolis-dev/docs/readme.hub.md` → "Curation Workflow".

Kurz:
- staging/: Aufbereitung & Review
- staging/*.finalgate.md: Promotion-Checkliste/Decision Records pro Export
- final/: Geplant für abgenommene Artefakte
- RAW bleibt in `database-raw/99-exports/`


