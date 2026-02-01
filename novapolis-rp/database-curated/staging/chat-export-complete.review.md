---
stand: 2026-02-01 14:08
update: Review-Status aktualisiert; finalGate-Record verlinkt; nächste Schritte präzisiert; Checks receipted.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-02-01 14:08); & .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis-rp\database-curated\staging PASS (2026-02-01 14:08); npm --prefix novapolis-rp/coding/tools/validators run validate:rp PASS (2026-02-01 14:08)
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
- [ ] Curated-Validator (Schema) laufen lassen (staging/manifest)
- [ ] FinalGate-Record pflegen: `database-curated/staging/chat-export-complete.finalgate.md`
- [ ] SSOT-Änderungen (Admin + Logistik/Inventar) umsetzen und verlinken
- [ ] Receipt im Root `DONELOG.md` nach grünen Checks

Links
-----

- Reviewed-Index: `database-curated/reviewed/chat-export-complete/index_review.json`
- FinalGate-Record: `database-curated/staging/chat-export-complete.finalgate.md`
