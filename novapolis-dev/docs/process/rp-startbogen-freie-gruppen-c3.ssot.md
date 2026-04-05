---
stand: 2026-04-05 19:43
update: C3 ist jetzt als eigener neutraler Startbogen fuer Freie Gruppen mit teilaktivem Schwellenraum und Hazard-Druck festgezogen.
checks: snapshot-lock PASS (2026-04-05 19:19); markdownlint PASS; frontmatter PASS
---

RP Startbogen: Freie Gruppen C3
===============================

Zweck
-----

Dieser Startbogen hebt `C3` als dritten fraktionslosen Neutralstart auf einen eigenen spielbaren Einstiegsbogen.

Quellenbasis
------------

- `novapolis-rp/database-rp/03-locations/C3.md`
- `novapolis-rp/database-rp/03-locations/B1.md`
- `novapolis-rp/database-rp/01-factions/schienenbund/03-locations/B2.md`
- `novapolis-rp/database-rp/04-inventory/Freie-Gruppen-inventar.md`
- `novapolis-rp/database-rp/00-admin/Fraktionen-Taxonomie.md`
- `novapolis-rp/database-rp/00-admin/Stationskontroll-Matrix.md`
- `novapolis-rp/database-rp/00-admin/Metrokarte-T0.md`

Startklasse
-----------

- Modus: `factionless_start`
- Bereich: `C3`
- Gebietsklasse: `neutral_transit`
- Dichtegrad: `full_slice`

Belegte Ausgangslage
--------------------

- `C3` ist als `Neutral/Transit` mit Status `teilaktiv` belegt.
- `B2 -> C3` ist aktiv, `C3 -> D3` nur partiell.
- Der Hazard `HZ-C3-D3-01` markiert einen belegten Mikro-Kollaps im Weiterlauf.
- `Freie Gruppen` bleiben der fraktionslose Anker fuer Figuren ohne feste Zugehoerigkeit.

Startpraemisse
--------------

Der PC startet in einem neutralen Schwellenraum, in dem Bewegung moeglich, aber nie selbstverstaendlich ist. `C3` ist kein Staging-Hub, sondern ein riskanter Zwischenhalt, an dem Weiterlauf, Rueckzug und Aufenthaltsdauer staendig neu austariert werden muessen.

Startkern
---------

- PC-Figur aus `Freie Gruppen`
- Umweltkern: teilaktiver Zugang, Mikro-Kollaps-Risiko, knappe Sicherheitsmarge

Lokale Tiefenschaerfe (T0)
--------------------------

- `C3` trennt den aktiven `B2`-Weiterlauf von einem bereits geschwaechten Korridor Richtung `D3`.
- Der Raum ist durch Transit und Gefahrenwahrnehmung geprägt, nicht durch feste Institutionen.
- Jede Bewegung muss Tempo gegen Sicherheit stellen.

Erste Stakes
------------

- Wer in `C3` bleibt, sammelt Lagebild, setzt sich aber laenger einem schwachen Schutzraum aus.
- Wer Richtung `D3` drueckt, nimmt teilaktive Strecke und Mikro-Kollaps-Risiko bewusst in Kauf.
- Wer zurueck nach `B2` oder weiter in sichere Bereiche ausweicht, verliert Reichweite, gewinnt aber Stabilitaet.

Erster Entscheidungsraum
------------------------

1. `C3` nur als kurzen Zwischenhalt und Sichtungsraum nutzen.
2. Den partiellen Weiterlauf Richtung `D3` trotz Risiko versuchen.
3. Nach `B2` oder in einen stabileren Rueckraum ausweichen.
4. Zeit investieren, um den Hazard besser einzuschaetzen, statt sofort weiterzugehen.

Fail-forward
------------

- Riskante Bewegung fuehrt zuerst zu Umweg, Rueckzug oder Zusatzvorsicht.
- Zu langes Zaudern kostet Tempo und Reichweite, beendet den Run aber nicht.

Reveal-Regeln
-------------

- `pc_visible`: teilaktive Lage, sichtbarer Hazard-Druck, unmittelbare Wegwahl
- `allies_only`: situative Abstimmung ueber Rueckzug, Timing oder Weiterlauf
- `world_only`: tiefere Anschlusslagen hinter `D3` oder nicht sichtbare Folgenketten
- `rumor`: ungesicherte Hinweise auf sichere Durchlaeufe oder alternative Wege

Nebenstart-Hooks
----------------

- Schwellen-Hook: Einstieg ueber `C3` als fragilen Zwischenraum statt stabilen Startbasis.
- Risiko-Hook: Einstieg ueber den Mikro-Kollaps und die Frage nach Tempo gegen Sicherheit.
- Mobilitaets-Hook: Einstieg ueber Rueckzug, Ausweichen oder vorsichtigen Vorstoss.

Guardrails
----------

- Keine lokale C3-Crew oder feste Stationsleitung erfinden.
- Keine Details zu `D3` ueber die belegte Teilaktivitaet hinaus behaupten.
- Keine Hazard-Folgen frei zu Grossereignissen aufblasen.