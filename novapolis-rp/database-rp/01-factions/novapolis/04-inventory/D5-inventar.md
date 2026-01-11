---
stand: 2026-01-11 07:14
update: D5-Inventar ins Novapolis-Fraktionsinventar verschoben (Scope=location).
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-01-11 07:14); & .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis-rp\database-rp PASS (2026-01-11 07:14); & .\.venv\Scripts\python.exe scripts\checks_rp_consistency.py --strict PASS (2026-01-11 07:14)
last_updated: 2025-11-07T04:32:00+01:00
category: inventory
slug: d5-inventar
owner: novapolis
scope: location
location: d5
version: "0.1"
tags: []
---

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
