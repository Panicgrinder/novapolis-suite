---
stand: 2026-04-02 06:27
update: H-47, C6-Handelsstuetzpunkt und der erste belegte Austauschkorridor sind jetzt im Karawanenlog verankert.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260402_062604.md
canvas: Karawanenbewegungen
last_updated: 2026-03-31T17:50:25+02:00
category: project
slug: caravan-moves
title: Karawanenbewegungen (Übersicht)
status: active
version: "0.1"
tags: []
---

Karawanenbewegungen (Übersicht)
-------------------------------

Ziel: Bewegungen/Pläne der Händlerkarawanen erfassen (Zeitleiste, Routen, Risiken, Abhängigkeiten). Dient Logistik und Missionsplanung.

Zeitplan (Woche)
----------------
- Tag 9: Erste Handelsroute `H-47` nach D5 / C6; dauerhafte Kooperation erfolgreich verhandelt, `C6 als Handelsstuetzpunkt aktiviert`.
- Tag 20: `Trupp H-47` aktiv; kleine Karawane verlaesst die Suedlinie Richtung D-Sektor, Ankunft in ca. `24 Stunden`.

Routen
------
- Primaer: `G7 <-> C6` als externer Kontakt-/Umschlagpfad des Haendlerbunds.
- Sekundaer: `C6 <-> D5` als interner Weitergabe-/Materialpfad unter Novapolis-Logistik.

Belegte Austauschklassen
------------------------

- Richtung Aufbaupfad Novapolis/Haendlerbund: `Energie`, `technische Reparaturen`, `Kommunikationszugang`.
- Gegenrichtung / Bezugsseite: `Nahrungsmittel`, `Filter`, `Grundbedarfsgueter`.
- Konkrete Konvoi-Mengen, Packlisten und Abrechnungen bleiben `tbd`.

Risiken / Ereignisse
--------------------
- Tunnelzustand/Anomalien (Verbindungstunnel D5-C6)
- Fraktionsaktivität (Diebstahl, Blockaden)
- Energie/Leitungen (Ladefenster, Prioritäten)
- Sicherheits- und Kommunikationsfreigaben laufen vor externen Kontakten ueber Reflex/Novapolis.

Abhängigkeiten
--------------
- Energie-Konten (D5/C6)
- Inventare (Material, Zellen, Werkzeug)
- Missionslog (L.1: Abschluss → Archiv)
- G7 als externer Kontaktpunkt, C6 als aktiver Handelsstuetzpunkt

Links
-----
- Logistik → ../../../00-admin/Logistik.md
- C6 → ../../novapolis/03-locations/C6.md
- D5 → ../../novapolis/03-locations/D5.md
- G7 → ../03-locations/G7.md
- Missionslog → ./Missionslog-Haendlerbund.md
- Draisine-/Transportmodul (D5 Prototyp) → ../../novapolis/05-projects/Draisine-Transportmodul.md


