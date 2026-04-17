---
stand: 2026-04-18 00:55
update: Der Folgepfad hinter slot 30 fuehrt jetzt auch die kanonische player-facing Kurzformel fuer den ersten aktiven RP-Anschluss.
checks: snapshot-lock PASS (2026-04-18 00:55); markdownlint=PASS; frontmatter=PASS
---

RP Folgekorridor: Slot 31-35
============================

Zweck
-----

Diese SSOT fuehrt den Produktpfad hinter `slot 30` in eine vierte Kampagnenstufe. Der Fokus liegt auf einem operativen Wiedereinstieg nach dem Slice-2-Handover, erneuter Schwerpunktbildung zwischen Innenpfad, Kontaktpfad und schmalem Neutralpfad sowie einem belastbaren Folgeanker statt freier Weltverbreiterung.

Quellenbasis
------------

- `novapolis-dev/docs/process/rp-folgekorridor-slot-26-30.ssot.md`
- `novapolis-dev/docs/process/text-rpg-slice-2-handover-v1.ssot.md`
- `novapolis-dev/docs/process/text-rpg-product-gate-v1.ssot.md`
- `novapolis-dev/docs/specs/text-rpg-session-contract-v1.md`
- `novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5.md`
- `novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md`
- `novapolis-rp/database-rp/01-factions/novapolis/05-projects/Nordlinie-01.md`
- `novapolis-rp/database-rp/01-factions/novapolis/05-projects/Missionslog-Novapolis.md`
- `novapolis-rp/database-rp/01-factions/haendlerbund/03-locations/G7.md`
- `novapolis-rp/database-rp/03-locations/E2.md`
- `novapolis-rp/database-rp/03-locations/F1.md`

Korridorvertrag
---------------

- `slot 31-35` setzt `Text-RPG Slice 2 Handover v1` ohne Namens- oder Vertragsdrift in eine spielbare Folgephase um.
- Die knappe player-facing Kurzformel fuer diesen Wiedereinstieg lautet verbindlich: `Weiter im selben Lauf: offener Druck, offene Aufgaben, klarer naechster Zug.`
- `D5`, `C6`, `G7`, `E2` und `F1` bleiben weiterhin die einzigen belastbaren Anschlussraeume; neue Stationen, Direktverbindungen oder Fraktionsrechte werden nicht frei ergaenzt.
- Der Slice bleibt resume-, save- und replay-lesbar; `slot 35` endet mit einem klaren Folgeanker statt mit einem losen Lore-Sprung.
- Innenpfad, Kontaktpfad und Neutralpfad bleiben gegeneinander verschiebbar, aber keiner dieser Pfade darf den bestehenden Missions- und Reveal-Rahmen verlassen.

Slotfolge
---------

### Slot 31 - Handover in einen belastbaren Arbeitsrhythmus ueberfuehren

- Primaerlinse: `pc_visible` mit Resume- und Taktkonsolidierung.
- Startanker: derselbe Resume-Anker aus `slot 30`.
- Player-facing Lesart: `Weiter im selben Lauf: offener Druck, offene Aufgaben, klarer naechster Zug.`
- Kernentscheidungen:
  1) den begonnenen Schwerpunkt direkt weiterfahren,
  2) erst Lage und Ressourcen neu ordnen,
  3) Kontaktpfad oder Neutralpfad nur kontrolliert wieder oeffnen,
  4) den Slice bewusst auf wenige lesbare Naechstschritte begrenzen.
- Konsequenzklassen: Taktklarheit, Startverzoegerung, stabile Wiederaufnahme, begrenzte Reichweite.
- Fail-forward: Ein holpriger Neustart kostet Tempo oder Flexibilitaet, aber nicht den Kampagnenast.

### Slot 32 - D5 und C6 als gekoppeltes Rueckgrat unter Folgedruck halten

- Primaerlinse: `pc_visible` mit `allies_only`-Rueckkopplung im Innenpfad.
- Startanker: Werkstatt-, Sicherungs- und Nordlinienkontext zwischen `D5` und `C6`.
- Kernentscheidungen:
  1) `D5` als Planungs- und Wartungskern priorisieren,
  2) `C6` enger an die laufende Schwerpunktarbeit binden,
  3) Innenstabilitaet nur minimal gegen Aussenreichweite tauschen,
  4) den laufenden Druck fuer klare Priorisierung nutzen.
- Konsequenzklassen: Wartungsdruck, Sicherheitskosten, Innenklarheit, spaeterer Aussenbedarf.
- Fail-forward: Zu breite Innenarbeit produziert Folgekosten oder Zeitverlust, aber keinen Abbruch des Slice.

### Slot 33 - G7 als Reservehebel, Tauschpfad oder bewusst knapper Kontakt

- Primaerlinse: `pc_visible` mit `allies_only`-Randwissen im Kontaktpfad.
- Startanker: `G7` als belegter externer Kontakt- und Rueckzugsraum.
- Kernentscheidungen:
  1) `G7` aktiv zur Entlastung und Reichweitenpflege nutzen,
  2) nur einen schmalen Kontaktkanal offenhalten,
  3) Kontakt zugunsten des Innenpfads vertagen,
  4) Kontakt nur als Vorbereitung fuer den naechsten Folgeblock lesen.
- Konsequenzklassen: Reichweitengewinn, Konditionsdruck, Reservewert, spaetere Anschlussqualitaet.
- Fail-forward: Ein enger oder spaeter Kontakt reduziert Spielraum, aber zerlegt den Produktpfad nicht.

### Slot 34 - E2 und F1 als begrenzte Puffer- oder Druckraeume lesen

- Primaerlinse: `pc_visible` mit `world_only`-Druck an den Randraeumen.
- Startanker: `E2/F1` als duenne Neutralraeume ohne freie Tiefennetzlogik.
- Kernentscheidungen:
  1) `E2/F1` als vorsichtige Pufferlinie nutzen,
  2) nur einen Raum aktiv anfassen,
  3) Reichweite bewusst klein halten,
  4) den Neutralpfad zugunsten stabilerer Korridore wieder schliessen.
- Konsequenzklassen: Routenfragilitaet, Informationsgewinn, Erschoepfung, klare Begrenzung.
- Fail-forward: Zuviel Ehrgeiz fuehrt zu Zusatzkosten, Rueckschritt oder engerem Fokus, nicht zu freier Kanonerweiterung.

### Slot 35 - Folgeanker fuer den naechsten Kampagnenblock festschreiben

- Primaerlinse: `pc_visible` mit Produkt- und Uebergabesicht.
- Startanker: konsolidierter Slice-2-Stand aus `slot 31-34`.
- Kernentscheidungen:
  1) den Innenpfad als stabiles Rueckgrat abschliessen,
  2) den Kontaktpfad als offenen Folgehebel markieren,
  3) den Neutralpfad bewusst schmal und lesbar halten,
  4) einen klaren Anschluss fuer `slot 36+` oder einen weiteren modulartigen Episodenbogen setzen.
- Konsequenzklassen: Wiederanlaufbarkeit, Fokusklarheit, offener Restdruck, sauberer Hand-off.
- Fail-forward: Auch ein rauer Abschluss bleibt ein belastbarer Folgeanker statt eines freien Abrisses.

Konsequenzklassen
-----------------

- Resume-Kosten: Der Wiedereinstieg braucht Klarheit, Zeit und bewusst begrenzte Breite.
- Innenkosten: `D5/C6` sichern Stabilitaet gegen Wartungs- und Sicherheitsdruck.
- Kontaktkosten: `G7` vergroessert Reichweite gegen Konditions- und Fokusverlust.
- Randkosten: `E2/F1` bleiben nutzbar, aber nie frei skalierbar oder tief vernetzt.
- Folgekosten: Ein lesbarer Handover verlangt Schwerpunktklarheit statt maximaler Expansion.

Guardrails
----------

- Keine direkte spielbare Verbindung `C6 -> F1` frei behaupten.
- Keine neuen Stationen, Crews, Besitzansprueche oder Infrastrukturretcons aus dem Folgekorridor ableiten.
- Keine neue Tiefennetz- oder Fraktionslogik hinter `E2/F1` frei erfinden.
- Keine vom Sessionvertrag abweichenden Resume-, Save- oder Replay-Annahmen in den RP-Pfad einbauen.

Weiterer Ausbau
---------------

- Der weitere Ausbau hinter `slot 35` soll entweder `slot 36-40` als naechste SSOT fuehren oder einen explizit benannten Folgeblock unter demselben Vertragsrahmen ausweisen.
