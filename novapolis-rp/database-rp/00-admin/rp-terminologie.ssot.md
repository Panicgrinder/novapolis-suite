---
stand: 2026-04-28 05:46
update: Diese SSOT fuehrt erstmals eine allgemeine RP-Terminologie fuer belastbare Benennung von Raum, Schadstellen, Befunden und Reparaturfolgen.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp/results/reports/checks_report_20260428_052348.md; snapshot-lock PASS (2026-04-28 05:46)
title: RP-Terminologie
category: Admin
slug: rp-terminologie
schemaVersion: 1
language: de
owners: [admin-novapolis]
tags: [rp, ssot, terminologie, benennung]
status: active
relatedSlugs: [reference-campaign-state, current-state, verbindungstunnel-d5-c6, nordlinie-01]
---

<!-- markdownlint-disable MD025 -->

RP-Terminologie (SSOT)
======================

Zweck
-----

Diese SSOT fuehrt eine kontrollierte Terminologie fuer RP, Runtime und spaetere Promotion.

Sie soll verhindern, dass identische oder nahe Sachverhalte wechselnd, zu vage oder fachlich schief benannt werden.
Besonders wichtig ist das bei:

- Raumbegriffen
- Schadstellen und Problemherden
- Befund- und Untersuchungsstatus
- Reparaturfolgen
- Aufwand- und Kostenklassen

Anwendungsbereich
-----------------

- Gilt fuer RP-SSOT unter `novapolis-rp/database-rp/**`.
- Gilt als bevorzugter Referenzrahmen fuer Runtime-Dateien unter `novapolis-rp/database-curated/staging/rp-runtime/**`.
- Wenn eine projektspezifische SSOT feinere Begriffe fuehrt, darf sie diese enger ziehen, aber nicht in Widerspruch zu dieser Datei.

Kernregeln
----------

- Benenne konkrete Dinge nach Funktion, Lage und technischem Charakter statt nach Atmosphaere.
- Nutze fuer Raum, Schaden und Reparatur moeglichst dieselben Begriffe ueber Szene, Runtime-State und spaetere Promotion hinweg.
- Vage Ersatzwoerter bleiben zulaessig nur dort, wo noch kein belastbarer Befund vorliegt.
- Sobald ein Befund hinreichend untersucht ist, ist die praezisere Benennung Pflicht.
- Aufwand und Kosten werden bevorzugt ueber Klassen oder Preisbaender gefuehrt, nicht ueber frei erfundene Scheingenauigkeit.

Benennungsmuster
----------------

Raum oder Abschnitt

- Muster: `Ortstyp` plus `Abschnitt/Lage`
- Beispiele: `U-Bahn-Tunnel D5-C6`, `Tunnelabschnitt Nordkante`, `Engbogen vor C6`

Schadstelle oder Problemherd

- Muster: `Bauteil/System` plus `Lage` plus `Fehlerart`
- Beispiele: `Schottertasche Nordkante`, `Schienenversatz Engbogen`, `Haltepunktpaar Leitungszug Suedseite`

Befundstatus

- `offen`: nur als Verdacht oder grobe Beobachtung vorhanden
- `teilweise untersucht`: Schaden ist benannt, aber noch nicht technisch voll freigelegt oder bewertet
- `hinreichend untersucht`: Schaden ist soweit geprueft, dass Reparaturfolge und Aufwandsklasse belastbar eingegrenzt werden koennen

Reparaturfolge

- Kurz, technisch und sequenziell schreiben
- Bevorzugte Form: `freilegen`, `ausrichten`, `unterfuettern`, `nacharbeiten`, `sichern`, `ersetzen`, `einpassen`

Aufwand und Kosten
------------------

- Bevorzugt Preisbaender oder klar benannte Aufwandsklassen nutzen.
- Wenn Preisbaender verwendet werden, gilt die Referenz aus `novapolis-pricebands`.
- Wenn die Untersuchung nicht ausreicht, bleibt die Kostenklasse explizit `offen`.

Bevorzugte Raumbegriffe
-----------------------

- `U-Bahn-Tunnel`: bevorzugter Oberbegriff fuer den Verbindungstunnel D5-C6
- `Tunnelabschnitt`: klar abgegrenzter Teilbereich innerhalb eines Tunnels
- `Trassenbereich`: Bereich von Schiene, Unterbau und unmittelbarer Fuehrung
- `Leitungszug`: Leitungs- oder Versorgungslinie entlang des Abschnitts
- `Engbogen`: enger, geometrisch auffaelliger Bogenbereich innerhalb eines Tunnels

Zu vermeidende Begriffe
-----------------------

- `Korridor`, wenn eigentlich ein Tunnel oder Tunnelabschnitt gemeint ist
- `Stelle`, `Problemzone`, `Schadbereich` ohne technische Einordnung
- `Materialproblem`, wenn der konkrete Mangel benannt werden kann
- `Reparaturbedarf`, wenn bereits eine belastbare Reparaturfolge bekannt ist

Nordlinie-01 Startset
---------------------

Diese Begriffe sind fuer den aktuellen Nordlinie-Kontext bereits bevorzugt lesbar:

- `U-Bahn-Tunnel D5-C6` statt bloß `Korridor`
- `Schottertasche Nordkante` fuer ausgespuelten Unterbau an der seitlichen Kante
- `Schienenversatz Engbogen` fuer einen im Bogen nicht sauber gefuehrten Schienen- oder Gleisabschnitt
- `Haltepunktpaar Leitungszug` fuer zwei nur vorlaeufig tragende Leitungs-Haltepunkte
- `Uebergang Engbogen` fuer den technisch relevanten Uebergangsbereich vor dem engeren Bogen

Verweise
--------

- Ortsanker: ../01-factions/novapolis/03-locations/Verbindungstunnel-D5-C6.md
- Projektanker: ../01-factions/novapolis/05-projects/Nordlinie-01.md
- Materialklassen: ../01-factions/novapolis/05-projects/Nordlinie-01-Stuetzbaukasten.md
- Preisbaender: ../01-factions/novapolis/06-handel-diplomatie/novapolis-pricebands.md
