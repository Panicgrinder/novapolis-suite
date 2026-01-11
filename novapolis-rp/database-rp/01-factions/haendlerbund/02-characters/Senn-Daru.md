---
stand: 2026-01-11 05:27
update: "Profil/Struktur überarbeitet (ohne Ronja-Layout); TBDs entfernt; SSOT-Referenzen ergänzt."
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/**/*.md' PASS (2026-01-11 05:26); & .\.venv\Scripts\python.exe scripts\check_frontmatter.py --touch novapolis-rp\database-rp\02-characters\Senn-Daru.md novapolis-rp\database-rp\00-admin\Relationslog-Novapolis.md PASS (2026-01-11 05:27); & .\.venv\Scripts\python.exe scripts\checks_rp_consistency.py --strict PASS (2026-01-11 05:27)
title: Senn Daru
category: character
slug: senn-daru
version: "1.0"
last_updated: 2025-11-07T03:32:00+01:00
tags: []
affiliations: ["haendlerbund"]
dependencies: ["c6"]
primary_location: c6
last_seen: c6
---

Senn Daru
---------

Kurzprofil
----------
- Rolle/Funktion: Händler/Vermittler (extern), Kontaktpunkt Händlerbund ↔ Novapolis (C6).
- Auftreten: verhandelt empathisch, bleibt neugierig-offen, priorisiert Ausgleich vor Eigeninteresse.
- Verhaltenssignatur: `SND1=E72-N64-L58-O46-S42-T38-C30-M22-P44-s`.

Rollen & Verantwortlichkeiten (Pflichtfelder)
---------------------------------------------
- Handel/Diplomatie: Schnittstelle Händlerbund ↔ Novapolis (C6), Erstkontakte/Protokolle.

Zugehörigkeit & Standort
------------------------

- Zugehörigkeit: Händlerbund (extern).
- Standort: C6 (Kontaktpunkt zu Novapolis).
- Status: eigenständige Figur (nicht Marven/Arlen); im Personenindex/Relationslog geführt.

Kanonischer Auftritt
--------------------

- Erwähnt als Händlerkontakt im Novapolis-Relationslog (Erstkontakt über Karawane H-47 in C6).

Notizen
-------

- Abgrenzung: kein „Karawanenführer“ im Kanon (siehe Rollenabgrenzung Marven/Kora im Personenindex).

Beziehungen & Schnittstellen
----------------------------

- Novapolis: Erstkontakt/Anbahnung über C6; operative Schnittstelle über Handels-/Diplomatie-Protokolle.
- Händlerbund: eingebunden in externe Routen/Versorgung; genaue Rolle innerhalb des Händlerbunds ist offen.

Wissensstand (Matrix - Auszug)
------------------------------

- Extern (Händlerbund): kennt Novapolis über persönliche Kontakte/Erstkontakt, keine Freigaben für D5.
- Geheimhaltung: Einhaltung der Freigabe-/C6-Only-Regeln (FR-KNOWLEDGE).

Offene Punkte
-------------

- Klären: Status/Rolle in der Karawane H-47 (Kontakt vs. operative Verantwortung).
- Klären: konkrete Tauschgüter/Angebote und Bedingungen (Deals, Red Lines, Protokoll).
- Optional: Basiswerte/Skills/Ausrüstung nur ergänzen, wenn RAW/Scene/Missionslog das explizit stützt.

Links
-----

- Relationslog Novapolis → ../00-admin/Relationslog-Novapolis.md
- Handel & Diplomatie (Händlerbund) → ../00-admin/Handel-Diplomatie-Haendlergilde.md
- Personenindex Novapolis → ../00-admin/person_index_np.md
- C6 → ../03-locations/C6.md

Quellen & Review
----------------

- SSOT: ../00-admin/Relationslog-Novapolis.md
- SSOT: ../00-admin/person_index_np.md


