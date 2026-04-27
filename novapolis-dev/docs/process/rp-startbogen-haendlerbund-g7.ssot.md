---
stand: 2026-04-27 02:30
update: G7 fuehrt jetzt zusaetzlich die konservative Lesart als externe Zentrale des Haendlerbunds mit eingebettetem C6-Niederlassungsfenster.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260427_022916.md
---

RP Startbogen: Haendlerbund G7
==============================

Zweck
-----

Dieser Startbogen hebt den Haendlerbund-Start in `G7` von einem reinen Rahmenanker auf einen echten spielbaren Einstiegsbogen mit externer Zentrale und eingebettetem Niederlassungsfenster.

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

- `G7` ist aktive externe Zentrale des Haendlerbunds fuer Leitstelle, Handelsplanung und Sicherheitsfreigabe.
- `H-47` ist als ueberlebende Haendlerkarawane mit dauerhafter Kooperation zu Novapolis belegt.
- `C6` ist als Handelsstuetzpunkt aktiviert und fungiert als eingebettete Niederlassung des Haendlerbunds in Novapolis; `G7 <-> C6` ist der primaere externe Kontaktpfad.
- Belegte Austauschklassen sind `Energie`, `technische Reparaturen`, `Kommunikationszugang` gegen `Nahrungsmittel`, `Filter` und `Grundbedarfsgueter`.
- `G7` haengt topologisch aktiv an `G2` und weiter Richtung `H3/H12`; damit ist der Start nicht isoliert.

Startpraemisse
--------------

Der PC startet als Figur im Haendlerbund-Kontext an einer schmalen externen Zentrale. Der Einstieg ist nicht lokal-statisch, sondern von Route, Risiko, Deal-Pruefung, Niederlassungslogik und dem Verhaeltnis zu Novapolis gepraegt.

Startkern
---------

- Mara Quell: Leitstelle, Freigaben, Krisensteuerung in `G7`
- Tovin Rek: Handels- und Routenleitstand in `G7`
- Runa Fehr: Sicherheitsfreigaben, Begleitschutz, Alarmprotokolle in `G7`
- optionaler Niederlassungspfad: Marven Kael, Arlen Dross, Senn Daru oder Tess Avari im `C6`-Fenster

Mind-Cluster-Anbindung
----------------------

- `novapolis-rp/database-rp/01-factions/novapolis/07-mind-clusters/marven-kael-mind-cluster.md`
- `novapolis-rp/database-rp/01-factions/novapolis/07-mind-clusters/arlen-dross-mind-cluster.md`
- `novapolis-rp/database-rp/01-factions/novapolis/07-mind-clusters/senn-daru-mind-cluster.md`

Lokale Tiefenschaerfe (T0)
--------------------------

- Route `G7 <-> C6`: operativer Kern des Starts zwischen Zentrale und Niederlassung.
- Leitstellenfenster: Mara, Tovin und Runa ziehen Ziele, Deal-Timing und Sicherheitsfreigaben in `G7` zusammen.
- Deal- und Moderationsfenster: das `C6`-Fenster oeffnet sich ueber Marven, Arlen und die H-47-Kontakte.
- Sicherheits- und Rueckzugsrahmen: jede Bewegung bleibt an Konvoilogik und Ruecklauf nach `G7` gebunden.

Erste Stakes
------------

- Der Kontakt zu Novapolis ist tragfaehig, aber nicht blind vertrauensbasiert.
- G7 ist eine schmale externe Zentrale, aber keine flaechige Festung oder voll ausgebaute Marktstadt.
- C6 ist strategisch wichtig, bleibt aber eingebettete Niederlassung statt zweiter Eigenzentrale.
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

- Leitstellen-Hook: Einstieg ueber Mara, Tovin oder Runa in der G7-Zentrale.
- Niederlassungs-Hook: Einstieg ueber Marven und Arlen im `C6`-Fenster.
- Uebergabe-Hook: Einstieg ueber Senns oder Tess' kleineren Kontakt- und Austauschpfad.

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
- Keine stillschweigende Novapolis-Vollintegration behaupten; der externe Charakter von `G7` und die eingebettete Natur von `C6` bleiben erhalten.
