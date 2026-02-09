---
stand: 2026-02-09 02:59
update: Konfliktliste/FACT?-Liste verlinkt und Checklist aktualisiert; Checks vermerkt.
checks: "& .\\.venv\\Scripts\\python.exe scripts\\run_checks_and_report.py PASS (2026-02-09 02:59)"
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

- [x] Curated-Validator (schema) grün
- [x] Konfliktliste vorhanden (Top-10 aus [OPEN])
- [x] FACT?-Liste vorhanden
- [x] Entscheidungen dokumentiert (Decision Records)
- [x] SSOT-Änderungen umgesetzt und verlinkt
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
- Konfliktliste: [Curated-Konfliktliste](../../database-rp/00-admin/Curated-Konfliktliste.md)

Hinweis: Konfliktpunkte werden in der Konfliktliste gepflegt; Report dient als Extrakt aus Curated-Reviews.

Admin + Logistik/Inventar: Kandidaten (Extrakt, verify-first)
------------------------------------------------------------

Aus `.tmp/results/reports/curated_conflicts_postflight_20260112_0657.md` (Auswahl, Admin/Logistik/Inventar-nah):

- Logistik-/Mission-Canvas vorgesehen: „Eigenständige Canvas „Logistik“ und „Mission Tunnel“ sind vorgesehen“.
- Inventar-Transferregel: „D5 und C6 Inventare bleiben getrennt; Transfers nur via Mission/Logistik“.
- Trennung als Leitregel: „Stationen physisch getrennt → Inventare/Produktionen trennen“.
- Währungs-Notation: „Währung „Kugeln“ … als Gegenstand in Inventaren geführt“.
- Buchungsregel: „Material-/Verbrauchsbuchung … Inventar korrekt zuordnen“.

Decisions + SSOT-Patches (Admin/Logistik/Inventar)
-------------------------------------------------

- Decision: Inventare bleiben getrennt; Transfers nur via Mission/Logistik; Buchungen mit Quelle/Ziel.
  - SSOT: [Logistik](../../database-rp/00-admin/Logistik.md), [D5-Inventar](../../database-rp/01-factions/novapolis/04-inventory/D5-inventar.md), [C6-Inventar](../../database-rp/01-factions/novapolis/04-inventory/C6-inventar.md)
- Decision: Waehrung "Kugeln" wird als Inventar-Item gefuehrt (neu/gebraucht).
  - SSOT: [Novapolis-Inventar](../../database-rp/01-factions/novapolis/04-inventory/Novapolis-inventar.md), [Logistik](../../database-rp/00-admin/Logistik.md)

Nächste Schritte
----------------

- [x] Curated-Validator für `database-curated/staging/manifest.json` laufen lassen (Schema).
- [x] Review `chat-export-complete.review.md` auf Ist-Stand bringen (Tagging/Write-Run ist bereits vorhanden; finalGate/SSOT-Plan verlinken).
- [x] Für Admin/Logistik/Inventar: betroffene SSOT-Zielstellen festlegen und pro Konflikt/FACT? Decision + Patch-Link ergänzen.
- [ ] DONELOG-Receipt setzen (Root) nach grünen Checks.
