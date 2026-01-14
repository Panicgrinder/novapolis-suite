---
stand: 2026-01-12 12:02
update: "Schema-Gate: title ergaenzt; MD025-Override (Frontmatter-title + H1)."
checks: npm --prefix novapolis-rp\coding\tools\validators run validate:rp PASS (2026-01-12 12:01); npm --prefix novapolis-rp\coding\tools\validators run validate:crossrefs PASS (2026-01-12 12:01); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/01-factions/novapolis/04-inventory/C6-inventar.md' PASS (2026-01-12 12:02); & .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis-rp\database-rp PASS (2026-01-12 12:02)
title: Inventar - C6
last_updated: 2026-01-11T07:14:00+01:00
category: inventory
slug: c6-inventar
owner: novapolis
scope: location
location: c6
version: "0.1"
tags: []
---

<!-- markdownlint-disable MD025 -->

C6 - Inventar
=============

Bestände (verbucht)
-------------------
- tbd

Potenziale
----------
- tbd

Fehlend / Offen
---------------
- tbd

Aktionen
--------
- [ ] Lagerplätze/Container definieren
- [ ] Verbrauchslog anlegen
