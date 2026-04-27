---
stand: 2026-04-27 05:33
update: C6-E3 fuehrt jetzt explizit den belegten Fussbetrieb aus Evakuierung und Sicherung, ohne daraus einen normalisierten Korridor zu machen.
checks: snapshot-lock PASS (2026-04-27 04:18); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/01-factions/novapolis/05-projects/Nordlinie-01.md' 'novapolis-rp/database-rp/01-factions/novapolis/03-locations/Verbindungstunnel-C6-E3.md' 'novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md' 'novapolis-dev/docs/donelog.md' PASS (2026-04-27 04:26); .venv-py313-backup-20260409_1832/Scripts/python.exe scripts/check_frontmatter.py 'novapolis-rp/database-rp/01-factions/novapolis/05-projects/Nordlinie-01.md' 'novapolis-rp/database-rp/01-factions/novapolis/03-locations/Verbindungstunnel-C6-E3.md' 'novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md' 'novapolis-dev/docs/donelog.md' PASS (2026-04-27 04:26); npm --prefix novapolis-rp/coding/tools/validators run validate:rp PASS (2026-04-27 04:26)
title: Verbindungstunnel C6-E3
last_updated: 2026-04-27T04:18:00+02:00
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
- Offen, begehbar; durch Evakuierung und Folge-Sicherungen im Fussbetrieb belegt, aber nicht instandgesetzt
- E3-Ende bleibt versiegelt und als Anomalie markiert (Monitoring passiv)

Bevölkerung
-----------
- Keine dauerhafte Belegung (Transit-/Sicherungsbereich)

Infrastruktur / Zugänge
-----------------------
- Zugänge: C6 ↔ E3 (E3-Ende verriegelt)
- Provisorische Sicherung/Monitoring durch C6
- C6-seitig kontrollierter Fussbetrieb; keine freie Durchgaengigkeit ueber das verriegelte E3-Ende hinaus

Risiken
-------
- E3-Ende: Anomalie-/Warnstatus („E3-Gefahr“)
- Fehlende dauerhafte Stabilisierung/Belüftung
- Begehbar heisst hier nicht normalisiert; der Korridor bleibt ein enger Sicherungs- und Erinnerungsraum

Nutzung
------
- Evakuierungsroute: 20 Evakuierte aus E3 wurden nach C6 verlegt (Quelle: chat-export.txt, Abschnitt C6-Bewohner)
- Evakuierungsroute: 20 Evakuierte aus E3 wurden nach C6 verlegt (Quelle: [C6-Bewohner](../02-characters/C6-Bewohner.md))
- Provisorische Sicherung durch C6-Teams; Betrieb vorerst nur zu Fuß
- Der belegte Fussbetrieb macht den Tunnel nutzbar, aber nicht zu einer sicheren oder breit freigegebenen Routineverbindung

Aufgaben
-------
- [ ] Sensorik/Belüftung überprüfen und mit D5-Zentrale koppeln
- [ ] Rückweg aus E3 sichern, Zugangskontrollen definieren
- [ ] Materialliste für dauerhafte Stabilisierung vorbereiten

