---
stand: 2026-04-27 01:53
update: Arkologie-A1 fuehrt jetzt den belegten Dreistationskern A1/A3/A5 als Kerngebiet mit Funktionsrahmen.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260427_015145.md
canvas: Inventar Arkologie
last_updated: 2026-04-27T01:14:00+02:00
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

Kerngebiet A1/A3/A5 (belegt, konservativ)
-----------------------------------------

Hinweise

- Arkologie-A1 fuehrt nicht nur einen Ein-Station-Sockel, sondern einen kontrollierten Dreistationskern aus `A1`, `A3` und `A5`.
- Belastbar sind Status, Kernfunktion und Guardrails je Station; unbelastbar bleiben Mengen, Lagerquoten und echte Stationsbilanzen.

| Station | Status | Lager- / Funktionsrahmen |
| --- | --- | --- |
| [A1](../03-locations/A1.md) | aktiv | Fuehrungs-, Forschungs-, Freigabe- und Screeningzentrum; hier laufen selektive Austauschgueter nur unter harter Sicherheits- und Biosicherheitskette |
| [A3](../03-locations/A3.md) | teilaktiv | Validierungs-, Quarantaene- und Sicherungspuffer; sensible Reservegueter und gepruefte Eingaenge duerfen hier zwischengelagert oder zurueckgehalten werden |
| [A5](../03-locations/A5.md) | aktiv | Versorgungs- und Aufbereitungsanker; Grundversorgung sowie vorbereitete Austauschgueter koennen hier intern gepuffert und fuer enge Fenster bereitgestellt werden |

Arbeitslesart

- `A1` fuehrt die Freigabe und den sichtbaren Aussenkontakt.
- `A3` entlastet den Kern ueber Pruef-, Puffer- und Abschirmfunktion statt ueber hohen Durchsatz.
- `A5` traegt den internen Versorgungs- und Vorbereitungspfad, ohne daraus freie Marktlogik zu machen.

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
- 2026-04-27 01:14 [REVIEW] Arkologie-A1 fuehrt jetzt ihr Kerngebiet explizit als Dreistationskern `A1/A3/A5`. `A1` bleibt Leit- und Freigabeknoten, `A3` der teilaktive Validierungs- und Quarantaenepuffer, `A5` der aktive Versorgungs- und Aufbereitungsanker. Mengen und Stationsquoten bleiben bewusst offen. Quelle: [A1](../03-locations/A1.md), [A3](../03-locations/A3.md), [A5](../03-locations/A5.md), [Arkologie-A1](../Arkologie-A1.md), [Stationskontroll-Matrix](../../../00-admin/Stationskontroll-Matrix.md), [Metrokarte-T0](../../../00-admin/Metrokarte-T0.md), [Missionslog-Arkologie-A1](../05-projects/Missionslog-Arkologie-A1.md).
- Template: YYYY-MM-DD | Bezug: scene-/missionslog-/admin-artefakt | Delta: +/− | Gegenpartei: ... | Abrechnung: Kugeln/Tausch | Notiz: ...

Links
-----
- Logistik (Admin) → ../../../00-admin/Logistik.md
- Missionslog → ../05-projects/Missionslog-Arkologie-A1.md
- Handelslog → ../06-handel-diplomatie/Handelslog-Arkologie-A1.md
- Relationslog → ../06-handel-diplomatie/Relationslog-Arkologie-A1.md
- Währung "Kugeln" (Reference) → ../../../00-admin/Reference-Campaign-State.md

