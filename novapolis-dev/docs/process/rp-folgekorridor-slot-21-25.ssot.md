---
stand: 2026-04-07 10:20
update: Der Folgekorridor hinter `slot 20` fuehrt jetzt die naechste Kampagnenstufe `slot 21-25` ueber `E2/F1`, Rueckkopplung und episodischen Uebergang als eigene SSOT.
checks: snapshot-lock PASS (2026-04-07 10:20); markdownlint PASS; frontmatter PASS
---

RP Folgekorridor: Slot 21-25
============================

Zweck
-----

Diese SSOT fuehrt den Produktpfad hinter `slot 20` in eine zweite Kampagnenstufe. Der Fokus liegt auf Rueckkopplung zwischen Innenstabilisierung, neutraler Reichweite ueber `E2/F1`, Aussenkontakt und einem ersten episodischen Uebergabeanker statt bloss weiterer Slotverlaengerung.

Quellenbasis
------------

- `novapolis-dev/docs/process/rp-folgekorridor-slot-16-20.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-freie-gruppen-e2.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-freie-gruppen-f1.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-haendlerbund-g7.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-novapolis-d5.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-novapolis-c6.ssot.md`
- `novapolis-dev/docs/process/rp-startgebiete-reveal-matrix.ssot.md`
- `novapolis-rp/database-rp/03-locations/E2.md`
- `novapolis-rp/database-rp/03-locations/F1.md`
- `novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md`
- `novapolis-rp/database-rp/01-factions/novapolis/05-projects/Nordlinie-01.md`
- `novapolis-rp/database-rp/01-factions/novapolis/05-projects/Missionslog-Novapolis.md`

Korridorvertrag
---------------

- `slot 21-25` vertieft den bestehenden Produktpfad, ohne neue Stations- oder Fraktionskanons zu erfinden.
- `E2` dient als belegter, beschaedigter Neutralraum mit Druck aus Transit, Schaden und Nachhall des Gasunfalls.
- `F1` bleibt ein realer, aber duenner T0-Knoten; ein freier Direktpfad `C6 -> F1` wird nicht behauptet.
- Die Kampagnenstufe endet mit einem episodischen Uebergabeanker, nicht mit einem harten Cliff oder freien Lore-Sprung.

Slotfolge
---------

### Slot 21 - Kampagnenmodus unter Last halten

- Primaerlinse: `pc_visible` mit Rueckkopplung aus `slot 20`.
- Startanker: bereits gewaehlter Kampagnenmodus aus Innenpfad, Kontaktpfad oder mobilem Neutralpfad.
- Kernentscheidungen:
  1) denselben Schwerpunkt trotz Last weiterziehen,
  2) Reichweite zugunsten von Stabilitaet senken,
  3) die mobile Linie fuer Entlastung nutzen,
  4) Kontakt- und Innenpfad neu austarieren.
- Konsequenzklassen: Fokusdruck, Wartungsdruck, Sichtbarkeit, langsamere Expansion.
- Fail-forward: Eine ueberlastete Priorisierung erzeugt Zusatzkosten oder Umwege, aber keinen Kampagnenabbruch.

### Slot 22 - E2 als Druckraum, Detour oder Absicherungsfenster

- Primaerlinse: `pc_visible` mit Transit- und Schadensdruck.
- Startanker: `E2` als aktiver Neutralraum mit scharfer Schadens- und Luftqualitaetslogik.
- Kernentscheidungen:
  1) `E2` als vorsichtigen Durchlauf nutzen,
  2) den Raum nur fuer begrenzte Absicherung verwenden,
  3) Belastung fuer Zeitgewinn akzeptieren,
  4) Rueckzug zugunsten sichererer Pfade waehlen.
- Konsequenzklassen: Reichweite, Belastung, Sicherheits- und Versorgungsdruck.
- Fail-forward: Zu riskante Nutzung fuehrt zu Verzoegerung, Erschoepfung oder engerem Korridor, nicht zu Unspielbarkeit.

### Slot 23 - F1 als duenne Vorwaertslinie oder bewusstes Nein

- Primaerlinse: `pc_visible` mit world-only Randwissen.
- Startanker: `F1` als realer T0-Knoten mit bewusst begrenzter Anschlussdichte.
- Kernentscheidungen:
  1) `F1` als schmale Vorwaertslinie akzeptieren,
  2) den Knoten nur als Beobachtungsfenster lesen,
  3) Reichweite nicht erzwingen,
  4) einen Ruecksprung auf stabilere Pfade vorziehen.
- Konsequenzklassen: Routenfragilitaet, Informationsgewinn, Vorsichtskosten.
- Fail-forward: Ein zu ambitionierter Zugriff produziert Unsicherheit und Mehrarbeit, aber keinen freien Retcon oder Totalausfall.

### Slot 24 - Innen-, Kontakt- und Neutralpfad wieder zusammenfuehren

- Primaerlinse: `pc_visible`/`allies_only` im Rueckkopplungsfenster.
- Startanker: D5/C6-Innenpfad, `G7`-Kontakt und Neutralpfade `E2/F1`.
- Kernentscheidungen:
  1) Innenpfad vor Reichweite schuetzen,
  2) Kontaktpfad zur Entlastung nutzen,
  3) Neutralpfad als episodische Bruecke halten,
  4) Breite zugunsten klarer Identitaet wieder reduzieren.
- Konsequenzklassen: Synergie, Fokusverlust, Rueckkopplungskosten.
- Fail-forward: Unguenstige Kopplung erzeugt Reibung und spaeteren Nachholbedarf, nicht aber einen harten Dead End.

### Slot 25 - Episodischen Uebergabeanker festziehen

- Primaerlinse: `pc_visible` mit Produkt- und Replaysicht.
- Startanker: laufender Kampagnenmodus nach `slot 21-24`.
- Kernentscheidungen:
  1) eine Episode auf Innenstabilisierung enden lassen,
  2) eine Episode auf Kontakt- oder Mobilitaetsdruck enden lassen,
  3) den naechsten Bogen als hybride Rueckkopplung vorbereiten,
  4) einen klaren Save-/Replay-geeigneten Uebergabeanker setzen.
- Konsequenzklassen: Wiederanlaufbarkeit, Fokusklarheit, offener Druck fuer den Folgebogen.
- Fail-forward: Auch ein unsauberer Abschluss bleibt ein lesbarer Uebergabepunkt statt eines unrettbaren Kampagnenabbruchs.

Konsequenzklassen
-----------------

- Kampagnenlast: wiederkehrender Fokus- und Wartungsdruck.
- Routenfragilitaet: `E2/F1` bleiben belastbar, aber nicht frei skalierbar.
- Kontaktreibung: Aussenkontakt bringt Reichweite gegen Konditions- und Sicherheitskosten.
- Uebergabekosten: Ein episodischer Abschluss braucht Klarheit statt maximaler Breite.

Guardrails
----------

- Keine direkte spielbare `C6 -> F1`-Verbindung frei behaupten.
- Keine neuen Crews, Besitzansprueche oder verdeckten Fraktionsrechte in `E2/F1` erfinden.
- Keine freie Tiefennetzausdehnung hinter `F1` oder `E3` setzen.
- Keine harten Lager-, Mengen- oder Infrastrukturretcons aus dem Kampagnenpfad ableiten.

Weiterer Ausbau
---------------

- Der naechste Ausbau hinter `slot 25` soll entweder `slot 26-30` als neue SSOT fuehren oder den Produktpfad bewusst in modulare Episodenform aufspalten.