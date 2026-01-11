---
stand: 2026-01-11 05:18
update: Handel/Diplomatie: Hub-Index ergänzt (Übersicht + Linkziele).
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/**/*.md' PASS (2026-01-11 05:18); & .\.venv\Scripts\python.exe scripts\check_frontmatter.py --touch novapolis-rp\database-rp\00-admin\Index-Handel-Diplomatie.md novapolis-rp\database-rp\00-admin\Handel-Diplomatie-Haendlergilde.md novapolis-rp\database-rp\00-admin\Relationslog-Novapolis.md novapolis-rp\database-rp\00-admin\Index-Haendlergilde.md DONELOG.md PASS (2026-01-11 05:18); & .\.venv\Scripts\python.exe scripts\checks_rp_consistency.py --strict PASS (2026-01-11 05:18)
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
- Novapolis (Kern-SSOT): `database-rp/01-factions/novapolis/06-handel-diplomatie/Relationslog-Novapolis.md`
- Weltgeschehen / Zeitanker: `database-rp/00-admin/Ereignislog-Weltgeschehen.md`
- Logistik (Transfers/Flows): `database-rp/00-admin/Logistik.md`
- Missionen (Belege/Incidents): `database-rp/00-admin/Missionslog.md`

Fraktionsbezogene Dokumente
---------------------------

### Händlerbund (Händlergilde-ID)

- Index: `database-rp/00-admin/Index-Haendlergilde.md`
- Relationslog: `database-rp/01-factions/haendlerbund/06-handel-diplomatie/Relationslog-Haendlerbund.md`
- Handelslog: `database-rp/01-factions/haendlerbund/06-handel-diplomatie/Handelslog-Haendlerbund.md`
- Fraktionsakte (Handel/Diplomatie): `database-rp/01-factions/haendlerbund/06-handel-diplomatie/Handel-Diplomatie-Haendlergilde.md`

### Eisenkonklave

- Relationslog: `database-rp/01-factions/eisenkonklave/06-handel-diplomatie/Relationslog-Eisenkonklave.md`

Hinweis
-------
- Weitere Fraktionsakten (z. B. Arkologie / Schattenbund / Schienenbund) werden bei Bedarf ergänzt.
- Dieser Hub enthält bewusst keine Detail-Tabellen (Deals/Red Lines), sondern verweist auf die jeweiligen SSOT-Quellen.
