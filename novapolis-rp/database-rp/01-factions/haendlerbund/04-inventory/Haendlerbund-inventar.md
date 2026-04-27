---
stand: 2026-04-27 02:30
update: Der Haendlerbund fuehrt jetzt zusaetzlich den konservativen Betriebskorridor T0 fuer G7 als Zentrale und C6 als eingebettete Niederlassung.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260427_022916.md
canvas: Inventar Händlerbund
last_updated: 2026-04-27T02:17:00+02:00
category: inventory
slug: haendlerbund-inventar
owner: haendlerbund
scope: faction
version: "0.1"
---

Inventar - Händlerbund (Fraktion)
=================================

Bestände (Auszug)
-----------------
- Kugeln (neu): hochwertig (1 neu ≈ 10 gebraucht; Bestand nicht quantifiziert)
- Kugeln (gebraucht): Alltagswährung/Hauptmunition (Qualität streut; Bestand nicht quantifiziert)
- Handelswaren: variabel (Umlaufgüter vorhanden, keine Stückzahlen)
- Ersatzteile/Werkzeug: variabel (keine Stückzahlen)
- Stationäre Reserven: schwankend, nicht quantifiziert

Rahmenlage (T0)
---------------

- Haendlerbund bleibt als Umlauf- und Versorgungsraum mit variablen stationären Reserven gerahmt.
- Dominante Herkunftslabel: `legacy`, `scavenged`, `produced`.
- Konkrete Umlaufmengen, feste Stationslager und belastbare Bestandsketten bleiben bis zu neuer Belegkette `tbd`.

Betriebskorridor T0
-------------------

- Das konservative Betriebsmodell fuehrt `G7` als aktive externe Zentrale und `C6` als belegte eingebettete Niederlassung desselben Haendlerbund-Blocks; siehe [haendlerbund-betriebsmodell-t0](../00-doctrine/haendlerbund-betriebsmodell-t0.md) und [haendlerbund-nahraum-t0](../00-doctrine/haendlerbund-nahraum-t0.md).
- Inventarseitig folgt daraus: belastbar ist der Kernsockel in `G7`, waehrend `C6` als Partner- und Niederlassungsfenster Austausch, Ruecklauf und Versorgungslogik rahmt, aber kein zweites unabhaengiges Haendlerbund-Vollinventar begruendet.

Handelslage (belegt)
--------------------

- `H-47` ist als ueberlebende Haendlerkarawane mit dauerhafter Kooperation zu Novapolis belegt; `C6` ist als Handelsstuetzpunkt aktiviert.
- `G7` bleibt externer Eigenkern des Haendlerbunds; `H-47` fuehrt in `C6 / Novapolis` die belegte eingebettete Niederlassung und den wichtigsten Partnerpfad.
- Belegte Austauschklassen im Aufbaupfad sind `Energie`, `technische Reparaturen`, `Kommunikationszugang` gegen `Nahrungsmittel`, `Filter` und `Grundbedarfsgueter`.
- Konkrete Dealmengen, Konvoi-Manifest, Abrechnung und standortscharfe Lageranteile bleiben `tbd`.

Bewegungen (Log)
----------------
- 2026-03-31 [RAHMENWERT] Umlauf- und Versorgungsraum aus `Warenueberblick-T0.md` und Arbeitsledger fuer die finale Metro-Warenzuteilung bestaetigt; keine Mengensetzung vorgenommen.
- 2026-03-31 [FACT?] `E-0004: Erste Handelsroute (H-47)` belegt fuer `D5 / C6` die erfolgreiche Verhandlung ueber dauerhafte Kooperation, die Integration der Haendlergruppe und `C6 als Handelsstuetzpunkt aktiviert`. Quelle: `../../../database-raw/99-exports/RAW-canvas-2025-10-16T05-34-00-000Z.txt`, [Missionslog-Haendlerbund](../05-projects/Missionslog-Haendlerbund.md), [caravan-moves](../05-projects/caravan-moves.md).
- 2026-03-31 [FACT?] Das diplomatische Lagebild fuehrt erste Handelskontakte ueber Karawane `H-47 (Senn Daru)` in `C6`; belegt sind die Austauschklassen `Energie`, `technische Reparaturen`, `Kommunikationszugang` sowie `Nahrungsmittel`, `Filter`, `Grundbedarfsgueter`. Quelle: `../../../database-raw/99-exports/RAW-canvas-2025-10-16T08-07-00-000Z.txt`, [G7](../03-locations/G7.md), [Handel-Diplomatie-Haendlergilde](../06-handel-diplomatie/Handel-Diplomatie-Haendlergilde.md).
- Template: YYYY-MM-DD | Bezug: scene-/missionslog-/admin-artefakt | Delta: +/− | Gegenpartei: ... | Abrechnung: Kugeln/Tausch | Notiz: ...

Links
-----
- Logistik (Admin) → ../../../00-admin/Logistik.md
- Missionslog → ../05-projects/Missionslog-Haendlerbund.md
- G7 → ../03-locations/G7.md
- Karawanenbewegungen → ../05-projects/caravan-moves.md
- Währung "Kugeln" (Reference) → ../../../00-admin/Reference-Campaign-State.md

