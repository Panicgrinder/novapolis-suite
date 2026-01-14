---
stand: 2026-01-13 03:02
update: Wissensstand-/Trainingsstand-Datei ist kein eigener Charakter (category entfernt).
checks: npm --prefix novapolis-rp\coding\tools\validators run validate:rp PASS (2026-01-13 03:05); npm --prefix novapolis-rp\coding\tools\validators run validate:crossrefs PASS (2026-01-13 03:05); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/01-factions/novapolis/02-characters/Reflex-Wissensstand-Trainingsstand.md' PASS (2026-01-13 03:05); & .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis-rp\database-rp PASS (2026-01-13 03:05); & .\.venv\Scripts\python.exe scripts\checks_rp_consistency.py --strict PASS (2026-01-13 03:05)
title: Reflex - Wissensstand & Trainingsstand
slug: reflex-wissensstand-trainingsstand
version: "0.1"
last_updated: 2025-11-07T03:32:00+01:00
tags: []
affiliations: [novapolis]
dependencies: []
---

<!-- markdownlint-disable MD025 -->

Reflex - Wissensstand & Trainingsstand
======================================

Wissensstand (Detailmatrix)
---------------------------
- Ronja - Bezugsperson (maximal)
- Lumen - eigene Instanz (sehr hoch)
- Echo - eigene Instanz (sehr hoch)
- Jonas - Bezugsperson von Lumen (sehr hoch)
- Kora - Bezugsperson von Echo (sehr hoch)
- Eigenes System/Mechaniken - hoher Detailgrad (Dämpfung, Kopplung, Materialbildung)
- Intern (Novapolis): Reflex/Instanzen bekannt (reguliert)
- Extern: keine Offenlegung ohne Freigabe [FR-KNOWLEDGE]

Trainingsstand
--------------
- Dämpfung motorischer Signale: in Arbeit; Verhalten noch unsicher.
- Stop-Reaktionen: Training erforderlich; kurze Überreaktionen möglich; Zielzustand: sofortiges Lösen bei "Stop" (Status: im Aufbau).
- Sensorische Kopplung: derzeit zurückgestellt bis Freigabe (Stufe-Definition offen).
- Notfall-Umhüllung/Kokon: nur gemäß Guards in `Reflex.md` (Lebensgefahr; Ausmaß/Dauer dynamisch).

Notizen
-------
- Exoskelett-Entwicklung (perlmutt/Neopren-ähnliche Trägerarchitektur): Stabilität/Energie/Schnittstellen tbd.



