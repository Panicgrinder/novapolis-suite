---
stand: 2026-04-20 21:22
update: T0-Ueberblick verdichtet jetzt nur noch belegte Metro-Pfade aus D5/C6, Haendlerbund G7-<->-C6 und den externen T0-Bandbreiten; neutrale Lager und Weltsummen bleiben explizit offen.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260420_210436.md
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

Kompakte operative Übersicht, welche Warengruppen und Fraktionspfade aktuell
als belegt, knapp oder bewusst offen gelten.

Abgrenzung
----------

- Der [Waren-Index](./Waren-Index.md) bleibt die Katalog-/Definitions-SSOT.
- Dieser Überblick zeigt nur den T0-Lagestatus ohne Mengenretcon.
- Metro-weite Summen und neutrale Stationslager bleiben offen, solange sie
  nicht aus belastbaren Stations- oder Fraktionspfaden abgeleitet werden koennen.

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
| Novapolis (D5/C6/E3) | Energie/Wasser/Werkzeuge verfuegbar, Medizin/Nahrung teils knapp; D5/C6 bleiben fruehe Aufbauphase mit belegter Transfer- und Verbrauchslogik, aber ohne Marktnormalisierung | legacy, evac_e3, scavenged | [Fraktionen-Taxonomie](./Fraktionen-Taxonomie.md), [Stationskontroll-Matrix](./Stationskontroll-Matrix.md), [Logistik](./Logistik.md) |
| Arkologie-A1 | Grundversorgung stabil, Austausch gueter selektiv | produced, legacy | [Fraktionen-Taxonomie](./Fraktionen-Taxonomie.md) |
| Schienenbund | Logistik-/Reparaturfokus, Verbrauchsgueter variabel | produced, scavenged | [Fraktionen-Taxonomie](./Fraktionen-Taxonomie.md) |
| Schattenbund | Versorgung uneinheitlich, Schwerpunkt opportunistische Beschaffung | scavenged, unknown | [Fraktionen-Taxonomie](./Fraktionen-Taxonomie.md) |
| Haendlerbund | Umlaufgueter verfuegbar, stationaere Reserven variabel; `G7` bleibt Kontakt-/Umschlagpunkt, `H-47` fuehrt einen belegten G7-<->-C6-Korridor mit aktivem Handelsstuetzpunkt `C6` | legacy, scavenged, produced | [Fraktionen-Taxonomie](./Fraktionen-Taxonomie.md), [Logistik](./Logistik.md) |
| Eisenkonklave | Werkstoff-/Instandsetzungsgueter verfuegbar, Verbrauchsgueter variabel | produced, legacy | [Fraktionen-Taxonomie](./Fraktionen-Taxonomie.md) |
| Fluesterkollektiv | Lagerbild nur teilweise belastbar | unknown, scavenged | [Fraktionen-Taxonomie](./Fraktionen-Taxonomie.md) |

D5/C6-Modell (fruehe Aufbauphase)
---------------------------------

- D5/C6 bleiben in T0 explizit als fruehe Aufbauphase modelliert.
- Keine impliziten Handelsnormalisierungen: Verfuegbarkeit wird aus Altbestand (`legacy`), Mitnahme (`evac_e3`) und Fund-/Rueckgewinnung (`scavenged`) abgeleitet.
- Mengenretcons bleiben untersagt, bis belastbare Inventar-/Transferbelege vorliegen.

Aktive Metro-Pfade (verdichtet)
-------------------------------

- Novapolis: `D5` bleibt aktiver Kernanker, `C6` teilaktiver Empfangs- und Baustellenknoten; belegte Energie-, Transfer- und Verbrauchspfade duerfen aggregiert werden, ohne daraus harte Metro-Summen abzuleiten.
- Haendlerbund: `G7` bleibt externer Kontakt-/Umschlagpunkt; `H-47` fuehrt den belegten Austauschpfad nach `C6`, inklusive Handelsstuetzpunkt und belegter Austauschklassen, aber ohne Manifest- oder Mengenpromotion.
- Weitere externe Fraktionen: Arkologie-A1, Schienenbund, Eisenkonklave, Schattenbund und Fluesterkollektiv bleiben auf ihren belastbaren T0-Bandbreiten, solange keine neuen stationsscharfen Ketten vorliegen.
- Neutrale Metro-Lager und weltweite Gesamtsummen bleiben weiterhin `tbd`.

Statuslegende
-------------

- `verfuegbar`: einsatzbereit laut belegter Operativlage.
- `knapp`: vorhanden, aber priorisierungsbeduerftig.
- `tbd`: keine belastbare globale Zusammenfuehrung.

Guardrails
----------

- Keine absoluten Mengen ohne belegte Inventar-/Transferbasis.
- Keine implizite Marktnormalisierung fuer fruehe Aufbauphase D5/C6.
- Keine implizite Verdichtung neutraler Stationslager oder einer Metro-Gesamtsumme.
- Fortschreibung erfolgt aus Fraktionsinventaren und Missionslogs.

Verlinkungen
------------

- [Waren-Index](./Waren-Index.md)
- [Logistik](./Logistik.md)
- [Current-State](./Current-State.md)
- [Stationskontroll-Matrix](./Stationskontroll-Matrix.md)


