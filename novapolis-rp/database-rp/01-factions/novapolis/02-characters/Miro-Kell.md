---
stand: 2026-01-14 12:32
update: "Neu: NPC ergänzt (Funk/Signal). Receipts aktualisiert (Gates PASS)."
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/**/*.md' PASS (2026-01-14 12:32); & .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py novapolis-rp\\database-rp PASS (2026-01-14 12:32); & .\\.venv\\Scripts\\python.exe scripts\\checks_rp_consistency.py --strict PASS (2026-01-14 12:32); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:rp PASS (2026-01-14 12:32); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:crossrefs PASS (2026-01-14 12:32)

title: Miro Kell
category: character
slug: miro-kell
version: "0.1"
last_updated: 2026-01-14T10:16:22+01:00
tags: ["npc", "funk", "signal"]
affiliations: ["novapolis"]
dependencies: ["d5", "d5-funkraum"]
primary_location: d5
last_seen: d5
---
<!-- markdownlint-disable MD025 -->

Miro Kell
=========

- Rolle: Funker/Signal-Operator D5
- Status: aktiv
- Kurzprofil: ruhig, beobachtet Muster, protokolliert lieber zu viel als zu wenig

Rollen & Verantwortlichkeiten (Pflichtfelder)
--------------------------------------------

- Funkfenster planen (D5↔C6), Callsigns pflegen
- Meta-Logs führen (Zeit, Kanal, Beteiligte) + Abgleich mit Missionslog

Zugehörigkeit & Standort
------------------------

- Zugehörigkeit: Novapolis
- Standort: D5 (Funkraum)

Hooks
-----

- Unbekannter Ping mit wiederkehrender Signatur → Entscheidung: antworten, blocken, triangulieren
- Zeitstempel driftet zwischen Logs → Konsistenz-Check auslösen

Verlinkungen
------------

- D5 Funkraum → ../03-locations/D5-Funkraum.md
- Missionslog → ../00-admin/Missionslog.md
