---
stand: 2026-01-09 05:15
update: P0 Pflichtfelder ergänzt (Bevölkerung/Infrastruktur/Risiken) für Ortsgraph-Konsistenz.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/**/*.md' PASS (2026-01-09 05:15); & .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis-rp\database-rp PASS (2026-01-09 05:15); & .\.venv\Scripts\python.exe scripts\checks_rp_consistency.py --strict PASS (2026-01-09 05:15)
title: Verbindungstunnel D5-C6
last_updated: 2026-01-09T05:14:03+01:00
category: location
slug: verbindungstunnel-d5-c6
version: "1.0"
affiliations: [novapolis]
status: beschädigt
connections: ["d5", "c6"]
tags: []
---

Verbindungstunnel D5-C6
-----------------------

Status
------
- Strukturelle Schäden; kartiert

Bevölkerung
-----------
- Keine dauerhafte Belegung (Transit-/Arbeitsbereich)

Infrastruktur / Zugänge
-----------------------
- Zugänge: D5 ↔ C6
- Engstellen/Abschnitte werden im Projekt [Nordlinie-01](../05-projects/Nordlinie-01.md) geführt

Risiken
-------
- Statik/Trümmer
- Belüftung/Schadstoffe
- Sicht-/Stromausfall in Teilabschnitten

Material/Bedarf
----------------
- Schweißgerät (fehlt)
- Adapter DN60 (fehlt)
- Stützelemente, Kabeltrassen

Aufgaben
-------
- [ ] Abschnitte priorisieren
- [ ] Materiallauf planen
- [ ] Sicherheit (Belüftung/Fluchtwege)

