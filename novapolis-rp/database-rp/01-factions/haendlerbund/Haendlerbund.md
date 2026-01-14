---
stand: 2026-01-14 17:50
update: "Karawane H-47: Anschluss an Novapolis (C6) reflektiert; Händlerbund-Überblick präzisiert.; Checks PASS."
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc **/*.md PASS (2026-01-14 17:50); & .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py novapolis-rp\\database-rp PASS (2026-01-14 17:50); & .\\.venv\\Scripts\\python.exe scripts\\checks_rp_consistency.py --strict PASS (2026-01-14 17:50); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:rp PASS (2026-01-14 17:50); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:crossrefs PASS (2026-01-14 17:50)
slug: haendlerbund
category: faction
status: draft
version: "0.1"
tags: [fraktion]
---

Händlerbund (Fraktion)
======================

Überblick
---------
- Status: aktiv (mobil; Knoten/Anlaufpunkt in [G7](./03-locations/G7.md))
- Hinweis: ehem. Karawane H-47 (6) hat sich Novapolis angeschlossen (Basis C6); Charakter-SSOTs liegen pfadbedingt weiterhin unter ./02-characters/
- Rolle im Setting: mobile Handelsfraktion mit Knoten/Anlaufpunkt in [G7](./03-locations/G7.md) (Details über Logs/Bewegungen)

Assets in diesem Ordner
-----------------------
- Charaktere → ./02-characters/
- Orte → ./03-locations/
- Inventar → ./04-inventory/Haendlerbund-inventar.md
- Projekte → ./05-projects/caravan_moves.md

Offene Punkte
-------------
- [ ] Führungs-/Kontaktpunkte konkretisieren (SSOT-only)
- [ ] Handelsfenster/Protokolle verlinken (Handel/Diplomatie-Admin)
