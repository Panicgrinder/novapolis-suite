---
stand: 2026-03-30 05:08
update: ADR-Ordner aktiviert; zwei akzeptierte Grundsatzentscheidungen fuer DONELOG-Ebenen und Quality-Gate-Sequenz aufgenommen.
checks: snapshot-lock PASS; markdownlint PASS; frontmatter PASS; todo-index PASS; naming-policy PASS; path-portability PASS; logs-policy PASS; doc-freshness PASS; scan-links PASS; validate-rp PASS (2026-03-30 05:08)
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
