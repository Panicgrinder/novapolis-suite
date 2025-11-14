---
stand: 2025-11-14 15:13
update: Report zu Frontmatter-Autofix & DONELOG-Sort erstellt
checks: markdownlint-cli2 PASS; frontmatter-validator PASS
---

# Report: Frontmatter fixes & DONELOG sort (2025-11-14 15:13)

Kurz: Kleine, konservative Korrekturen an Markdown-Frontmatter durchgeführt, `novapolis_agent/docs/DONELOG.txt` programmatisch sortiert, Validator und Linter ausgeführt und Änderungen committed + gepusht.

Geänderte Dateien
- `novapolis_agent/docs/DONELOG.txt` (Eintrag ergänzt; Inhalt vorher durch `.tmp-results/sorted_DONELOG.txt` validiert und angewendet)
- `.tmp-results/todo.cleaned.md` (öffnenden YAML-Delimiter normalisiert, `stand` aktualisiert)
- `eval/config/context.local.md` (minimaler YAML-Frontmatter-Header hinzugefügt)
- `novapolis_agent/eval/config/context.local.md` (minimaler YAML-Frontmatter-Header hinzugefügt)

Kurzablauf
- Prüflauf: `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md'` → PASS
- Validator: `pwsh -File .\scripts\run_frontmatter_validator.ps1` → initial FAIL (3 Dateien fehlender `---`) → Auto-Fix (auf Anweisung) → Validator erneuert → PASS
- DONELOG-Sort: Programmatisches Sortieren der Einträge in `.tmp-results/sorted_DONELOG.txt`, anschließend ersetzt `novapolis_agent/docs/DONELOG.txt`
- Git: Commit + Push der Frontmatter-Fixes und Agent-DONELOG-Updates (Commit-Message: "chore(docs): add missing frontmatter for validator (auto-fix)")

Anmerkungen
- Änderungen sind konservativ (nur Frontmatter-Header hinzugefügt/normalisiert und eine sorting-Anwendung auf DONELOG). Keine inhaltlichen Textänderungen an Einträgen.
- Backups: vorherige Zwischenstände in `.tmp-results/` verbleiben; bei Bedarf kann `git log` genutzt werden, um Commit-Hashes zu prüfen.

Nächste Schritte (optional)
- Falls gewünscht: Ich kann ein kurzes Diff-File (`.tmp-results/reports/diff_frontmatter_fixes_20251114_1513.patch`) erzeugen und committen.
- Auf Wunsch schreibe ich einen formalisierten Receipt-Eintrag in Root-`DONELOG.md` (bereits ergänzt) und Agent-DONELOG (bereits ergänzt).

Ende des Berichts
