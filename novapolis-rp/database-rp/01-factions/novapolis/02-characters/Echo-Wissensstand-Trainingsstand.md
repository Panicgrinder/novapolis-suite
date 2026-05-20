---
stand: 2026-05-20 17:42
update: Unbelegte formale Request-/Stop-Kommandos aus dem Echo-Trainingsstand entfernt.
checks: snapshot-lock PASS (2026-05-20 17:42); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-05-20 17:42); .\.venv\Scripts\python.exe scripts\check_frontmatter.py changed-md PASS (EXITCODE=0, 2026-05-20 17:42); .\.venv\Scripts\python.exe scripts\check_todo_index_sync.py PASS (2026-05-20 17:42); npm --prefix novapolis-rp/coding/tools/validators run validate:rp PASS (2026-05-20 17:42); git diff --check PASS (CRLF warnings only, 2026-05-20 17:42).
title: Echo - Wissensstand & Trainingsstand
category: character-attachment
slug: echo-wissensstand-trainingsstand
version: "1.0"
last_updated: 2025-11-07T03:32:00+01:00
parent_character: echo
is_standalone_character: false
tags: [knowledge, training]
affiliations: [novapolis]
primary_location: d5
last_seen: d5
dependencies: [echo, d5]
---

<!-- markdownlint-disable MD025 -->

Echo - Wissensstand & Trainingsstand
====================================

Hinweis
-------
- Dieses Dokument ist ein Anhang zu **Echo** und kein eigenständiger Charakter.

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
- Abbruch-/Arbeitszeichen: formale Request-/Stop-Kommandos sind nicht belegt; Reaktion auf ausgespielte Arbeits-, Abbruch- und Distanzzeichen bleibt Trainings-/Reviewpunkt.
- Assistenz-Scopes: Näheschutz, leichte Signalisierung; Sicht/Atmung der Bezugsperson frei halten (Feinsteuerung tbd).

Notizen
-------
- Zielsetzung: Schutz nah an Kora ohne unnötige Einschränkungen; Statusmeldungen an C6-Leitung.



