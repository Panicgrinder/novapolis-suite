---
stand: 2026-03-05 01:00
update: T0-Ergaenzung fuer Fraktionsueberblick mit Herkunftslabeln sowie explizite D5/C6-Aufbauphasenregel ohne implizite Handelsannahmen.
checks: scripts/run_checks_and_report.py overall=FAIL; markdownlint=PASS; frontmatter=PASS; path-portability=FAIL; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260305_005843.md
slug: warenueberblick-t0
category: Admin
canvas: warenueberblick-t0
status: active
owners: [admin-novapolis]
tags: [rp, admin, waren, logistik, t0]
relatedSlugs: [logistik, current-state, stationskontroll-matrix]
---

Warenueberblick (T0)
====================

Zweck
-----

Kompakte operative Übersicht, welche Warengruppen an welchen Kernstandorten
aktuell als verfuegbar, knapp oder offen gelten.

Abgrenzung
----------

- Der [Waren-Index](./Waren-Index.md) bleibt die Katalog-/Definitions-SSOT.
- Dieser Überblick zeigt nur den T0-Lagestatus ohne Mengenretcon.

Lagebild nach Warengruppen (MVP)
--------------------------------

| Warengruppe | D5 | C6 | E3 | Hinweis |
| --- | --- | --- | --- | --- |
| Energie / Zellen | verfuegbar | knapp | tbd | C6 mit teilaktivem Betrieb |
| Wasser / Filter | verfuegbar | knapp | tbd | C6-Monitoring als Engpasssignal |
| Werkzeuge / Reparatur | verfuegbar | verfuegbar | tbd | aus Missions-/Inventarplaenen fortschreiben |
| Medizin / Erste Hilfe | tbd | tbd | tbd | global noch nicht belastbar zusammengeführt |
| Nahrung / Verbrauchsgueter | tbd | tbd | tbd | fraktionsseitig nachziehen |

Fraktionsueberblick T0 (Herkunftslabel)
---------------------------------------

Hinweis: Die Label folgen dem P0-Schema `legacy|evac_e3|scavenged|produced|unknown`.

| Fraktion | T0-Warenbild (Bandbreite) | Herkunftslabel (dominant) | Verweis |
| --- | --- | --- | --- |
| Novapolis (D5/C6/E3) | Energie/Wasser/Werkzeuge verfuegbar, Medizin/Nahrung teils knapp | legacy, evac_e3, scavenged | [Fraktionen-Taxonomie](./Fraktionen-Taxonomie.md), [Stationskontroll-Matrix](./Stationskontroll-Matrix.md) |
| Arkologie-A1 | Grundversorgung stabil, Austausch gueter selektiv | produced, legacy | [Fraktionen-Taxonomie](./Fraktionen-Taxonomie.md) |
| Schienenbund | Logistik-/Reparaturfokus, Verbrauchsgueter variabel | produced, scavenged | [Fraktionen-Taxonomie](./Fraktionen-Taxonomie.md) |
| Schattenbund | Versorgung uneinheitlich, Schwerpunkt opportunistische Beschaffung | scavenged, unknown | [Fraktionen-Taxonomie](./Fraktionen-Taxonomie.md) |
| Haendlerbund | Umlaufgueter verfuegbar, stationaere Reserven variabel | legacy, scavenged, produced | [Fraktionen-Taxonomie](./Fraktionen-Taxonomie.md) |
| Eisenkonklave | Werkstoff-/Instandsetzungsgueter verfuegbar, Verbrauchsgueter variabel | produced, legacy | [Fraktionen-Taxonomie](./Fraktionen-Taxonomie.md) |
| Fluesterkollektiv | Lagerbild nur teilweise belastbar | unknown, scavenged | [Fraktionen-Taxonomie](./Fraktionen-Taxonomie.md) |

D5/C6-Modell (fruehe Aufbauphase)
---------------------------------

- D5/C6 bleiben in T0 explizit als fruehe Aufbauphase modelliert.
- Keine impliziten Handelsnormalisierungen: Verfuegbarkeit wird aus Altbestand (`legacy`), Mitnahme (`evac_e3`) und Fund-/Rueckgewinnung (`scavenged`) abgeleitet.
- Mengenretcons bleiben untersagt, bis belastbare Inventar-/Transferbelege vorliegen.

Statuslegende
-------------

- `verfuegbar`: einsatzbereit laut belegter Operativlage.
- `knapp`: vorhanden, aber priorisierungsbeduerftig.
- `tbd`: keine belastbare globale Zusammenfuehrung.

Guardrails
----------

- Keine absoluten Mengen ohne belegte Inventar-/Transferbasis.
- Keine implizite Marktnormalisierung fuer fruehe Aufbauphase D5/C6.
- Fortschreibung erfolgt aus Fraktionsinventaren und Missionslogs.

Verlinkungen
------------

- [Waren-Index](./Waren-Index.md)
- [Logistik](./Logistik.md)
- [Current-State](./Current-State.md)
- [Stationskontroll-Matrix](./Stationskontroll-Matrix.md)


