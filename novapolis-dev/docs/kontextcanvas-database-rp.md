---
stand: 2026-02-04 06:28
update: Kontextcanvas database-rp erstellt (Batch A Audit, read-only)
checks: Batch A dry-run (Naming/Validatoren/Link-Audit)
---

Kontextcanvas: database-rp
=========================

Scope-Inventar
--------------

### Markdown-only (nur .md)

- [novapolis-rp/database-rp/00-ops](novapolis-rp/database-rp/00-ops) (Ops-Notizen)
- [novapolis-rp/database-rp/06-scenes](novapolis-rp/database-rp/06-scenes) (Scenes/Chronik)

### md+json (Paare vorhanden)

- [novapolis-rp/database-rp/00-admin](novapolis-rp/database-rp/00-admin)
- [novapolis-rp/database-rp/01-factions](novapolis-rp/database-rp/01-factions)
- [novapolis-rp/database-rp/04-inventory](novapolis-rp/database-rp/04-inventory)
- [novapolis-rp/database-rp/01-factions](novapolis-rp/database-rp/01-factions) (pro Fraktion unter 06-handel-diplomatie/)

Einstiegspunkte (mit Pfaden)
----------------------------

- [novapolis-rp/database-rp/00-admin/Current-State.md](novapolis-rp/database-rp/00-admin/Current-State.md#L10-L25) (Single Entry Point)
- [novapolis-rp/database-rp/00-admin/memory-bundle.md](novapolis-rp/database-rp/00-admin/memory-bundle.md#L10-L16) (Kanon-Start)
- [novapolis-rp/database-rp/00-admin/system-prompt.md](novapolis-rp/database-rp/00-admin/system-prompt.md#L1-L10) (System-Prompt)
- [novapolis-rp/database-rp/00-ops/README.md](novapolis-rp/database-rp/00-ops/README.md#L7-L19) (Ops-Kanal)

Begriffe (Belege)
-----------------

- SSOT: [novapolis-rp/database-rp/00-admin/Current-State.md](novapolis-rp/database-rp/00-admin/Current-State.md#L71-L75) "SSOT (RP): novapolis-rp/database-rp/"
- Kanon: [novapolis-rp/database-rp/00-admin/memory-bundle.md](novapolis-rp/database-rp/00-admin/memory-bundle.md#L10-L13) "Memory-Bundle (Kanon, kompakt)"
- Ops: [novapolis-rp/database-rp/00-ops/README.md](novapolis-rp/database-rp/00-ops/README.md#L7-L19) "Ops / Systemnotes (nicht-diegetisch)"

Naming-Regeln (Auszug)
----------------------

Quelle: [novapolis-dev/docs/naming-policy.md](novapolis-dev/docs/naming-policy.md#L21-L28)

- ASCII, Bindestrich, keine Leerzeichen/Unterstriche/Klammern.
- Umlaute -> ae/oe/ue/ss.
- Endungen klein (.md, .txt).

Validatoren (Gates)
-------------------

Quellen: [novapolis-rp/coding/tools/validators/package.json](novapolis-rp/coding/tools/validators/package.json), [scripts/check_frontmatter.py](scripts/check_frontmatter.py), [scripts/checks_rp_consistency.py](scripts/checks_rp_consistency.py)

- Naming (Dry-Run): `npm --prefix novapolis-rp/coding/tools/validators run check:names`
- RP-Validator: `npm --prefix novapolis-rp/coding/tools/validators run validate:rp`
- Crossrefs: `npm --prefix novapolis-rp/coding/tools/validators run validate:crossrefs`
- Frontmatter: `& .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis-rp\database-rp`
- RP-Consistency: `& .\.venv\Scripts\python.exe scripts\checks_rp_consistency.py --strict`

Link-Audit (Batch A, Kategorien A/B/C)
--------------------------------------

### Kategorie A (00-admin -> ../01-factions/)

Total: 77

Dateien + Count

- [novapolis-rp/database-rp/00-admin/Canvas-T+0-Timeline.md](novapolis-rp/database-rp/00-admin/Canvas-T+0-Timeline.md) — 6
- [novapolis-rp/database-rp/00-admin/Logistik.md](novapolis-rp/database-rp/00-admin/Logistik.md) — 7
- [novapolis-rp/database-rp/00-admin/Metrograph.md](novapolis-rp/database-rp/00-admin/Metrograph.md) — 11
- [novapolis-rp/database-rp/00-admin/Ortsgraph.md](novapolis-rp/database-rp/00-admin/Ortsgraph.md) — 5
- [novapolis-rp/database-rp/00-admin/memory-bundle.md](novapolis-rp/database-rp/00-admin/memory-bundle.md) — 13
- [novapolis-rp/database-rp/00-admin/Missionslog.md](novapolis-rp/database-rp/00-admin/Missionslog.md) — 14
- [novapolis-rp/database-rp/00-admin/Fraktionen-Taxonomie.md](novapolis-rp/database-rp/00-admin/Fraktionen-Taxonomie.md) — 8
- [novapolis-rp/database-rp/00-admin/Current-State.md](novapolis-rp/database-rp/00-admin/Current-State.md) — 7
- [novapolis-rp/database-rp/00-admin/AI-Behavior-Mapping.md](novapolis-rp/database-rp/00-admin/AI-Behavior-Mapping.md) — 6

Exzerpte (3)

- [Canvas-T+0-Timeline](novapolis-rp/database-rp/00-admin/Canvas-T+0-Timeline.md#L43)
- [Fraktionen-Taxonomie](novapolis-rp/database-rp/00-admin/Fraktionen-Taxonomie.md#L50)
- [AI-Behavior-Mapping](novapolis-rp/database-rp/00-admin/AI-Behavior-Mapping.md#L83)

### Kategorie B (06-scenes -> ../01-factions/)

Total: 61

Dateien + Count

- [novapolis-rp/database-rp/06-scenes/scene-2025-10-27-f.md](novapolis-rp/database-rp/06-scenes/scene-2025-10-27-f.md) — 6
- [novapolis-rp/database-rp/06-scenes/scene-2025-10-27-k.md](novapolis-rp/database-rp/06-scenes/scene-2025-10-27-k.md) — 4
- [novapolis-rp/database-rp/06-scenes/scene-2025-10-27-m.md](novapolis-rp/database-rp/06-scenes/scene-2025-10-27-m.md) — 3
- [novapolis-rp/database-rp/06-scenes/scene-2025-10-27-p.md](novapolis-rp/database-rp/06-scenes/scene-2025-10-27-p.md) — 3
- [novapolis-rp/database-rp/06-scenes/scene-2025-10-27-s.md](novapolis-rp/database-rp/06-scenes/scene-2025-10-27-s.md) — 3
- [novapolis-rp/database-rp/06-scenes/scene-2026-01-14-a.md](novapolis-rp/database-rp/06-scenes/scene-2026-01-14-a.md) — 3
- [novapolis-rp/database-rp/06-scenes/scene-2026-01-15-a.md](novapolis-rp/database-rp/06-scenes/scene-2026-01-15-a.md) — 3
- [novapolis-rp/database-rp/06-scenes/scene-2026-01-16-a.md](novapolis-rp/database-rp/06-scenes/scene-2026-01-16-a.md) — 3
- [novapolis-rp/database-rp/06-scenes/scene-2025-10-27-r.md](novapolis-rp/database-rp/06-scenes/scene-2025-10-27-r.md) — 1
- [novapolis-rp/database-rp/06-scenes/scene-2025-10-27-j.md](novapolis-rp/database-rp/06-scenes/scene-2025-10-27-j.md) — 6
- [novapolis-rp/database-rp/06-scenes/scene-2025-10-27-l.md](novapolis-rp/database-rp/06-scenes/scene-2025-10-27-l.md) — 4
- [novapolis-rp/database-rp/06-scenes/scene-2025-10-27-i.md](novapolis-rp/database-rp/06-scenes/scene-2025-10-27-i.md) — 1
- [novapolis-rp/database-rp/06-scenes/scene-2025-10-27-h.md](novapolis-rp/database-rp/06-scenes/scene-2025-10-27-h.md) — 1
- [novapolis-rp/database-rp/06-scenes/scene-2025-10-27-g.md](novapolis-rp/database-rp/06-scenes/scene-2025-10-27-g.md) — 2
- [novapolis-rp/database-rp/06-scenes/scene-2025-10-27-e.md](novapolis-rp/database-rp/06-scenes/scene-2025-10-27-e.md) — 3
- [novapolis-rp/database-rp/06-scenes/scene-2025-10-27-d.md](novapolis-rp/database-rp/06-scenes/scene-2025-10-27-d.md) — 3
- [novapolis-rp/database-rp/06-scenes/scene-2025-10-27-c.md](novapolis-rp/database-rp/06-scenes/scene-2025-10-27-c.md) — 7
- [novapolis-rp/database-rp/06-scenes/scene-2025-10-27-b.md](novapolis-rp/database-rp/06-scenes/scene-2025-10-27-b.md) — 2
- [novapolis-rp/database-rp/06-scenes/scene-2025-10-27-a.md](novapolis-rp/database-rp/06-scenes/scene-2025-10-27-a.md) — 3

Exzerpte (3)

- [scene-2025-10-27-f](novapolis-rp/database-rp/06-scenes/scene-2025-10-27-f.md#L33)
- [scene-2025-10-27-c](novapolis-rp/database-rp/06-scenes/scene-2025-10-27-c.md#L31)
- [scene-2026-01-15-a](novapolis-rp/database-rp/06-scenes/scene-2026-01-15-a.md#L41)

### Kategorie C (01-factions + 04-inventory -> ../00-admin/)

Total: 142

Dateien + Count

- [novapolis-rp/database-rp/01-factions/novapolis/README.md](novapolis-rp/database-rp/01-factions/novapolis/README.md) — 2
- [novapolis-rp/database-rp/01-factions/schienenbund/README.md](novapolis-rp/database-rp/01-factions/schienenbund/README.md) — 2
- [novapolis-rp/database-rp/01-factions/novapolis/05-projects/README.md](novapolis-rp/database-rp/01-factions/novapolis/05-projects/README.md) — 1
- [novapolis-rp/database-rp/01-factions/novapolis/05-projects/Nordlinie-01.md](novapolis-rp/database-rp/01-factions/novapolis/05-projects/Nordlinie-01.md) — 3
- [novapolis-rp/database-rp/01-factions/novapolis/04-inventory/Novapolis-inventar.md](novapolis-rp/database-rp/01-factions/novapolis/04-inventory/Novapolis-inventar.md) — 3
- [novapolis-rp/database-rp/01-factions/novapolis/04-inventory/README.md](novapolis-rp/database-rp/01-factions/novapolis/04-inventory/README.md) — 1
- [novapolis-rp/database-rp/01-factions/novapolis/05-projects/Draisine-Transportmodul.md](novapolis-rp/database-rp/01-factions/novapolis/05-projects/Draisine-Transportmodul.md) — 2
- [novapolis-rp/database-rp/01-factions/schienenbund/05-projects/README.md](novapolis-rp/database-rp/01-factions/schienenbund/05-projects/README.md) — 1
- [novapolis-rp/database-rp/01-factions/schienenbund/04-inventory/Schienenbund-inventar.md](novapolis-rp/database-rp/01-factions/schienenbund/04-inventory/Schienenbund-inventar.md) — 3
- [novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md) — 1
- [novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5-Logistik-Policy.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5-Logistik-Policy.md) — 2
- [novapolis-rp/database-rp/01-factions/novapolis/03-locations/E3-Wasseraufbereitung.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/E3-Wasseraufbereitung.md) — 1
- [novapolis-rp/database-rp/01-factions/novapolis/03-locations/README.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/README.md) — 1
- [novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5-Funkraum.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5-Funkraum.md) — 1
- [novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6-Logistik-Policy.md](novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6-Logistik-Policy.md) — 2
- [novapolis-rp/database-rp/01-factions/schienenbund/04-inventory/README.md](novapolis-rp/database-rp/01-factions/schienenbund/04-inventory/README.md) — 1
- [novapolis-rp/database-rp/01-factions/schienenbund/03-locations/README.md](novapolis-rp/database-rp/01-factions/schienenbund/03-locations/README.md) — 1
- [novapolis-rp/database-rp/01-factions/novapolis/02-characters/Echo.md](novapolis-rp/database-rp/01-factions/novapolis/02-characters/Echo.md) — 5
- [novapolis-rp/database-rp/01-factions/novapolis/02-characters/Jonas-Merek.md](novapolis-rp/database-rp/01-factions/novapolis/02-characters/Jonas-Merek.md) — 3
- [novapolis-rp/database-rp/01-factions/novapolis/02-characters/Lumen.md](novapolis-rp/database-rp/01-factions/novapolis/02-characters/Lumen.md) — 5
- [novapolis-rp/database-rp/01-factions/novapolis/02-characters/Lyra-Hest.md](novapolis-rp/database-rp/01-factions/novapolis/02-characters/Lyra-Hest.md) — 2
- [novapolis-rp/database-rp/01-factions/novapolis/02-characters/Marei.md](novapolis-rp/database-rp/01-factions/novapolis/02-characters/Marei.md) — 2
- [novapolis-rp/database-rp/01-factions/novapolis/02-characters/Miro-Kell.md](novapolis-rp/database-rp/01-factions/novapolis/02-characters/Miro-Kell.md) — 1
- [novapolis-rp/database-rp/01-factions/novapolis/02-characters/README.md](novapolis-rp/database-rp/01-factions/novapolis/02-characters/README.md) — 1
- [novapolis-rp/database-rp/01-factions/novapolis/02-characters/Reflex.md](novapolis-rp/database-rp/01-factions/novapolis/02-characters/Reflex.md) — 7
- [novapolis-rp/database-rp/01-factions/novapolis/02-characters/Ronja-Kerschner.md](novapolis-rp/database-rp/01-factions/novapolis/02-characters/Ronja-Kerschner.md) — 6
- [novapolis-rp/database-rp/01-factions/novapolis/02-characters/person_index_np.md](novapolis-rp/database-rp/01-factions/novapolis/02-characters/person_index_np.md) — 1
- [novapolis-rp/database-rp/01-factions/novapolis/02-characters/C6-Bewohner.md](novapolis-rp/database-rp/01-factions/novapolis/02-characters/C6-Bewohner.md) — 1
- [novapolis-rp/database-rp/01-factions/schienenbund/02-characters/README.md](novapolis-rp/database-rp/01-factions/schienenbund/02-characters/README.md) — 1
- [novapolis-rp/database-rp/01-factions/schienenbund/00-doctrine/schienenbund-logistics.md](novapolis-rp/database-rp/01-factions/schienenbund/00-doctrine/schienenbund-logistics.md) — 1
- [novapolis-rp/database-rp/01-factions/schienenbund/00-doctrine/schienenbund-history.md](novapolis-rp/database-rp/01-factions/schienenbund/00-doctrine/schienenbund-history.md) — 1
- [novapolis-rp/database-rp/01-factions/novapolis/00-doctrine/novapolis-logistics.md](novapolis-rp/database-rp/01-factions/novapolis/00-doctrine/novapolis-logistics.md) — 1
- [novapolis-rp/database-rp/01-factions/novapolis/00-doctrine/novapolis-history.md](novapolis-rp/database-rp/01-factions/novapolis/00-doctrine/novapolis-history.md) — 2
- [novapolis-rp/database-rp/01-factions/novapolis/00-doctrine/novapolis-diplomacy.md](novapolis-rp/database-rp/01-factions/novapolis/00-doctrine/novapolis-diplomacy.md) — 2
- [novapolis-rp/database-rp/01-factions/haendlerbund/README.md](novapolis-rp/database-rp/01-factions/haendlerbund/README.md) — 2
- [novapolis-rp/database-rp/01-factions/schattenbund/README.md](novapolis-rp/database-rp/01-factions/schattenbund/README.md) — 2
- [novapolis-rp/database-rp/01-factions/haendlerbund/05-projects/README.md](novapolis-rp/database-rp/01-factions/haendlerbund/05-projects/README.md) — 1
- [novapolis-rp/database-rp/01-factions/haendlerbund/05-projects/caravan_moves.md](novapolis-rp/database-rp/01-factions/haendlerbund/05-projects/caravan_moves.md) — 2
- [novapolis-rp/database-rp/01-factions/haendlerbund/04-inventory/README.md](novapolis-rp/database-rp/01-factions/haendlerbund/04-inventory/README.md) — 1
- [novapolis-rp/database-rp/01-factions/haendlerbund/04-inventory/Haendlerbund-inventar.md](novapolis-rp/database-rp/01-factions/haendlerbund/04-inventory/Haendlerbund-inventar.md) — 3
- [novapolis-rp/database-rp/01-factions/haendlerbund/03-locations/README.md](novapolis-rp/database-rp/01-factions/haendlerbund/03-locations/README.md) — 1
- [novapolis-rp/database-rp/01-factions/schattenbund/05-projects/README.md](novapolis-rp/database-rp/01-factions/schattenbund/05-projects/README.md) — 1
- [novapolis-rp/database-rp/01-factions/haendlerbund/03-locations/G7.md](novapolis-rp/database-rp/01-factions/haendlerbund/03-locations/G7.md) — 3
- [novapolis-rp/database-rp/01-factions/haendlerbund/02-characters/Kora-Malenkov.md](novapolis-rp/database-rp/01-factions/haendlerbund/02-characters/Kora-Malenkov.md) — 3
- [novapolis-rp/database-rp/01-factions/haendlerbund/02-characters/README.md](novapolis-rp/database-rp/01-factions/haendlerbund/02-characters/README.md) — 1
- [novapolis-rp/database-rp/01-factions/haendlerbund/02-characters/Senn-Daru.md](novapolis-rp/database-rp/01-factions/haendlerbund/02-characters/Senn-Daru.md) — 3
- [novapolis-rp/database-rp/01-factions/schattenbund/04-inventory/Schattenbund-inventar.md](novapolis-rp/database-rp/01-factions/schattenbund/04-inventory/Schattenbund-inventar.md) — 3
- [novapolis-rp/database-rp/01-factions/schattenbund/04-inventory/README.md](novapolis-rp/database-rp/01-factions/schattenbund/04-inventory/README.md) — 1
- [novapolis-rp/database-rp/01-factions/schattenbund/03-locations/README.md](novapolis-rp/database-rp/01-factions/schattenbund/03-locations/README.md) — 1
- [novapolis-rp/database-rp/01-factions/haendlerbund/00-doctrine/haendlerbund-logistics.md](novapolis-rp/database-rp/01-factions/haendlerbund/00-doctrine/haendlerbund-logistics.md) — 1
- [novapolis-rp/database-rp/01-factions/haendlerbund/00-doctrine/haendlerbund-history.md](novapolis-rp/database-rp/01-factions/haendlerbund/00-doctrine/haendlerbund-history.md) — 1
- [novapolis-rp/database-rp/01-factions/schattenbund/02-characters/README.md](novapolis-rp/database-rp/01-factions/schattenbund/02-characters/README.md) — 1
- [novapolis-rp/database-rp/01-factions/schattenbund/00-doctrine/schattenbund-history.md](novapolis-rp/database-rp/01-factions/schattenbund/00-doctrine/schattenbund-history.md) — 1
- [novapolis-rp/database-rp/01-factions/schattenbund/00-doctrine/schattenbund-logistics.md](novapolis-rp/database-rp/01-factions/schattenbund/00-doctrine/schattenbund-logistics.md) — 1
- [novapolis-rp/database-rp/01-factions/eisenkonklave/README.md](novapolis-rp/database-rp/01-factions/eisenkonklave/README.md) — 2
- [novapolis-rp/database-rp/01-factions/arkologie-a1/README.md](novapolis-rp/database-rp/01-factions/arkologie-a1/README.md) — 2
- [novapolis-rp/database-rp/01-factions/arkologie-a1/05-projects/README.md](novapolis-rp/database-rp/01-factions/arkologie-a1/05-projects/README.md) — 1
- [novapolis-rp/database-rp/01-factions/fluesterkollektiv/README.md](novapolis-rp/database-rp/01-factions/fluesterkollektiv/README.md) — 2
- [novapolis-rp/database-rp/01-factions/arkologie-a1/04-inventory/Arkologie-inventar.md](novapolis-rp/database-rp/01-factions/arkologie-a1/04-inventory/Arkologie-inventar.md) — 3
- [novapolis-rp/database-rp/01-factions/arkologie-a1/04-inventory/README.md](novapolis-rp/database-rp/01-factions/arkologie-a1/04-inventory/README.md) — 1
- [novapolis-rp/database-rp/01-factions/arkologie-a1/03-locations/README.md](novapolis-rp/database-rp/01-factions/arkologie-a1/03-locations/README.md) — 1
- [novapolis-rp/database-rp/01-factions/eisenkonklave/05-projects/README.md](novapolis-rp/database-rp/01-factions/eisenkonklave/05-projects/README.md) — 1
- [novapolis-rp/database-rp/01-factions/arkologie-a1/02-characters/README.md](novapolis-rp/database-rp/01-factions/arkologie-a1/02-characters/README.md) — 1
- [novapolis-rp/database-rp/01-factions/fluesterkollektiv/05-projects/README.md](novapolis-rp/database-rp/01-factions/fluesterkollektiv/05-projects/README.md) — 1
- [novapolis-rp/database-rp/01-factions/fluesterkollektiv/04-inventory/README.md](novapolis-rp/database-rp/01-factions/fluesterkollektiv/04-inventory/README.md) — 1
- [novapolis-rp/database-rp/01-factions/eisenkonklave/04-inventory/README.md](novapolis-rp/database-rp/01-factions/eisenkonklave/04-inventory/README.md) — 1
- [novapolis-rp/database-rp/01-factions/arkologie-a1/00-doctrine/arkologie-a1-logistics.md](novapolis-rp/database-rp/01-factions/arkologie-a1/00-doctrine/arkologie-a1-logistics.md) — 1
- [novapolis-rp/database-rp/01-factions/fluesterkollektiv/04-inventory/Fluesterkollektiv-inventar.md](novapolis-rp/database-rp/01-factions/fluesterkollektiv/04-inventory/Fluesterkollektiv-inventar.md) — 3
- [novapolis-rp/database-rp/01-factions/arkologie-a1/00-doctrine/arkologie-a1-history.md](novapolis-rp/database-rp/01-factions/arkologie-a1/00-doctrine/arkologie-a1-history.md) — 1
- [novapolis-rp/database-rp/01-factions/eisenkonklave/04-inventory/Eiserne-Enklave-inventar.md](novapolis-rp/database-rp/01-factions/eisenkonklave/04-inventory/Eiserne-Enklave-inventar.md) — 3
- [novapolis-rp/database-rp/01-factions/fluesterkollektiv/03-locations/README.md](novapolis-rp/database-rp/01-factions/fluesterkollektiv/03-locations/README.md) — 1
- [novapolis-rp/database-rp/01-factions/eisenkonklave/03-locations/README.md](novapolis-rp/database-rp/01-factions/eisenkonklave/03-locations/README.md) — 1
- [novapolis-rp/database-rp/01-factions/eisenkonklave/02-characters/README.md](novapolis-rp/database-rp/01-factions/eisenkonklave/02-characters/README.md) — 1
- [novapolis-rp/database-rp/01-factions/fluesterkollektiv/02-characters/README.md](novapolis-rp/database-rp/01-factions/fluesterkollektiv/02-characters/README.md) — 1
- [novapolis-rp/database-rp/01-factions/eisenkonklave/00-doctrine/eisenkonklave-history.md](novapolis-rp/database-rp/01-factions/eisenkonklave/00-doctrine/eisenkonklave-history.md) — 1
- [novapolis-rp/database-rp/01-factions/fluesterkollektiv/00-doctrine/fluesterkollektiv-logistics.md](novapolis-rp/database-rp/01-factions/fluesterkollektiv/00-doctrine/fluesterkollektiv-logistics.md) — 1
- [novapolis-rp/database-rp/01-factions/fluesterkollektiv/00-doctrine/fluesterkollektiv-history.md](novapolis-rp/database-rp/01-factions/fluesterkollektiv/00-doctrine/fluesterkollektiv-history.md) — 1
- [novapolis-rp/database-rp/01-factions/eisenkonklave/00-doctrine/eisenkonklave-logistics.md](novapolis-rp/database-rp/01-factions/eisenkonklave/00-doctrine/eisenkonklave-logistics.md) — 1
- [novapolis-rp/database-rp/04-inventory/Marktpreise-inventar.md](novapolis-rp/database-rp/04-inventory/Marktpreise-inventar.md) — 3
- [novapolis-rp/database-rp/04-inventory/Freie-Gruppen-inventar.md](novapolis-rp/database-rp/04-inventory/Freie-Gruppen-inventar.md) — 3

Exzerpte (3)

- [novapolis-rp/database-rp/01-factions/novapolis/README.md](novapolis-rp/database-rp/01-factions/novapolis/README.md#L30)
- [novapolis-rp/database-rp/01-factions/novapolis/05-projects/Nordlinie-01.md](novapolis-rp/database-rp/01-factions/novapolis/05-projects/Nordlinie-01.md#L101)
- [novapolis-rp/database-rp/04-inventory/Marktpreise-inventar.md](novapolis-rp/database-rp/04-inventory/Marktpreise-inventar.md#L52)

Auffaelligkeiten (Audit-Flags)
-------------------------------

- Naming (Dry-Run, kein Apply):
  - [novapolis-rp/database-rp/00-admin/Canvas-T+0-Timeline.json](novapolis-rp/database-rp/00-admin/Canvas-T+0-Timeline.json)
  - [novapolis-rp/database-rp/00-admin/Canvas-T+0-Timeline.md](novapolis-rp/database-rp/00-admin/Canvas-T+0-Timeline.md)
  - [novapolis-rp/database-rp/01-factions/haendlerbund/05-projects/caravan_moves.json](novapolis-rp/database-rp/01-factions/haendlerbund/05-projects/caravan_moves.json)
  - [novapolis-rp/database-rp/01-factions/haendlerbund/05-projects/caravan_moves.md](novapolis-rp/database-rp/01-factions/haendlerbund/05-projects/caravan_moves.md)
  - [novapolis-rp/database-rp/01-factions/novapolis/02-characters/person_index_np.json](novapolis-rp/database-rp/01-factions/novapolis/02-characters/person_index_np.json)
  - [novapolis-rp/database-rp/01-factions/novapolis/02-characters/person_index_np.md](novapolis-rp/database-rp/01-factions/novapolis/02-characters/person_index_np.md)
- Validator-H1-Fehler: [novapolis-rp/database-rp/00-admin/Fraktionen-Taxonomie.md](novapolis-rp/database-rp/00-admin/Fraktionen-Taxonomie.md)
- Legacy-Name (Audit-Flag, keine Migration in Batch A): [novapolis-rp/database-rp/01-factions/haendlerbund/06-handel-diplomatie/README.md](novapolis-rp/database-rp/01-factions/haendlerbund/06-handel-diplomatie/README.md#L17)
- Doppelte Metadatenzeile: [novapolis-rp/database-rp/04-inventory/Freie-Gruppen-inventar.md](novapolis-rp/database-rp/04-inventory/Freie-Gruppen-inventar.md#L13-L20)
- Scene-Frontmatter: harte Norm im Audit (keine Edits in Batch A).

Batch-Plan (A-D)
----------------

- Batch A: Mechanik und Gates (Naming/Links/Validatoren, nur Dry-Run).
- Batch B: 00-admin + 00-ops (Entry-Points/Index/Links).
- Batch C: 01-factions fraktionsweise (Scaffold/Links/Dateinamen zuerst, Inhalte danach).
- Batch D: 06-scenes + 04-inventory quer (Crossrefs, Frontmatter, Linkbarkeit).

STOP-Gate (Normen)
------------------

1) Link-Audit: vollstaendige Dateiliste je Kategorie + Count pro Datei; genau 3 Exzerpte mit Zeilenangaben.
2) Legacy-Begriffe (z. B. Haendlergilde) nur als Audit-Flag in Batch A.
3) Naming-Apply in Batch A verboten (nur Dry-Run).
4) Scene-Frontmatter-Pflichten als harte Norm im Audit, keine Scene-Edits in Batch A.
5) Begriffe SSOT/Kanon/Ops nur mit Pfad + Kurztext (siehe Belege oben).
