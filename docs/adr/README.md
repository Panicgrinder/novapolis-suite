---
stand: 2026-03-19 11:09
update: ADR-Ordner aktiviert; zwei akzeptierte Grundsatzentscheidungen fuer DONELOG-Ebenen und Quality-Gate-Sequenz aufgenommen.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260318_052318.md
---

Architecture Decision Records (ADR)
===================================

Ziel
----

- Grosse Strukturentscheidungen nachvollziehbar dokumentieren.
- Kontext, Entscheidung und Konsequenzen langfristig auffindbar machen.

Namensschema
------------

- Dateien als `NNNN-kurztitel.md`, z. B. `0001-donelog-ebenen.md`.
- `NNNN` fortlaufend, vierstellig.

Minimalstruktur
---------------

- Status: proposed | accepted | superseded | deprecated
- Kontext
- Entscheidung
- Konsequenzen
- Verweise (Issues, PRs, Commits, betroffene Pfade)

Template (Kurzform)
-------------------

```markdown
# ADR NNNN: <Titel>

- Status: proposed
- Datum: YYYY-MM-DD

## Kontext

## Entscheidung

## Konsequenzen

## Verweise
```

Aktive ADRs
-----------

- `0001-donelog-ebenen.md` - akzeptiert; normiert die drei operativen DONELOG-Ebenen und ihre Verantwortlichkeiten.
- `0002-quality-gate-sequenz.md` - akzeptiert; fixiert die verbindliche Reihenfolge und Bewertung der Quality-Gates.
