---
stand: 2026-03-11 04:52
update: ADR-Einstieg fuer Architekturentscheidungen angelegt.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc docs/adr/README.md CHANGELOG.md SECURITY.md CODE_OF_CONDUCT.md PASS (2026-03-11 04:49); .\.venv\Scripts\python.exe scripts/check_frontmatter.py docs/adr/README.md CHANGELOG.md SECURITY.md CODE_OF_CONDUCT.md PASS (EXITCODE=0, 2026-03-11 04:49)
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
