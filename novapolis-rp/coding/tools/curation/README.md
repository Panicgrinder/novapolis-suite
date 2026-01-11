---
stand: 2026-01-11 03:44
update: checks aktualisiert (Basis-Stabilisierung)
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-01-11 03:44); & .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis-rp\coding\tools\validators\README.md novapolis-rp\coding\tools\metadata\README.md novapolis-rp\coding\tools\chat-exporter\README.md novapolis-rp\coding\tools\curation\README.md PASS (2026-01-11 03:44)
---

Curation Tools (RP)
==================

Kurz-Einstieg in die Kurations-Tools für `novapolis-rp`.

Ziele
-----

- Rohdaten (RAW) ingestieren und in bearbeitbare Chunks überführen.
- Chunks anhand SSOT-Canvases (`database-rp/`) taggen.
- Ergebnisse nach `database-curated/` schreiben (staging → reviewed → final).

Wichtige Pfade
--------------

- SSOT (RP): `novapolis-rp/database-rp/`
- RAW (ungefiltert): `novapolis-rp/database-raw/` (insb. `database-raw/99-exports/`)
- Curated: `novapolis-rp/database-curated/` (staging/reviewed/final)

Wichtige Skripte
----------------

- Ingest (JSONL): `novapolis-rp/coding/tools/curation/ingest_jsonl.py`
- Tagging (YAML/SSOT → Chunks): `novapolis-rp/coding/tools/curation/tag_chunks_from_yaml.py`

Policy
------

- Keine ungefilterten Exporte in `database-rp/` ablegen.
- Alle SSOT-Änderungen in `database-rp/` konsistent halten (Frontmatter/Links/Slugs).
