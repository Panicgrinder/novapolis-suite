---
stand: 2026-02-23 02:35
update: Frische-Review durchgeführt; Verweise/Scope geprüft und weiterhin gültig bestätigt (kein Inhaltsdelta).
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/00-admin/Index-Handel-Diplomatie.md' 'novapolis-rp/database-rp/00-admin/Curated-Konfliktliste.md' 'novapolis-rp/database-rp/00-admin/Waren-Index.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-23 02:36); .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py 'novapolis-rp/database-rp/00-admin/Index-Handel-Diplomatie.md' 'novapolis-rp/database-rp/00-admin/Curated-Konfliktliste.md' 'novapolis-rp/database-rp/00-admin/Waren-Index.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-23 02:36); npm --prefix novapolis-rp/coding/tools/validators run validate:rp PASS (2026-02-23 02:36)
slug: index_handel_diplomatie_v1
category: admin
status: draft
version: "0.1"
---

Index Handel & Diplomatie (Hub, v1)
=================================

Zweck
-----
- Navigations-/Übersichtsseite für Handels- und Diplomatie-Dokumente (SSOT), ohne Inhalte zu duplizieren.
- Trennt klar zwischen (a) Novapolis-internem Relationslog und (b) fraktionsspezifischen Akten/Logs.

Kanonische Anker
---------------
- Novapolis (Kern-SSOT): [Relationslog-Novapolis](../01-factions/novapolis/06-handel-diplomatie/Relationslog-Novapolis.md)
- Weltgeschehen / Zeitanker: [Ereignislog-Weltgeschehen](Ereignislog-Weltgeschehen.md)
- Logistik (Transfers/Flows): [Logistik](Logistik.md)
- Missionen (Belege/Incidents): [Missionslog](Missionslog.md)

Fraktionsbezogene Dokumente
---------------------------

### Händlerbund (Händlergilde-ID)

- Index: [Index-Haendlergilde](../01-factions/haendlerbund/06-handel-diplomatie/Index-Haendlergilde.md)
- Relationslog: [Relationslog-Haendlerbund](../01-factions/haendlerbund/06-handel-diplomatie/Relationslog-Haendlerbund.md)
- Handelslog: [Handelslog-Haendlerbund](../01-factions/haendlerbund/06-handel-diplomatie/Handelslog-Haendlerbund.md)
- Fraktionsakte (Handel/Diplomatie): [Handel-Diplomatie-Haendlergilde](../01-factions/haendlerbund/06-handel-diplomatie/Handel-Diplomatie-Haendlergilde.md)

### Eisenkonklave

- Relationslog: [Relationslog-Eisenkonklave](../01-factions/eisenkonklave/06-handel-diplomatie/Relationslog-Eisenkonklave.md)

Hinweis
-------
- Weitere Fraktionsakten (z. B. Arkologie / Schattenbund / Schienenbund) werden bei Bedarf ergänzt.
- Dieser Hub enthält bewusst keine Detail-Tabellen (Deals/Red Lines), sondern verweist auf die jeweiligen SSOT-Quellen.
