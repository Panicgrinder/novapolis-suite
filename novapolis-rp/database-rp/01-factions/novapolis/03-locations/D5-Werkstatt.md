---
stand: 2026-01-14 12:32
update: "Neu: POI (Werkstatt) ergänzt. Receipts aktualisiert (Gates PASS)."
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/**/*.md' PASS (2026-01-14 12:32); & .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py novapolis-rp\\database-rp PASS (2026-01-14 12:32); & .\\.venv\\Scripts\\python.exe scripts\\checks_rp_consistency.py --strict PASS (2026-01-14 12:32); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:rp PASS (2026-01-14 12:32); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:crossrefs PASS (2026-01-14 12:32)

title: D5 Werkstatt
last_updated: 2026-01-14T10:15:02+01:00
category: location
slug: d5-werkstatt
version: "0.1"
affiliations: [novapolis]
status: aktiv
connections: ["d5"]
tags: ["poi", "d5", "werkstatt"]
---

D5 - Werkstatt
--------------

Status
------
- Aktiv; Kernbereich für Reparaturen und Improvisation

Funktion
--------
- Primär: Instandsetzung, Umbau, Kleinserien-Fertigung (Adapter/Fittings, Halterungen, Gehäuse)
- Sekundär: Materialausgabe (Werkzeug, Verbrauchsmittel) über Freigabe

Zugang
------
- Zugang über D5-Innenkorridor; Ausgabe nur mit Log-Eintrag (Inventar-SSOT)

Risiken
-------
- Engpass: Verbrauchsmaterial (Schleifscheiben, Schweißdraht, Filter)
- Sicherheitsrisiko: Funkenflug/Brandlast → klare Zonenmarkierung

Hooks
-----
- Fehlteil-Liste blockiert Reparatur an der Nordlinie (Adapter DN60/Passstücke)
- „Gefundenes“ Werkzeug taucht ohne Log auf → Audit/Spurensuche

Verlinkungen
------------
- D5 → ./D5.md
- Inventar D5 → ../04-inventory/D5-inventar.md
