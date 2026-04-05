---
stand: 2026-04-05 19:43
update: Der erste Folgekorridor hinter `slot 05` verweist jetzt explizit auf die Langzeitfolge `slot 11-15` und die neutralen Puffer-SSOTs.
checks: snapshot-lock PASS (2026-04-05 18:49); markdownlint PASS; frontmatter PASS
---

RP Folgekorridor: Slot 06-10
============================

Zweck
-----

Diese SSOT fuehrt den kanonischen Novapolis-Folgekorridor hinter `slot 05` weiter. Der Fokus liegt auf Tunnelarbeit, dem belegten Materiallauf `D5 -> C6`, dem kontrollierten Aussenkontakt ueber `G7` und einer ersten stabilen Verzweigung nach innen oder aussen.

Quellenbasis
------------

- `novapolis-dev/docs/process/rp-folgekorridor-slot-00-05.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-novapolis-d5.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-novapolis-c6.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-haendlerbund-g7.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-freie-gruppen-a2.ssot.md`
- `novapolis-dev/docs/process/rp-startkorridor-reveal-matrix.ssot.md`
- `novapolis-dev/docs/process/rp-startgebiete-reveal-matrix.ssot.md`
- `novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5.md`
- `novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md`
- `novapolis-rp/database-rp/01-factions/novapolis/05-projects/Nordlinie-01.md`
- `novapolis-rp/database-rp/01-factions/novapolis/05-projects/Missionslog-Novapolis.md`
- `novapolis-rp/database-rp/01-factions/haendlerbund/03-locations/G7.md`

Korridorvertrag
---------------

- `slot 06-10` bleibt derselben Fail-Forward-Logik wie `slot 00-05` verpflichtet.
- Der Korridor baut nur auf bereits belegten Pfaden auf: Nordlinie, Materiallauf, C6-Uebergabe, G7-Kontaktfenster, neutrale Pufferkante `A2`.
- Kein Slot zwingt einen einzigen Branch als einzig richtige Loesung auf; der Lauf verzweigt in Schwerpunktpfade statt in harte Sackgassen.

Slotfolge
---------

### Slot 06 - Nordlinie priorisieren

- Primaerlinse: `pc_visible` mit Projektbezug in `D5`.
- Startanker: Nordlinie-Stand `E/S/B`, Tunnelarbeit, Trassen- und Sicherungsdruck.
- Kernentscheidungen:
  1) Abschnitt A weiter sichern,
  2) Abschnitt B/Trasse priorisieren,
  3) Werkstatt- und Materialbedarf vor Arbeit vorziehen,
  4) Tunneltempo zugunsten Basisstabilitaet drosseln.
- Konsequenzklassen: Projektgeschwindigkeit, Sicherheitsaufschlag, Materialbindung.
- Fail-forward: Falsche Gewichtung verlangsamt oder verteuert den Tunnelpfad, blockiert ihn aber nicht.
- Folgeartefakte: `Nordlinie-01.md`, `D5.md`.

### Slot 07 - Materiallauf D5 -> C6 vorbereiten und fahren

- Primaerlinse: `pc_visible` in D5, mit spaeterem `allies_only`-Uebergang nach C6.
- Startanker: belegter Materiallauf, Verpacken/Abmeldung/Transport, ReflexAssist.
- Kernentscheidungen:
  1) schmalen Versorgungslauf priorisieren,
  2) breiteren Baustellenlauf wagen,
  3) Schutz und Transporttempo neu balancieren,
  4) Lauf verschieben und erst Tunnel-/Basislage stabilisieren.
- Konsequenzklassen: Ressourcenbindung, Zeitkosten, C6-Versorgungsdruck, Risikoaufschlaege im Transit.
- Fail-forward: Ein schlechter Lauf kippt in Verzoegerung, Zusatzschutz oder engere Baustellenverteilung statt in Totalausfall.
- Folgeartefakte: `Missionslog-Novapolis.md`, `Nordlinie-01.md`, `D5.md`.

### Slot 08 - C6 Empfang, Bestandsaufnahme und Baustellenverteilung

- Primaerlinse: `allies_only`, kontrolliert nach `pc_visible` hebbar.
- Startanker: bestaetigter Empfang, Bestandsaufnahme, nachgelagerte Baustellenverteilung.
- Kernentscheidungen:
  1) Primaerlager/Baustelle zuerst versorgen,
  2) Sicherheits- und Schutzbedarf gegen Betriebsaufnahme gewichten,
  3) D5 frueh Rueckmeldung geben,
  4) lokale Reserven enger halten.
- Konsequenzklassen: Reveal-Geschwindigkeit, Baustellenfortschritt, C6-Sicherheitsmarge.
- Fail-forward: Schlechte Verteilung erzeugt Folgeaufwand und Misstrauen, aber keinen dead stop.
- Folgeartefakte: `Missionslog-Novapolis.md`, `C6.md`, Reveal-Matrix.

### Slot 09 - G7-Kontaktfenster und Aussenkontakt

- Primaerlinse: `pc_visible` oder `allies_only` je nach Kontaktseite.
- Startanker: `G7 <-> C6`, Deal- und Rueckzugsrahmen, Austauschklassen `Energie/Reparaturen/Kommunikationszugang <-> Nahrung/Filter/Grundbedarf`.
- Kernentscheidungen:
  1) Kontaktpfad vertiefen,
  2) erst Sicherheits- und Rueckzugsrahmen absichern,
  3) Deal enger pruefen,
  4) Informationen vor Waren priorisieren.
- Konsequenzklassen: Konditionsdruck, Wartezeit, externe Sichtbarkeit, spaetere Fraktionspfade.
- Fail-forward: Misslungener Kontakt fuehrt zu engeren Fenstern oder Umwegpfaden, nicht zum Abbruch.
- Folgeartefakte: `rp-startbogen-haendlerbund-g7.ssot.md`, `G7.md`, spaetere Aussenzweige.

### Slot 10 - Schwerpunktwahl nach innen oder aussen

- Primaerlinse: `pc_visible` mit Branch-Entscheidung.
- Startanker: Tunnelstand, C6-Versorgung, G7-Kontakt, Pufferlogik `A2`.
- Kernentscheidungen:
  1) Innenpfad: D5/C6/Nordlinie weiter priorisieren,
  2) Aussenpfad: G7-Kontakt und externe Austauschfenster ausbauen,
  3) Pufferpfad: ueber neutrale Routen wie `A2` oder aehnliche Pufferraeume Sichtbarkeit klein halten,
  4) Mischpfad: Fortschritt breiter verteilen und dafuer Tempo opfern.
- Konsequenzklassen: Sichtbarkeit, Branching, Ressourcenstreckung, Sicherheits- und Kontaktkosten.
- Fail-forward: Kein Branch ist singulaer; jede Wahl verschiebt den spaeteren Schwerpunkt statt den Lauf zu beenden.
- Folgeartefakte: Nachfolgende Korridor- oder Startgebiets-SSOTs, Reveal-Matrizen, Missions- und Projektlogs.

Konsequenzklassen
-----------------

- Projektkosten: Nordlinie-Fortschritt, Baustellen- oder Reparaturtempo.
- Transferkosten: Verpackung, Transport, Empfang, Verteilungsaufwand.
- Sichtbarkeitskosten: wann und wie C6-, G7- oder Pufferwissen sichtbar wird.
- Aussenkontaktkosten: Konditionen, Wartezeiten, sicherheitliche Auflagen, Verhandlungsdruck.
- Branchkosten: Fokusverlust oder Spezialisierung auf Innen-, Aussen- oder Mischpfad.

Guardrails
----------

- Keine konkreten Mengen, Chargen oder Inventarquoten setzen, die ueber den belegten Materiallauf hinausgehen.
- Keine neuen Fraktionskontakte oder Gegenparteien ohne belegten Startbogen/Relationslog behaupten.
- Kein `world_only`-Wissen aus G7, A2 oder anderen Startgebieten ungefiltert in den PC-Zweig heben.

Nachfolger
----------

- Die direkte Anschluss-SSOT fuer denselben Produktpfad liegt in `novapolis-dev/docs/process/rp-folgekorridor-slot-11-15.ssot.md`.