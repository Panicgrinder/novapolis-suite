---
stand: 2026-04-05 19:43
update: D1 ist jetzt als eigener neutraler Startbogen fuer Freie Gruppen mit Uebergangs- und Teilaktivitaetsdruck festgezogen.
checks: snapshot-lock PASS (2026-04-05 19:24); markdownlint PASS; frontmatter PASS
---

RP Startbogen: Freie Gruppen D1
===============================

Zweck
-----

Dieser Startbogen hebt `D1` als weiteren fraktionslosen Neutralstart auf einen eigenen spielbaren Einstiegsbogen.

Quellenbasis
------------

- `novapolis-rp/database-rp/03-locations/D1.md`
- `novapolis-rp/database-rp/03-locations/C1.md`
- `novapolis-rp/database-rp/04-inventory/Freie-Gruppen-inventar.md`
- `novapolis-rp/database-rp/00-admin/Fraktionen-Taxonomie.md`
- `novapolis-rp/database-rp/00-admin/Stationskontroll-Matrix.md`
- `novapolis-rp/database-rp/00-admin/Metrokarte-T0.md`

Startklasse
-----------

- Modus: `factionless_start`
- Bereich: `D1`
- Gebietsklasse: `neutral_transit`
- Dichtegrad: `full_slice`

Belegte Ausgangslage
--------------------

- `D1` ist als `Neutral/Transit` mit Status `aktiv` belegt.
- `C1 -> D1` ist aktiv, `D1 -> D2` nur partiell.
- `Freie Gruppen` bleiben der fraktionslose Anker fuer Figuren ohne feste Zugehoerigkeit.

Startpraemisse
--------------

Der PC startet in einem neutralen Uebergangsknoten, der offen genug fuer Bewegung, aber nicht stabil genug fuer sorglose Expansion ist. `D1` eignet sich fuer Figuren, die den Schritt in einen unsichereren Folgepfad bewusst abwaegen wollen.

Startkern
---------

- PC-Figur aus `Freie Gruppen`
- Umweltkern: aktiver Rueckraum, partieller Folgepfad, zunehmender Unsicherheitsdruck

Lokale Tiefenschaerfe (T0)
--------------------------

- `D1` ist ein neutraler Uebergangsraum hinter `C1` und vor der teilaktiven Strecke nach `D2`.
- Der Raum belohnt Timing, nicht Besitz.
- Die Differenz zwischen aktivem Rueckraum und partiellem Vorlauf ist der Kern des Starts.

Erste Stakes
------------

- Wer in `D1` bleibt, haelt sich im Uebergang auf, ohne echte Stabilitaet zu gewinnen.
- Wer nach `D2` drueckt, riskiert Tempo- und Sicherheitskosten.
- Wer nach `C1` rueckorientiert, tauscht Reichweite gegen Sicherheit.

Erster Entscheidungsraum
------------------------

1. `D1` als taktischen Uebergangsraum nutzen.
2. Den partiellen Vorlauf nach `D2` vorsichtig antesten.
3. Nach `C1` zurueckgehen und die aktive Kette bevorzugen.
4. Sichtbarkeit, Reichweite und Versorgung neu austarieren.

Fail-forward
------------

- Zu frueher Druck auf `D2` fuehrt zuerst zu Rueckzug, Verzoegerung oder engerer Vorsicht.
- Rueckorientierung kostet Tempo, blockiert den Run aber nicht.

Reveal-Regeln
-------------

- `pc_visible`: Uebergangslage, aktive Rueckroute, partieller Folgepfad
- `allies_only`: situative Reise- oder Rueckzugsabsprachen nach aktivem Anschluss
- `world_only`: nicht sichtbare Anschlusslagen hinter `D2` oder tieferer Netzkontext
- `rumor`: ungesicherte Hinweise auf tragfaehigere Fenster oder alternative Routen

Nebenstart-Hooks
----------------

- Uebergangs-Hook: Einstieg ueber `D1` als neutralen Schwellenraum.
- Vorsichts-Hook: Einstieg ueber die Frage, wann ein partieller Pfad tragbar ist.
- Rueckzugs-Hook: Einstieg ueber die Balance zwischen `C1`-Rueckraum und `D2`-Vorlauf.

Guardrails
----------

- Keine lokale D1-Crew oder feste Stationsleitung erfinden.
- Keine Details zu `D2` ueber die belegte Teilaktivitaet hinaus behaupten.
- Keine freie Innenarchitektur ueber die Orts-SSOT hinaus setzen.