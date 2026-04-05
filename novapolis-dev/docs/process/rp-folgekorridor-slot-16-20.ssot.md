---
stand: 2026-04-05 19:43
update: Der Folgekorridor hinter `slot 15` fuehrt jetzt die erste Kampagnenfolge fuer Innen-, Aussen- und Mobilitaetspfad als eigene SSOT.
checks: snapshot-lock PASS (2026-04-05 19:19); markdownlint PASS; frontmatter PASS
---

RP Folgekorridor: Slot 16-20
============================

Zweck
-----

Diese SSOT fuehrt den Produktpfad hinter `slot 15` in eine erste stabile Kampagnenfolge. Der Fokus liegt auf wiederkehrender Innenstabilisierung, neutraler Mobilitaet ueber `B1/C3`, dem Aussenpfad `G7` und der Rueckkopplung dieser Entscheidungen aufeinander.

Quellenbasis
------------

- `novapolis-dev/docs/process/rp-folgekorridor-slot-11-15.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-freie-gruppen-b1.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-freie-gruppen-c3.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-freie-gruppen-a2.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-haendlerbund-g7.ssot.md`
- `novapolis-dev/docs/process/rp-startgebiete-reveal-matrix.ssot.md`
- `novapolis-rp/database-rp/03-locations/B1.md`
- `novapolis-rp/database-rp/03-locations/C3.md`
- `novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5.md`
- `novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md`
- `novapolis-rp/database-rp/01-factions/novapolis/05-projects/Nordlinie-01.md`
- `novapolis-rp/database-rp/01-factions/novapolis/05-projects/Missionslog-Novapolis.md`
- `novapolis-rp/database-rp/01-factions/haendlerbund/03-locations/G7.md`

Korridorvertrag
---------------

- `slot 16-20` fuehrt den ersten Kampagnenrahmen fort, ohne neue Lore- oder Stationslogik zu erfinden.
- Innen-, Aussen- und Mobilitaetspfad bleiben kombinierbar, kosten aber zunehmend Fokus und Tempo.
- Neutrale Starts `A2/B1/C3` duerfen in dieser Phase als wiederkehrende Bewegungs- und Tarnpfade dienen, nicht als voll ausgebaute Fraktionsbasen.

Slotfolge
---------

### Slot 16 - Wiederkehrenden Schwerpunkt festigen

- Primaerlinse: `pc_visible` mit Kampagnenfokus.
- Startanker: zuvor gewaehlt gewordener Innen-, Aussen- oder Mobilitaetspfad.
- Kernentscheidungen:
  1) Schwerpunkt verdoppeln,
  2) zweiten Pfad flankierend oeffnen,
  3) Tempo zugunsten Stabilitaet reduzieren,
  4) Sichtbarkeit gegen Reichweite neu balancieren.
- Konsequenzklassen: Kampagnenidentitaet, Fokuskosten, langsamere Breite.
- Fail-forward: Ueberdehnung erzeugt Folgekosten statt Totalausfall.

### Slot 17 - B1 als wiederkehrendes Vorfeld oder Engpass

- Primaerlinse: `pc_visible` im neutralen Vorfeld.
- Startanker: `B1` als wiederkehrender Filterraum vor `B2`.
- Kernentscheidungen:
  1) `B1` als Beobachtungs- und Rueckzugsfenster etablieren,
  2) ihn nur situativ und schmal nutzen,
  3) den partiellen `B2`-Kontakt forcieren,
  4) den Raum zugunsten anderer Pfade meiden.
- Konsequenzklassen: Mobilitaetsgewinn, Sichtbarkeitsdruck, Engpasskosten.
- Fail-forward: Zu aggressive Nutzung fuehrt zu Verzoegerung oder Rueckzug, nicht zum Dead End.

### Slot 18 - C3 als Schwellenroute oder Risikobremse

- Primaerlinse: `pc_visible` mit Transitrisiko.
- Startanker: teilaktives `C3`, Mikro-Kollaps, begrenzte Aufenthaltsqualitaet.
- Kernentscheidungen:
  1) `C3` als schmale Vorwaertsroute nutzen,
  2) den Raum bewusst meiden,
  3) Risiko fuer Zeitgewinn tragen,
  4) Zeit fuer bessere Einschaetzung investieren.
- Konsequenzklassen: Reichweite, Sicherheitskosten, Kampagnentempo.
- Fail-forward: Riskante Nutzung fuehrt zu Zusatzaufwand oder Ruecksprung, nicht zu Unspielbarkeit.

### Slot 19 - Aussenkontakt rueckkoppeln oder abschirmen

- Primaerlinse: `pc_visible`/`allies_only` im Kontaktpfad.
- Startanker: `G7`, bestehende Austauschklassen, Rueckzugsrahmen.
- Kernentscheidungen:
  1) G7 enger an den laufenden Schwerpunkt binden,
  2) Kontakt nur als Reserve- oder Infofenster halten,
  3) Innenpfad vor Kontaktpfad schuetzen,
  4) Mobilitaetspfad zur Kontaktabsicherung nutzen.
- Konsequenzklassen: Konditionsdruck, Aussenreichweite, Fokusverlust oder Synergie.
- Fail-forward: Kontakt verengt sich oder verteuert sich, reißt den Produktpfad aber nicht ab.

### Slot 20 - Ersten Kampagnenmodus fixieren

- Primaerlinse: `pc_visible` mit Produkt- und Kampagnenrahmen.
- Startanker: belastbarer Innenpfad, schmaler Aussenpfad, wiederkehrender Neutralpfad.
- Kernentscheidungen:
  1) kampagnenartige Innenstabilisierung priorisieren,
  2) kontaktgetriebene Kampagne aufbauen,
  3) mobilen Neutralpfad als dominanten Spielmodus setzen,
  4) bewusst hybriden Kampagnenmodus halten.
- Konsequenzklassen: Wiederholbarkeit, Reichweite, Sichtbarkeit, Wartungsdruck.
- Fail-forward: Keine Wahl blockiert die Kampagne; sie praegt nur ihren weiteren Schwerpunkt.

Konsequenzklassen
-----------------

- Kampagnenkosten: wiederkehrende Fokus-, Zeit- und Sicherheitsbindung.
- Mobilitaetskosten: neutrale Pfade bleiben flexibel, aber nie voll abgesichert.
- Kontaktkosten: Konditionen, Verzoegerung und Abschirmdruck im Aussenpfad.
- Innenkosten: langsamere Expansion zugunsten stabilerer Kernraeume.
- Hybridkosten: mehr Breite auf Kosten von Klarheit und Tempo.

Guardrails
----------

- Keine neuen Crew-, Stations- oder Fraktionsbeziehungen ohne eigene SSOTs setzen.
- Keine Details hinter `D3` oder tiefere Netze hinter `B2` frei behaupten.
- Keine stillen Mengen-, Lager- oder Infrastruktur-Retcons aus Mobilitaetspfaden ableiten.