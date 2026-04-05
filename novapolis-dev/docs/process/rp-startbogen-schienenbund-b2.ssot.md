---
stand: 2026-04-05 19:43
update: B2 fuehrt jetzt Mind-Cluster-Anbindung, lokale Unterraeume und konservative Nebenstart-Hooks.
checks: snapshot-lock PASS (2026-04-05 10:53); markdownlint PASS; frontmatter PASS
---

RP Startbogen: Schienenbund B2
==============================

Zweck
-----

Dieser Startbogen definiert `B2` als spielbaren Start fuer den Schienenbund, obwohl Diplomatie- und Ortsdetails lokal noch duenn sind.

Quellenbasis
------------

- `novapolis-rp/database-rp/01-factions/schienenbund/03-locations/B2.md`
- `novapolis-rp/database-rp/01-factions/schienenbund/02-characters/Helia-Vorn.md`
- `novapolis-rp/database-rp/01-factions/schienenbund/02-characters/Rian-Kord.md`
- `novapolis-rp/database-rp/01-factions/schienenbund/02-characters/Tera-Solm.md`
- `novapolis-rp/database-rp/01-factions/schienenbund/05-projects/Missionslog-Schienenbund.md`
- `novapolis-rp/database-rp/01-factions/schienenbund/04-inventory/Schienenbund-inventar.md`
- `novapolis-rp/database-rp/00-admin/Stationskontroll-Matrix.md`
- `novapolis-rp/database-rp/00-admin/Metrokarte-T0.md`

Startklasse
-----------

- Modus: `faction_start`
- Bereich: `B2`
- Gebietsklasse: `faction_core`
- Dichtegrad: `full_slice`

Startpraemisse
--------------

Der PC startet in einem aktiven Schienenbund-Knoten, der vor allem ueber Netzhoheit, Trassenbetrieb, Reparaturfokus und Zugangskontrolle definiert ist.

Belegte Ausgangslage
--------------------

- `B2` ist aktiver Schienenbund-Knoten und in der Stationskontroll-Matrix als Basis, gross markiert.
- Helia Vorn fuehrt den Schienenbund strategisch und territorial.
- Rian Kord steuert Handels- und Routenfenster.
- Tera Solm fuehrt Sicherheit, Sperrprotokolle und Freigaben.
- Der Schienenbund ist als logistischer Reparatur- und Baukontext gerahmt.
- `B1 -> B2` ist nur partiell, `B2 -> C3` dagegen aktiv; der Start ist damit zugleich Betriebs- und Engpassstart.

Startkern
---------

- Helia Vorn
- Rian Kord
- Tera Solm

Mind-Cluster-Anbindung
----------------------

- `novapolis-rp/database-rp/01-factions/schienenbund/07-mind-clusters/helia-vorn-mind-cluster.md`
- `novapolis-rp/database-rp/01-factions/schienenbund/07-mind-clusters/rian-kord-mind-cluster.md`
- `novapolis-rp/database-rp/01-factions/schienenbund/07-mind-clusters/tera-solm-mind-cluster.md`

Lokale Tiefenschaerfe (T0)
--------------------------

- Kommandoknoten: Helias Netzhoheits- und Prioritaetenlinse.
- Handelszentrale: Rians Durchsatz- und Transitfenster unter enger Freigabe.
- Sicherheitsleitstand: Teras Sperr- und Zugangskontrolle.
- Trassenengpass `B1 -> B2` bei aktivem `B2 -> C3`: lokaler Konfliktherd zwischen Reparatur und Betrieb.

Erste Stakes
------------

- Netzhoheit und Durchsatz sind wichtiger als offene Diplomatie.
- Ein partieller Zugang nach `B1` erzeugt dauernden Sicherungs- und Reparaturdruck.
- Bau- und Reparaturgueter sind zentral, aber nicht quantifiziert.

Erster Entscheidungsraum
------------------------

1. Den partiellen `B1`-Korridor zuerst absichern oder verbessern.
2. Einen Handels- oder Transitkorridor nur unter strikten Freigaben oeffnen.
3. Material und Baukapazitaet auf Netzbetrieb statt Wachstum konzentrieren.
4. Sicherheit gegen Durchsatz gewichten und die Trasse enger kontrollieren.

Fail-forward
------------

- Falsche Priorisierung fuehrt zuerst zu Engpaessen, Wartezeit oder strengeren Sperrfenstern.
- Ein zu offener Transit kippt eher in Gegenmassnahmen als in unmittelbaren Kollaps.

Nebenstart-Hooks
----------------

- Netzhoheits-Hook: Einstieg ueber Helias Entscheidung im Kommandoknoten.
- Transit-Hook: Einstieg ueber Rians Freigabefenster in der Handelszentrale.
- Sperr-Hook: Einstieg ueber Teras Leitstand und den partiellen `B1`-Engpass.

Reveal-Regeln
-------------

- `pc_visible`: Betriebsdruck, Trassenlage, Freigabefenster, Reparaturprioritaeten
- `allies_only`: interne Sperrlogik und Sicherheitsentscheidungen
- `world_only`: nicht belastbare Fremdfraktionsdeutungen
- `rumor`: ungesicherte Hinweise auf stoerende Akteure oder bessere Routen

Guardrails
----------

- Keine externen Beziehungen erfinden, die lokal nicht belegt sind.
- Keine konkrete B2-Ortsarchitektur setzen.
- Keine Mengen oder Lieferlisten behaupten.
