---
stand: 2026-04-05 19:43
update: H12 fuehrt jetzt Mind-Cluster-Anbindung, lokale Unterraeume und konservative Nebenstart-Hooks.
checks: snapshot-lock PASS (2026-04-05 10:53); markdownlint PASS; frontmatter PASS
---

RP Startbogen: Eisenkonklave H12
================================

Zweck
-----

Dieser Startbogen definiert `H12` als spielbaren Start der Eisenkonklave mit starkem Fokus auf Kontrolle, Sicherheitsfreigabe und selektive Handelsfenster.

Quellenbasis
------------

- `novapolis-rp/database-rp/01-factions/eisenkonklave/03-locations/H12.md`
- `novapolis-rp/database-rp/01-factions/eisenkonklave/02-characters/Varek-Solun.md`
- `novapolis-rp/database-rp/01-factions/eisenkonklave/02-characters/Kaspar-Dorn.md`
- `novapolis-rp/database-rp/01-factions/eisenkonklave/02-characters/Yara-Kest.md`
- `novapolis-rp/database-rp/01-factions/eisenkonklave/05-projects/Missionslog-Eisenkonklave.md`
- `novapolis-rp/database-rp/01-factions/eisenkonklave/06-handel-diplomatie/Relationslog-Eisenkonklave.md`
- `novapolis-rp/database-rp/01-factions/eisenkonklave/04-inventory/Eiserne-Enklave-inventar.md`
- `novapolis-rp/database-rp/00-admin/Stationskontroll-Matrix.md`
- `novapolis-rp/database-rp/00-admin/Metrokarte-T0.md`

Startklasse
-----------

- Modus: `faction_start`
- Bereich: `H12`
- Gebietsklasse: `faction_core`
- Dichtegrad: `full_slice`

Startpraemisse
--------------

Der PC startet in einem stark kontrollierten Eisenkonklave-Knoten, in dem Sicherheitsdisziplin, Werkstofflogik und begrenzte Handelsfenster den Alltag bestimmen.

Belegte Ausgangslage
--------------------

- `H12` ist aktiver Kern der Eisenkonklave.
- Varek Solun fuehrt die Kommandostruktur.
- Kaspar Dorn fuehrt kontrollierte Handelsfenster.
- Yara Kest gibt Sicherheitsfreigaben fuer Transit und Konvois.
- Die Aussenlage lautet `Haendlerbund = handel_gelegentlich`, `Schienenbund = feindselig`, `Arkologie = umkaempft`.
- Der Korridor `H3 -> H12` ist beschaedigt; magnetische Interferenz ist als aktive Gefahr belegt.

Startkern
---------

- Varek Solun
- Kaspar Dorn
- Yara Kest

Mind-Cluster-Anbindung
----------------------

- `novapolis-rp/database-rp/01-factions/eisenkonklave/07-mind-clusters/varek-solun-mind-cluster.md`
- `novapolis-rp/database-rp/01-factions/eisenkonklave/07-mind-clusters/kaspar-dorn-mind-cluster.md`
- `novapolis-rp/database-rp/01-factions/eisenkonklave/07-mind-clusters/yara-kest-mind-cluster.md`

Lokale Tiefenschaerfe (T0)
--------------------------

- Kommandobunker H12: Vareks Leitungs- und Kontrolllinse.
- Handels- und Versorgungszelle: Kaspars schmale Oeffnungsfenster unter Ressourcen- und Sanktionsdruck.
- Sicherheitsleitstand: Yaras Freigabe- und Alarmkette.
- Schadenskorridor `H3 -> H12`: lokaler Engpass fuer jede Oeffnung oder Versorgung.

Erste Stakes
------------

- Jede Oeffnung nach aussen steht unter Sicherheitsvorbehalt.
- Der beschaedigte Zulauf nach `H12` macht Bewegung und Versorgung zum Risiko.
- Konflikt mit dem Schienenbund und Konkurrenzdruck gegen die Arkologie rahmen den Start.

Erster Entscheidungsraum
------------------------

1. Den Schadenskorridor `H3 -> H12` zuerst absichern.
2. Ein gelegentliches Handelsfenster mit dem Haendlerbund trotz Risiko oeffnen.
3. Sicherheit ueber Versorgung priorisieren und H12 weiter verriegeln.
4. Ressourcen eher auf Kontrolle und Archiv-/Infrastrukturziele als auf Offenheit legen.

Fail-forward
------------

- Schlechte Oeffnung fuehrt zuerst zu engeren Freigaben, Zeitverlust oder verschaerfter Kontrolle.
- Uebervorsicht verlangsamt H12, schneidet den Start aber nicht ab.

Nebenstart-Hooks
----------------

- Kommandorouten-Hook: Einstieg ueber Vareks Priorisierung zwischen Kontrolle und Oeffnung.
- Handels-Hook: Einstieg ueber Kaspars belastetes Handelsfenster in der Versorgungszelle.
- Sicherheits-Hook: Einstieg ueber Yaras Schadenskorridor- und Leitstandsfokus.

Reveal-Regeln
-------------

- `pc_visible`: Sicherheitslage, Handelsfreigaben, Korridorschaden, unmittelbarer Druck
- `allies_only`: Kommandokette und konkrete Freigabepfade
- `world_only`: nicht verifizierte Fremdfraktionsplaene und tiefe Archivziele
- `rumor`: Geruechte ueber neue Kontakte oder gegnerische Aktivitaet

Guardrails
----------

- Keine konkrete H12-Innenstruktur erfinden.
- Keine bestätigten Novapolis-Kontakte setzen.
- Keine Dealmengen, Konvoi- oder Waffenlisten behaupten.
