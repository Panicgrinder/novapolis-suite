---
stand: 2026-01-14 12:32
update: "Neu: POI (Wasseraufbereitung) ergänzt. Receipts aktualisiert (Gates PASS)."
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/**/*.md' PASS (2026-01-14 12:32); & .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py novapolis-rp\\database-rp PASS (2026-01-14 12:32); & .\\.venv\\Scripts\\python.exe scripts\\checks_rp_consistency.py --strict PASS (2026-01-14 12:32); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:rp PASS (2026-01-14 12:32); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:crossrefs PASS (2026-01-14 12:32)

title: E3 Wasseraufbereitung
last_updated: 2026-01-14T10:15:02+01:00
category: location
slug: e3-wasseraufbereitung
version: "0.1"
affiliations: [novapolis]
status: unbekannt
connections: ["e3"]
tags: ["poi", "e3", "infrastruktur"]
---

E3 - Wasseraufbereitung
-----------------------

Status
------
- Unklar; Anlage vermutlich vorhanden, Zustand unbestätigt

Funktion
--------
- Wasseraufbereitung und Filterkreislauf (kritische Infrastruktur)

Zugang
------
- Zugang aktuell nicht vorgesehen; erst nach Aufhebung der E3-Verriegelung

Risiken
-------
- Fehlende Zustandsdaten → Risiko für Evakuierte/Expansion

Hooks
-----
- Filterbedarf steigt → Entscheidung: Risiko-Run oder Ausbau in C6
- Sensorik liefert widersprüchliche Werte (Wasserqualität)

Verlinkungen
------------
- E3 → ./E3.md
- Logistik → ../00-admin/Logistik.md
