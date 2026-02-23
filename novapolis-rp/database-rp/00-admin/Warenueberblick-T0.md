---
stand: 2026-02-23 04:15
update: Frische-Review durchgeführt; T0-Lagebild, Statuslegende und Guardrails weiterhin gültig (kein Kanon-Delta).
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md' PASS (2026-02-23 04:15); .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py 'novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md' PASS (2026-02-23 04:15); npm --prefix novapolis-rp/coding/tools/validators run validate:rp PASS (2026-02-23 04:15)
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
