---
stand: 2026-01-14 12:32
update: "Fix: Standort von D5/C6 auf F9 verschoben (D5/C6-Guard). Receipts aktualisiert (Gates PASS)."
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/**/*.md' PASS (2026-01-14 12:32); & .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py novapolis-rp\\database-rp PASS (2026-01-14 12:32); & .\\.venv\\Scripts\\python.exe scripts\\checks_rp_consistency.py --strict PASS (2026-01-14 12:32); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:rp PASS (2026-01-14 12:32); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:crossrefs PASS (2026-01-14 12:32)

title: Oren Silt
category: character
slug: oren-silt
version: "0.1"
last_updated: 2026-01-14T10:16:22+01:00
tags: ["npc", "schattenbund", "bote"]
affiliations: ["schattenbund"]
dependencies: ["f9"]
primary_location: f9
last_seen: f9
---
<!-- markdownlint-disable MD025 -->

Oren Silt
=========

- Rolle: Bote/Runner (Schattenbund)
- Status: aktiv
- Kurzprofil: sparsam mit Worten; liefert Fakten nur als „Belege“ (Karte, Token, Kennwort)

Rollen & Verantwortlichkeiten (Pflichtfelder)
--------------------------------------------

- Übergaben: klein, häufig, schwer nachverfolgbar
- Prüft Gegenüber über kurze Challenge-Response (Token/Passphrase)

Zugehörigkeit & Standort
------------------------

- Zugehörigkeit: Schattenbund
- Standort: primär F9; Kontaktpunkte D5/C6 nur indirekt/kurz (keine dauerhafte Präsenz)

Hooks
-----

- Bietet eine „diskrete“ Option für Engpassgüter – verlangt absolute Geheimhaltung
- Droht nicht offen, aber macht Konsequenzen spürbar (Entzug von Informationen)

Verlinkungen
------------

- Relationslog Schattenbund → ../06-handel-diplomatie/Relationslog-Schattenbund.md
- Handelslog Schattenbund → ../06-handel-diplomatie/Handelslog-Schattenbund.md
