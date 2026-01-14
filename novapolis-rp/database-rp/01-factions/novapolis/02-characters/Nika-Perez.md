---
stand: 2026-01-14 12:32
update: "Neu: NPC ergänzt (Quartermaster/Werkstatt-Interface). Receipts aktualisiert (Gates PASS)."
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/**/*.md' PASS (2026-01-14 12:32); & .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py novapolis-rp\\database-rp PASS (2026-01-14 12:32); & .\\.venv\\Scripts\\python.exe scripts\\checks_rp_consistency.py --strict PASS (2026-01-14 12:32); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:rp PASS (2026-01-14 12:32); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:crossrefs PASS (2026-01-14 12:32)

title: Nika Perez
category: character
slug: nika-perez
version: "0.1"
last_updated: 2026-01-14T10:16:22+01:00
tags: ["npc", "logistik", "werkstatt"]
affiliations: ["novapolis"]
dependencies: ["d5", "d5-werkstatt"]
primary_location: d5
last_seen: d5
---
<!-- markdownlint-disable MD025 -->

Nika Perez
==========

- Rolle: Quartermaster D5 (Ausgabe/Verbrauch), Schnittstelle zur Werkstatt
- Status: aktiv
- Kurzprofil: pragmatisch, prozessgetrieben, misstraut „Nebenwegen“ ohne Log

Rollen & Verantwortlichkeiten (Pflichtfelder)
--------------------------------------------

- Bestandsführung D5: Ein-/Ausgänge konsistent im Inventar-Log
- Freigaben: „kritisch“ vs. „frei“ (in Abstimmung mit Logistik-Policy)
- Konfliktpuffer: Eskaliert erst nach zweiter Abweichung (Audit-Mechanik)

Zugehörigkeit & Standort
------------------------

- Zugehörigkeit: Novapolis
- Standort: D5

Hooks
-----

- Fehlende Verbrauchsmittel blockieren Reparatur-Backlog → Prioritätenliste erzwingen
- Unstimmige Ausgabe (Werkzeug taucht doppelt auf) → Inventar-Audit

Verlinkungen
------------

- D5 → ../03-locations/D5.md
- D5 Werkstatt → ../03-locations/D5-Werkstatt.md
- Inventar D5 → ../04-inventory/D5-inventar.md
