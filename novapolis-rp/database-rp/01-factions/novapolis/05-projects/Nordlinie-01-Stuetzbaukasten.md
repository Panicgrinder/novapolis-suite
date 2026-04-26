---
stand: 2026-04-27 01:53
update: Diese SSOT fuehrt jetzt zusaetzlich eine konservative Beispielbuchung fuer den kleinen Nordlinie-Turn-7-Satz.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260427_015145.md
title: Nordlinie 01 - Stuetzbaukasten und Verbindungsklassen
category: project
slug: nordlinie-01-stuetzbaukasten
status: active
dependencies: ["nordlinie-01", "d5-inventar"]
version: "0.1"
last_updated: 2026-04-27T00:44:00+02:00
tags: []
---

Projekt: Nordlinie 01 - Stuetzbaukasten und Verbindungsklassen
-------------------------------------------------------------

Zweck
-----

Diese SSOT legt fest, wie der Nordlinie-Bedarf `Stuetzelemente` fachlich zu lesen und spaeter zu buchen ist.

- `Stuetzelemente` meint im Nordlinie-Kontext standardmaessig keinen Stapel fertig montierter Lagerstuetzen.
- Gemeint ist ein komponentenbasierter Stuetzbaukasten, aus dem vor Ort je nach Schadstelle eine passende Sicherung montiert wird.
- Dadurch bleiben Materialart, Belastbarkeit und Restbestand getrennt lesbar, statt in einer vagen Sammelbezeichnung zu verschwimmen.

Kernregel
---------

- Vor Ort verbaute Stuetzen sind Baugruppen, keine primaeren Lagerartikel.
- Lager- und Transferbuchung laufen deshalb ueber Komponentenklassen, nicht ueber eine einzige pauschale Position `fertige Stuetzen`.
- Wenn ein RP-Zug nur `Stuetzelemente` nennt, ist das kuenftig als Kurzform fuer diesen Baukasten zu lesen, bis eine feinere Aufschluesselung folgt.

Materialklassen
---------------

Metallprofile

- `metallprofil-lang`: tragende Laengenteile fuer groessere Spannweiten oder schräge Abstuetzung
- `metallprofil-mittel`: Standardprofil fuer die meisten behelfmaessigen Sicherungen im Tunnel
- `metallprofil-kurz`: Versteifung, Querzug oder lokale Unterfuetterung

Form- und Verbindungsteile

- `klemme`: schnelle Fixierung und Verspannung an vorbereiteten Punkten
- `lasche-knotenblech`: flaechige Verbindung oder Lastverteilung zwischen Profilen
- `ausgleichsplatte`: Unterlage oder Distanzstueck fuer unruhige Auflagepunkte

Verbindungsmittel nach Belastbarkeit

- `klebmasse-schwach`: nur fuer Ansetzen, Ausrichten oder leichte Fixierung; nie als primaere tragende Endverbindung lesen
- `schraubensatz-mittel`: mittlere Sicherung fuer behelfmaessige, kontrollierbare Verbindung
- `bolzen-mutter-satz-stark`: starke mechanische Verbindung fuer hoeher belastete Baugruppen

Qualitaetsstufen
----------------

- `alt`: funktional moeglich, aber mit hoeherem Pruef- und Ausfallrisiko
- `normal`: gebrauchstauglicher Standard ohne besonderen Zuschlag
- `neuwertig`: kaum beansprucht oder frisch aufgearbeitet, bevorzugt fuer kritische Punkte

Hinweis zur Alterung
--------------------

- Bei Metallteilen beschreibt die Qualitaetsstufe vor allem Verschleiss, Rost, Verzug und Passgenauigkeit.
- Bei `klebmasse-schwach` ist die Frische wichtiger als reine Oberflaechenoptik; alte oder zweifelhafte Masse darf nicht wie `normal` oder `neuwertig` behandelt werden.

Buchungseinheiten
-----------------

- Metallprofile, Klemmen, Laschen/Knotenbleche und Ausgleichsplatten werden in `Stueck` gefuehrt.
- Schraubensaetze und Bolzen-Muttern-Saetze werden in `Satz` gefuehrt.
- Klebmasse wird in `Kartusche` oder klar benannter `Portion` gefuehrt.
- Verbaute Feldstuetzen werden nicht als neuer Lagerartikel gebucht, sondern als Einsatz von Komponenten am Zielort.

Buchungsregeln fuer RP und Runtime
----------------------------------

- Ein belastbarer Transfer benoetigt mindestens: Quelle oder Bestandstraeger, Ziel oder Einsatzort, Materialklasse, Einheit und zaehlbare Groesse.
- Ein belastbarer Nachzustand trennt mindestens zwischen `transferiert`, `eingesetzt/verbraucht` und `Rest offen` oder `Rest belegt`.
- Wenn ein RP-Zug nur von einem `schmalen Satz` spricht, darf daraus kein exakter Restbestand abgeleitet werden.
- Solange Zahlen fehlen, ist klassenweise `tbd` zulaessig; eine pauschale Sammelbuchung ohne Materialart ist es nicht.

Konservative Beispielbuchung Turn 7
----------------------------------

Die erste kleine Teilbereitstellung aus dem Runtime-Zug wird im RP-SSOT konservativ wie folgt gelesen:

| Klasse | transferiert | eingesetzt | Rest vor Ort |
| --- | --- | --- | --- |
| metallprofil-mittel | `2` | `2` | `0` |
| metallprofil-kurz | `4` | `3` | `1` |
| klemme | `4` | `4` | `0` |
| lasche-knotenblech | `2` | `2` | `0` |
| ausgleichsplatte | `2` | `1` | `1` |
| schraubensatz-mittel | `4 Saetze` | `3 Saetze` | `1 Satz` |
| bolzen-mutter-satz-stark | `1 Satz` | `1 Satz` | `0` |
| klebmasse-schwach | `1 Kartusche` | `1 Kartusche` | `0` |

Hinweis

- Diese Beispielbuchung schliesst genau den kleinen Turn-7-Satz und nichts darueber hinaus.
- Die chargenscharfe Vorhistorie in D5 sowie jeder weitere Folgeabgang bleiben weiterhin Review-Flaeche.

Abgrenzung zu Hauptblockern
---------------------------

- Der Stuetzbaukasten deckt Sicherung, Versteifung und lokale Vorbereitung ab.
- Er ersetzt weder `Schweißgeraet` noch `Adapter DN60`.
- Ein positiver Einsatz des Baukastens darf deshalb nie als Beleg fuer vollstaendige Reparatur oder Leitungsabschluss gelesen werden.

Verknuepfte Quellen
-------------------

- [Nordlinie-01](./Nordlinie-01.md)
- [D5-inventar](../04-inventory/D5-inventar.md)
- [Missionslog-Novapolis](./Missionslog-Novapolis.md)
