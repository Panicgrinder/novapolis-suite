---
stand: 2026-01-11 01:50
update: "Scope präzisiert: Inventar für fraktionslose NPC; doppelte Frontmatter entfernt."
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/**/*.md' PASS (2026-01-11 01:54); & .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis-rp\database-rp PASS (2026-01-11 01:54); & .\.venv\Scripts\python.exe scripts\checks_rp_consistency.py --strict PASS (2026-01-11 01:54)
canvas: Inventar Freie Gruppen
last_updated: 2025-11-07T04:32:00+01:00
category: inventory
slug: freie-gruppen-inventar
owner: freie-gruppen
scope: global
version: "0.1"
---

Inventar - Freie Gruppen (Sammelgruppe)
=======================================

Definition
----------

- Dieses Inventar gehört ausschließlich zu **fraktionslosen NPC** (Freie Gruppen).
- Fraktionsgebundene NPC/Gruppen führen ihre Bestände in den jeweiligen Fraktionsinventaren unter `01-factions/*/04-inventory/`.

Bestände (Auszug)
-----------------
- Kugeln (neu): tbd (hochwertig; 1 neu ≈ 10 gebraucht)
- Kugeln (gebraucht): tbd (Alltag/Hauptmunition; Qualität streut)
- Vorräte: tbd
- Diverse: tbd

Bewegungen (Log)
----------------
- tbd

Links
-----
- Logistik (Admin) → ../00-admin/Logistik.md
- Missionslog → ../00-admin/Missionslog.md
- Währung "Kugeln" (Reference) → ../00-admin/Reference-Campaign-State.md

