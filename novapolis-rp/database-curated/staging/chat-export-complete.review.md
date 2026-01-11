---
stand: 2026-01-11 03:35
update: Review-Stub: checks aktualisiert; Basis-Stabilisierung (verify-first) fortgesetzt.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-01-11 03:35); & .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis-rp\database-curated\staging\chat-export-complete.review.md PASS (2026-01-11 03:35)
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
- [ ] Tagging-Dry-Run ausführen, Warnings/Unresolved prüfen
- [ ] Tagging Write-Run → reviewed/ schreiben
- [ ] Validatoren/Checks laufen lassen + Receipt in `DONELOG.md`
