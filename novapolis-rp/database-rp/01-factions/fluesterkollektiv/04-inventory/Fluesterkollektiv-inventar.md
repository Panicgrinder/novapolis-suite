---
stand: 2026-01-14 12:32
update: Bestände/Logs als variabel konkretisiert; tbd reduziert. Receipts aktualisiert (Gates PASS).
checks: "npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/**/*.md' PASS (2026-01-14 09:51); & .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py novapolis-rp\\database-rp PASS (2026-01-14 09:51); & .\\.venv\\Scripts\\python.exe scripts\\checks_rp_consistency.py --strict PASS (2026-01-14 09:51); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:rp PASS (2026-01-14 09:51); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:crossrefs PASS (2026-01-14 09:51)"
canvas: Inventar Fluesterkollektiv
last_updated: 2026-01-14T08:56:04+01:00
category: inventory
slug: fluesterkollektiv-inventar
owner: fluesterkollektiv
scope: faction
version: "0.1"
tags: []
---

Inventar - Fluesterkollektiv (Fraktion)
======================================

Bestände (Auszug)
-----------------
- Kugeln (neu): hochwertig (1 neu ≈ 10 gebraucht; Bestand nicht quantifiziert)
- Kugeln (gebraucht): Alltagswährung/Hauptmunition (Qualität streut; Bestand nicht quantifiziert)
- Informationsgüter: variabel (Gerüchte, Kontakte, Zugangscodes; Abrechnung nach Trust)
- Tarn-/Signaltechnik: variabel (keine Stückzahlen; abhängig von Lage)
- Verbrauchsmaterial: variabel (Batterien/Filter/Verbrauch; keine Stückzahlen)

Bewegungen (Log)
----------------
- 2026-01-14: Baseline angelegt; keine Buchungen dokumentiert.
- Template: YYYY-MM-DD | Bezug: scene-... | Delta: +/− | Gegenpartei: ... | Abrechnung: Kugeln/Tausch | Notiz: ...

Links
-----
- Logistik (Admin) → ../../../00-admin/Logistik.md
- Missionslog → ../../../00-admin/Missionslog.md
- Währung "Kugeln" (Reference) → ../../../00-admin/Reference-Campaign-State.md
