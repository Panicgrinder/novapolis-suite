---
stand: 2026-04-27 05:33
update: Diese SSOT legt fuer das gesamte RP die Defaultregel fest, dass Hauptorte zuerst in einer starken Ortsdatei gefuehrt und Unterorte nur bei echtem Separationsgrund ausgelagert werden.
checks: snapshot-lock PASS (2026-04-27 05:05); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-dev/docs/process/rp-ortsmodell-granularitaet.ssot.md' 'novapolis-dev/docs/donelog.md' PASS (2026-04-27 05:06); f:/VS-Code-Workspace/Main/.venv-py313-backup-20260409_1832/Scripts/python.exe scripts/check_frontmatter.py 'novapolis-dev/docs/process/rp-ortsmodell-granularitaet.ssot.md' 'novapolis-dev/docs/donelog.md' PASS (2026-04-27 05:07)
---

RP-Ortsmodell: Granularitaetsregel SSOT
=======================================

Zweck
-----

Diese SSOT legt fuer das gesamte RP fest, wann ein Ort als starke Hauptdatei gefuehrt wird und wann ein Unterort eine eigene Orts-SSOT erhalten darf.

- Sie verhindert, dass Ortsstruktur nur aus Gewohnheit oder Namensattraktivitaet in viele Kleindateien zerfaellt.
- Sie erlaubt Ausnahmen dort, wo ein Unterort betrieblich, riskoseitig oder referenziell wirklich eigenstaendig ist.
- Sie ersetzt keine Orts- oder Fraktions-SSOT, sondern definiert deren Strukturregel.

Nicht Ziel
----------

- keine pauschale Rueckmigration aller bestehenden Unterortsdateien
- keine freie Erfindung neuer Unterorte ohne Beleglage
- keine Dopplung von Szenen-, Projekt- oder Inventarlogik in Ortsdateien

Quellenbasis
------------

- `novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5.md`
- `novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md`
- `novapolis-rp/database-rp/01-factions/novapolis/03-locations/E3.md`
- `novapolis-rp/database-rp/01-factions/novapolis/03-locations/E3-Wasseraufbereitung.md`
- `novapolis-rp/database-rp/01-factions/novapolis/03-locations/README.md`
- `novapolis-dev/docs/process/rp-start-chooser.ssot.md`

Kernbefund
----------

- `D5` und `C6` tragen aktive Kernstationen gut als starke Hauptdateien: Status, Zugaenge, Betriebscharakter, Teilraeume und lokale Tiefenschaerfe bleiben dort lesbar zusammen.
- `E3` funktioniert als Ausnahme mit ausgelagerten Unterorten, weil dort verriegelte Infrastruktur, Evakuierungslogik und separater Risikodruck nicht nur atmosphaerische Unterpunkte, sondern eigenstaendige Arbeits- und Entscheidungsflaechen bilden.
- Die Produkt- und Startschicht kennt bereits `subarea` als zulaessige Klasse, fuehrte bisher aber keine RP-weite Regel, wann daraus eine eigene Ortsdatei werden darf.

Defaultregel fuer das gesamte RP
--------------------------------

- Ein Ort beginnt im RP als starke Hauptdatei.
- Diese Hauptdatei traegt mindestens Status, Funktion, Zugaenge, Risiken, betriebliche Lesart und lokale Tiefenschaerfe des Ortes.
- Unterorte bleiben zunaechst Abschnitte innerhalb dieser Hauptdatei.
- Eine Auslagerung in eine eigene Unterortsdatei ist die Ausnahme und braucht einen belegbaren Separationsgrund.

Harte Separationsgruende
------------------------

Ein Unterort darf eine eigene Ortsdatei bekommen, wenn mindestens einer der folgenden harten Gruende belastbar vorliegt:

1. eigener Betriebszustand oder eigene Freigabe-/Verriegelungslogik
2. eigenstaendige Risiko- oder Infrastrukturfrage, die nicht nur eine Randnotiz des Hauptortes ist
3. wiederkehrender eigener Missions-, Arbeits- oder Entscheidungsraum
4. wiederholte separate Referenz in Szenen, Projekten, Inventaren, Startboegen oder Folge-SSOTs

Weiche Zusatzgruende
--------------------

Die folgenden Gruende allein reichen nicht, koennen eine Auslagerung aber zusammen mit einem harten Grund stuetzen:

- die Hauptdatei wird ohne Auslagerung unlesbar oder semantisch unscharf
- ein Unterort braucht eigene Hooks, offene Aufgaben oder klar getrennte Anschlussfragen
- dieselbe Teilflaeche muss wiederkehrend separat verlinkt werden, obwohl sie kein eigener Tunnelknoten ist

Was nicht fuer eine eigene Datei reicht
---------------------------------------

- ein gut klingender Raumname allein
- ein einzelner Grundriss- oder Planhinweis
- reine Atmosphaere ohne eigenen Betriebs- oder Risikohaken
- ein moeglicher spaeterer Ausbau ohne aktuelle Belegkette
- einmalige Szenenerwaehnung ohne wiederkehrende Eigenfunktion

Bestandslesart nach dieser Regel
--------------------------------

- `D5` und `C6` bleiben das RP-Defaultmodell: starke Hauptorte zuerst, lokale Teilraeume in der Hauptdatei, keine automatische Zersplitterung in `Werkstatt`, `Funkraum`, `Schleuse` oder `Lagerhalle`.
- `E3` bleibt ein zulaessiger Ausnahmefall: verriegelte, getrennt bewertete Infrastrukturreste wie `E3-Wasseraufbereitung` duerfen eigenstaendig gefuehrt werden, weil sie eigene Freigabe-, Risiko- und Folgefragen tragen.
- Tunneldateien bleiben davon unberuehrt: Wenn ein Verbindungstunnel bereits als eigener Knoten gefuehrt wird, ist er weiterhin eigene Ortsdatei und nicht nur Unterabschnitt einer Station.

Ableitungsregel fuer neue RP-Orte
---------------------------------

- Neue Kernorte in Fraktionen, Neutralraeumen oder Spezialgebieten beginnen mit einer Hauptdatei.
- Unterorte werden erst dann angelegt, wenn die Beleglage mindestens einen harten Separationsgrund traegt.
- Bei jeder neuen Unterortsdatei muessen Hauptort und Unterort sich gegenseitig eindeutig verorten, ohne denselben Kanon doppelt auszuformulieren.
- Bestehende Unterortsdateien werden nicht aus Prinzip eingeebnet; Korrekturen passieren nur bei Widerspruch, Redundanz oder wenn eine angefasste Ortsfamilie ohnehin nachgezogen wird.

Guardrails
----------

- Evidence first: keine Unterortsdatei nur als Platzhalter fuer spaetere Ideen.
- SSOT sauber halten: Hauptort traegt die Gesamtlesart, Unterort nur seinen echten Sonderfall.
- Keine Schattenwelt neben der Hauptdatei: neue Dateien duerfen keinen zweiten, konkurrierenden Gesamtort erzaehlen.
- Start-, Projekt-, Inventar- und Szenendokumente referenzieren Unterorte nur dann separat, wenn diese Regel erfuellt ist.