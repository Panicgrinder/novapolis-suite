---
stand: 2026-02-21 21:58
update: Delta-zum-Missionslog ergänzt und D5-Inventar mit Missionsankern konsolidiert.
checks: "npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-dev/docs/todo.rp.md' 'novapolis-dev/docs/donelog.md' 'novapolis-rp/database-rp/01-factions/novapolis/06-handel-diplomatie/Relationslog-Novapolis.md' 'novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5.md' 'novapolis-rp/database-rp/01-factions/novapolis/04-inventory/Novapolis-inventar.md' 'novapolis-rp/database-rp/01-factions/novapolis/04-inventory/D5-inventar.md' PASS (2026-02-21 21:55); .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py 'novapolis-dev/docs/todo.rp.md' 'novapolis-dev/docs/donelog.md' 'novapolis-rp/database-rp/01-factions/novapolis/06-handel-diplomatie/Relationslog-Novapolis.md' 'novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5.md' 'novapolis-rp/database-rp/01-factions/novapolis/04-inventory/Novapolis-inventar.md' 'novapolis-rp/database-rp/01-factions/novapolis/04-inventory/D5-inventar.md' PASS (EXITCODE=0, 2026-02-21 21:55)"
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

Policy
------
- Inventare bleiben getrennt; Transfers nur via Mission/Logistik.
- Buchungen mit Quelle/Ziel in [Logistik](../../../00-admin/Logistik.md) dokumentieren.

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

Bewegungen (Log)
----------------
- 2026-02-10 17:09 [FACT?] Werkzeugtasche (Fundstueck) in D5 beobachtet; Ownership/Inhalt offen. Quelle: scene-2025-10-27-g.

Delta zum Missionslog
---------------------

- Delta 1 (belegt): D5-Werkzeug-/Wartungskontext als Missionsanker vorhanden; Inventar-Ownership der Werkzeugtasche bleibt offen bis belastbare Zuordnung vorliegt.
  - Quelle: [Missionslog-Novapolis - D5: Wartungsauftrag & Wartungsgang](../05-projects/Missionslog-Novapolis.md#d5-wartungsauftrag--wartungsgang), [scene-2025-10-27-g](../../../06-scenes/scene-2025-10-27-g.md)
- Delta 2 (belegt/offen): Trennung D5↔C6 bleibt verbindlich; Detailbuchungen nur nach belegter Transferzeile.
  - Quelle: [Missionslog-Novapolis - Anomalie: Verbindungstunnel D5-C6](../05-projects/Missionslog-Novapolis.md#anomalie-verbindungstunnel-d5-c6), [scene-2025-10-27-x](../../../06-scenes/scene-2025-10-27-x.md)

Aktionen
--------
- [ ] Lagerplätze definieren und QR/Tagging überlegen
- [ ] Verbrauchslog anlegen
