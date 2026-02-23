---
stand: 2026-02-23 03:24
update: Frische-Review durchgeführt; globale Ereignisregeln und Fraktionsverweise geprüft (kein Kanon-Delta).
checks: "npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/00-admin/Ereignislog-Weltgeschehen.md' 'novapolis-rp/database-rp/00-admin/Cluster-Index.md' 'novapolis-rp/database-rp/00-admin/Missionslog.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-23 03:25); .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py 'novapolis-rp/database-rp/00-admin/Ereignislog-Weltgeschehen.md' 'novapolis-rp/database-rp/00-admin/Cluster-Index.md' 'novapolis-rp/database-rp/00-admin/Missionslog.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-23 03:25); npm --prefix novapolis-rp/coding/tools/validators run validate:rp PASS (2026-02-23 03:25)"
title: Ereignislog – Weltgeschehen
category: admin
slug: ereignislog_weltgeschehen_v1
version: "0.1"
---

<!-- markdownlint-disable MD025 -->

Ereignislog – Weltgeschehen (Globaler Index)
============================================

Zweck
-----
Dieses Dokument hält nur **globale Ereignisregeln und Verweisstruktur**.
Fraktions-/Stationsspezifische Ereignisse werden in den jeweiligen
Fraktions-Ereignislogs geführt.

Quellen
-------
- RAW-Exporte: `database-raw/99-exports/`
- Canon-Pflege: fraktionsspezifisch unter `01-factions/*/00-doctrine/*-ereignislog.md`

Globale Lesart
--------------

- Relative Marker (z. B. `[Tag X]`) bleiben relative Chronikanker.
- Kanonischer Spielanker bleibt T0/T+X gemäß fraktionsspezifischer Timeline.
- Keine Retcons ohne explizite Korrekturdokumentation.

SECRECY-Guardrail (Außenwissen)
-------------------------------

- Externe Fraktionen erhalten keine bestätigten D5/Novapolis-Detaildaten ohne belegte Offenlegung.
- Für H-47 gilt global: Außenperspektive kann Funkstille/unsicheren Status führen; interne Operativdetails bleiben im fraktionsspezifischen Log.
- Legacy-Begriffe aus RAW (z. B. uneinheitliche Bündnislabels) werden nicht als neue Canon-Behauptung fortgeschrieben.

Fraktions-Ereignislogs
----------------------

- Novapolis: [novapolis-ereignislog](../01-factions/novapolis/00-doctrine/novapolis-ereignislog.md)
- Arkologie A1: [arkologie-a1-ereignislog](../01-factions/arkologie-a1/00-doctrine/arkologie-a1-ereignislog.md)
- Eisenkonklave: [eisenkonklave-ereignislog](../01-factions/eisenkonklave/00-doctrine/eisenkonklave-ereignislog.md)
- Flüsterkollektiv: [fluesterkollektiv-ereignislog](../01-factions/fluesterkollektiv/00-doctrine/fluesterkollektiv-ereignislog.md)
- Händlerbund: [haendlerbund-ereignislog](../01-factions/haendlerbund/00-doctrine/haendlerbund-ereignislog.md)
- Schattenbund: [schattenbund-ereignislog](../01-factions/schattenbund/00-doctrine/schattenbund-ereignislog.md)
- Schienenbund: [schienenbund-ereignislog](../01-factions/schienenbund/00-doctrine/schienenbund-ereignislog.md)

Verlinkungen
------------

- Admin-Timeline: [Canvas-T0-Timeline](Canvas-T0-Timeline.md)
- Missionslog (global): [Missionslog](./Missionslog.md)
