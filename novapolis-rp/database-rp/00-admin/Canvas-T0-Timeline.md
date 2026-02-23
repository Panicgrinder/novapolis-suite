---
stand: 2026-02-23 03:01
update: Frische-Review durchgeführt; globaler Timeline-Index und Fraktionsverweise geprüft (kein Inhaltsdelta).
checks: "npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/00-admin/Reference-Campaign-State.md' 'novapolis-rp/database-rp/00-admin/Canvas-T0-Timeline.md' 'novapolis-rp/database-rp/00-admin/Migrationsplan-Admin-Novapolis.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-23 03:02); .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py 'novapolis-rp/database-rp/00-admin/Reference-Campaign-State.md' 'novapolis-rp/database-rp/00-admin/Canvas-T0-Timeline.md' 'novapolis-rp/database-rp/00-admin/Migrationsplan-Admin-Novapolis.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-23 03:02); npm --prefix novapolis-rp/coding/tools/validators run validate:rp PASS (2026-02-23 03:02)"
slug: canvas-t0-timeline
canvas: Timeline T+0
last-updated: 2025-11-07T04:09:00+01:00
category: Admin
version: 0.1
---

Timeline (T0) - Globaler Index
==============================

Zweck
-----

Dieses Dokument definiert **globale Timeline-Regeln** und verweist auf die
fraktionsspezifischen T0-Timelines unter `01-factions/*/00-doctrine/`.

Globale Regeln
--------------

- T0/T+X Marker sind relative Kampagnenanker, keine stillen Datums-Retcons.
- Fraktionsdetails (Orte, Szenen, konkrete Ereignisfolgen) werden nur in der
  jeweiligen Fraktions-Timeline gepflegt.
- Tageswechsel/Debug-Mechanik bleibt global referenziert über
  [Canvas-Admin-Day-Switch-Debug](./Canvas-Admin-Day-Switch-Debug.md).

Fraktions-Timelines (Zielablage)
--------------------------------

- Novapolis: [novapolis-t0-timeline](../01-factions/novapolis/00-doctrine/novapolis-t0-timeline.md)
- Arkologie A1: [arkologie-a1-t0-timeline](../01-factions/arkologie-a1/00-doctrine/arkologie-a1-t0-timeline.md)
- Eisenkonklave: [eisenkonklave-t0-timeline](../01-factions/eisenkonklave/00-doctrine/eisenkonklave-t0-timeline.md)
- Flüsterkollektiv: [fluesterkollektiv-t0-timeline](../01-factions/fluesterkollektiv/00-doctrine/fluesterkollektiv-t0-timeline.md)
- Händlerbund: [haendlerbund-t0-timeline](../01-factions/haendlerbund/00-doctrine/haendlerbund-t0-timeline.md)
- Schattenbund: [schattenbund-t0-timeline](../01-factions/schattenbund/00-doctrine/schattenbund-t0-timeline.md)
- Schienenbund: [schienenbund-t0-timeline](../01-factions/schienenbund/00-doctrine/schienenbund-t0-timeline.md)

Links
-----

- [Admin: Day-Switch & Debug](./Canvas-Admin-Day-Switch-Debug.md)
- [Missionslog (globaler Index)](./Missionslog.md)
- [Logistik (globales Regelwerk)](./Logistik.md)


