---
stand: 2026-04-05 19:43
update: Arkologie A1 fuehrt jetzt Mind-Cluster-Anbindung, lokale Unterraeume und konservative Nebenstart-Hooks.
checks: snapshot-lock PASS (2026-04-05 10:53); markdownlint PASS; frontmatter PASS
---

RP Startbogen: Arkologie A1
==========================

Zweck
-----

Dieser Startbogen hebt `A1` vom reinen Auswahlknoten auf einen spielbaren Arkologie-Start mit klarer Leitungs-, Handels- und Sicherheitsachse.

Quellenbasis
------------

- `novapolis-rp/database-rp/01-factions/arkologie-a1/03-locations/A1.md`
- `novapolis-rp/database-rp/01-factions/arkologie-a1/02-characters/Liora-Navesh.md`
- `novapolis-rp/database-rp/01-factions/arkologie-a1/02-characters/Nera-Vossen.md`
- `novapolis-rp/database-rp/01-factions/arkologie-a1/02-characters/Borin-Khade.md`
- `novapolis-rp/database-rp/01-factions/arkologie-a1/05-projects/Missionslog-Arkologie-A1.md`
- `novapolis-rp/database-rp/01-factions/arkologie-a1/06-handel-diplomatie/Relationslog-Arkologie-A1.md`
- `novapolis-rp/database-rp/01-factions/arkologie-a1/04-inventory/Arkologie-inventar.md`
- `novapolis-rp/database-rp/00-admin/Stationskontroll-Matrix.md`
- `novapolis-rp/database-rp/00-admin/Metrokarte-T0.md`

Startklasse
-----------

- Modus: `faction_start`
- Bereich: `A1`
- Gebietsklasse: `faction_core`
- Dichtegrad: `full_slice`

Startpraemisse
--------------

Der PC startet in einem aktiven Arkologie-Knoten, in dem Datenvaliditaet, Biosicherheit und kontrollierte Tauschfenster jede Aussenentscheidung ueberformen.

Belegte Ausgangslage
--------------------

- `A1` ist aktiver Arkologie-Kern.
- Liora Navesh fuehrt Fraktion, Forschung und MedTech-Leitplanken.
- Nera Vossen fuehrt Handel und beschraenkte Lieferkorridore.
- Borin Khade kontrolliert Sicherheits- und Transitfreigaben.
- Die Aussenlage lautet `Haendlerbund = beschraenkt`, `Eisenkonklave = umkaempft`, `Novapolis = unbekannt`.
- `A1` haengt aktiv an `A2`; der Pufferraum Richtung Neutralnetz ist real belegt.

Startkern
---------

- Liora Navesh
- Nera Vossen
- Borin Khade

Mind-Cluster-Anbindung
----------------------

- `novapolis-rp/database-rp/01-factions/arkologie-a1/07-mind-clusters/liora-navesh-mind-cluster.md`
- `novapolis-rp/database-rp/01-factions/arkologie-a1/07-mind-clusters/nera-vossen-mind-cluster.md`
- `novapolis-rp/database-rp/01-factions/arkologie-a1/07-mind-clusters/borin-khade-mind-cluster.md`

Lokale Tiefenschaerfe (T0)
--------------------------

- Forschungskuppel Nordost: Lioras Leitungs- und Validierungslinse fuer Forschung, MedTech und Risikoabwägung.
- Handelsknoten Nordost: Neras enger Aussen- und Gegenleistungspfad fuer schmale Tauschfenster.
- Sicherheitsleitstand: Borins Screening- und Freigabefilter vor jeder Oeffnung.
- Vorzone `A2`: kontrollierter Pufferraum statt direkter Offenheit nach aussen.

Erste Stakes
------------

- Versorgung und Austausch sind moeglich, aber nur unter harten Sicherheits- und Biosicherheitsauflagen.
- Jede oeffnende Bewegung nach aussen erhoeht Validierungs- und Sicherheitsdruck.
- Die Eisenkonklave bleibt als umkaempfter Gegenraum relevant.

Erster Entscheidungsraum
------------------------

1. Ein beschraenktes Tauschfenster absichern und kontrolliert oeffnen.
2. Sicherheitsauflagen weiter anziehen und den Aussenkontakt verlangsamen.
3. Forschungs- und Validierungsinteressen ueber offene Diplomatie priorisieren.
4. Den Pufferraum `A2` als kontrollierte Vorzone nutzen statt direkte Offenheit zu wagen.

Fail-forward
------------

- Fehlentscheidungen fuehren zuerst zu strengeren Freigaben, verpassten Tauschfenstern oder internem Druck.
- Offene Kontakte kippen eher in Misstrauen und Screening als in sofortige Katastrophe.

Nebenstart-Hooks
----------------

- Forschungs-Hook: Einstieg direkt ueber Lioras Validierungs- und Biosicherheitsdruck in der Forschungskuppel.
- Handels-Hook: Einstieg ueber Neras enges Tauschfenster im Handelsknoten Nordost.
- Sicherheits-Hook: Einstieg ueber Borins Screening- und Transitfilter im Sicherheitsleitstand.

Reveal-Regeln
-------------

- `pc_visible`: Sicherheitsauflagen, Tauschfenster, Leitungsprioritaeten, unmittelbare Aussenrisiken
- `allies_only`: interne Freigabeketten und Validierungslogik
- `world_only`: ungepruefte Anomalie- und Gegenfraktionsdeutungen
- `rumor`: unbestaetigte Meldungen ueber Novapolis oder neue Lieferkorridore

Guardrails
----------

- Keine freie A1-Innenarchitektur erfinden.
- Keine direkten Novapolis-Kontakte behaupten.
- Keine konkreten Dealmengen oder Routen setzen.
