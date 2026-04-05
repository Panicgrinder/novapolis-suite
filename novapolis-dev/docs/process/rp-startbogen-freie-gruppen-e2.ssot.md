---
stand: 2026-04-05 19:43
update: E2 ist jetzt als eigener neutraler Startbogen fuer Freie Gruppen mit Schadennachhall und aktiver Transitlogik festgezogen.
checks: snapshot-lock PASS (2026-04-05 19:33); markdownlint PASS; frontmatter PASS
---

RP Startbogen: Freie Gruppen E2
===============================

Zweck
-----

Dieser Startbogen hebt `E2` als weiteren fraktionslosen Neutralstart auf einen eigenen spielbaren Einstiegsbogen.

Quellenbasis
------------

- `novapolis-rp/database-rp/03-locations/E2.md`
- `novapolis-rp/database-rp/01-factions/novapolis/05-projects/Missionslog-Novapolis.md`
- `novapolis-rp/database-rp/01-factions/novapolis/02-characters/Jonas-Merek.md`
- `novapolis-rp/database-rp/04-inventory/Freie-Gruppen-inventar.md`
- `novapolis-rp/database-rp/00-admin/Fraktionen-Taxonomie.md`
- `novapolis-rp/database-rp/00-admin/Stationskontroll-Matrix.md`
- `novapolis-rp/database-rp/00-admin/Metrokarte-T0.md`

Startklasse
-----------

- Modus: `factionless_start`
- Bereich: `E2`
- Gebietsklasse: `neutral_transit`
- Dichtegrad: `full_slice`

Belegte Ausgangslage
--------------------

- `E2` ist als `Neutral/Transit` mit Status `aktiv` belegt.
- `E1 -> E2` und `E2 -> F2` sind aktiv.
- Der Zugang `E3 -> E2` bleibt geschaedigt/ eingeschraenkt und fuehrt einen aktiven Struktur-Hazard.
- `E2` ist als Gasunfall-Station im aktiven Novapolis-Kontext belegt.

Startpraemisse
--------------

Der PC startet in einem aktiven Neutralraum, dessen Bewegungsfreiheit real ist, der aber durch einen belegten Schadens- und Erinnerungskontext gezeichnet bleibt. `E2` ist kein leerer Transitknoten, sondern ein Raum, in dem offene Wege und belastete Vergangenheit zugleich spuerbar sind.

Startkern
---------

- PC-Figur aus `Freie Gruppen`
- Umweltkern: aktiver Transit, geschaedigter E3-Bezug, Nachhall eines belegten Unfalls

Lokale Tiefenschaerfe (T0)
--------------------------

- `E2` verbindet aktive Neutralrouten mit einem riskanteren E3-Rand.
- Der belegte Gasunfall-Nachhall macht den Raum emotional und praktisch aufgeladen, ohne neue Figuren zu setzen.
- Die sichere Wahl und die erinnerungsbelastete Wahl liegen hier sichtbar dicht beieinander.

Erste Stakes
------------

- Wer `E2` nutzt, muss den Unterschied zwischen aktiven und geschaedigten Pfaden ernst nehmen.
- Der Raum bietet Reichweite, aber keine neutrale Beliebigkeit.
- Ein Vorstoss Richtung E3 steht unter deutlich hoeherem Risiko als Bewegung ueber `E1` oder `F2`.

Erster Entscheidungsraum
------------------------

1. `E2` als aktiven Transit- und Sichtungsraum nutzen.
2. Die E3-Naehe vorsichtig antesten, statt sie zu ignorieren.
3. Sich auf die stabileren aktiven Pfade `E1/F2` konzentrieren.
4. Risiko, Erinnerung und Reichweite gegeneinander abwaegen.

Fail-forward
------------

- Riskante Bewegung fuehrt zuerst zu Rueckzug, Verzoegerung oder engerer Vorsicht.
- Zu viel Vorsicht kostet Reichweite, beendet den Run aber nicht.

Reveal-Regeln
-------------

- `pc_visible`: aktive Wege, geschaedigter E3-Bezug, sichtbarer Schadendruck
- `allies_only`: situative Reise- oder Warnabsprachen nach aktivem Anschluss
- `world_only`: tiefere Ursachen oder Anschlusslagen jenseits des unmittelbaren Schadenskontexts
- `rumor`: ungesicherte Hinweise auf sicherere Fenster oder Restnutzung Richtung E3

Nebenstart-Hooks
----------------

- Schadens-Hook: Einstieg ueber den Gegensatz zwischen aktivem Transit und hohem E3-Risiko.
- Erinnerungs-Hook: Einstieg ueber den belegten Nachhall des Gasunfalls.
- Mobilitaets-Hook: Einstieg ueber Reichweite mit realen Kosten.

Guardrails
----------

- Keine lokale E2-Crew oder feste Stationsleitung erfinden.
- Keine freien Detailretcons zum Gasunfall oder zu E3 setzen.
- Keine lokale Innenarchitektur ueber die Orts-SSOT hinaus setzen.