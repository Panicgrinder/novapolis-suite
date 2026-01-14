---
stand: 2026-01-12 12:02
update: "Schema-Gate: title ergaenzt; MD025-Override (Frontmatter-title + H1)."
checks: npm --prefix novapolis-rp\coding\tools\validators run validate:rp PASS (2026-01-12 12:01); npm --prefix novapolis-rp\coding\tools\validators run validate:crossrefs PASS (2026-01-12 12:01); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/01-factions/novapolis/04-inventory/D5-inventar.md' PASS (2026-01-12 12:02); & .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis-rp\database-rp PASS (2026-01-12 12:02)
title: Inventar - D5
last_updated: 2025-11-07T04:32:00+01:00
category: inventory
slug: d5-inventar
owner: novapolis
scope: location
location: d5
version: "0.1"
tags: []
---

<!-- markdownlint-disable MD025 -->

D5 - Inventar
=============

Bestände (verbucht)
-------------------
- Filter (C6)
- Energiezellen (C6)
- Werkzeuge (C6 + D5)

Potenziale
----------
- Hydrofilter-Behälter (C6) - Reserve, Aufbereitung offen

Fehlend / Offen
---------------
- Schweißausrüstung
- Adapter DN60

Aktionen
--------
- [ ] Lagerplätze definieren und QR/Tagging überlegen
- [ ] Verbrauchslog anlegen
