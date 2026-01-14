---
stand: 2026-01-14 12:32
update: "Neu: POI (Quarantänehof) ergänzt. Receipts aktualisiert (Gates PASS)."
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/**/*.md' PASS (2026-01-14 12:32); & .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py novapolis-rp\\database-rp PASS (2026-01-14 12:32); & .\\.venv\\Scripts\\python.exe scripts\\checks_rp_consistency.py --strict PASS (2026-01-14 12:32); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:rp PASS (2026-01-14 12:32); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:crossrefs PASS (2026-01-14 12:32)

title: E3 Quarantaenehof
last_updated: 2026-01-14T10:15:02+01:00
category: location
slug: e3-quarantaenehof
version: "0.1"
affiliations: [novapolis]
status: verriegelt
connections: ["e3", "verbindungstunnel-c6-e3"]
tags: ["poi", "e3", "quarantaene"]
---

E3 - Quarantänehof
------------------

Status
------
- Verriegelt; Monitoring aktiv

Funktion
--------
- Übergangsbereich für Dekontamination, Sichtung, temporäre Separierung

Zugang
------
- Nur nach Freigabe; Standard ist „kein Zutritt“

Risiken
-------
- Unklare biologische/chemische Belastungen
- Proben/Material ohne Chain-of-Custody

Hooks
-----
- Ein Evakuierter meldet „vergessene“ Kiste im Hof
- Sensor meldet Bewegung trotz Verriegelung

Verlinkungen
------------
- E3 → ./E3.md
- Verbindungstunnel C6-E3 → ./Verbindungstunnel-C6-E3.md
