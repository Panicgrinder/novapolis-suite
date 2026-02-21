---
stand: 2026-02-21 21:41
update: Auf globalen Ereignislog-Index umgestellt; fraktionsspezifische Ereignisse in Fraktionslogs auslagern.
checks: "ausstehend (nach Mutation neu ausführen)"
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
