---
stand: 2026-04-05 19:43
update: F1 ist jetzt als eigener neutraler Startbogen fuer Freie Gruppen mit realem Stationsstatus und schmalem Folgepfad festgezogen.
checks: snapshot-lock PASS (2026-04-05 19:33); markdownlint PASS; frontmatter PASS
---

RP Startbogen: Freie Gruppen F1
===============================

Zweck
-----

Dieser Startbogen hebt `F1` als weiteren fraktionslosen Neutralstart auf einen eigenen spielbaren Einstiegsbogen.

Quellenbasis
------------

- `novapolis-rp/database-rp/03-locations/F1.md`
- `novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md`
- `novapolis-rp/database-rp/04-inventory/Freie-Gruppen-inventar.md`
- `novapolis-rp/database-rp/00-admin/Fraktionen-Taxonomie.md`
- `novapolis-rp/database-rp/00-admin/Stationskontroll-Matrix.md`
- `novapolis-rp/database-rp/00-admin/Metrokarte-T0.md`

Startklasse
-----------

- Modus: `factionless_start`
- Bereich: `F1`
- Gebietsklasse: `neutral_transit`
- Dichtegrad: `full_slice`

Belegte Ausgangslage
--------------------

- `F1` ist als `Neutral/Transit` mit Status `aktiv` belegt.
- `F1 -> F3` ist nur partiell.
- `F1` ist im aktiven C6-Kontext als realer Linien-/Stationsbezug belegt und nicht mehr nur stationsloser Codename.

Startpraemisse
--------------

Der PC startet in einem realen, aber operativ noch duennen Neutralraum. `F1` ist kein voll abgesicherter Knoten, sondern ein Start aus Netzrelevanz, Unschaerfe und vorsichtiger Vorwaertsbewegung.

Startkern
---------

- PC-Figur aus `Freie Gruppen`
- Umweltkern: aktiver Stationsraum, partieller Folgepfad, historischer Linienbezug ohne sichere Direktverbindung

Lokale Tiefenschaerfe (T0)
--------------------------

- `F1` ist ein realer Stationsknoten mit knapper, aber belastbarer Eigenexistenz.
- Der partielle F3-Pfad macht jede Vorwaertsbewegung kostenbehaftet.
- Der C6-Bezug sorgt fuer Netzgewicht, ohne freie Novapolis-Integration zu begruenden.

Erste Stakes
------------

- Wer `F1` nutzt, startet aus einem echten Knoten, aber ohne dichte Schutz- oder Besitzstruktur.
- Der schmale Weiterlauf nach `F3` macht Reichweite teuer.
- Der Raum darf nicht mehr als blosses Geruecht gelesen werden, bleibt aber operativ duenn.

Erster Entscheidungsraum
------------------------

1. `F1` als vorsichtigen Sichtungs- und Ausgangsraum nutzen.
2. Den partiellen `F3`-Weiterlauf antesten.
3. Den Raum nur kurz nutzen und auf sicherere Netzknoten umorientieren.
4. Netzrelevanz gegen reale operative Duennheit abwaegen.

Fail-forward
------------

- Zu fruehe Expansion fuehrt zuerst zu Rueckzug, Zeitverlust oder vorsichtigerer Planung.
- Zu viel Vorsicht kostet Reichweite, blockiert den Start aber nicht.

Reveal-Regeln
-------------

- `pc_visible`: realer Stationsstatus, partieller Folgepfad, unmittelbare Transitfragen
- `allies_only`: situative Reise- oder Rueckzugsabsprachen nach aktivem Anschluss
- `world_only`: tiefere Linien- oder Netzkontexte jenseits des unmittelbaren Stationsrahmens
- `rumor`: ungesicherte Hinweise auf bessere Fenster oder tiefere Anschluesse

Nebenstart-Hooks
----------------

- Linien-Hook: Einstieg ueber `F1` als realen, aber nicht uebervoll belegten Netzknoten.
- Engpass-Hook: Einstieg ueber den partiellen Folgepfad nach `F3`.
- Kontext-Hook: Einstieg ueber die Spannung zwischen C6-Bezug und neutralem Eigenstatus.

Guardrails
----------

- Keine lokale F1-Crew oder feste Stationsleitung erfinden.
- Keine direkte C6-F1-Vollverbindung behaupten, solange die Topologie das nicht traegt.
- Keine freie Innenarchitektur ueber die Orts-SSOT hinaus setzen.