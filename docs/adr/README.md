---
stand: 2026-03-11 04:45
update: ADR-Einstieg fuer Architekturentscheidungen angelegt.
checks: pending (laufender Umbau)
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
