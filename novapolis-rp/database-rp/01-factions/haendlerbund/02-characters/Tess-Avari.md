---
stand: 2026-01-14 17:50
update: "Zugehörigkeit/Position aktualisiert: Anschluss an Novapolis; Basis C6.; Checks PASS."
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc **/*.md PASS (2026-01-14 17:50); & .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py novapolis-rp\\database-rp PASS (2026-01-14 17:50); & .\\.venv\\Scripts\\python.exe scripts\\checks_rp_consistency.py --strict PASS (2026-01-14 17:50); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:rp PASS (2026-01-14 17:50); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:crossrefs PASS (2026-01-14 17:50)

title: Tess Avari
category: character
slug: tess-avari
version: "0.1"
last_updated: 2026-01-14T17:31:10+01:00
tags: ["npc", "karawane", "novapolis", "vermittler"]
affiliations: ["novapolis"]
dependencies: ["c6"]
primary_location: c6
last_seen: c6
---
<!-- markdownlint-disable MD025 -->

Tess Avari
==========

- Rolle: Vermittlerin (Deals, Lieferfenster, Konfliktentschärfung)
- Status: aktiv
- Kurzprofil: freundlich, präzise, merkt sich Schulden; handelt über Regeln statt Drohung

Rollen & Verantwortlichkeiten (Pflichtfelder)
--------------------------------------------

- Moderiert Übergaben: Zeitpunkt, Ort, Umfang, Rückfragen (Meta-Log)
- Eskaliert nur, wenn „Wortbruch“ dokumentiert ist

Zugehörigkeit & Standort
------------------------

- Zugehörigkeit: Novapolis (C6; ehem. Karawane H-47)
- Standort: primär C6; Kontaktpunkte außerhalb nur über Protokoll/Funk

Hooks
-----

- Bietet „saubere“ Lieferkette an – verlangt dafür strenge Log-Disziplin
- Kennt eine Abkürzung im Handelsnetz, nennt sie aber nur gegen Gegenleistung

Verlinkungen
------------

- Handelslog Händlerbund → ../06-handel-diplomatie/Handelslog-Haendlerbund.md
- Relationslog Händlerbund → ../06-handel-diplomatie/Relationslog-Haendlerbund.md
