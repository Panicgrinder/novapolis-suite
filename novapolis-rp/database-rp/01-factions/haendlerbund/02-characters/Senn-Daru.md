---
stand: 2026-01-14 17:50
update: "Zugehörigkeit/Position aktualisiert: Anschluss an Novapolis; Basis C6.; Checks PASS."
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc **/*.md PASS (2026-01-14 17:50); & .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py novapolis-rp\\database-rp PASS (2026-01-14 17:50); & .\\.venv\\Scripts\\python.exe scripts\\checks_rp_consistency.py --strict PASS (2026-01-14 17:50); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:rp PASS (2026-01-14 17:50); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:crossrefs PASS (2026-01-14 17:50)
title: Senn Daru
category: character
slug: senn-daru
version: "1.0"
last_updated: 2026-01-14T17:31:10+01:00
tags: ["karawane", "novapolis"]
affiliations: ["novapolis"]
dependencies: ["c6", "g7"]
primary_location: c6
last_seen: c6
---

Senn Daru
---------

Kurzprofil
----------
- Rolle/Funktion: Händler/Vermittler, Karawane H-47; nach Anschluss an Novapolis Basis C6.
- Auftreten: verhandelt empathisch, bleibt neugierig-offen, priorisiert Ausgleich vor Eigeninteresse.
- Verhaltenssignatur: `SND1=E72-N64-L58-O46-S42-T38-C30-M22-P44-s`.

Rollen & Verantwortlichkeiten (Pflichtfelder)
---------------------------------------------
- Handel/Diplomatie: Schnittstelle nach außen (u. a. G7), Erstkontakte/Protokolle.

Zugehörigkeit & Standort
------------------------

- Zugehörigkeit: Novapolis (C6; ehem. Karawane H-47).
- Standort: C6 (Basis; G7 nur als Kontaktpunkt nach Bedarf).
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
- Personenindex Novapolis → ../../novapolis/02-characters/person_index_np.md
- G7 → ../03-locations/G7.md

Quellen & Review
----------------

- SSOT: ../00-admin/Relationslog-Novapolis.md
- SSOT: ../../novapolis/02-characters/person_index_np.md


