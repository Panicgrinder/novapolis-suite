---
stand: 2026-02-23 04:21
update: Frische-Review durchgeführt; Kontrollmatrix und 54/54-Referenzabdeckung weiterhin gültig (kein Kanon-Delta).
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/00-admin/Stationskontroll-Matrix.md' PASS (2026-02-23 04:22); .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py 'novapolis-rp/database-rp/00-admin/Stationskontroll-Matrix.md' PASS (2026-02-23 04:22); npm --prefix novapolis-rp/coding/tools/validators run validate:rp PASS (2026-02-23 04:22)
slug: stationskontroll-matrix
category: Admin
canvas: stationskontrolle-t0
status: active
owners: [admin-novapolis]
tags: [rp, admin, stationskontrolle, t0]
relatedSlugs: [metrokarte-t0, current-state, logistik]
---

Stationskontroll-Matrix (T0)
============================

Zweck
-----

Globale Übersicht, welche Fraktion eine Station aktuell primär kontrolliert
und wie stabil diese Kontrolle ist.

Kontroll- und Stabilitätsmatrix
-------------------------------

| Station | Primaere Kontrolle | Stabilitaet | Evidenzanker |
| --- | --- | --- | --- |
| D5 | Novapolis | aktiv | Missionslog Novapolis / D5 |
| C6 | Novapolis | teilaktiv | Missionslog Novapolis / C6 |
| E3 | Novapolis (historisch) | evakuiert | Missionslog Novapolis / E3 |
| A1 | Arkologie-A1 | aktiv | Fraktions-Missionslog |
| A3 | Arkologie-A1 | teilaktiv | Fraktions-Missionslog |
| A5 | Arkologie-A1 | aktiv | Fraktions-Missionslog |
| B2 | Schienenbund | aktiv | Fraktions-Missionslog (Basis, groß) |
| B3 | Schienenbund | aktiv | Fraktions-Missionslog |
| G7 | Haendlerbund | aktiv | Fraktions-Missionslog |
| G5 | Haendlerbund | teilaktiv | Fraktions-Missionslog |
| F5 | Haendlerbund | aktiv | Fraktions-Missionslog |
| F9 | Schattenbund | aktiv | Fraktions-Missionslog |
| F7 | Schattenbund | aktiv | Fraktions-Missionslog |
| H12 | Eisenkonklave | aktiv | Fraktions-Missionslog |
| H3 | Eisenkonklave | teilaktiv | Fraktions-Missionslog |
| H2 | Eisenkonklave | aktiv | Fraktions-Missionslog |
| G1 | Eisenkonklave | aktiv | Fraktions-Missionslog |
| K4 | Fluesterkollektiv | aktiv | Fraktions-Missionslog |
| H1 | Fluesterkollektiv | teilaktiv | Fraktions-Missionslog |
| G6 | Fluesterkollektiv | aktiv | Fraktions-Missionslog |
| A2 | Neutral/Transit | aktiv | Metrokarte-T0 / A2 |
| A4 | Neutral/Transit | teilaktiv | Metrokarte-T0 / A4 |
| A6 | Neutral/Transit | tbd | Metrokarte-T0 / A6 |
| B1 | Neutral/Transit | aktiv | Metrokarte-T0 / B1 |
| B4 | Neutral/Transit | aktiv | Metrokarte-T0 / B4 |
| B5 | Neutral/Transit | teilaktiv | Metrokarte-T0 / B5 |
| B6 | Neutral/Transit | tbd | Metrokarte-T0 / B6 |
| C1 | Neutral/Transit | aktiv | Metrokarte-T0 / C1 |
| C2 | Neutral/Transit | aktiv | Metrokarte-T0 / C2 |
| C3 | Neutral/Transit | teilaktiv | Metrokarte-T0 / C3 |
| C4 | Neutral/Transit | aktiv | Metrokarte-T0 / C4 |
| C5 | Neutral/Transit | aktiv | Metrokarte-T0 / C5 |
| C7 | Neutral/Transit | teilaktiv | Metrokarte-T0 / C7 |
| D1 | Neutral/Transit | aktiv | Metrokarte-T0 / D1 |
| D2 | Neutral/Transit | teilaktiv | Metrokarte-T0 / D2 |
| D3 | Neutral/Transit | aktiv | Metrokarte-T0 / D3 |
| D4 | Neutral/Transit | aktiv | Metrokarte-T0 / D4 |
| D6 | Neutral/Transit | teilaktiv | Metrokarte-T0 / D6 |
| D7 | Neutral/Transit | aktiv | Metrokarte-T0 / D7 |
| E1 | Neutral/Transit | teilaktiv | Metrokarte-T0 / E1 |
| E2 | Neutral/Transit | aktiv | Metrokarte-T0 / E2 |
| E4 | Neutral/Transit | tbd | Metrokarte-T0 / E4 |
| E5 | Neutral/Transit | aktiv | Metrokarte-T0 / E5 |
| E6 | Neutral/Transit | teilaktiv | Metrokarte-T0 / E6 |
| E7 | Neutral/Transit | aktiv | Metrokarte-T0 / E7 |
| F1 | Neutral/Transit | aktiv | Metrokarte-T0 / F1 |
| F2 | Neutral/Transit | aktiv | Metrokarte-T0 / F2 |
| F3 | Neutral/Transit | teilaktiv | Metrokarte-T0 / F3 |
| F4 | Neutral/Transit | tbd | Metrokarte-T0 / F4 |
| F6 | Neutral/Transit | teilaktiv | Metrokarte-T0 / F6 |
| F8 | Neutral/Transit | teilaktiv | Metrokarte-T0 / F8 |
| G2 | Neutral/Transit | teilaktiv | Metrokarte-T0 / G2 |
| G3 | Neutral/Transit | aktiv | Metrokarte-T0 / G3 |
| G4 | Neutral/Transit | tbd | Metrokarte-T0 / G4 |

Definitionen
------------

- `aktiv`: operativ kontrolliert und nutzbar.
- `teilaktiv`: kontrolliert, aber mit funktionalen Einschraenkungen.
- `evakuiert`: kein normaler Betrieb; nur Sonderlagen.
- `tbd`: noch nicht belastbar aus globaler Sicht belegt.

Hinweis Groessenklassen (Vormerkung)
------------------------------------

- `B2` ist als **große Station** des Schienenbunds vorgemerkt.
- Exakte m²-Werte je Größenklasse folgen nach separater Freigabe/Übergabe.

Guardrails
----------

- Keine Umwidmung der Kontrolle ohne verlinkbaren Missions-/Szenenbeleg.
- Globalebene bleibt kompakt; operative Details in den Fraktionsdateien.
- Unbelegte Konfliktlagen als offen markieren, nicht antizipieren.

Verlinkungen
------------

- [Current-State](./Current-State.md)
- [Metrokarte-T0](./Metrokarte-T0.md)
- [Logistik](./Logistik.md)
- [Missionslog](./Missionslog.md)
