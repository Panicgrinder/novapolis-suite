---
stand: 2026-03-30 05:08
update: checks aktualisiert (Basis-Stabilisierung)
checks: snapshot-lock PASS; markdownlint PASS; frontmatter PASS; todo-index PASS; naming-policy PASS; path-portability PASS; logs-policy PASS; doc-freshness PASS; scan-links PASS; validate-rp PASS (2026-03-30 05:08)
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
