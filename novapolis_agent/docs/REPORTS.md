---
stand: 2026-05-19 04:34
update: Markdownlint geprüft (Setext-Stil bestätigt)
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp/results/reports/checks_report_20260518_222833.md; snapshot-lock PASS (2026-05-19 04:34)
---

Reports-Standard
================

Dieser Leitfaden definiert eine einheitliche Struktur für Prüf- und Konsistenzberichte.

Ordnerstruktur

```text
eval/results/reports/<topic>/<YYYYMMDD_HHMM>/
  report.md      # Zusammenfassung/Ergebnisse
  params.txt     # Parameter/Scope der Prüfung
  data.json      # optional: Rohdaten/Snippets
```

Beispiele

- topic = consistency
- topic = dependencies
- topic = coverage

Hinweise

- Zeitstempel immer lokal im Format YYYYMMDD_HHMM
- Pfade relativ zum Repository angeben
- Keine sensiblen Daten/Secrets ablegen

