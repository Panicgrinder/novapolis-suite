---
stand: 2026-04-05 19:43
update: Der erste spielbare Folgekorridor `slot 00-05` verweist jetzt explizit auf die Folge-SSOT `slot 06-10` und die erweiterte Reveal-Matrix der weiteren Startgebiete.
checks: snapshot-lock PASS (2026-04-05 11:34); markdownlint PASS; frontmatter PASS
---

RP Folgekorridor: Slot 00-05
============================

Zweck
-----

Diese SSOT kanonisiert den ersten spielbaren Folgekorridor des Novapolis-Starts als mehrslotige Folgeform. Sie uebersetzt das Arbeitsblatt in einen belastbaren Slot-Vertrag fuer Spielleitung, Missionslog, Reveal-Pfade und spaetere State-/Replay-Systeme.

Quellenbasis
------------

- `novapolis-dev/docs/process/rp-text-rpg-startpaket-slot-00-05-2026-04-05.md`
- `novapolis-dev/docs/process/rp-startbogen-novapolis-d5.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-novapolis-c6.ssot.md`
- `novapolis-dev/docs/process/rp-startkorridor-reveal-matrix.ssot.md`
- `novapolis-dev/docs/process/rp-startgebiete-reveal-matrix.ssot.md`
- `novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5.md`
- `novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md`
- `novapolis-rp/database-rp/01-factions/novapolis/05-projects/Nordlinie-01.md`
- `novapolis-rp/database-rp/01-factions/novapolis/05-projects/Missionslog-Novapolis.md`
- `novapolis-rp/database-rp/01-factions/novapolis/02-characters/Ronja-Kerschner.md`
- `novapolis-rp/database-rp/01-factions/novapolis/02-characters/Reflex.md`
- `novapolis-rp/database-rp/01-factions/novapolis/02-characters/Jonas-Merek.md`
- `novapolis-rp/database-rp/01-factions/novapolis/02-characters/Pahl-Brenner.md`
- `novapolis-rp/database-rp/01-factions/novapolis/02-characters/Kora-Malenkov.md`
- `novapolis-rp/database-rp/01-factions/novapolis/02-characters/Echo.md`

Korridorvertrag
---------------

- `slot 00-05` ist ein kanonischer Folgekorridor, kein freies Szenenbasteln.
- Jeder Slot fuehrt eine primaere Linse, zulaessige Konsequenzklassen und mindestens einen fail-forward-faehigen Ausweichpfad.
- Kein Slot darf den Lauf mit einem einzelnen Fehlgriff hart beenden; Kosten laufen ueber Zeit, Sicherheit, Ressourcen, Reveal und Beziehungsdruck.
- `world_only`- und Mind-Cluster-Rohdaten bleiben auch im Folgekorridor von PC-Text getrennt.
- Persistenz laeuft ueber vorhandene SSOTs statt ueber freie Sessionnotizen.

Persistenz- und Log-Vertrag
---------------------------

- Missions- und Projektfolgen werden in `Missionslog-Novapolis.md` und `Nordlinie-01.md` gespiegelt.
- Orts- und Reveal-Folgen bleiben an `D5.md`, `C6.md` und `rp-startkorridor-reveal-matrix.ssot.md` gebunden.
- Beziehungs- oder Innenlagen werden nie als Rohwerte geschrieben, sondern nur ueber Entscheidungen, Freigaben und sichtbare Reaktionen in Charakter-/Missions-/Log-Kontexten verdichtet.
- Spaetere Agent-/Replay-Implementierungen sollen pro Slot mindestens `pc_log`, `world_log`, `mission_delta`, `reveal_delta` und `resource_or_security_cost` unterscheiden.

Slotfolge
---------

### Slot 00 - D5 Wartungsauftrag und vorsichtige Beobachtung

- Primaerlinse: `pc_visible` in D5.
- Startanker: Wartungsgang, Werkzeugtasche, lokale Unsicherheit.
- Kernentscheidungen:
  1) vorsichtig beobachten,
  2) Werkzeugtasche sichern oder markieren,
  3) Jonas oder Pahl frueh einbinden,
  4) allein weitergehen.
- Konsequenzklassen: Zeitkosten, erste Sicherheitsaufschlaege, leichte Misstrauens- oder Freigabedeltas.
- Fail-forward: Auch ein Fehlgriff fuehrt hoechstens zu Zusatzkontrolle, spaeterem Reveal oder engerem Teamrahmen.
- Folgeartefakte: `Missionslog-Novapolis.md` (Wartungsanker), `D5.md` (lokale Lage), spaeter `Ronja`/`Reflex`-Handlungsfenster.

### Slot 01 - D5 Terminal, Port und System-Link

- Primaerlinse: `pc_visible` mit `log/reflex`-Pfad.
- Startanker: D5-Terminal, moeglicher System-Link, Schutz- und Dämpfungsrisiko.
- Kernentscheidungen:
  1) tiefer in den Link gehen,
  2) Reflex Schutz priorisieren,
  3) Jonas technisch dazuholen,
  4) sichere Analyse vertagen.
- Konsequenzklassen: Systemrauschen, Schutzbedarf, Erkenntnisgewinn oder Erkenntnisaufschub.
- Fail-forward: Riskante Nutzung erzeugt Rauschen oder Belastung, aber keinen harten Session-Abbruch.
- Folgeartefakte: `D5.md` Knowledge/Actions, `Reflex.md` Schutz-/Scanfade, Reveal-Matrix fuer `log/reflex`.

### Slot 02 - D5 Werkstatt-, Funk- und Freigabepfad

- Primaerlinse: `pc_visible` mit teaminterner Verzweigung.
- Startanker: Werkstattkern, Funkoption, Hausregeln und Freigabepfad ueber Pahl.
- Kernentscheidungen:
  1) Funk priorisieren,
  2) Pahl fuer Sicherheits- oder Belastungsabwaegung holen,
  3) Jonas fuer Werkstatt-/Tunnelkontext aktivieren,
  4) C6-Status aktiv abfragen.
- Konsequenzklassen: Freigabekosten, Teamdruck, Umpriorisierung von Tunnel- gegen Basisarbeit.
- Fail-forward: Schlechte Priorisierung verschiebt nur, welcher Folgepfad spaeter teurer wird.
- Folgeartefakte: `D5.md`, `Missionslog-Novapolis.md`, `Nordlinie-01.md`, Folgewissen fuer D5 -> C6.

### Slot 03 - C6 Sicherung und Markierung als Parallelfaden

- Primaerlinse: `world_only`, spaeter kontrolliert Richtung `allies_only` hebbar.
- Startanker: C6-N3, Sicherung/Markierung, lokaler Risikodruck.
- Kernentscheidungen:
  1) Marker `7A` strikt im Sicherungsmodus halten,
  2) Such- und Schutzaufwand austarieren,
  3) Meldung nach D5 staffeln oder lokal halten,
  4) Echo-/Kora-Protokolle eng fuehren.
- Konsequenzklassen: Reveal-Verzoegerung, Sicherheitskosten, spaeterer Informationsdruck in D5.
- Fail-forward: Spaeterer oder enger Reveal erhoeht Unschaerfe, blockiert den Lauf aber nicht.
- Folgeartefakte: `C6.md`, `Missionslog-Novapolis.md`, Reveal-Matrix.

### Slot 04 - C6 Abschluss, Uebergabe und Echo-Moment

- Primaerlinse: `allies_only` mit optionalem kontrolliertem PC-Reveal.
- Startanker: Uebergabemoment, Echo-Schutzsignal, Freigabefenster.
- Kernentscheidungen:
  1) Abschluss lokal konsolidieren,
  2) D5 frueh informieren,
  3) nur Log-/Funkweg freigeben,
  4) Schutz vor Tempo priorisieren.
- Konsequenzklassen: Reveal-Geschwindigkeit, Teamvertrauen, spaetere Vorbereitung fuer Tunnel- oder Materialentscheidungen.
- Fail-forward: Ein enger Reveal verlangsamt nur die D5-Reaktion und erzeugt keinen Dead End.
- Folgeartefakte: `C6.md`, `Missionslog-Novapolis.md`, `rp-startkorridor-reveal-matrix.ssot.md`.

### Slot 05 - D5 Grundriss-/Systemordnung und Nordlinie-Fenster

- Primaerlinse: `pc_visible` mit Projektbezug.
- Startanker: D5-Ordnung, Nordlinie, Materiallauf, C6-Reveal.
- Kernentscheidungen:
  1) D5 erst stabilisieren,
  2) Tunnel/Nordlinie pushen,
  3) Materiallauf vorbereiten,
  4) C6-Reveal systematisch nachziehen.
- Konsequenzklassen: Ressourcenbindung, Projektgeschwindigkeit, Sichtbarkeitsfenster, spaetere Startverzweigung.
- Fail-forward: Das Ergebnis ist Schwerpunktverschiebung, nicht Abbruch; Kosten laufen ueber Zeit, Sicherheit, Material oder unvollstaendige Lage.
- Folgeartefakte: `Nordlinie-01.md`, `Missionslog-Novapolis.md`, `D5.md`, spaetere Folgeslots ausserhalb des Startkorridors.

Konsequenzklassen
-----------------

- Zeitkosten: spaeterer Slot-Transfer, Wartezeit, verzoegerte Freigabe.
- Sicherheitskosten: mehr Schutzbedarf, engere Pahl-/Echo-/Reflex-Intervention, strengere Zugriffe.
- Ressourcenkosten: Werkzeug, Filter, Material, Funk- oder Tunnelaufwand.
- Beziehungskosten: Misstrauen, mehr Kontrolle, engere Beobachtung, aber kein isolierter Totalbruch.
- Wissenskosten: spaeterer Reveal, unschaerfere Lage, mehr Geruechtraum.

Guardrails
----------

- Keine freie Szene ausserhalb der belegten Slotanker setzen.
- Keine Artefakt-, Anomalie- oder Fremdfraktionsdetails ueber den aktuellen Belegstand hinaus behaupten.
- Kein Slot ueberschreibt still die Reveal-Matrix oder die bestehenden Orts-/Projekt-SSOTs.

Nachfolger
----------

- Die direkte Anschluss-SSOT fuer denselben Produktpfad liegt in `novapolis-dev/docs/process/rp-folgekorridor-slot-06-10.ssot.md`.