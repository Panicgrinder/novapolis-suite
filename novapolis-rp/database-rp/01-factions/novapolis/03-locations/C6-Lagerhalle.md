---
stand: 2026-01-14 12:32
update: "Neu: POI (Lagerhalle) ergänzt. Receipts aktualisiert (Gates PASS)."
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/**/*.md' PASS (2026-01-14 12:32); & .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py novapolis-rp\\database-rp PASS (2026-01-14 12:32); & .\\.venv\\Scripts\\python.exe scripts\\checks_rp_consistency.py --strict PASS (2026-01-14 12:32); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:rp PASS (2026-01-14 12:32); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:crossrefs PASS (2026-01-14 12:32)

title: C6 Lagerhalle
last_updated: 2026-01-14T10:15:02+01:00
category: location
slug: c6-lagerhalle
version: "0.1"
affiliations: [novapolis]
status: aktiv
connections: ["c6"]
tags: ["poi", "c6", "lager"]
---

C6 - Lagerhalle
---------------

Status
------
- Aktiv; zentrale Ablage für Material, Filter, Energiezellen, Werkzeuge

Funktion
--------
- Annahme/Abgabe nur über Logistik-Policy; Trennung in „kritisch“ vs. „frei“

Zugang
------
- Ausgabe gegen Freigabe + Eintrag im Inventar-Log

Risiken
-------
- Vermischung von Chargen → Verlust der Nachvollziehbarkeit
- „Nebenlager“ entstehen spontan → Audit nötig

Hooks
-----
- Fehlbestand bei kritischem Gut → Transfer-Stopp bis Klärung
- Unmarkierte Kiste aus Tunnel → Quarantäne-Prozess

Verlinkungen
------------
- C6 → ./C6.md
- Logistik-Policy C6 → ./C6-Logistik-Policy.md
- Inventar C6 → ../04-inventory/C6-inventar.md
