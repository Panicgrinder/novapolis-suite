---
stand: 2026-02-01 14:14
update: Staging-Stub: FinalGate-Record Pattern/Link ergänzt.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-02-01 14:14); & .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis-rp\database-curated PASS (2026-02-01 14:14); npm --prefix novapolis-rp/coding/tools/validators run validate:rp PASS (2026-02-01 14:14)
---

Staging Leitfaden (Stub)
=======================
Details & Tagging-Regeln jetzt im Hub: `novapolis-dev/docs/readme.hub.md` → "Curation Workflow".

Kurz:
- Normalisieren → Annotieren → Review → Approve → final/

FinalGate (Promotion)
---------------------

- Pro Export (staging) gibt es einen FinalGate-Record als Audit-Dokument:
  - Pattern: `database-curated/staging/<export>.finalgate.md`
  - Beispiel: `database-curated/staging/chat-export-complete.finalgate.md`


