---
stand: 2026-05-20 17:42
update: Unbelegte formale Request-/Stop-Kommandos aus dem Lumen-Trainingsstand entfernt.
checks: snapshot-lock PASS (2026-05-20 17:42); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-05-20 17:42); .\.venv\Scripts\python.exe scripts\check_frontmatter.py changed-md PASS (EXITCODE=0, 2026-05-20 17:42); .\.venv\Scripts\python.exe scripts\check_todo_index_sync.py PASS (2026-05-20 17:42); npm --prefix novapolis-rp/coding/tools/validators run validate:rp PASS (2026-05-20 17:42); git diff --check PASS (CRLF warnings only, 2026-05-20 17:42).
title: Lumen - Wissensstand & Trainingsstand
category: character-attachment
slug: lumen-wissensstand-trainingsstand
version: "1.0"
last_updated: 2025-11-07T03:32:00+01:00
parent_character: lumen
is_standalone_character: false
tags: [knowledge, training]
affiliations: [novapolis]
primary_location: c6
last_seen: c6
dependencies: [lumen, c6]
---

<!-- markdownlint-disable MD025 -->

Lumen - Wissensstand & Trainingsstand
=====================================

Hinweis
-------
- Dieses Dokument ist ein Anhang zu **Lumen** und kein eigenständiger Charakter.

Wissensstand (Detailmatrix)
---------------------------
- Jonas - Bezugsperson (maximal)
- Reflex - Primärinstanz (sehr hoch)
- Ronja - Leitung Novapolis (hoch)
- Echo - Schwester-Instanz (mittel/hoch)
- Arbeitskontext: D5 Werkstatt, Logistik/Prototypen
- Intern: Reflex/Instanzen bekannt (begrenzter Kreis)
- Extern: keine Offenlegung ohne Freigabe [FR-KNOWLEDGE]

Trainingsstand
--------------
- Stabilität bei Distanz: tbd - Kopplungsfenster (Distanz/Zeit) ermitteln; Schonmodus bei Trennung.
- Abbruch-/Arbeitszeichen: formale Request-/Stop-Kommandos sind nicht belegt; Reaktion auf ausgespielte Arbeits-, Abbruch- und Distanzzeichen bleibt Trainings-/Reviewpunkt.
- Assistenz-Scopes: Kurzdiagnose/Werkzeugscan/leichte Schutzschicht (Feinsteuerung tbd).

Notizen
-------
- Zielsetzung: Werkstatt-Assistenz ohne Overreach; Logbucheinträge bei Eingriffen.



