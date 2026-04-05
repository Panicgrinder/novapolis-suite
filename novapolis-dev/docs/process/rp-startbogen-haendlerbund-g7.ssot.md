---
stand: 2026-04-05 19:43
update: G7 fuehrt jetzt Mind-Cluster-Anbindung und konservative Nebenstart-Hooks fuer den H-47-Kern.
checks: snapshot-lock PASS (2026-04-05 10:53); markdownlint PASS; frontmatter PASS
---

RP Startbogen: Haendlerbund G7
==============================

Zweck
-----

Dieser Startbogen hebt den Haendlerbund-Start in `G7` von einem reinen Rahmenanker auf einen echten spielbaren Einstiegsbogen.

Quellenbasis
------------

- `novapolis-rp/database-rp/01-factions/haendlerbund/03-locations/G7.md`
- `novapolis-rp/database-rp/01-factions/haendlerbund/05-projects/caravan-moves.md`
- `novapolis-rp/database-rp/01-factions/haendlerbund/05-projects/Missionslog-Haendlerbund.md`
- `novapolis-rp/database-rp/01-factions/haendlerbund/04-inventory/Haendlerbund-inventar.md`
- `novapolis-rp/database-rp/01-factions/novapolis/02-characters/Marven-Kael.md`
- `novapolis-rp/database-rp/01-factions/novapolis/02-characters/Arlen-Dross.md`
- `novapolis-rp/database-rp/01-factions/novapolis/02-characters/Senn-Daru.md`
- `novapolis-rp/database-rp/00-admin/Metrokarte-T0.md`

Startklasse
-----------

- Modus: `faction_start`
- Bereich: `G7`
- Gebietsklasse: `faction_core`
- Dichtegrad: `full_slice`

Belegte Ausgangslage
--------------------

- `G7` ist aktiver Haendlerbund-Knoten und externer Kontakt-/Umschlagpunkt.
- `H-47` ist als ueberlebende Haendlerkarawane mit dauerhafter Kooperation zu Novapolis belegt.
- `C6` ist als Handelsstuetzpunkt aktiviert; `G7 <-> C6` ist der primaere externe Kontaktpfad.
- Belegte Austauschklassen sind `Energie`, `technische Reparaturen`, `Kommunikationszugang` gegen `Nahrungsmittel`, `Filter` und `Grundbedarfsgueter`.
- `G7` haengt topologisch aktiv an `G2` und weiter Richtung `H3/H12`; damit ist der Start nicht isoliert.

Startpraemisse
--------------

Der PC startet als Figur im Haendlerbund-Kontext an einem externen Umschlag- und Kontaktpunkt. Der Einstieg ist nicht lokal-statisch, sondern von Route, Risiko, Deal-Pruefung und dem Verhaeltnis zu Novapolis gepraegt.

Startkern
---------

- Marven Kael: Konvoifuehrung, Risikoanalyse, Sicherheitsrahmen
- Arlen Dross: Diplomatie, Moderation, Vertrags- und Kontaktpfade
- optionaler Nahkontakt im H-47-Raum: Senn Daru oder Tess Avari als Handels-/Uebergabepfad

Mind-Cluster-Anbindung
----------------------

- `novapolis-rp/database-rp/01-factions/novapolis/07-mind-clusters/marven-kael-mind-cluster.md`
- `novapolis-rp/database-rp/01-factions/novapolis/07-mind-clusters/arlen-dross-mind-cluster.md`
- `novapolis-rp/database-rp/01-factions/novapolis/07-mind-clusters/senn-daru-mind-cluster.md`

Lokale Tiefenschaerfe (T0)
--------------------------

- Route `G7 <-> C6`: operativer Kern des Starts.
- Deal- und Moderationsfenster: Arlens verhandelter Nahraum statt offener Marktplatz.
- Sicherheits- und Rueckzugsrahmen: Marvens Risikolinse vor jedem Umlauf.
- Kontaktpfad: Senn oder Tess als erster kleinerer Uebergabe- und Beziehungsanker.

Erste Stakes
------------

- Der Kontakt zu Novapolis ist tragfaehig, aber nicht blind vertrauensbasiert.
- G7 ist externer Knoten, nicht volle Sicherheitsbasis.
- Jeder Deal beruehrt Versorgung, Risiko und Rueckzugsplanung zugleich.
- Die Figur muss entscheiden, ob sie den Kontaktpfad vertieft, absichert oder neu prueft.

Erster Entscheidungsraum
------------------------

1. Einen Umlauf nach `C6` vorbereiten und den Kontaktpfad aktiv vertiefen.
2. Erst Sicherheits- und Rueckzugsrahmen fuer die Route absichern.
3. Deal-Fenster mit Novapolis enger pruefen, bevor Ressourcen bewegt werden.
4. Informationen oder Gegenleistungen sammeln, um die Verhandlungsposition zu verbessern.

Fail-forward
------------

- Schlechte Verhandlungen fuehren zuerst zu schlechteren Konditionen, Wartezeit oder engeren Sicherheitsauflagen.
- Uebervorsicht verlangsamt die Route, blockiert sie aber nicht automatisch.
- Ein misslungener Kontakt kann in einen Sicherheits-, Aufklaerungs- oder Umwegslot kippen, statt den Start zu beenden.

Nebenstart-Hooks
----------------

- Konvoifuehrungs-Hook: Einstieg ueber Marvens Sicherheits- und Rueckzugsrahmen.
- Diplomatie-Hook: Einstieg ueber Arlens Moderation eines engen Deal-Fensters.
- Uebergabe-Hook: Einstieg ueber Senns kleineren Kontakt- und Austauschpfad.

Reveal-Regeln
-------------

- `pc_visible`: Routenlage `G7 <-> C6`, unmittelbare Konvoi- und Dealfragen, sichtbare Sicherheitsbedenken
- `allies_only`: interne Konvoilogik, Crew-Prioritaeten, bekannte Austauschklassen und Vorsichtsregeln
- `world_only`: fremde Fraktionsabsichten, ungepruefte Risiken hinter `H3/H12`, verdeckte Langfristziele anderer Lager
- `rumor`: Geruechte ueber sichere Korridore, bessere Maerkte oder drohende Blockaden

Guardrails
----------

- Keine konkreten Dealmengen, Manifeste oder Stationslager setzen.
- Keine G7-Lokalstruktur erfinden, die ueber die aktuelle Orts-SSOT hinausgeht.
- Keine stillschweigende Novapolis-Vollintegration behaupten; der externe Charakter von `G7` bleibt erhalten.
