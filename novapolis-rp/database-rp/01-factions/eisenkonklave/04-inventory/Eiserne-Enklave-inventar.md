---
stand: 2026-04-02 06:27
update: Die Eisenkonklave fuehrt jetzt den belegten Haendlerbund-Handelsrahmen samt Freigabekette; Mengen bleiben offen.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260402_062604.md
canvas: Inventar Eiserne Enklave
last_updated: 2026-03-31T18:12:34+02:00
category: inventory
slug: eiserne-enklave-inventar
owner: eiserne-enklave
scope: faction
version: "0.1"
---

Inventar - Eiserne Enklave (Fraktion)
=====================================

Bestände (Auszug)
-----------------
- Kugeln (neu): hochwertig (1 neu ≈ 10 gebraucht; Bestand nicht quantifiziert)
- Kugeln (gebraucht): Alltagswährung/Hauptmunition (Qualität streut; Bestand nicht quantifiziert)
- Waffen/Schutzausrüstung: variabel (keine Stückzahlen)
- Rohstoffe: variabel (keine Stückzahlen)
- Werkstoff-/Instandsetzungsgüter: belastbarer Rollenrahmen, aber nicht quantifiziert

Rahmenlage (T0)
---------------

- Eisenkonklave bleibt als Werkstoff- und Schutzgüterraum gerahmt, nicht als quantifiziertes Gesamtlager.
- Dominante Herkunftslabel: `produced`, `legacy`.
- Konkrete Rohstoffmengen, Waffenbestände und stationsscharfe Lageranteile bleiben bis zu neuer Belegkette `tbd`.

Handelslage (belegt)
--------------------

- Der Haendlerbund ist fuer die Eisenkonklave als `handel_gelegentlich` belegt.
- Kaspar Dorn fuehrt Tauschfenster und Priorlisten; Yara Kest gibt Sicherheitsfreigaben fuer Handelsfenster und Konvois.
- Werkstoff-/Instandsetzungsgueter, Rohstoffe und Schutzgueter bleiben die belegten Eigenklassen der Fraktion; ob und wann daraus konkrete Handelsware wird, bleibt pro Fenster `tbd`.
- Konkrete Gegenleistungen, Liefermengen, Route und Zeitfenster bleiben ohne Dealbeleg `tbd`.

Bewegungen (Log)
----------------
- 2026-03-31 [RAHMENWERT] Werkstoff- und Schutzgüterrahmen aus `Warenueberblick-T0.md` und Arbeitsledger fuer die finale Metro-Warenzuteilung bestaetigt; keine Mengensetzung vorgenommen.
- 2026-03-31 [FACT?] Der RAW-Cluster `eisenkonklave_operativ` belegt fuer die Eisenkonklave `Haendlergilde(handel_gelegentlich)` als aktive Aussenlage. Quelle: `../../../database-raw/99-exports/RAW-canvas-2025-10-16T16-55-00-000Z.txt`, [Relationslog-Eisenkonklave](../06-handel-diplomatie/Relationslog-Eisenkonklave.md).
- 2026-03-31 [FACT?] Handelsfenster laufen nur ueber die Freigabekette `Kaspar Dorn -> Yara Kest`; Kaspar fuehrt Tauschfenster/Priorlisten, Yara erteilt Sicherheitsfreigaben fuer Handelsfenster und Konvois. Quelle: [Kaspar-Dorn](../02-characters/Kaspar-Dorn.md), [Yara-Kest](../02-characters/Yara-Kest.md), [Handelslog-Eisenkonklave](../06-handel-diplomatie/Handelslog-Eisenkonklave.md).
- Template: YYYY-MM-DD | Bezug: scene-/missionslog-/admin-artefakt | Delta: +/− | Gegenpartei: ... | Abrechnung: Kugeln/Tausch | Notiz: ...

Links
-----
- Logistik (Admin) → ../../../00-admin/Logistik.md
- Missionslog → ../05-projects/Missionslog-Eisenkonklave.md
- Handelslog → ../06-handel-diplomatie/Handelslog-Eisenkonklave.md
- Währung "Kugeln" (Reference) → ../../../00-admin/Reference-Campaign-State.md

