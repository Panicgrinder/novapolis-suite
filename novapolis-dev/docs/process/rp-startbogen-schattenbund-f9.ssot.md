---
stand: 2026-04-05 19:43
update: F9 fuehrt jetzt Mind-Cluster-Anbindung, lokale Unterraeume und konservative Nebenstart-Hooks.
checks: snapshot-lock PASS (2026-04-05 10:53); markdownlint PASS; frontmatter PASS
---

RP Startbogen: Schattenbund F9
==============================

Zweck
-----

Dieser Startbogen definiert `F9` als spielbaren Start des Schattenbunds mit Fokus auf verdeckte Warenstroeme, Gegenaufklaerung und Informationskontrolle.

Quellenbasis
------------

- `novapolis-rp/database-rp/01-factions/schattenbund/03-locations/F9.md`
- `novapolis-rp/database-rp/01-factions/schattenbund/02-characters/Nyra-Vehl.md`
- `novapolis-rp/database-rp/01-factions/schattenbund/02-characters/Jarek-Voan.md`
- `novapolis-rp/database-rp/01-factions/schattenbund/02-characters/Sera-Nol.md`
- `novapolis-rp/database-rp/01-factions/schattenbund/05-projects/Missionslog-Schattenbund.md`
- `novapolis-rp/database-rp/01-factions/schattenbund/06-handel-diplomatie/Relationslog-Schattenbund.md`
- `novapolis-rp/database-rp/01-factions/schattenbund/04-inventory/Schattenbund-inventar.md`
- `novapolis-rp/database-rp/00-admin/Stationskontroll-Matrix.md`
- `novapolis-rp/database-rp/00-admin/Metrokarte-T0.md`

Startklasse
-----------

- Modus: `faction_start`
- Bereich: `F9`
- Gebietsklasse: `faction_core`
- Dichtegrad: `full_slice`

Startpraemisse
--------------

Der PC startet in einem Schattenbund-Knoten, in dem jede Bewegung zwischen Beschaffung, Tarnung und Leak-Vermeidung austariert werden muss.

Belegte Ausgangslage
--------------------

- `F9` ist aktiver Schattenbund-Knoten.
- Nyra Vehl fuehrt Strategie und verdeckte Operationen.
- Jarek Voan fuehrt verdeckte Warenstroeme ueber Zwischenhaendler.
- Sera Nol verantwortet Abschirmung und Gegenaufklaerung.
- Die Aussenlage lautet `Novapolis = unbekannt`, `Eisenkonklave = feindselig`, `Arkologie = verdeckt`.
- `F9 -> G6` ist als aktiver Korridor belegt.

Startkern
---------

- Nyra Vehl
- Jarek Voan
- Sera Nol

Mind-Cluster-Anbindung
----------------------

- `novapolis-rp/database-rp/01-factions/schattenbund/07-mind-clusters/nyra-vehl-mind-cluster.md`
- `novapolis-rp/database-rp/01-factions/schattenbund/07-mind-clusters/jarek-voan-mind-cluster.md`
- `novapolis-rp/database-rp/01-factions/schattenbund/07-mind-clusters/sera-nol-mind-cluster.md`

Lokale Tiefenschaerfe (T0)
--------------------------

- Fuehrungszelle: Nyra priorisiert dort Informationskontrolle und verdeckte Zielsetzung.
- Handelszelle: Jarek fuehrt gestaffelte Beschaffung nur ueber schmale Kanaele.
- Sicherheitszentrale: Sera filtert Leaks, Musterbrueche und Zugriff.
- Aktiver Korridor `F9 -> G6`: lokaler Tarnungs- und Bewegungsanker.

Erste Stakes
------------

- Beschaffung funktioniert nur, solange Abschirmung und Kanaldisziplin halten.
- Die feindselige Lage zur Eisenkonklave macht offene Fehler teuer.
- Verdeckte Arkologie-Bezuege duerfen nicht ungefiltert auffliegen.

Erster Entscheidungsraum
------------------------

1. Einen verdeckten Beschaffungslauf absichern statt beschleunigen.
2. Gegenaufklaerung priorisieren und Leaks frueh jagen.
3. Die Kontaktkette bewusst strecken, um Tarnung vor Durchsatz zu stellen.
4. Einen riskanteren Informationsgewinn versuchen, statt nur Gueterfluss zu sichern.

Fail-forward
------------

- Fehlentscheidungen fuehren zuerst zu erhöhter Abschirmung, schlechteren Kanaelen oder internem Misstrauen.
- Ein misslungener Lauf kippt eher in Umwege und neue Deckung als in sofortige Unspielbarkeit.

Nebenstart-Hooks
----------------

- Leitungs-Hook: Einstieg ueber Nyras Fuehrungszelle und Priorisierung verdeckter Operationen.
- Beschaffungs-Hook: Einstieg ueber Jareks Handelszelle und die Frage Tarnung gegen Durchsatz.
- Gegenaufklaerungs-Hook: Einstieg ueber Seras Sicherheitszentrale und Leak-Druck am `G6`-Korridor.

Reveal-Regeln
-------------

- `pc_visible`: lokale Abschirmung, Beschaffungsdruck, unmittelbare Sicherheitsfragen
- `allies_only`: interne Kanal- und Gegenaufklaerungslogik
- `world_only`: ungeprüfte Gegenparteien, tiefe Tarnstrukturen, nicht bestaetigte Zielbilder
- `rumor`: Geruechte ueber Leaks, Gegenparteien oder guenstigere Schattenfenster

Guardrails
----------

- Keine konkreten Gegenparteien oder Routen erfinden.
- Keine offene Diplomatie behaupten, wo nur verdeckte Bezüge belegt sind.
- Keine harten Lager-, Mengen- oder Schmuggelwerte setzen.
