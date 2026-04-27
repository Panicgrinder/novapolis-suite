---
stand: 2026-04-27 02:30
update: Schattenbund fuehrt jetzt zusaetzlich den konservativen Betriebskorridor T0 fuer F9 und den Korridor F9-G6.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260427_022916.md
canvas: Inventar Schattenbund
last_updated: 2026-04-27T02:06:00+02:00
category: inventory
slug: schattenbund-inventar
owner: schattenbund
scope: faction
version: "0.1"
tags: []
---

Inventar - Schattenbund (Fraktion)
=================================

Bestände (Auszug)
-----------------
- Kugeln (neu): hochwertig (1 neu ≈ 10 gebraucht; Bestand nicht quantifiziert)
- Kugeln (gebraucht): Alltagswährung/Hauptmunition (Qualität streut; Bestand nicht quantifiziert)
- Schmuggelware: variabel (stark situationsabhängig; keine Stückzahlen)
- Werkzeuge (leise/kompakt): variabel (keine Stückzahlen)
- Tarnmaterial/Identitäten: variabel (Dokumente, Plomben, Marker; keine Stückzahlen)

Rahmenlage (T0)
---------------

- Schattenbund bleibt als opportunistischer Beschaffungs- und Abschirmraum gerahmt, nicht als hartes Mengendepot.
- Dominante Herkunftslabel: `scavenged`, `unknown`.
- Konkrete Ware, Lagerstände und Quoten zwischen Schmuggel, Tarnung und Werkzeug bleiben bis zu neuer Belegkette `tbd`.

Betriebskorridor T0
-------------------

- Das konservative Betriebsmodell fuehrt `F9` als aktiven Kern und `F9 -> G6` als aktiven Tarnungs- und Bewegungskorridor desselben Schattenblocks; siehe [schattenbund-betriebsmodell-t0](../00-doctrine/schattenbund-betriebsmodell-t0.md) und [schattenbund-nahraum-t0](../00-doctrine/schattenbund-nahraum-t0.md).
- Inventarseitig folgt daraus: belastbar ist der Kernsockel in `F9`, waehrend der Korridor Beschaffung, Abschirmung und Risiko rahmt, aber kein zweites Vollinventar begruendet.

Aussenlage (belegt)
-------------------

- Novapolis bleibt fuer den Schattenbund `unbekannt`.
- Die Eisenkonklave ist als `feindselig` belegt; Arkologie A1 bleibt als `verdeckt` gerahmter Bezug bestehen.
- Jarek Voan fuehrt verdeckte Warenstroeme ueber redundante Zwischenhaendler, Ausweichrouten und gestaffelte Uebergaben.
- Sera Nol sichert kritische Uebergaben und Gegenaufklaerung ab; Nyra Vehl setzt Prioritaeten und Eskalationslinien.
- Konkrete Gegenparteien, Mengen, Routen und Stationslager pro Aussenkontakt bleiben ohne Dealbeleg `tbd`.

Bewegungen (Log)
----------------
- 2026-01-14: Baseline angelegt; keine Buchungen dokumentiert.
- 2026-03-31 [RAHMENWERT] Opportunistischer Schmuggel- und Tarnraum aus `Warenueberblick-T0.md` und Arbeitsledger fuer die finale Metro-Warenzuteilung bestaetigt; keine Mengensetzung vorgenommen.
- 2026-04-01 [FACT?] Der RAW-Cluster `schattenbund_feld` belegt fuer den Schattenbund die Aussenlage `Novapolis(unbekannt)`, `Eisenkonklave(feindselig)`, `Arkologie(verdeckt)`. Quelle: `../../../database-raw/99-exports/RAW-canvas-2025-10-16T16-55-00-000Z.txt`, [Relationslog-Schattenbund](../06-handel-diplomatie/Relationslog-Schattenbund.md).
- 2026-04-01 [FACT?] Beschaffungs- und Sicherheitskette laufen ueber `Jarek Voan -> Sera Nol -> Nyra Vehl`: Jarek fuehrt verdeckte Warenstroeme, Sera schirmt kritische Uebergaben ab, Nyra verantwortet Eskalations- und Prioritaetslinien. Quelle: [Jarek-Voan](../02-characters/Jarek-Voan.md), [Sera-Nol](../02-characters/Sera-Nol.md), [Nyra-Vehl](../02-characters/Nyra-Vehl.md), [Handelslog-Schattenbund](../06-handel-diplomatie/Handelslog-Schattenbund.md).
- Template: YYYY-MM-DD | Bezug: scene-... | Delta: +/− | Gegenpartei: ... | Abrechnung: Kugeln/Tausch | Notiz: ...

Links
-----
- Logistik (Admin) → ../../../00-admin/Logistik.md
- Missionslog → ../05-projects/Missionslog-Schattenbund.md
- Handelslog → ../06-handel-diplomatie/Handelslog-Schattenbund.md
- Relationslog → ../06-handel-diplomatie/Relationslog-Schattenbund.md
- Währung "Kugeln" (Reference) → ../../../00-admin/Reference-Campaign-State.md
