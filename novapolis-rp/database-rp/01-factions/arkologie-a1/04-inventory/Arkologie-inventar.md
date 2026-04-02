---
stand: 2026-04-02 06:27
update: Arkologie-A1 fuehrt jetzt den belegten beschraenkten Haendlergilden-Kanal und die umkaempfte Eisenkonklave-Lage; Mengen bleiben offen.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260402_062604.md
canvas: Inventar Arkologie
last_updated: 2026-03-31T18:22:53+02:00
category: inventory
slug: arkologie-inventar
owner: arkologie
scope: location
version: "0.1"
---

Inventar - Arkologie (Fraktion)
================================

Bestände (Auszug)
-----------------
- Kugeln (neu): hochwertig (1 neu ≈ 10 gebraucht; Bestand nicht quantifiziert)
- Kugeln (gebraucht): Alltagswährung/Hauptmunition (Qualität streut; Bestand nicht quantifiziert)
- Grundversorgung: stabil (ohne Stückzahlen)
- Austauschgüter: selektiv verfügbar (ohne Stückzahlen)
- Ersatzteile: variabel (keine Stückzahlen)

Rahmenlage (T0)
---------------

- Arkologie-A1 bleibt als etablierter externer Block mit stabiler Grundversorgung und selektiven Austauschgütern gerahmt.
- Dominante Herkunftslabel: `produced`, `legacy`.
- Konkrete Stationslager, interne Lagerquoten und harte Mengen bleiben bis zu neuer Belegkette `tbd`.

Aussenlage (belegt)
-------------------

- Der Haendlerbund ist fuer Arkologie A1 als `beschraenkt` belegt; nur gepruefte Lieferketten und freigegebene Tauschfenster sind impliziert.
- Nera Vossen fuehrt externe Verhandlungen und Lieferkorridore; Borin Khade gibt Sicherheitsfreigaben fuer Tausch- und Transitfenster.
- Liora Navesh setzt die strategischen Leitplanken ueber Datenvaliditaet, Biosicherheit und harte Sicherheitsauflagen.
- Die Eisenkonklave bleibt als `umkaempft` belegt; Novapolis bleibt fuer Arkologie A1 weiter `unbekannt`.
- Konkrete Gegenleistungen, Mengen, Routen und Stationslager pro Aussenkontakt bleiben ohne Dealbeleg `tbd`.

Bewegungen (Log)
----------------
- 2026-03-31 [RAHMENWERT] T0-Warenbild aus `Warenueberblick-T0.md` und dem Arbeitsledger fuer die finale Metro-Warenzuteilung bestaetigt; keine Mengensetzung vorgenommen.
- 2026-03-31 [FACT?] Der RAW-Cluster `arkologie_a1` belegt fuer Arkologie A1 die Aussenlage `Haendlergilde(beschraenkt)` und `Eisenkonklave(umkaempft)`; Novapolis bleibt `unbekannt`. Quelle: `../../../database-raw/99-exports/RAW-canvas-2025-10-16T16-55-00-000Z.txt`, [Relationslog-Arkologie-A1](../06-handel-diplomatie/Relationslog-Arkologie-A1.md).
- 2026-03-31 [FACT?] Handels- und Sicherheitskette laufen ueber `Nera Vossen -> Borin Khade -> Liora Navesh`: Nera fuehrt Tauschfenster/Lieferkorridore, Borin gibt Sicherheitsfreigaben, Liora setzt Biosicherheits- und Validierungsleitplanken. Quelle: [Nera-Vossen](../02-characters/Nera-Vossen.md), [Borin-Khade](../02-characters/Borin-Khade.md), [Liora-Navesh](../02-characters/Liora-Navesh.md), [Handelslog-Arkologie-A1](../06-handel-diplomatie/Handelslog-Arkologie-A1.md).
- Template: YYYY-MM-DD | Bezug: scene-/missionslog-/admin-artefakt | Delta: +/− | Gegenpartei: ... | Abrechnung: Kugeln/Tausch | Notiz: ...

Links
-----
- Logistik (Admin) → ../../../00-admin/Logistik.md
- Missionslog → ../05-projects/Missionslog-Arkologie-A1.md
- Handelslog → ../06-handel-diplomatie/Handelslog-Arkologie-A1.md
- Relationslog → ../06-handel-diplomatie/Relationslog-Arkologie-A1.md
- Währung "Kugeln" (Reference) → ../../../00-admin/Reference-Campaign-State.md

