---
stand: 2026-02-01 14:08
update: FinalGate-Record initial angelegt (Admin + Logistik/Inventar); Checks receipted.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-02-01 14:08); & .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis-rp\database-curated\staging PASS (2026-02-01 14:08); npm --prefix novapolis-rp/coding/tools/validators run validate:rp PASS (2026-02-01 14:08)
source: novapolis-rp/database-curated/staging/manifest.json (export-2-chat-export-complete)
---

FinalGate Record: chat-export-complete
====================================

Kontext
-------

- Zweck: Nachweis- und Entscheidungsdokument für die Promotion `staging/` → `final/` und die anschließende Übernahme relevanter Inhalte in den Canon (SSOT).
- Scope dieser Runde: **Admin** + **Logistik/Inventar** (ohne Canon-Erfindung; nur belegte Aussagen/Extrakte).

Kriterien-Checkliste (laut manifest)
----------------------------------

Quelle: `novapolis-rp/database-curated/staging/manifest.json` → `promotion.finalGate.criteria`.

- [ ] Curated-Validator (schema) grün
- [ ] Konfliktliste vorhanden (Top-10 aus [OPEN])
- [ ] FACT?-Liste vorhanden
- [ ] Entscheidungen dokumentiert (Decision Records)
- [ ] SSOT-Änderungen umgesetzt und verlinkt
- [ ] Receipt im Root `DONELOG.md`

Status: Reviewed-Artefakte (chat-export-complete)
------------------------------------------------

- Reviewed-Index: `novapolis-rp/database-curated/reviewed/chat-export-complete/index_review.json`
- Unresolved-Status: `novapolis-rp/database-curated/reviewed/chat-export-complete/unresolved.json` (laut Datei: keine offenen Dependencies/Kollisionen/Unknowns)

FACT?-Teile (aus index_review.json)
----------------------------------

Die folgenden Teile enthalten `FACT?`-Tags (Zählung aus `index_review.json`):

- `chat-export-complete.part-003.txt` (1)
- `chat-export-complete.part-006.txt` (1)
- `chat-export-complete.part-007.txt` (2)
- `chat-export-complete.part-008.txt` (2)
- `chat-export-complete.part-009.txt` (5)
- `chat-export-complete.part-010.txt` (4)
- `chat-export-complete.part-011.txt` (2)
- `chat-export-complete.part-014.txt` (1)
- `chat-export-complete.part-017.txt` (1)
- `chat-export-complete.part-018.txt` (2)
- `chat-export-complete.part-019.txt` (2)
- `chat-export-complete.part-020.txt` (4)
- `chat-export-complete.part-021.txt` (2)
- `chat-export-complete.part-022.txt` (4)

Top-10 Konflikte (aus [OPEN])
-----------------------------

Aktueller Extrakt liegt als Report vor:

- `.tmp/results/reports/curated_conflicts_postflight_20260112_0657.md`

Hinweis: Der Report referenziert aktuell hauptsächlich `chat-export (1).review.md` als Quelle der `[OPEN]`-Punkte. Für `chat-export-complete` müssen ggf. zusätzliche `[OPEN]`-Notizen im Review ergänzt und der Extrakt erneut erzeugt werden.

Admin + Logistik/Inventar: Kandidaten (Extrakt, verify-first)
------------------------------------------------------------

Aus `.tmp/results/reports/curated_conflicts_postflight_20260112_0657.md` (Auswahl, Admin/Logistik/Inventar-nah):

- Logistik-/Mission-Canvas vorgesehen: „Eigenständige Canvas „Logistik“ und „Mission Tunnel“ sind vorgesehen“.
- Inventar-Transferregel: „D5 und C6 Inventare bleiben getrennt; Transfers nur via Mission/Logistik“.
- Trennung als Leitregel: „Stationen physisch getrennt → Inventare/Produktionen trennen“.
- Währungs-Notation: „Währung „Kugeln“ … als Gegenstand in Inventaren geführt“.
- Buchungsregel: „Material-/Verbrauchsbuchung … Inventar korrekt zuordnen“.

Nächste Schritte
----------------

- [ ] Curated-Validator für `database-curated/staging/manifest.json` laufen lassen (Schema).
- [ ] Review `chat-export-complete.review.md` auf Ist-Stand bringen (Tagging/Write-Run ist bereits vorhanden; finalGate/SSOT-Plan verlinken).
- [ ] Für Admin/Logistik/Inventar: betroffene SSOT-Zielstellen festlegen (vermutet: `novapolis-rp/database-rp/00-admin/` und `novapolis-rp/database-rp/04-inventory/`) und pro Konflikt/FACT? Decision + Patch-Link ergänzen.
- [ ] DONELOG-Receipt setzen (Root) nach grünen Checks.
