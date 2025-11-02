---
stand: 2025-11-02 23:36
update: YAML-Frontmatter ergänzt; Inhalt unverändert
checks: markdownlint-cli2 (docs focused) PASS
---

# Reports-Standard

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
