---
stand: 2026-01-14 12:32
update: "Neu: POI (Schleuse) ergänzt. Receipts aktualisiert (Gates PASS)."
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/**/*.md' PASS (2026-01-14 12:32); & .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py novapolis-rp\\database-rp PASS (2026-01-14 12:32); & .\\.venv\\Scripts\\python.exe scripts\\checks_rp_consistency.py --strict PASS (2026-01-14 12:32); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:rp PASS (2026-01-14 12:32); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:crossrefs PASS (2026-01-14 12:32)

title: C6 Schleuse
last_updated: 2026-01-14T10:15:02+01:00
category: location
slug: c6-schleuse
version: "0.1"
affiliations: [novapolis]
status: teilaktiv
connections: ["c6", "verbindungstunnel-d5-c6"]
tags: ["poi", "c6", "zugang"]
---

C6 - Schleuse
-------------

Status
------
- Teilaktiv; Zugangskontrolle und Quarantäne-Übergang

Funktion
--------
- Kontrollpunkt für Ein-/Ausgang (Personen und Güter)
- Checkpoint für „unklare Funde“ aus Tunneln

Zugang
------
- Zutritt nach Protokoll: Wer/Was/Wann/Wohin (Missionslog + Inventarlog)

Risiken
-------
- Unklare Herkunft von Gütern → Kontamination/Manipulation
- „Abkürzungen“ unterlaufen Policy → Audit/Entzug von Freigaben

Hooks
-----
- Ein Paket ohne Absender taucht im Schleusenbereich auf
- Ein Transfer wird von einer Fraktion „beschleunigt“ → Konflikt mit Gate-Policy

Verlinkungen
------------
- C6 → ./C6.md
- Verbindungstunnel D5-C6 → ./Verbindungstunnel-D5-C6.md
