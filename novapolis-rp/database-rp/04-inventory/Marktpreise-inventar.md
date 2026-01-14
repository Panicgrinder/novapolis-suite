---
stand: 2026-01-14 12:32
update: Baseline-Preise (ohne Zahlen) präzisiert; tbd reduziert. Receipts aktualisiert (Gates PASS).
checks: "npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/**/*.md' PASS (2026-01-14 09:51); & .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py novapolis-rp\\database-rp PASS (2026-01-14 09:51); & .\\.venv\\Scripts\\python.exe scripts\\checks_rp_consistency.py --strict PASS (2026-01-14 09:51); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:rp PASS (2026-01-14 09:51); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:crossrefs PASS (2026-01-14 09:51)"
canvas: Marktpreise - Baseline
last_updated: 2026-01-14T08:56:04+01:00
category: inventory
slug: marktpreise-inventar
owner: market
scope: global
version: "0.1"
tags: [handel, baseline]
---

Marktpreise - Baseline
======================

Zweck
-----
Diese Seite ist eine SSOT-Baseline für Preisgefühl und Knappheit im Setting.
Sie ersetzt keine fraktionsspezifischen Inventare, sondern liefert eine gemeinsame Referenz,
wenn Szenen Handel, Tausch oder Beschaffung dokumentieren.

Währung (Kurz)
--------------
- Standard: "Kugeln" (neu/gebraucht)
- Faustregel: 1 neu ≈ 10 gebraucht (Qualität streut)

Baseline-Preise (Richtwerte)
----------------------------
- Energiezelle (Standard): Richtwert ohne Zahl; Preis folgt Modifikatoren (Knappheit/Route/Trust)
- Filter (Wasser/Luft): Richtwert ohne Zahl; Preis folgt Modifikatoren (Knappheit/Route/Trust)
- Adapter / Fittings (DN60 / Sonder): Richtwert ohne Zahl; Preis folgt Modifikatoren (Knappheit/Route/Trust)
- Schweißausrüstung (kompakt): Richtwert ohne Zahl; Preis folgt Modifikatoren (Knappheit/Route/Trust)
- Werkzeugsatz (Mechanik): Richtwert ohne Zahl; Preis folgt Modifikatoren (Knappheit/Route/Trust)

Modifikatoren
-------------
- Knappheit: +20% bis +80%
- Bulk (Mengenrabatt): -10% bis -25%
- Risiko/Route (Tunnel/Anomalien): +10% bis +50%
- Beziehung/Trust: -10% bis -30% (oder Alternativ: bessere Qualität statt Preis)

Logging-Konvention (für Szenen)
-------------------------------
- Jede Szene, die Handel beeinflusst, verlinkt auf die betroffenen Inventare.
- Bestandsänderungen werden in den jeweiligen Inventaren unter "Bewegungen (Log)" nachgezogen.
- Verhandlungen/Beziehungen werden im jeweiligen Relationslog dokumentiert.

Links
-----
- Logistik (Admin) → ../00-admin/Logistik.md
- Missionslog → ../00-admin/Missionslog.md
- Währung "Kugeln" (Reference) → ../00-admin/Reference-Campaign-State.md
