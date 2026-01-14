---
stand: 2026-01-14 12:32
update: "Neu: NPC ergänzt (Zugang/Schleuse). Receipts aktualisiert (Gates PASS)."
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/**/*.md' PASS (2026-01-14 12:32); & .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py novapolis-rp\\database-rp PASS (2026-01-14 12:32); & .\\.venv\\Scripts\\python.exe scripts\\checks_rp_consistency.py --strict PASS (2026-01-14 12:32); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:rp PASS (2026-01-14 12:32); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:crossrefs PASS (2026-01-14 12:32)

title: Jaro Quinn
category: character
slug: jaro-quinn
version: "0.1"
last_updated: 2026-01-14T10:16:22+01:00
tags: ["npc", "zugang", "checkpoint"]
affiliations: ["novapolis"]
dependencies: ["c6", "c6-schleuse", "verbindungstunnel-d5-c6"]
primary_location: c6
last_seen: c6
---
<!-- markdownlint-disable MD025 -->

Jaro Quinn
==========

- Rolle: Schleusenwart/Checkpoint (C6)
- Status: aktiv
- Kurzprofil: misstrauisch gegenüber Abkürzungen; lässt sich über klare Regeln beruhigen

Rollen & Verantwortlichkeiten (Pflichtfelder)
--------------------------------------------

- Zutritt & Transfers protokollieren (Wer/Was/Wann/Wohin)
- Eskalation bei Policy-Verstößen (Gate: Logistik-Policy)

Zugehörigkeit & Standort
------------------------

- Zugehörigkeit: Novapolis
- Standort: C6 (Schleuse)

Hooks
-----

- Ein „beschleunigter“ Transfer ohne Freigabe → Konflikt eskaliert sofort
- Spur: gleiche Handschrift auf mehreren Kisten → Verdacht auf internen Bypass

Verlinkungen
------------

- C6 Schleuse → ../03-locations/C6-Schleuse.md
- Verbindungstunnel D5-C6 → ../03-locations/Verbindungstunnel-D5-C6.md
