---
stand: 2026-04-02 06:27
update: Der D5-Materiallauf nach C6 fuehrt jetzt einen expliziten Entnahmeanker mit Ronja und Reflex; Mengen und saubere Item-Abgaenge bleiben offen.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260402_062604.md
title: Inventar - D5
last_updated: 2026-03-31T08:46:44+02:00
category: inventory
slug: d5-inventar
owner: novapolis
scope: location
location: d5
version: "0.1"
tags: []
---

<!-- markdownlint-disable MD025 -->

D5 - Inventar
=============

Policy
------
- Inventare bleiben getrennt; Transfers nur via Mission/Logistik.
- Buchungen mit Quelle/Ziel in [Logistik](../../../00-admin/Logistik.md) dokumentieren.

Bestände (verbucht)
-------------------
- Keine separat belastbar verbuchten D5-Bestaende aus der C6-Expedition.
- Lokaler D5-Werkzeug-/Wartungskontext ist belegt, aber ohne saubere Bestandszeile oder belastbare Mengenangabe noch nicht als eigener Item-Posten kanonisiert.
- Energiefluss D5 (Tag 12 -> 13) ist als Bilanz belegt: `+10 Produktion`, `-8 Grundlast`, `-12 Export nach C6`; absolute Speicherstaende bleiben `tbd`.

Startsnapshot D5 (2025-10-16, teilquantifizierter Stationsanker)
-----------------------------------------------------------------
- Union-Kisten mit Ersatzteilen `3`
- Alte Filterkartuschen (leer)
- Ersatzrohre und Ventilkomponenten - belegt, Menge `tbd`
- Reparaturstation - defekt, planmaessig zu reaktivieren
- Schaltplaene und technische Dokumentation - Fragment `60 %` lesbar

Potenziale
----------
- Werkzeug-/Wartungsmaterial aus D5-Kontext moeglich, aber derzeit nur als Umfeld- und Fundkontext belegt.
- Tunnelbaumaterial ist fuer Tag 12 -> 13 als gemeinsamer Verbrauch belegt, aber noch nicht standortscharf D5 oder C6 zugeordnet.

Fehlend / Offen
---------------
- Schweißausrüstung (D5-Priorität, aber nicht als lokaler Bestand belegt)
- Adapter / Fitting (DN60) (D5-Priorität, aber nicht als lokaler Bestand belegt)
- Saubere Trennung lokalem D5-Bestand vs. C6-Expeditionsgut im Wochenzyklus weiter nachziehen

Bewegungen (Log)
----------------
- 2026-02-10 17:09 [FACT?] Werkzeugtasche (Fundstueck) in D5 beobachtet; Ownership/Inhalt offen. Quelle: scene-2025-10-27-g.
- 2026-03-20 06:28 [REVIEW] Fruehere C6-Posten (`Filter`, `Energiezellen`, `Hydrofilter-Behälter`) aus D5 entfernt; RAW/Staging und `scene-2025-10-27-x` bestaetigen die Standorttrennung ohne impliziten Transfer.
- 2026-03-20 06:45 [FACT?] Tagesabschluss Tag 12 -> 13: D5 `+10 Produktion - 8 Eigenverbrauch - 12 Export` => `-10` Tagesbilanz; nur Flusslogik belegt, keine absolute Zellmenge. Quelle: `database-curated/staging/chat-export.normalized.txt`, [Logistik](../../../00-admin/Logistik.md).
- 2026-03-20 06:52 [FACT?] Tagesabschluss Tag 12 -> 13: Tunnelarbeiten verbrauchen fraktionsweit `1,3 t Baustoffe`, `120 m Schienenprofil`, `18 m² Betonplatten`; `2` Werkzeuge sind beschaedigt, geschaetzt reparabel. Lokaler D5-Anteil bleibt offen. Quelle: `database-curated/staging/chat-export.normalized.txt`.
- 2026-03-20 07:22 [FACT?] Startsnapshot 2025-10-16: D5 fuehrt im Basis-Canvas ein Stationsinventar mit `Union-Kisten (3)`, leeren Filterkartuschen, Ersatzrohren/Ventilkomponenten, defekter Reparaturstation und zu `60 %` lesbaren Schaltplaenen. Quelle: `database-curated/staging/RAW-canvas-2025-10-16T12-00-00-000Z.normalized.txt`.
- 2026-03-20 11:49 [REVIEW] Ein Materiallauf `D5 -> C6` fuer Reparatur- und Versorgungsgueter ist als Vorgang belegt. Belastbar sind Richtung und Zweck sowie generische Frachtarten wie `Bauteile`, `Werkzeuge` und `Versorgungsgueter`; nicht belastbar sind Entnahmemengen, konkrete D5-Abbuchungen und die spaetere Zielbuchung in C6. Quelle: `database-raw/99-exports/RAW-canvas-2025-10-16T13-05-00-000Z.txt`, `database-raw/99-exports/chat-export.txt`, [Missionslog-Novapolis](../05-projects/Missionslog-Novapolis.md).
- 2026-03-31 08:46 [FACT?] Der Chat-RAW fuehrt den D5-Abgang jetzt explizit auf Prozessebene: `Ronja wird das notwendige einpacken` und das Material `zusammen mit Reflex Unterstuetzung zur Station bringen`; der RAW-Logistikcanvas stuetzt dazu `manuellerTransport` und `Tragegestell(ReflexAssist)`. Konkrete Item-Mengen und eine saubere D5-Abbuchung bleiben weiter `tbd`. Quelle: `database-raw/99-exports/RAW-chat-export-2025-10-27T09-16-00-188Z.txt`, `database-raw/99-exports/RAW-canvas-2025-10-16T13-05-00-000Z.txt`.

Delta zum Missionslog
---------------------

- Delta 1 (belegt): D5-Werkzeug-/Wartungskontext als Missionsanker vorhanden; Inventar-Ownership der Werkzeugtasche bleibt offen bis belastbare Zuordnung vorliegt.
  - Quelle: [Missionslog-Novapolis - D5: Wartungsauftrag & Wartungsgang](../05-projects/Missionslog-Novapolis.md#d5-wartungsauftrag--wartungsgang), [scene-2025-10-27-g](../../../06-scenes/scene-2025-10-27-g.md)
- Delta 2 (belegt/offen): Trennung D5↔C6 bleibt verbindlich; fuer den Materiallauf sind D5-Abmeldung, Verpacken in D5 und Transportfuehrung durch Ronja mit Reflex-Assist jetzt explizit belegt. Offen bleiben weiter Itemliste, Charge und die eigentliche Mengenabbuchung aus D5.
  - Quelle: [Missionslog-Novapolis - D5 -> C6: Materiallauf / Guetertransport](../05-projects/Missionslog-Novapolis.md#d5---c6-materiallauf--guetertransport), `database-raw/99-exports/RAW-chat-export-2025-10-27T09-16-00-188Z.txt`, `database-raw/99-exports/RAW-canvas-2025-10-16T13-05-00-000Z.txt`
- Delta 3 (belegt): Staging/RAW bestaetigen, dass die C6-Expeditionsgueter nicht stillschweigend im D5-Inventar landen duerfen.
  - Quelle: `database-raw/99-exports/chat-export-complete.txt` (Inventar & Ressourcen), `database-curated/staging/chat-export-complete.finalgate.md`, `database-curated/staging/chat-export (1).review.md`
- Delta 4 (belegt): Der D5-Reaktor-/Energiepfad bleibt lokal verankert; fuer Tag 12 -> 13 ist eine exportgetriebene Tagesbilanz `-10` belegt, ohne dass daraus ein absoluter Restbestand ableitbar waere.
  - Quelle: `database-curated/staging/chat-export.normalized.txt` (Tagesabrechnung Tag 12 -> 13), [Logistik](../../../00-admin/Logistik.md)
- Delta 5 (belegt/offen): Materialverbrauch und Werkzeugschaden des Tunnel-Tagesabschlusses sind als gemeinsames Novapolis-Delta belegbar, aber noch nicht standortscharf D5 oder C6 zuzuweisen.
  - Quelle: `database-curated/staging/chat-export.normalized.txt` (Materialverbrauch / Werkzeuginspektion Tag 12 -> 13)
- Delta 6 (belegt): Fuer D5 existiert ein frueher Stationsanker mit teilquantifiziertem Basisinventar; er taugt fuer lokale Startwerte, aber nicht fuer aktuelle Restbestaende ohne spaetere Verbrauchs- und Transferkette.
  - Quelle: `database-curated/staging/RAW-canvas-2025-10-16T12-00-00-000Z.normalized.txt`, [D5](../03-locations/D5.md)

Aktionen
--------
- [ ] Lagerplätze definieren und QR/Tagging überlegen
- [ ] Verbrauchslog anlegen
