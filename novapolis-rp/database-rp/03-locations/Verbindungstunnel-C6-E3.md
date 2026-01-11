---
stand: 2026-01-09 05:15
update: P0 Pflichtfelder ergänzt (Bevölkerung/Infrastruktur/Risiken) für Ortsgraph-Konsistenz.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/**/*.md' PASS (2026-01-09 05:15); & .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis-rp\database-rp PASS (2026-01-09 05:15); & .\.venv\Scripts\python.exe scripts\checks_rp_consistency.py --strict PASS (2026-01-09 05:15)
title: Verbindungstunnel C6-E3
last_updated: 2026-01-09T05:14:03+01:00
category: location
slug: verbindungstunnel-c6-e3
version: "1.0"
affiliations: [novapolis]
status: offen
connections: ["c6", "e3"]
tags: []
---

Verbindungstunnel C6-E3
-----------------------

Status
------
- Offen, begehbar; nicht instandgesetzt
- E3-Ende bleibt versiegelt und als Anomalie markiert (Monitoring passiv)

Bevölkerung
-----------
- Keine dauerhafte Belegung (Transit-/Sicherungsbereich)

Infrastruktur / Zugänge
-----------------------
- Zugänge: C6 ↔ E3 (E3-Ende verriegelt)
- Provisorische Sicherung/Monitoring durch C6

Risiken
-------
- E3-Ende: Anomalie-/Warnstatus („E3-Gefahr“)
- Fehlende dauerhafte Stabilisierung/Belüftung

Nutzung
------
- Evakuierungsroute: 20 Evakuierte aus E3 wurden nach C6 verlegt (Quelle: chat-export.txt, Abschnitt C6-Bewohner)
- Provisorische Sicherung durch C6-Teams; Betrieb vorerst nur zu Fuß

Aufgaben
-------
- [ ] Sensorik/Belüftung überprüfen und mit D5-Zentrale koppeln
- [ ] Rückweg aus E3 sichern, Zugangskontrollen definieren
- [ ] Materialliste für dauerhafte Stabilisierung vorbereiten

