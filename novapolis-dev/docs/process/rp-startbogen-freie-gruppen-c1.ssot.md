---
stand: 2026-04-05 19:43
update: C1 ist jetzt als eigener neutraler Startbogen fuer Freie Gruppen mit aktivem Transit- und Richtungsraum festgezogen.
checks: snapshot-lock PASS (2026-04-05 19:24); markdownlint PASS; frontmatter PASS
---

RP Startbogen: Freie Gruppen C1
===============================

Zweck
-----

Dieser Startbogen hebt `C1` als weiteren fraktionslosen Neutralstart auf einen eigenen spielbaren Einstiegsbogen.

Quellenbasis
------------

- `novapolis-rp/database-rp/03-locations/C1.md`
- `novapolis-rp/database-rp/03-locations/D1.md`
- `novapolis-rp/database-rp/04-inventory/Freie-Gruppen-inventar.md`
- `novapolis-rp/database-rp/00-admin/Fraktionen-Taxonomie.md`
- `novapolis-rp/database-rp/00-admin/Stationskontroll-Matrix.md`
- `novapolis-rp/database-rp/00-admin/Metrokarte-T0.md`

Startklasse
-----------

- Modus: `factionless_start`
- Bereich: `C1`
- Gebietsklasse: `neutral_transit`
- Dichtegrad: `full_slice`

Belegte Ausgangslage
--------------------

- `C1` ist als `Neutral/Transit` mit Status `aktiv` belegt.
- `C2 -> C1 -> D1` ist aktiv und macht `C1` zu einem offenen Richtungsraum.
- `Freie Gruppen` bleiben der fraktionslose Anker fuer Figuren ohne feste Zugehoerigkeit.

Startpraemisse
--------------

Der PC startet in einem neutralen Transitknoten, der weniger von Engpaessen als von offener Wegwahl und fehlender Schutzinstitution gepraegt ist. `C1` ist ein guter Start fuer mobile, vorsichtige oder suchende Figuren, die Bewegung vor Bindung priorisieren.

Startkern
---------

- PC-Figur aus `Freie Gruppen`
- Umweltkern: aktiver Transit, offene Wegwahl, knappe Absicherung

Lokale Tiefenschaerfe (T0)
--------------------------

- `C1` ist ein aktiver Durchlaufraum mit zwei belastbaren Anschluessen.
- `D1` bildet den naechsten Uebergangsraum, in dem der Weiterlauf bereits unsicherer wird.
- Der Start lebt von Richtungs- und Timingentscheidungen statt von Besitz oder institutionellem Schutz.

Erste Stakes
------------

- Offene Bewegung schafft Reichweite, aber wenig Rueckhalt.
- Wer zu lange in `C1` bleibt, gewinnt keine feste Basis, sondern nur mehr Beobachtungsdruck.
- Der Schritt nach `D1` oeffnet den Raum, fuehrt aber zugleich in einen weniger sicheren Folgepfad.

Erster Entscheidungsraum
------------------------

1. `C1` als offenen Sichtungs- und Richtungsraum nutzen.
2. Zuegig nach `D1` weitergehen, solange die aktive Kette traegt.
3. Rueckzug oder Umorientierung Richtung `C2` bevorzugen.
4. Mobilitaet gegen Sichtbarkeit und Versorgung abwaegen.

Fail-forward
------------

- Fehlentscheidungen fuehren zuerst zu Wegverlust, Verzoegerung oder mehr Sichtbarkeit.
- Ein zu frueher Vorstoss macht den Lauf nicht unspielbar, sondern verschiebt nur den Folgepfad.

Reveal-Regeln
-------------

- `pc_visible`: aktive Korridorlage, unmittelbare Wegeoptionen, sichtbare Offenheit des Raums
- `allies_only`: situative Reise- oder Tauschabsprachen nach aktivem Anschluss
- `world_only`: nicht sichtbare Folgepfade oder verdeckte Lage jenseits des unmittelbaren Transitkontexts
- `rumor`: ungesicherte Hinweise auf bessere Weiterlaeufe oder ruhigere Zonen

Nebenstart-Hooks
----------------

- Transit-Hook: Einstieg ueber `C1` als offenen Durchlaufraum.
- Richtungs-Hook: Einstieg ueber die Frage, ob `D1` oder der Ruecklauf priorisiert wird.
- Mobilitaets-Hook: Einstieg ueber Reichweite ohne feste Schutzrechte.

Guardrails
----------

- Keine lokale C1-Crew oder feste Stationsleitung erfinden.
- Keine tieferen Anschlusslagen ohne eigene Orts-SSOTs behaupten.
- Keine freie Innenarchitektur ueber die Orts-SSOT hinaus setzen.