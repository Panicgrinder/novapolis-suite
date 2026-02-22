---
stand: 2026-02-22 04:16
update: NPC-Fraktionszuordnung für T0 konkretisiert (Varianzmodell) und B2 als große Basisstation des Schienenbunds vorgemerkt.
checks: npm --prefix novapolis-rp/coding/tools/validators run validate:rp PASS (2026-02-22 04:05); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/00-admin/Metrokarte-T0.md' 'novapolis-rp/database-rp/00-admin/Stationskontroll-Matrix.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-22 04:05); .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py 'novapolis-rp/database-rp/00-admin/Metrokarte-T0.md' 'novapolis-rp/database-rp/00-admin/Stationskontroll-Matrix.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-22 04:05)
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
