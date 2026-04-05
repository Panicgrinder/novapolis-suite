---
stand: 2026-04-05 19:43
update: Der zweite Folgekorridor hinter `slot 10` verweist jetzt explizit auf die Kampagnenfolge `slot 16-20` und die neutralen Startboegen `B1/C3`.
checks: snapshot-lock PASS (2026-04-05 19:19); markdownlint PASS; frontmatter PASS
---

RP Folgekorridor: Slot 11-15
============================

Zweck
-----

Diese SSOT fuehrt den ersten belegten Langzeitast hinter `slot 10` weiter. Die Folge-Slots bilden die Konsequenzen einer Innen-, Aussen- oder Pufferpriorisierung auf Nordlinie, Materiallauf, G7-Kontakt und die neutralen Knoten `A2`, `B1` und `C3` ab.

Quellenbasis
------------

- `novapolis-dev/docs/process/rp-folgekorridor-slot-06-10.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-freie-gruppen-a2.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-haendlerbund-g7.ssot.md`
- `novapolis-dev/docs/process/rp-startgebiete-reveal-matrix.ssot.md`
- `novapolis-rp/database-rp/03-locations/A2.md`
- `novapolis-rp/database-rp/03-locations/B1.md`
- `novapolis-rp/database-rp/03-locations/C3.md`
- `novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5.md`
- `novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md`
- `novapolis-rp/database-rp/01-factions/novapolis/05-projects/Nordlinie-01.md`
- `novapolis-rp/database-rp/01-factions/novapolis/05-projects/Missionslog-Novapolis.md`
- `novapolis-rp/database-rp/01-factions/haendlerbund/03-locations/G7.md`
- `novapolis-rp/database-rp/00-admin/Metrokarte-T0.md`

Korridorvertrag
---------------

- `slot 11-15` ist der erste Langzeitfolgeast des Startprodukts und bleibt an bereits belegte Tunnel-, Kontakt- und Neutralpfade gebunden.
- Die Langzeitfolgen laufen ueber Schwerpunktdruck, Sichtbarkeit, Materialbindung und Kontaktkosten statt ueber harte Fail-States.
- Neutrale Pufferknoten duerfen Orientierung, Deckung und Verzoegerung liefern, aber keine frei erfundenen Fraktionsinfrastrukturen.

Slotfolge
---------

### Slot 11 - Innenpfad konsolidieren oder strecken

- Primaerlinse: `pc_visible` mit Langzeitfokus auf `D5/C6`.
- Startanker: Nordlinie-Fortschritt, Materiallauf-Folgen, C6-Betriebsdruck.
- Kernentscheidungen:
  1) Innenpfad weiter konsolidieren,
  2) Material in Folgezyklen strecken,
  3) Tempo zugunsten Schutz und Stabilitaet drosseln,
  4) Aussenkontakt nur flankierend weiterfuehren.
- Konsequenzklassen: Projektstabilitaet, Ressourcenbindung, geringere Aussenreichweite.
- Fail-forward: Ein zu enger Innenpfad verlangsamt Aussenoeffnung, bleibt aber spielbar.

### Slot 12 - Pufferpfad A2/B1 aktiv nutzen

- Primaerlinse: `pc_visible` im neutralen Zwischenraum.
- Startanker: `A2` als aktive Pufferkante, `B1` als Vorfilter vor `B2`.
- Kernentscheidungen:
  1) ueber `A2` Sichtbarkeit klein halten,
  2) `B1` nur als Beobachtungs- und Rueckzugsraum nutzen,
  3) vorsichtigen Anschluss an den `B2`-Korridor suchen,
  4) im Neutralraum Ressourcen und Zeit gegeneinander abwaegen.
- Konsequenzklassen: Sichtbarkeitsgewinn oder -verlust, langsamere aber kontrolliertere Bewegung, schwache Kontaktfenster.
- Fail-forward: Unsichere Schritte fuehren zu Umwegen oder mehr Vorsicht, nicht zum Totalausfall.

### Slot 13 - Aussenpfad G7 vertiefen oder verknappen

- Primaerlinse: `pc_visible`/`allies_only` im Aussenkontakt.
- Startanker: `G7 <-> C6`, Konditionsdruck, Rueckzugsrahmen.
- Kernentscheidungen:
  1) Austauschklassen vertiefen,
  2) nur Informationspfade offenhalten,
  3) Sicherheitsrahmen vor Dealtempo setzen,
  4) Aussenpfad zugunsten Innen- oder Pufferweg verknappen.
- Konsequenzklassen: Dealqualitaet, Wartezeit, Rueckzugssicherheit, spaetere Branchingtiefe.
- Fail-forward: Schlechtere Konditionen oder engeres Fenster statt Abbruch.

### Slot 14 - C3 als teilaktiven Schwellenraum behandeln

- Primaerlinse: `pc_visible` mit Risiko- und Transitdruck.
- Startanker: aktives `B2 -> C3`, partielles `C3 -> D3`, Hazard `HZ-C3-D3-01`.
- Kernentscheidungen:
  1) `C3` nur als kurzen Zwischenhalt nutzen,
  2) Teilaktivitaet absichern, bevor weitergelaufen wird,
  3) den Raum meiden und frueher umschichten,
  4) das Risiko fuer schnellere Verbindung bewusst tragen.
- Konsequenzklassen: Zeitverlust, Sicherheitskosten, spaetere Pfadreichweite.
- Fail-forward: Risiko erzeugt Zusatzaufwand oder Rueckzug, aber keinen harten Endpunkt.

### Slot 15 - Langzeitprioritaet festziehen

- Primaerlinse: `pc_visible` mit Produktzweig.
- Startanker: Innenpfad `D5/C6`, Aussenpfad `G7`, Pufferpfad `A2/B1/C3`.
- Kernentscheidungen:
  1) Novapolis-Kern vertiefen,
  2) Aussenkontakt systematischer ausbauen,
  3) Neutralpuffer als wiederkehrenden Mobilitaets- und Tarnpfad etablieren,
  4) mehrere Pfade offenhalten und dafuer Tempo opfern.
- Konsequenzklassen: Spezialisierung, Reichweite, Reveal-Druck, Langzeitkosten.
- Fail-forward: Jede Wahl verschiebt den spaeteren Kampagnencharakter, ohne den Slice unspielbar zu machen.

Konsequenzklassen
-----------------

- Langzeitkosten: wiederkehrender Material- und Sicherheitsaufwand statt Einmalschaden.
- Pufferkosten: Zeitverlust gegen Sichtbarkeitsreduktion.
- Kontaktkosten: engere Konditionen, verzoegerte Antworten, kleinere Dealfenster.
- Stabilitaetskosten: weniger Expansion zugunsten tragfaehiger Innenpfade.
- Branchkosten: Schwerpunktsetzung auf Innen, Aussen oder Mobilitaet.

Guardrails
----------

- Keine neuen benannten Fraktionen oder Kontaktketten ohne vorhandene SSOTs einfuehren.
- Keine lokalen B1-, A2- oder C3-Crews erfinden.
- Keine Mengen- oder Lagerretcons aus dem Materiallauf ableiten.

Nachfolger
----------

- Die direkte Anschluss-SSOT fuer denselben Produktpfad liegt in `novapolis-dev/docs/process/rp-folgekorridor-slot-16-20.ssot.md`.