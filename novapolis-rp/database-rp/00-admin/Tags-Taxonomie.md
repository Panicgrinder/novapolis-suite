---
stand: 2026-02-23 03:55
update: Frische-Review durchgeführt; Tag-SSOT und Startersets weiterhin gültig (kein Kanon-Delta).
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/00-admin/Tags-Taxonomie.md' PASS (2026-02-23 03:56); .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py 'novapolis-rp/database-rp/00-admin/Tags-Taxonomie.md' PASS (2026-02-23 03:56); npm --prefix novapolis-rp/coding/tools/validators run validate:rp PASS (2026-02-23 03:56)
slug: tags-taxonomie
category: Admin
schemaVersion: 1
language: de
status: active
owners: [admin-novapolis]
tags: [rp, taxonomy, tags, metadata]
relatedSlugs: [schema-header-templates, index-rules, process-workflow]
---

Tags-Taxonomie (SSOT)
=====================

Zweck
-----
- Verbindliche, zentrale Tag-Liste für `database-rp`.
- Einheitliche Semantik für Suchbarkeit, Filterung und Auswertung.
- Minimales Kernset, das bei Bedarf kontrolliert erweitert wird.

Regeln
------
- Tags sind lowercase und slug-like (`a-z`, `0-9`, `-`).
- Keine Synonyme parallel pflegen (`maintenance` statt `wartung`).
- Typ-Tags (z. B. `location`) und Kontext-Tags (z. B. `monitoring`) kombinieren.
- `status`-Felder in Frontmatter bleiben maßgeblich; Status-Tags ergänzen nur den Blickwinkel.

Gültige Tags (Kernset)
----------------------

Typ
---
- `location`
- `project`
- `character`
- `inventory`
- `scene`

Fraktion
--------
- `novapolis`
- `haendlerbund`
- `eisenkonklave`
- `arkologie-a1`
- `schienenbund`
- `schattenbund`
- `fluesterkollektiv`

Funktion/Kontext
----------------
- `base`
- `outpost`
- `hub`
- `anomaly`
- `monitoring`
- `logistics`
- `mission`
- `operations`
- `maintenance`
- `exploration`

Status-Perspektive (ergänzend)
------------------------------
- `active`
- `partial`
- `sealed`
- `restricted`

Startersets (empfohlen)
-----------------------

`category: location`
- Mindestset: `location`, `<fraktion>`
- Optional je Kontext: `base|outpost|hub`, `monitoring|operations|maintenance|exploration`
- Optional Statussicht: `active|partial|sealed|restricted`

`category: project`
- Mindestset: `project`, `<fraktion>`, `mission|logistics|operations`

`category: character`
- Mindestset: `character`, `<fraktion>`

Beispiel (aktuelle Hauptschauplätze)
------------------------------------
- D5: `location`, `novapolis`, `base`, `operations`, `maintenance`, `active`
- C6: `location`, `novapolis`, `outpost`, `monitoring`, `anomaly`, `restricted`, `active`, `partial`

Erweiterungspfad
----------------
- Neue Tags nur bei wiederholtem Bedarf (mind. 2 betroffene Dateien) aufnehmen.
- Neue Tags zuerst hier eintragen, danach erst in Canvas-Dateien verwenden.
