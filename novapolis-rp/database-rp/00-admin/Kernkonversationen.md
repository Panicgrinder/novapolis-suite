---
stand: 2026-01-13 19:41
update: "Admin-Canvas ergänzt: Kernkonversationen (Index/Template) als Platzhalter für 1–2 wirklich zentrale Chat-Nachrichten/Belege. Befüllung folgt nur mit exakten RAW-Zitaten. Checks PASS."
checks: "npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/00-admin/Kernkonversationen.md' PASS (2026-01-13 19:41); & .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py 'novapolis-rp/database-rp/00-admin/Kernkonversationen.md' PASS (2026-01-13 19:41); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:crossrefs PASS (2026-01-13 19:41)"
slug: kernkonversationen
category: admin
version: "1.0"
---

Kernkonversationen (Belege)
==========================

Zweck
-----

Kuratiert 1–2 (max. wenige) wirklich zentrale Chat-Nachrichten als Beleganker. Inhalte dürfen ausschließlich als exakte RAW-Zitate (oder enges Paraphrasieren mit Verweis) übernommen werden.

Regeln
------

- Keine neuen Fakten: Nur zitieren, was im RAW wörtlich belegt ist.
- Jede Zeile mit eindeutiger RAW-Referenz (Timestamp/Export-Segment).
- Pro Eintrag: Kontext (1 Satz), Zitat (wörtlich), Folge (welcher Canvas/Entscheid betroffen ist).

Einträge
--------

- tbd

Links
-----

- RAW-Export: ../../database-raw/99-exports/RAW-chat-export-2025-10-27T09-16-00-188Z.txt
- Timeline → ./Canvas-T+0-Timeline.md
