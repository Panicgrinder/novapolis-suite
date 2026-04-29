---
stand: 2026-04-29 06:56
update: C6-State fuehrt jetzt Ronjas T12-Anfrage zur kontrollierten Schuttkeil-Verwertung als offene Prueffrage.
checks: snapshot-lock PASS (2026-04-29 06:56); markdownlint PASS; frontmatter PASS; todo-index-sync PASS; logs-policy PASS; snapshot-gate PASS
---
Runtime State - C6
==================

Status
------

- slug: c6
- scope: location
- state: Arbeitsstand
- review_state: working

Current State
-------------

- summary: C6 ist im aktuellen Nordlinie-Hauptpfad ein teilaktiver Aussenposten unter Doppelbelastung, aber nicht als ein einziger Block zu lesen. Der `C6-Tunneltrupp` arbeitet vorsichtig bis an den Kontaktpunkt weiter und bringt fuer seine Haelfte einen eigenen Reparaturbefund mit: `Schuttkeil Kontaktseite`, `Randauflage Suedlauf` und `Leitungsaufnahme C6-Vorlauf` sind dort eigenstaendige Arbeits- und Meldestellen. T12 legt auf diese Lage eine konkrete Anfrage aus D5: C6 soll pruefen, ob der Schuttkeil kontrolliert zerschlagen werden kann und ob tragfaehige Bruchstuecke fuer die `Schottertasche Nordkante` nutzbar waeren. Davon getrennt haelt die `C6-Station` unter `Kora` Schichtlogik, Sicherheitsordnung und Ruecklauf innen stabil. Die nicht im Tunnel eingesetzten Gefluechteten tragen weiter Wasser-, Lager-, Hygiene-, Kuechen-, Wache- und Entlastungsarbeit; `Mara Quell` bleibt zum Aufbau des H-47-Aussenpostens vor Ort in `C6`.
- drivers:
  - belegt knappe Versorgungs- und Werkzeuglage in C6
  - C6 bleibt teilaktiver Vorposten und keine freie Entlastungsstation
  - die C6-Seite arbeitet im Tunnel weiter und hat den D5-Trupp jetzt vorsichtig wahrgenommen
  - der C6-Tunneltrupp hat den vorsichtigen Kontakt jetzt in einen direkten Arbeitsabgleich mit Ronja ueberfuehrt
  - der C6-Tunneltrupp bringt jetzt einen eigenen Reparaturbefund seiner Haelfte in die gemeinsame Liste ein
  - `Kora Malenkov` bleibt als lokale Leit- und `Echo` als Schutzachse in der Stationsverwaltung statt im Tunnel
  - die nicht eingesetzten Gefluechteten halten den laufenden Innenbetrieb des Vorpostens praktisch aufrecht
  - `Mara Quell` bleibt in `C6`, um den H-47-Aussenposten aufzubauen, nicht in `G7`
  - die gemeinsame Bedarfsliste laeuft vom Tunneltrupp getrennt in den Ruecklauf der C6-Station
  - Turn 11 fuehrt Kora ausdruecklich weiter in Verteilung und Berichtsauswertung des C6-Tunneltrupps statt in Ronjas D5-Perspektive
  - T12 gibt C6 eine klare Prueffrage zum `Schuttkeil Kontaktseite`: kontrolliertes Zerschlagen, Bruchstueck-Eignung und Risiko am Kontaktpunkt muessen zuerst beurteilt werden
  - `inventory.md` fuehrt jetzt den aktuellen C6-Hauptpfad-Bestand statt nur des alten H-47-Probeinventars
  - `roster.md` fuehrt den Bewohner- und Vor-Ort-Roster fuer C6, ohne alle Bewohner als freie Einzelakteure zu behandeln
- blockers:
  - kein neuer realer Materialeingang fuer den aktuellen Hauptzug
  - keine belastbaren Mengen oder Lagerzuordnungen fuer einen neuen Folgeeingang
  - operative Schweißausruestung und `DN60` bleiben auch auf C6-Seite kritisch
  - auch der neue Kontaktpunkt ist noch kein freier Durchgang oder entspannter Materialaustausch
  - `Schuttkeil Kontaktseite`, `Randauflage Suedlauf` und `Leitungsaufnahme C6-Vorlauf` machen klar, dass die C6-Haelfte selbst nicht reparaturfrei ist
  - Bruchstuecke aus dem Schuttkeil sind noch kein nutzbares Material; Eignung und Gewinnungsrisiko bleiben bis zur C6-Antwort offen
- impacted_entities:
  - C6
  - C6-Tunneltrupp
  - C6-Station
  - Kora Malenkov
  - Echo
  - Evakuierte aus E3
  - Mara Quell
  - Haendlerbund
  - H-47
  - C6-Bewohner
  - Marei Falk
  - Marven Kael
  - Arlen Dross

Evidence
--------

- SSOT: `database-rp/01-factions/novapolis/03-locations/C6.md`
- SSOT: `database-rp/01-factions/novapolis/04-inventory/C6-inventar.md`
- SSOT: `database-rp/01-factions/novapolis/02-characters/Kora-Malenkov.md`
- SSOT: `database-rp/01-factions/novapolis/02-characters/Echo.md`
- SSOT: `database-rp/01-factions/haendlerbund/02-characters/Mara-Quell.md`
- SSOT: `database-rp/01-factions/haendlerbund/04-inventory/Haendlerbund-inventar.md`
- Runtime: `sessions/c6-h47-handelsfenster-01/scene-log.md`, Turn 1
- Runtime: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 9
- Runtime: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 10
- Runtime: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 11
- Runtime: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 12
- Runtime: `inventory.md`
- Runtime: `roster.md`
- Runtime: `../../characters/marei/entity.md`, `../../characters/marei/mind.md`
- Runtime: `../../characters/marven-kael/entity.md`, `../../characters/marven-kael/mind.md`
- Runtime: `../../characters/arlen-dross/entity.md`, `../../characters/arlen-dross/mind.md`

Promotion Notes
---------------

- C6 wird jetzt wieder als Teil des aktuellen Hauptfortsetzungsstands gelesen: mit eigener Tunnelkante, direktem Arbeitskontakt zu Ronjas Seite, offener Schuttkeil-Pruefung und zugleich getrenntem Stationsbetrieb unter Kora.
- Das alte H-47-Probefenster bleibt nur Vorgeschichte; aktuelle Fortschritte laufen ueber den Nordlinie-Hauptpfad und Mara vor Ort in `C6`, nicht ueber eine ferne G7-Reaktion.
