---
stand: 2026-01-13 03:02
update: Wissensstand-/Trainingsstand-Datei ist kein eigener Charakter (category entfernt).
checks: npm --prefix novapolis-rp\coding\tools\validators run validate:rp PASS (2026-01-13 03:05); npm --prefix novapolis-rp\coding\tools\validators run validate:crossrefs PASS (2026-01-13 03:05); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/01-factions/novapolis/02-characters/Echo-Wissensstand-Trainingsstand.md' PASS (2026-01-13 03:05); & .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis-rp\database-rp PASS (2026-01-13 03:05); & .\.venv\Scripts\python.exe scripts\checks_rp_consistency.py --strict PASS (2026-01-13 03:05)
title: Echo - Wissensstand & Trainingsstand
slug: echo-wissensstand-trainingsstand
version: "0.1"
last_updated: 2025-11-07T03:32:00+01:00
tags: []
affiliations: [novapolis]
dependencies: []
---

<!-- markdownlint-disable MD025 -->

Echo - Wissensstand & Trainingsstand
====================================

Wissensstand (Detailmatrix)
---------------------------
- Kora - Bezugsperson (maximal)
- Reflex - Primärinstanz (sehr hoch)
- Ronja - Leitung Novapolis (hoch)
- Lumen - Schwester-Instanz (mittel/hoch)
- Einsatzkontext: C6 Station, Crew-Sicherheit/Assistenz
- Intern: Reflex/Instanzen bekannt (erfasst)
- Extern: keine Offenlegung ohne Freigabe [FR-KNOWLEDGE]

Trainingsstand
--------------
- Stabilität bei Distanz: tbd - Nähe zu Kora priorisieren; Schonmodus bei Trennung.
- Signals/Kommandos: "Request"/"Stop" zuverlässig umsetzen (Training laufend).
- Assistenz-Scopes: Näheschutz, leichte Signalisierung; Sicht/Atmung der Bezugsperson frei halten (Feinsteuerung tbd).

Notizen
-------
- Zielsetzung: Schutz nah an Kora ohne unnötige Einschränkungen; Statusmeldungen an C6-Leitung.



