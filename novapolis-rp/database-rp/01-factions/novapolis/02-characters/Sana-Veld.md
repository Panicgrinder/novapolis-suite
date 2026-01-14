---
stand: 2026-01-14 12:32
update: "Neu: NPC ergänzt (Sanität/Quarantäne). Receipts aktualisiert (Gates PASS)."
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/**/*.md' PASS (2026-01-14 12:32); & .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py novapolis-rp\\database-rp PASS (2026-01-14 12:32); & .\\.venv\\Scripts\\python.exe scripts\\checks_rp_consistency.py --strict PASS (2026-01-14 12:32); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:rp PASS (2026-01-14 12:32); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:crossrefs PASS (2026-01-14 12:32)

title: Sana Veld
category: character
slug: sana-veld
version: "0.1"
last_updated: 2026-01-14T10:16:22+01:00
tags: ["npc", "med", "quarantaene"]
affiliations: ["novapolis"]
dependencies: ["c6", "c6-schleuse"]
primary_location: c6
last_seen: c6
---
<!-- markdownlint-disable MD025 -->

Sana Veld
=========

- Rolle: Sanitäterin/Protokollführung Quarantäne (C6)
- Status: aktiv
- Kurzprofil: vorsichtig, regelorientiert, aber mit klarem Blick für Pragmatik in Notlagen

Rollen & Verantwortlichkeiten (Pflichtfelder)
--------------------------------------------

- Quarantäne-Protokolle (Eintritt, Sichtung, Freigabe) führen
- Versorgungslage beobachten: Verbände, Desinfektion, Filter

Zugehörigkeit & Standort
------------------------

- Zugehörigkeit: Novapolis
- Standort: C6 (Schleuse/Übergang)

Hooks
-----

- Unmarkierte Kiste aus Tunnel → Quarantäne-Entscheidung (blocken vs. sichten)
- Widerspruch: logistischer Druck vs. medizinische Freigabe

Verlinkungen
------------

- C6 Schleuse → ../03-locations/C6-Schleuse.md
- Logistik-Policy C6 → ../00-admin/C6-Logistik-Policy.md
