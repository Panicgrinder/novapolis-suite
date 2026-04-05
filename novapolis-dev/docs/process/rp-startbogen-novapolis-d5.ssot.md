---
stand: 2026-04-05 19:43
update: Der D5-Startbogen referenziert jetzt den geschlossenen Mind-Cluster-Unterbau des Novapolis-Kerncasts ohne veraltete Lueckenhinweise.
checks: snapshot-lock PASS (2026-04-05 10:32); markdownlint PASS; frontmatter PASS
---

RP Startbogen: Novapolis D5
===========================

Zweck
-----

Diese SSOT definiert den kanonischen Default-Start fuer den ersten spielbaren Novapolis-Run.

Quellenbasis
------------

- `novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5.md`
- `novapolis-rp/database-rp/01-factions/novapolis/05-projects/Missionslog-Novapolis.md`
- `novapolis-rp/database-rp/01-factions/novapolis/05-projects/Nordlinie-01.md`
- `novapolis-rp/database-rp/06-scenes/scene-2025-10-27-g.md`
- `novapolis-rp/database-rp/06-scenes/scene-2025-10-27-h.md`
- `novapolis-rp/database-rp/06-scenes/scene-2025-10-27-j.md`
- `novapolis-rp/database-rp/01-factions/novapolis/02-characters/Ronja-Kerschner.md`
- `novapolis-rp/database-rp/01-factions/novapolis/02-characters/Reflex.md`
- `novapolis-rp/database-rp/01-factions/novapolis/02-characters/Jonas-Merek.md`
- `novapolis-rp/database-rp/01-factions/novapolis/02-characters/Pahl-Brenner.md`
- `novapolis-dev/docs/process/rp-start-chooser.ssot.md`
- `novapolis-dev/docs/process/rp-text-rpg-startpaket-slot-00-05-2026-04-05.md`

Startklasse
-----------

- Modus: `novapolis_default`
- Bereich: `D5`
- Gebietsklasse: `faction_core`
- Dichtegrad: `full_slice`

Startpraemisse
--------------

Der PC startet im aktiven Betriebskern von D5. Die Lage ist stabil genug fuer Spielraum, aber nicht ruhig: ein Wartungsauftrag, eine ungeklaerte Werkzeugtasche, ein moeglicher System-Link und der Druck der Nordlinie zwingen frueh zu Priorisierung statt Komfort.

Belegte Ausgangslage
--------------------

- D5 ist die bewohnte Hauptbasis von Novapolis mit Kontrollraum, Versorgung und Werkstattkern.
- Ronja ist die primaere Startlinse; Reflex ist ihr unmittelbarer Schutz- und Sensorverbund.
- Jonas und Pahl sind in D5 als Folgefiguren fuer Werkstatt, Technik, Funk und Sicherheitsfreigaben verfuegbar.
- Ein frueher Wartungsauftrag im Wartungsgang ist belegt.
- Ein frueher Terminal-/System-Link in D5 ist belegt.
- Der Tunnel D5-C6 ist als aktives Projekt `Nordlinie 01` belegt und erzeugt dauerhaften Druck auf Zeit, Material und Sicherheitslage.

Startkern
---------

- Ronja Kerschner: PC-Linse, Leitung, Technik, D5/C6-Bruecke
- Reflex: Schutz, Sensorik, riskanter System- und Gefahrenfilter
- Jonas Merek: Werkstatt, Materiallauf, Tunnel-Assessment, Funkbruecke
- Pahl Brenner: Freigabe, Wartungsplanung, Sicherheits- und Hausregelpfad

Erste Stakes
------------

- Eine ungeklaerte Werkzeugtasche und ein Wartungsauftrag erzwingen einen fruehen Umgang mit Unsicherheit.
- Der System-Link verspricht Erkenntnis, droht aber Dämpfung, Kontrollverlust oder Fehlpriorisierung.
- D5 muss betriebsfaehig bleiben, waehrend C6 und die Nordlinie nicht ignoriert werden koennen.
- Zeit-, Sicherheits- und Materialkosten sind frueh relevant, ohne den Run sofort zu blockieren.

Erster Entscheidungsraum
------------------------

1. Den Wartungsauftrag vorsichtig verfolgen und die Werkzeugtasche nur als Beleg sichern.
2. Den System-Link in D5 frueh angehen und Risiko gegen Erkenntnis abwaegen.
3. Jonas frueh in Werkstatt-, Funk- oder Tunnel-Assessment einbinden.
4. Pahl fuer Sicherheitsfreigabe, Regelhilfe und Belastungsabwaegung vorziehen.

Fail-forward
------------

- Ein vorsichtiger Fehlgriff fuehrt zuerst zu Zeitverlust, Zusatzkontrolle oder unschaerfer Lageeinschaetzung.
- Ein riskanter Systemzugriff darf Dämpfung, Rauschen oder Zusatzschutz erzeugen, aber keinen harten Session-Abbruch.
- Schlechte Priorisierung verschiebt vor allem, welcher Folgepfad spaeter teurer wird.

Reveal-Regeln
-------------

- `pc_visible`: Wartungsauftrag, Werkzeugtasche, unmittelbare D5-Lage, System-Link-Risiko, Jonas/Pahl als Folgekontakte
- `allies_only`: bestaetigte Monitoring- und E3-Risiko-Infos aus Missionslog und Teamkanälen
- `world_only`: rohe C6-Arbeitsdetails, ungepruefte Anomalie-Deutungen, verdeckte Fraktionslagen
- `rumor`: ungesicherte Signale, Paranoia, nicht verifizierte Tunnel- oder Lebenszeichenhinweise

Anschluss an Folgepfade
-----------------------

- D5-interner Folgepfad: Werkstatt, Funk, Sicherheitsfreigaben, Material- und Systemordnung
- Nordlinie-Folgepfad: Tunnel-Assessment, Materiallauf, spaetere Betriebsaufnahme Richtung C6
- C6-Folgepfad: kontrollierter Reveal ueber bestaetigte Log-, Funk- oder Instanzpfade

Offene Luecken
--------------

- Exakte Inhalte des Wartungsauftrags bleiben offen.
- Exakte Outputs des System-Links bleiben offen.
- Mind-Cluster fuer `Ronja`, `Reflex`, `Jonas` und `Pahl` liegen jetzt als eigenstaendige SSOTs vor; der direkte Anschlusscast ist ebenfalls separat unterlegt.
- Der kanonische Mehrslot-Korridor ist noch nicht als vollstaendige Folge-SSOT fixiert.

Guardrails
----------

- Keine freie Begegnung oder Konfrontation erfinden, die in den Szenen nicht belegt ist.
- Keine technische Ausgestaltung des System-Links setzen, die ueber die belegte Existenz hinausgeht.
- Keine stillen Retcons fuer D5-Raummaße, Lastenaufzug oder Inventarfluss einfuehren.
