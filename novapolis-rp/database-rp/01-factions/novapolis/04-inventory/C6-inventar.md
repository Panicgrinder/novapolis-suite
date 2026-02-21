---
stand: 2026-02-21 21:41
update: Belegte C6-Bestände/Potenziale aus SSOT nachgezogen; tbd-Blöcke durch faktenbasierte Einträge ersetzt.
checks: "npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/01-factions/novapolis/04-inventory/C6-inventar.md' 'novapolis-rp/database-rp/00-admin/Logistik.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-21 20:57); .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py 'novapolis-rp/database-rp/01-factions/novapolis/04-inventory/C6-inventar.md' 'novapolis-rp/database-rp/00-admin/Logistik.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-21 20:57)"
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

Policy
------
- Inventare bleiben getrennt; Transfers nur via Mission/Logistik.
- Buchungen mit Quelle/Ziel in [Logistik](../../../00-admin/Logistik.md) dokumentieren.

Bestände (verbucht)
-------------------
- Filter (C6) - belegt, Menge tbd
- Energiezellen (C6) - belegt, Menge tbd
- Werkzeuge (C6) - belegt, Menge/Typen tbd

Potenziale
----------
- Hydrofilter-Behälter (Reserve) - Potenzial vorhanden, Einbindung offen
- Mechanik-Werkzeug (priorisiert, ohne Stückzahlen)

Fehlend / Offen
---------------
- Adapter/Fittings DN60 (kritisch)
- Schweißausrüstung (kritisch)
- Lagerplätze/Containerstruktur für C6-Inventar

Bewegungen (Log)
----------------
- 2026-01-16 [FACT?] Prioritätenliste für C6-Inventar benannt (Filter, Energiezellen, Adapter/Fittings DN60, Schweißausrüstung, Mechanik-Werkzeug; ohne Stückzahlen). Quelle: scene-2026-01-16-a.
- 2026-02-10 17:09 [FACT?] Artefakt 7A im C6-Kontext markiert; Details erst nach Inventarisierung. Quelle: scene-2025-10-27-d.
- 2026-02-10 17:09 [FACT?] Datenkern (tragbar) am Fundort C6 belassen; nicht aufgenommen. Quelle: scene-2025-10-27-x.

Aktionen
--------
- [ ] Lagerplätze/Container definieren
- [ ] Verbrauchslog anlegen
