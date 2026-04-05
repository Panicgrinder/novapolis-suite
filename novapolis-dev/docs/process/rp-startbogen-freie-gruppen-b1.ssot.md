---
stand: 2026-04-05 19:43
update: B1 ist jetzt als eigener neutraler Startbogen fuer Freie Gruppen mit Vorpuffer- und Schienenbund-Anschlusslogik festgezogen.
checks: snapshot-lock PASS (2026-04-05 19:19); markdownlint PASS; frontmatter PASS
---

RP Startbogen: Freie Gruppen B1
===============================

Zweck
-----

Dieser Startbogen hebt `B1` als zweiten fraktionslosen Neutralstart auf einen eigenen spielbaren Einstiegsbogen.

Quellenbasis
------------

- `novapolis-rp/database-rp/03-locations/B1.md`
- `novapolis-rp/database-rp/03-locations/A2.md`
- `novapolis-rp/database-rp/01-factions/schienenbund/03-locations/B2.md`
- `novapolis-rp/database-rp/04-inventory/Freie-Gruppen-inventar.md`
- `novapolis-rp/database-rp/00-admin/Fraktionen-Taxonomie.md`
- `novapolis-rp/database-rp/00-admin/Stationskontroll-Matrix.md`
- `novapolis-rp/database-rp/00-admin/Metrokarte-T0.md`

Startklasse
-----------

- Modus: `factionless_start`
- Bereich: `B1`
- Gebietsklasse: `neutral_transit`
- Dichtegrad: `full_slice`

Belegte Ausgangslage
--------------------

- `B1` ist als `Neutral/Transit` mit Status `aktiv` belegt.
- `B1` haengt aktiv an `A2` und nur partiell an `B2`.
- `B1` ist vorgeschalteter Filterraum vor dem Schienenbund-Kern, ohne selbst ein fraktionaler Kommandoraum zu sein.
- `Freie Gruppen` bleiben der fraktionslose Anker fuer Figuren ohne feste Zugehoerigkeit.

Startpraemisse
--------------

Der PC startet in einem neutralen Vorpuffer, in dem jede Bewegung bereits unter dem Schatten kommender Sperr- und Reparaturregeln steht. `B1` ist kein sicherer Ruhepunkt, sondern ein Raum fuer vorsichtige Annäherung, Rueckzug oder Beobachtung Richtung `B2`.

Startkern
---------

- PC-Figur aus `Freie Gruppen`
- Umweltkern: partieller Weiterlauf, knappe Planungssicherheit, offener Transitdruck

Lokale Tiefenschaerfe (T0)
--------------------------

- `B1` ist der neutrale Vorraum vor dem partiellen `B2`-Korridor.
- `A2` bleibt der Rueckzugs- und Ausweichraum, falls der Schritt nach `B2` zu frueh oder zu riskant wird.
- Die Schienenbund-Naehe ist funktional spuerbar, aber nicht als eigener sozialer oder diplomatischer Startkern belegt.

Erste Stakes
------------

- Wer in `B1` bleibt, gewinnt Zeit und Sichtung, verliert aber Tempo.
- Wer Richtung `B2` drueckt, riskiert Sperr-, Reparatur- und Sichtbarkeitskosten.
- Der Raum bietet keine festen Rechte, nur vorsichtige Bewegungsoptionen.

Erster Entscheidungsraum
------------------------

1. `B1` als Beobachtungs- und Rueckzugsraum nutzen.
2. Den partiellen `B2`-Weiterlauf vorsichtig antesten.
3. Nach `A2` zurueckfallen und dort Kontakt oder Versorgung neu ordnen.
4. Zeit gegen Sichtbarkeit tauschen und auf ein besseres Fenster warten.

Fail-forward
------------

- Ein misslungener Vorstoss fuehrt zuerst zu Rueckzug, Verzoegerung oder engerer Vorsicht.
- Uebervorsicht kostet Reichweite, blockiert den Run aber nicht.

Reveal-Regeln
-------------

- `pc_visible`: Korridorlage, partielle Weiterfuehrung, unmittelbarer Transitdruck
- `allies_only`: situative Reise- oder Kontaktabsprachen nach aktivem Anschluss
- `world_only`: tiefere B2-Sperrlogik oder nicht sichtbare Anschlusslagen
- `rumor`: Geruechte ueber guenstigere Fenster oder schnellere Durchlaeufe

Nebenstart-Hooks
----------------

- Vorfeld-Hook: Einstieg ueber `B1` als neutralen Filterraum vor `B2`.
- Rueckzugs-Hook: Einstieg ueber den Wechsel zwischen `A2`-Rueckraum und `B2`-Vorlauf.
- Taktik-Hook: Einstieg ueber Wegwahl, Timing und Sichtbarkeit statt ueber feste Besitzrechte.

Guardrails
----------

- Keine lokale B1-Crew oder feste Stationsleitung erfinden.
- Keine implizite Schienenbund-Freigabe behaupten.
- Keine lokale Innenarchitektur ueber die bestehende Orts-SSOT hinaus setzen.