---
stand: 2026-02-09 02:59
update: Konfliktliste/Report verlinkt; Checks vermerkt.
checks: "& .\\.venv\\Scripts\\python.exe scripts\\run_checks_and_report.py PASS (2026-02-09 02:59)"
---

Review: chat-export-complete
==========================

Zweck
-----
- Review-Notizen/Entscheidungen für den konsolidierten Chat-Export.

Scope
-----
- Quelle: `database-raw/99-exports/chat-export-complete.txt`
- Staging: normalisiert + gechunked unter `database-curated/staging/chunks/chat-export-complete/`

Offen
-----
- [x] Tagging Write-Run → reviewed/ geschrieben (`database-curated/reviewed/chat-export-complete/`)
- [x] Unresolved geprüft (`reviewed/.../unresolved.json`)
- [x] Curated-Validator (Schema) laufen lassen (staging/manifest)
- [x] FinalGate-Record pflegen: `database-curated/staging/chat-export-complete.finalgate.md`
- [x] SSOT-Änderungen (Admin + Logistik/Inventar) umsetzen und verlinken
- [ ] Receipt im Root `DONELOG.md` nach grünen Checks

Links
-----

- Reviewed-Index: `database-curated/reviewed/chat-export-complete/index_review.json`
- FinalGate-Record: `database-curated/staging/chat-export-complete.finalgate.md`
- SSOT-Patches: `database-rp/00-admin/Logistik.md`, `database-rp/01-factions/novapolis/04-inventory/Novapolis-inventar.md`, `database-rp/01-factions/novapolis/04-inventory/D5-inventar.md`, `database-rp/01-factions/novapolis/04-inventory/C6-inventar.md`
- Curated-Konfliktliste: `database-rp/00-admin/Curated-Konfliktliste.md`
- Report: `.tmp/results/reports/curated_conflicts_postflight_20260112_0657.md`
