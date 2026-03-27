---
stand: 2026-03-27 09:54
update: Guetermission D5 -> C6 als Transferanker im Missionslog verankert; Fraktionssummen bleiben ohne Item-Buchungen offen.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260327_011507.md
canvas: Inventar Novapolis
last_updated: 2026-03-20T11:40:00+01:00
category: inventory
slug: novapolis-inventar
owner: novapolis
scope: faction
version: "0.1"
---
Inventar - Novapolis (Fraktion)
================================

Hinweis: Fraktionsinventare strikt getrennt (Policy Y.1). Abrechnung im Wochenzyklus.

- Transfers zwischen D5 und C6 nur via Mission/Logistik.
- Waehrung "Kugeln" wird als Inventar-Item gefuehrt (neu/gebraucht).

Bestände (Auszug)
-----------------
- Kugeln (neu): tbd (hochwertig; 1 neu ≈ 10 gebraucht)
- Kugeln (gebraucht): tbd (Alltag/Hauptmunition; Qualität streut)
- Energiezellen: Tagesabschluss Tag 12 -> 13 mit `-12 Nettoverlust` fuer Novapolis belegt; absolute Speicherstaende D5/C6 weiter `tbd`
- Werkzeuge/Material: C6-Expeditions- und D5-Wartungskontext belegt; fuer Tag 12 -> 13 sind `1,3 t Baustoffe`, `120 m Schienenprofil`, `18 m² Betonplatten` Verbrauch sowie `2` beschaedigte Werkzeuge belegt, Restbestand weiter `tbd`
- D5-Basisanker: fruehes Stationsinventar mit `Union-Kisten (3)`, Ersatzrohren/Ventilkomponenten, defekter Reparaturstation und `60 %` lesbaren Schaltplaenen ist belegt; daraus folgen noch keine aktuellen Fraktionssummen.

Bewegungen (Log)
----------------
- 2026-03-20 06:28 [REVIEW] RAW/Staging bestaetigen den Kontext `Filter`, `Energiezellen`, `Werkzeuge` fuer Novapolis, aber ohne ausreichende Transfer-/Aggregatbelege fuer eine harte Gesamtmenge.
- 2026-03-20 06:45 [FACT?] Tagesabschluss Tag 12 -> 13: Gesamt Novapolis `-12 Energiezellen Nettoverlust`; D5 exportiert `+10` nach C6 bei lokaler Produktion `+10`, C6 endet auf `-2` Tagesbilanz. Absolute Speicherstaende bleiben offen. Quelle: `database-curated/staging/chat-export.normalized.txt`, [Logistik](../../../00-admin/Logistik.md).
- 2026-03-20 06:52 [FACT?] Tagesabschluss Tag 12 -> 13: Tunnelarbeiten verbrauchen `1,3 t Baustoffe`, `120 m Schienenprofil`, `18 m² Betonplatten`; `2` Werkzeuge sind beschaedigt und geschaetzt reparabel. Standortscharfe Entnahme und Restmengen bleiben offen. Quelle: `database-curated/staging/chat-export.normalized.txt`.
- 2026-03-20 07:22 [FACT?] D5 fuehrt einen fruehen Stationsanker mit `Union-Kisten (3)`, Ersatzrohren/Ventilkomponenten, defekter Reparaturstation und `60 %` lesbaren Schaltplaenen; Aggregation bleibt ohne spaetere Transferkette offen. Quelle: `database-curated/staging/RAW-canvas-2025-10-16T12-00-00-000Z.normalized.txt`, [D5-inventar](./D5-inventar.md).
- 2026-03-20 11:40 [REVIEW] Ein missionierter Materiallauf `D5 -> C6` ist als Vorgang belegt; RAW nennt `Bauteile`, `Werkzeuge` und `Versorgungsgueter`, der Chatverlauf bestaetigt aber eine situative Auswahl statt fixer Stueckliste. Fuer Quelleninventar, Mengen, Zielbuchung und Quittung fehlen weiterhin harte Belegzeilen. Quelle: `database-raw/99-exports/RAW-canvas-2025-10-16T13-05-00-000Z.txt`, `database-raw/99-exports/chat-export.txt`, [Missionslog-Novapolis](../05-projects/Missionslog-Novapolis.md).

Delta zum Missionslog
---------------------

- Lagebild: C6-relevante Materialbedarfe/Bestände werden über das fraktionsspezifische Missionslog nachgeführt; Fraktionsinventar führt den aggregierten Stand.
- Delta 1 (offen): Übernahme belastbarer Mengen aus C6-/D5-Teilinventaren in den Fraktionsaggregatstand.
  - Quelle: [Missionslog-Novapolis](../05-projects/Missionslog-Novapolis.md), [C6-inventar](./C6-inventar.md), [D5-inventar](./D5-inventar.md)
- Delta 2 (offen): Verbuchung missionierter Transferzeilen (Quelle→Ziel) sobald Quittungen/Belege final sind.
  - Quelle: [Missionslog-Novapolis](../05-projects/Missionslog-Novapolis.md)
- Delta 3 (belegt): Waehrung `Kugeln` bleibt als Fraktions-Item gefuehrt; Mengen- und Umlaufverteilung bleiben bis zu expliziten Belegen offen.
  - Quelle: `database-curated/staging/chat-export-complete.finalgate.md`, `database-curated/staging/chat-export (1).review.md`, [Logistik](../../../00-admin/Logistik.md)
- Delta 4 (belegt): Fuer Tag 12 -> 13 liegt eine fraktionsweite Energie-Gesamtbilanz `-12` vor; sie taugt fuer den Bilanzanker, aber nicht fuer absolute Lagerzahlen ohne Vor-/Nachher-Stand.
  - Quelle: `database-curated/staging/chat-export.normalized.txt` (Tagesabrechnung Tag 12 -> 13), [Logistik](../../../00-admin/Logistik.md)
- Delta 5 (belegt): Fuer Tag 12 -> 13 liegt ein fraktionsweites Materialdelta fuer Tunnelarbeiten vor (`1,3 t Baustoffe`, `120 m Schienenprofil`, `18 m² Betonplatten`, `2` beschaedigte Werkzeuge); es taugt fuer den Verbrauchsanker, aber nicht fuer Restbestandszahlen ohne Vor-/Nachher-Stand.
  - Quelle: `database-curated/staging/chat-export.normalized.txt` (Materialverbrauch / Werkzeuginspektion Tag 12 -> 13)
- Delta 6 (belegt/offen): Mit D5 und C6 liegen jetzt zwei lokale Fruehanker vor; fuer harte Fraktionssummen fehlen aber weiterhin spaetere Transfer-, Verbrauchs- und Zustellketten.
  - Quelle: [D5-inventar](./D5-inventar.md), [C6-inventar](./C6-inventar.md), `database-curated/staging/RAW-canvas-2025-10-16T13-05-00-000Z.normalized.txt`
- Delta 7 (belegt/offen): Eine konkrete Guetermission `D5 -> C6` ist jetzt als Missionsvorgang verankert; sie belegt die Transportrichtung, aber nicht die Item-Kette `Entnahme -> Transport -> Ankunft -> Quittung`.
  - Quelle: [Missionslog-Novapolis](../05-projects/Missionslog-Novapolis.md), `database-raw/99-exports/RAW-canvas-2025-10-16T13-05-00-000Z.txt`, `database-raw/99-exports/chat-export.txt`
- Delta 8 (belegt/offen): `C6 -> D5 (Materialrueckfuehrung)` ist im RAW-Logistikcanvas ebenfalls nur generisch belegt; ohne Charge, Datum, Verantwortliche und Zielbuchung bleibt die Rueckfuehrung fuer Bestandsmathematik zu weich.
  - Quelle: `database-raw/99-exports/RAW-canvas-2025-10-16T13-05-00-000Z.txt`, [Logistik](../../../00-admin/Logistik.md)

Links
-----
- Logistik-Policy C6 → ../03-locations/C6-Logistik-Policy.md
- Logistik (Admin) → ../../../00-admin/Logistik.md
- Missionslog → ../05-projects/Missionslog-Novapolis.md
- Währung "Kugeln" (Reference) → ../../../00-admin/Reference-Campaign-State.md


