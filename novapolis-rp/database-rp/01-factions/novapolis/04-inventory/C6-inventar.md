---
stand: 2026-03-27 09:54
update: Materiallauf D5 -> C6 als lokaler Review-Anker ergänzt; C6-Zielbuchungen bleiben ohne Item-Belege offen.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260327_011507.md
title: Inventar - C6
last_updated: 2026-03-20T11:49:00+01:00
category: inventory
slug: c6-inventar
owner: novapolis
scope: location
location: c6
version: "0.1"
tags: []
---

<!-- markdownlint-disable MD025 -->

C6 - Inventar
=============

Policy
------
- Inventare bleiben getrennt; Transfers nur via Mission/Logistik.
- Buchungen mit Quelle/Ziel in [Logistik](../../../00-admin/Logistik.md) dokumentieren.

Bestände (lokal belegt, ohne Stückzahlen)
-----------------------------------------
- Filter - im C6-Expeditions-/Stationskontext wiederholt belegt; Typ und Menge tbd
- Energiezellen - im C6-Expeditions-/Stationskontext wiederholt belegt; Menge tbd
- Werkzeuge - im C6-Expeditions-/Stationskontext wiederholt belegt; Typen/Menge tbd
- Energiefluss C6 (Tag 12 -> 13) ist als Bilanz belegt: `+10 Zufuhr aus D5` bei `+12 Verbrauch`; absolute Speicherstaende bleiben `tbd`.

Startsnapshot C6 (2025-10-16, belegte Stückzahlen)
--------------------------------------------------
- Luftfilter `3`
- Ersatzrohre `12`
- Kabelspulen `6`
- Schmieroel `5`
- Strommodule `2`
- Wasserkanister `4`
- Werkzeugsets `2`
- Sensorpaket `1`
- Rationen `9`
- Wasserflaschen `10`
- Schutzanzuege `2`
- Ersatzmasken `3`
- Ergänzende Werkzeugliste aus `inventar_c6_v2`: Wartungsschluessel `2`, Druckmesser `1`, Schweissgeraet `1`; der tragbare Datenkern bleibt als Objekt vor Ort, aber funktional/offen.

Potenziale
----------
- Hydrofilter-Behälter (Reserve) - Potenzial vorhanden, Einbindung offen
- Mechanik-Werkzeug (priorisiert, ohne Stückzahlen)
- Tunnelbaumaterial ist fuer Tag 12 -> 13 als gemeinsamer Verbrauch belegt, aber noch nicht standortscharf D5 oder C6 zugeordnet.

Fehlend / Offen
---------------
- Adapter/Fittings DN60 (kritisch)
- Schweißausrüstung (kritisch)
- Lagerplätze/Containerstruktur für C6-Inventar

Bewegungen (Log)
----------------
- 2026-01-16 [FACT?] Prioritätenliste für C6-Inventar benannt (Filter, Energiezellen, Adapter/Fittings DN60, Schweißausrüstung, Mechanik-Werkzeug; ohne Stückzahlen). Quelle: scene-2026-01-16-a.
- 2026-02-10 17:09 [FACT?] Artefakt 7A im C6-Kontext markiert; Details erst nach Inventarisierung. Quelle: scene-2025-10-27-d.
- 2026-02-10 17:09 [FACT?] Datenkern (tragbar) am Fundort C6 belassen; nicht aufgenommen. Quelle: scene-2025-10-27-x.
- 2026-03-20 06:28 [REVIEW] RAW/Staging bestaetigen C6 als lokalen Fundort fuer Filter, Energiezellen und Werkzeuge; keine belastbaren Stückzahlen, aber klare lokale Zuordnung.
- 2026-03-20 06:45 [FACT?] Tagesabschluss Tag 12 -> 13: C6 `+12 Verbrauch` bei `+10 Zufuhr aus D5` => `-2` Tagesbilanz; nur Flusslogik belegt, keine absolute Zellmenge. Quelle: `database-curated/staging/chat-export.normalized.txt`, [Logistik](../../../00-admin/Logistik.md).
- 2026-03-20 06:52 [FACT?] Tagesabschluss Tag 12 -> 13: Tunnelarbeiten verbrauchen fraktionsweit `1,3 t Baustoffe`, `120 m Schienenprofil`, `18 m² Betonplatten`; `2` Werkzeuge sind beschaedigt, geschaetzt reparabel. Lokaler C6-Anteil bleibt offen. Quelle: `database-curated/staging/chat-export.normalized.txt`.
- 2026-03-20 07:14 [FACT?] Startsnapshot 2025-10-16: `inventar_c6_v2` und `logistik_c6_v2` belegen für C6 konkrete Lager-/Frachtwerte (`Luftfilter(3)`, `Ersatzrohre(12)`, `Kabelspulen(6)`, `Schmieroel(5)`, `Strommodule(2)`, `Wasserkanister(4)`, `Werkzeugsets(2)`, `Sensorpaket(1)`, `Rationen(9)`, `Wasserflaschen(10)`, `Schutzanzuege(2)`, `Ersatzmasken(3)`), plus Werkzeugliste `Wartungsschluessel(2)`, `Druckmesser(1)`, `Schweissgeraet(1)`. Quelle: `database-curated/staging/RAW-canvas-2025-10-16T12-30-00-000Z.normalized.txt`, `database-curated/staging/RAW-canvas-2025-10-16T12-55-00-000Z.normalized.txt`.
- 2026-03-20 11:49 [REVIEW] Ein missionierter Zugang aus D5 nach C6 ist als Reparatur- und Versorgungslauf belegt. Belastbar sind Transportrichtung und Kontext; nicht belastbar sind Ankunftsmengen je Item, saubere Zielbuchungen in der C6-Lagerstruktur und Quittungen an Schleuse oder Lagerhalle. Quelle: `database-raw/99-exports/RAW-canvas-2025-10-16T13-05-00-000Z.txt`, `database-raw/99-exports/chat-export.txt`, [Missionslog-Novapolis](../05-projects/Missionslog-Novapolis.md), [C6-Schleuse](../03-locations/C6-Schleuse.md), [C6-Lagerhalle](../03-locations/C6-Lagerhalle.md).

Delta zum Missionslog
---------------------

- Delta 1 (belegt): C6-Fund-/Sicherungsanker (Artefakt 7A, Datenkern am Fundort belassen) sind im Missionslog referenziert und im Inventar als offen markiert.
  - Quelle: [Missionslog-Novapolis - C6: Sicherung/Markierung (C6-N3) & Artefakt „7A“](../05-projects/Missionslog-Novapolis.md#c6-sicherungmarkierung-c6-n3--artefakt-7a), [scene-2025-10-27-d](../../../06-scenes/scene-2025-10-27-d.md), [scene-2025-10-27-x](../../../06-scenes/scene-2025-10-27-x.md)
- Delta 2 (belegt/offen): C6-Monitoring/Funk-Abschnitte sind als aktive Missionen geführt; daraus resultierende Material-/Transferdetails bleiben bis Belegzeile offen.
  - Quelle: [Missionslog-Novapolis - C6: Funk/Scan & Stationssuche](../05-projects/Missionslog-Novapolis.md#c6-funkscan--stationssuche), [Missionslog-Novapolis - Monitoring: C6-Überwachung](../05-projects/Missionslog-Novapolis.md#monitoring-c6-überwachung-auswertung)
- Delta 3 (belegt): RAW/Staging fuehren Filter, Energiezellen und Werkzeuge konsistent als C6-Expeditions- bzw. Stationskontext; fehlende Schweißausrüstung und Adapter DN60 bleiben Bedarf, nicht Bestand.
  - Quelle: `database-raw/99-exports/chat-export-complete.txt` (Inventar & Ressourcen), `database-curated/staging/chat-export (1).review.md`, [scene-2026-01-16-a](../../../06-scenes/scene-2026-01-16-a.md), [scene-2026-01-14-b](../../../06-scenes/scene-2026-01-14-b.md)
- Delta 4 (belegt): Der Energiepfad D5 -> C6 ist fuer Tag 12 -> 13 mit `+10` Transfer und `-2` Tagesbilanz auf C6-Seite belegt; belastbare Vor-/Nachher-Speicherstaende fehlen weiter.
  - Quelle: `database-curated/staging/chat-export.normalized.txt` (Tagesabrechnung Tag 12 -> 13), [Logistik](../../../00-admin/Logistik.md)
- Delta 5 (belegt/offen): Materialverbrauch und Werkzeugschaden des Tunnel-Tagesabschlusses sind als gemeinsames Novapolis-Delta belegbar, aber noch nicht standortscharf D5 oder C6 zuzuweisen.
  - Quelle: `database-curated/staging/chat-export.normalized.txt` (Materialverbrauch / Werkzeuginspektion Tag 12 -> 13)
- Delta 6 (belegt): Fuer C6 existiert ein frueher, quantifizierter Bestandssnapshot; er taugt als Startanker fuer lokale Restmengen, aber nicht als aktueller Fraktionsgesamtstand ohne D5-Gegenbeleg und spaetere Verbrauchs-/Transferkette.
  - Quelle: `database-curated/staging/RAW-canvas-2025-10-16T12-30-00-000Z.normalized.txt`, `database-curated/staging/RAW-canvas-2025-10-16T12-55-00-000Z.normalized.txt`, `database-curated/staging/RAW-canvas-2025-10-16T13-05-00-000Z.normalized.txt`
- Delta 7 (belegt/offen): Ein Reparatur- und Versorgungslauf aus D5 nach C6 ist als Missionskontext belegt; fuer konkrete C6-Bestandsfortschreibung fehlen jedoch Zielbuchung, Lagerzuordnung und Quittung.
  - Quelle: [Missionslog-Novapolis](../05-projects/Missionslog-Novapolis.md), `database-raw/99-exports/RAW-canvas-2025-10-16T13-05-00-000Z.txt`, `database-raw/99-exports/chat-export.txt`, [C6-Schleuse](../03-locations/C6-Schleuse.md), [C6-Lagerhalle](../03-locations/C6-Lagerhalle.md)

Aktionen
--------
- [ ] Lagerplätze/Container definieren
- [ ] Verbrauchslog anlegen
