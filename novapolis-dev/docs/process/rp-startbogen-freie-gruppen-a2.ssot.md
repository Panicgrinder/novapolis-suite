---
stand: 2026-04-05 19:43
update: Der A2-Startbogen verweist jetzt auf die neue Orts-SSOT und zieht lokale Tiefenschaerfe sowie Puffer-Hooks fuer A2/B1 nach.
checks: snapshot-lock PASS (2026-04-05 18:49); markdownlint PASS; frontmatter PASS
---

RP Startbogen: Freie Gruppen A2
===============================

Zweck
-----

Dieser Startbogen liefert den ersten belastbaren fraktionslosen Start fuer den Produktpfad.

Quellenbasis
------------

- `novapolis-rp/database-rp/03-locations/A2.md`
- `novapolis-rp/database-rp/03-locations/B1.md`
- `novapolis-rp/database-rp/04-inventory/Freie-Gruppen-inventar.md`
- `novapolis-rp/database-rp/00-admin/Fraktionen-Taxonomie.md`
- `novapolis-rp/database-rp/00-admin/Stationskontroll-Matrix.md`
- `novapolis-rp/database-rp/00-admin/Metrokarte-T0.md`

Startklasse
-----------

- Modus: `factionless_start`
- Bereich: `A2`
- Gebietsklasse: `neutral_transit`
- Dichtegrad: `full_slice`

Belegte Ausgangslage
--------------------

- `A2` ist als `Neutral/Transit` mit Status `aktiv` belegt.
- `A2` hat im T0-Modell eine aktive Hauptzugangsstruktur.
- `A2` sitzt auf einem aktiven Pfad zwischen `A1` und `B1` und damit an einer echten Pufferkante zwischen Kernraeumen.
- `Freie Gruppen` sind als Sammelkategorie fuer fraktionslose NPC explizit belegt.

Startpraemisse
--------------

Der PC startet nicht als Mitglied einer Hauptfraktion, sondern als freie, mobile oder lokal gestrandete Figur in einer neutralen Transitstation. Die Figur verfuegt ueber knappe, nicht spezifizierte Grundressourcen aus dem Scope `Freie Gruppen`, aber ueber keine privilegierten Zugriffsrechte einer Kernfraktion.

Startkern
---------

- PC-Figur aus `Freie Gruppen`
- keine fest eingebettete Fraktionscrew zu Beginn
- Umweltkern: neutrale Station, Durchgangsverkehr, unklare Sicherheitslage, begrenzte Versorgung

Lokale Tiefenschaerfe (T0)
--------------------------

- `A2` ist jetzt als eigener neutraler Transitknoten mit aktiver Kette `A1 -> A2 -> B1` beschrieben.
- `B1` bildet den vorgeschalteten Neutralpuffer vor dem partiellen Schienenbund-Zugang `B1 -> B2`.
- Der Start nutzt Sichtung, Wegwahl und Rueckzug eher als feste Leitungs- oder Lagerstruktur.

Erste Stakes
------------

- Versorgung ist knapp und unstrukturiert.
- Ohne Bindung fehlt Schutz durch feste Freigabe-, Lager- und Funkketten.
- Die Lage in A2 ist offen genug fuer Kontakt, Handel oder Konflikt, aber nicht sicher genug fuer Stillstand.
- Der naechste Schritt entscheidet, ob die Figur Anschluss nach `A1`, `B1` oder in ein anderes neutrales Netzwerk sucht.

Erster Entscheidungsraum
------------------------

1. In `A2` bleiben und lokale Lage sichern.
2. Richtung `A1` gehen und Kontakt zu einem fraktionsnahen Raum suchen.
3. Richtung `B1` gehen und ueber den Pufferkorridor weiter auf `B2` schielen.
4. Ressourcen, Tausch oder Informationen erst lokal beschaffen, bevor eine Seite gewaehlt wird.

Fail-forward
------------

- Fehlentscheidungen fuehren zuerst zu Zeit-, Ressourcen- oder Risikokosten.
- Ein frueher Kontaktabbruch blockiert nicht den gesamten Run, sondern verschiebt nur den spaeteren Fraktionsanschluss.
- Geruechte, Misstrauen oder schlechte Tauschbedingungen sind erlaubt; harte Sackgassen nicht.

Reveal-Regeln
-------------

- `pc_visible`: lokale Stationslage, unmittelbare Knappheit, sichtbare Kontakte und Wegeoptionen
- `allies_only`: nur nach aktivem Anschluss an Kontaktgruppen
- `world_only`: Fraktionsplaene, verdeckte Konfliktabsichten, nicht sichtbare Netzwerklage
- `rumor`: Hinweise auf sichere Routen, Schleichwege oder Fraktionsgeruechte ohne Verifikation

Anschlusslogik
--------------

- Richtung `A1`: moeglicher Anschluss an einen Arkologie-nahen Raum
- Richtung `B1 -> B2`: moeglicher Anschluss an den Schienenbund-Raum
- Bleiben in neutralen Zonen: moeglicher Aufbau eines laengeren fraktionslosen oder haendlernahen Pfads

Nebenstart-Hooks
----------------

- Puffer-Hook: Einstieg ueber `A2` als vorsichtigen Sichtungs- und Kontaktknoten.
- Vorfeld-Hook: Einstieg ueber `B1` als neutralen Vorraum vor dem partiellen `B2`-Korridor.
- Mobilitaets-Hook: Einstieg ueber das Abwaegen von Rueckzug, Weiterlauf und knapper Versorgung statt ueber feste Fraktionsrechte.

Guardrails
----------

- Keine lokale A2-Lore erfinden, die in keiner Orts-SSOT existiert.
- Keine feste Crew oder benannten NPC setzen, solange kein eigener A2-Ortsbogen existiert.
- Keine implizite Fraktionsbindung vor der ersten echten Entscheidung.
