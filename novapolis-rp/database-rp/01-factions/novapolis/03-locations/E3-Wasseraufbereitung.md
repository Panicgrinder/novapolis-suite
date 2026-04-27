---
stand: 2026-04-27 05:33
update: E3-Wasseraufbereitung fuehrt jetzt eine konservative Ortslesart als verriegelte Infrastrukturreserve mit Filter- und Versorgungsschatten.
checks: snapshot-lock PASS (2026-04-27 04:51); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/01-factions/novapolis/03-locations/E3-Wasseraufbereitung.md' 'novapolis-dev/docs/donelog.md' PASS (2026-04-27 04:55); .venv-py313-backup-20260409_1832/Scripts/python.exe scripts/check_frontmatter.py 'novapolis-rp/database-rp/01-factions/novapolis/03-locations/E3-Wasseraufbereitung.md' 'novapolis-dev/docs/donelog.md' PASS (2026-04-27 04:55); npm --prefix novapolis-rp/coding/tools/validators run validate:rp PASS (2026-04-27 04:55)
title: E3 Wasseraufbereitung
last_updated: 2026-04-27T04:51:00+02:00
category: location
slug: e3-wasseraufbereitung
version: "0.1"
affiliations: [novapolis]
status: unbekannt
connections: ["e3"]
tags: ["poi", "e3", "infrastruktur"]
---

E3 - Wasseraufbereitung
-----------------------

Status
------
- Unklar; Anlage vermutlich vorhanden, Zustand unbestaetigt
- Keine belastbare Freigabe; fuer Novapolis derzeit eher verriegelte Infrastrukturreserve als nutzbarer Betriebsraum

Funktion
--------
- Wasseraufbereitung und Filterkreislauf als kritische Infrastruktur des frueheren E3-Betriebs

Konservative Lesart (T0)
------------------------

- Die Wasseraufbereitung gehoerte funktional zum frueheren Stationsbetrieb von E3, ist nach Evakuierung und Verriegelung aber nicht mehr als aktive Versorgungsquelle belastbar.
- Gerade weil C6 bei Wasser, Hygiene und Filtern unter Druck steht, bleibt der Ort im Hintergrund wichtig, ohne dass daraus schon ein nutzbarer Rueckgriff behauptet werden darf.
- Fuer den aktuellen Weltstand ist die Anlage damit kein laufender Technikposten, sondern ein gesperrter Infrastrukturrest mit moeglichem Zukunftswert.

Zugang
------
- Zugang aktuell nicht vorgesehen; erst nach Aufhebung der E3-Verriegelung

Zugangs- und Risikoprofil
-------------------------

- Jeder Zugriff waere an dieselben Guards gebunden wie der restliche E3-Raum: Risikoanalyse, kontrollierter Zugang ueber den verriegelten C6-E3-Anschluss und keine freie Routinebegehung.
- Unklar bleiben Zustand, Wasserqualitaet, Filterstand und Netz- oder Energieanbindung; diese Unschaerfe ist hier selbst der Kern des Risikos.
- Ohne belastbare Belege wird weder eine intakte Produktion noch ein Totalausfall behauptet.

Risiken
-------
- Fehlende Zustandsdaten als Risiko fuer spaetere Expansion oder Rueckgriff auf E3-Infrastruktur

Betriebsrelevante Pruefpunkte (konservativ)
-------------------------------------------

- Filterkreislauf: unklar, ob Medien, Gehaeuse und Leitungsweg nach der E3-Abschaltung noch brauchbar sind.
- Wasserqualitaet: Messwert und Belastungsbild fehlen; widerspruechliche Sensorik bleibt moeglich.
- Energie- und Leitungszustand: Die getrennte Energiezufuhr von E3 macht jede spaetere Inbetriebnahme pruefpflichtig.
- C6-Schattennutzen: Falls die Anlage spaeter belastbar waere, koennte sie den Druck auf tragbares Wasser und Filter im C6-Kontext mindern; aktuell ist das nur strategische Reserve, nicht Betriebsfakt.

Hooks
-----
- Filterbedarf steigt -> Entscheidung: Risiko-Run oder Ausbau in C6
- Sensorik liefert widerspruechliche Werte zur Wasserqualitaet

Verlinkungen
------------
- E3 -> ./E3.md
- Logistik -> ../00-admin/Logistik.md
