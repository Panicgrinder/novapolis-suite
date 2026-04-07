---
stand: 2026-04-07 11:46
update: Der Produktpfad hinter slot 25 fuehrt jetzt eine modulare Anschlussstufe slot 26-30 als eigene RP-SSOT statt nur eines losen Folgehinweises.
checks: snapshot-lock PASS (2026-04-07 11:46); markdownlint PASS; frontmatter PASS
---

RP Folgekorridor: Slot 26-30
============================

Zweck
-----

Diese SSOT fuehrt den Produktpfad hinter slot 25 in eine dritte Kampagnenstufe. Der Fokus liegt auf einem wiederaufnehmbaren Episodenmodus, enger Rueckkopplung zwischen Innenpfad, Kontaktpfad und duennen Neutralraeumen sowie einem save-/replay-lesbaren Anschluss statt freier Lore-Ausdehnung.

Quellenbasis
------------

- novapolis-dev/docs/process/rp-folgekorridor-slot-21-25.ssot.md
- novapolis-dev/docs/process/rp-startbogen-freie-gruppen-e2.ssot.md
- novapolis-dev/docs/process/rp-startbogen-freie-gruppen-f1.ssot.md
- novapolis-dev/docs/process/rp-startbogen-haendlerbund-g7.ssot.md
- novapolis-dev/docs/process/rp-startbogen-novapolis-d5.ssot.md
- novapolis-dev/docs/process/rp-startbogen-novapolis-c6.ssot.md
- novapolis-dev/docs/process/rp-startgebiete-reveal-matrix.ssot.md
- novapolis-dev/docs/process/text-rpg-product-gate-v1.ssot.md
- novapolis-dev/docs/specs/text-rpg-session-contract-v1.md
- novapolis-rp/database-rp/03-locations/E2.md
- novapolis-rp/database-rp/03-locations/F1.md
- novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5.md
- novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md
- novapolis-rp/database-rp/01-factions/novapolis/05-projects/Nordlinie-01.md
- novapolis-rp/database-rp/01-factions/novapolis/05-projects/Missionslog-Novapolis.md
- novapolis-rp/database-rp/01-factions/haendlerbund/03-locations/G7.md

Korridorvertrag
---------------

- slot 26-30 setzt den episodischen Uebergabeanker aus slot 25 in einen wiederaufnehmbaren Folgebogen um, ohne neue Stations- oder Fraktionskanons zu erfinden.
- D5, C6, G7, E2 und F1 bleiben die einzigen belastbaren Anschlussraeume dieser Stufe; duenne Pfade werden nicht durch freie Tiefennetze ersetzt.
- Jeder Slot muss fuer denselben Produktpfad als Resume-, Save- oder Replay-Anker lesbar bleiben.
- Die Stufe endet mit einem klaren Modulanker fuer spaetere Episoden oder einen weiteren Slotkorridor, nicht mit freier Weltverbreiterung.

Slotfolge
---------

### Slot 26 - Wiedereinstieg nach dem Uebergabeanker ordnen

- Primaerlinse: pc_visible mit Resume- und Reorientierungsdruck.
- Startanker: Episoden- oder Sessionresume aus slot 25.
- Kernentscheidungen:
  1) denselben Schwerpunkt ohne Umbruch weiterziehen,
  2) vor dem Weitermarsch erst Lage, Ressourcen und Kontaktpfade neu sortieren,
  3) den Wiedereinstieg bewusst schmal halten,
  4) einen fruehen Rueckgriff auf vertraute D5/C6-Routinen waehlen.
- Konsequenzklassen: Resume-Klarheit, Zeitverlust, stabile Wiederaufnahme, langsamere Reichweite.
- Fail-forward: Ein holpriger Wiedereinstieg erzeugt Reibung oder Zusatzaufwand, aber keinen Reset des Kampagnenasts.

### Slot 27 - D5/C6 als Belastungsprobe oder Rueckgrat bestaetigen

- Primaerlinse: pc_visible und allies_only im Innenpfad.
- Startanker: laufender Innenpfad zwischen Werkstatt, Nordlinie und Sicherungskette.
- Kernentscheidungen:
  1) D5 als Wartungs- und Planungsrueckgrat festigen,
  2) C6 enger an den aktiven Schwerpunkt koppeln,
  3) Innenstabilitaet vor Reichweite stellen,
  4) beides nur so weit halten, wie der aktuelle Druck es traegt.
- Konsequenzklassen: Wartungsdruck, Innenklarheit, Sicherheitskosten, verzoegerte Aussenbreite.
- Fail-forward: Zu breite Innenarbeit fuehrt zu spaeterem Druck oder engem Fokus, nicht zum Abbruch des Pfads.

### Slot 28 - G7 als Reservekontakt, Tauschfenster oder bewusstes Auslassen

- Primaerlinse: pc_visible mit allies_only Randwissen im Kontaktpfad.
- Startanker: G7 als belegter externer Kontakt- und Rueckzugsraum.
- Kernentscheidungen:
  1) G7 aktiv zur Entlastung und Reichweitenpflege nutzen,
  2) nur minimalen Kontakt halten,
  3) Kontaktpfad zugunsten des Innenpfads bewusst auslassen,
  4) Kontakt nur als Vorbereitung fuer den naechsten Episodenbogen lesen.
- Konsequenzklassen: Aussenreichweite, Konditionsdruck, Reservewert, spaetere Anschlussqualitaet.
- Fail-forward: Kontakt bleibt enger, teurer oder spaeter, aber der Produktpfad verliert dadurch nicht seine Fortsetzbarkeit.

### Slot 29 - E2/F1 als schmale Schleife oder Abschlusskante lesen

- Primaerlinse: pc_visible mit world_only Druck an den Randraeumen.
- Startanker: E2/F1 als duenne Neutralraeume mit begrenzter Anschlussdichte.
- Kernentscheidungen:
  1) E2/F1 als vorsichtige Schleife fuer den laufenden Bogen nutzen,
  2) nur einen der beiden Raeume aktiv anfassen,
  3) den Neutralpfad bewusst schliessen und auf Kernrouten zurueckgehen,
  4) Reichweite nicht ueber schwache Belege hinaus erzwingen.
- Konsequenzklassen: Routenfragilitaet, Informationsgewinn, Erschoepfung, klare Begrenzung.
- Fail-forward: Zu viel Ehrgeiz produziert Zusatzkosten oder Rueckspruenge, aber keinen freien Retcon neuer Knoten.

### Slot 30 - Modulanker fuer die naechste Episode festschreiben

- Primaerlinse: pc_visible mit Produkt- und Uebergabesicht.
- Startanker: konsolidierter Kampagnenstand aus slot 26-29.
- Kernentscheidungen:
  1) die Episode ueber Innenstabilitaet sauber abschliessen,
  2) Kontaktpfad als offenen Folgehebel stehen lassen,
  3) den Neutralpfad bewusst als schmalen Anschluss sichern,
  4) einen klaren Modulanker fuer spaeteren Slot- oder Episodenfortsatz setzen.
- Konsequenzklassen: Wiederanlaufbarkeit, Episodenklarheit, offener Restdruck, sauberer Hand-off.
- Fail-forward: Auch ein rauer Abschluss bleibt ein lesbarer Modulanker statt eines unrettbaren Abrisses.

Konsequenzklassen
-----------------

- Resume-Kosten: Wiederaufnahme braucht Klarheit, Zeit und begrenzte Neuordnung.
- Innenkosten: D5/C6 tragen Stabilitaet, erzeugen aber Wartungs- und Sicherheitsdruck.
- Kontaktkosten: G7 vergroessert Reichweite gegen Konditions- und Fokuskosten.
- Randkosten: E2/F1 bleiben spielbar, aber nie frei skalierbar oder tief vernetzt.
- Modulkosten: Ein sauberer Episodenschnitt verlangt Klarheit statt maximaler Breite.

Guardrails
----------

- Keine neuen Korridore hinter F1, E3 oder anderen Randknoten frei behaupten.
- Keine direkte spielbare Verbindung C6 -> F1 erfinden.
- Keine neuen Crews, Besitzansprueche, Lager- oder Infrastrukturretcons aus dem Episodenmodus ableiten.
- Keine vom Sessionvertrag abweichenden Resume-, Save- oder Replay-Annahmen in den RP-Pfad einbauen.

Weiterer Ausbau
---------------

- Der weitere Ausbau hinter slot 30 soll entweder slot 31-35 als naechste SSOT fuehren oder den Produktpfad explizit in modular benannte Episoden ueber denselben Vertragsrahmen aufspalten.