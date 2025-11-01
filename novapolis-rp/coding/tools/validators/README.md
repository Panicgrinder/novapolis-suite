Validator-Suite (Novapolis-RP)

Validiert kuratierte Artefakte und RP-Daten (Schemata + Cross-Refs).

Inhalte
- JSON-Schema: `schemas/curated-manifest.schema.json`
- Skripte:
  - `src/validate-curated.js` – validiert `database-curated/staging/manifest.json`
  - `src/validate-rp.js` – prüft Markdown (H1 vorhanden, optionale Front-Matter-Typen)
  - `src/check-crossrefs.js` – prüft Szenen-Referenzen (characters/locations/inventory)
  - `src/validate-all.js` – führt alles nacheinander aus
  - `behavior_matrix_check.py` – prüft Signatur-Format & Quellen im Anchor-Register (`AI-Behavior-Mapping.md`) und vergleicht Intensitäten mit `ai_psymatrix_index_v1` (sobald vorhanden)

Nutzung (lokal)
- Voraussetzungen: Node.js 20+ oder Docker
- Install:
  - Lokal: `npm ci --prefix coding/tools/validators`
  - Docker: wird im Task/CI automatisch erledigt
- Run:
  - Lokal: `npm --prefix coding/tools/validators run validate`
  - Namen prüfen (robust, ohne Inline-Command):
    - `powershell -ExecutionPolicy Bypass -File coding/tools/validators/run_check_names.ps1`
  - Markdown-Lint (zentral, ohne Wrapper):
    - `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc "**/*.md"`
  - Behavior-Matrix-Check (optional):
    - `python coding/tools/validators/behavior_matrix_check.py`

CI/Tasks
- VS Code Task `validate:data` versucht zuerst Docker, sonst lokal.
- CI Workflow `.github/workflows/validate.yml` führt Schema-/Cross-Ref-Checks aus und lintet Markdown.
- Hinweis: Falls PowerShell-Tasks mit `Unexpected token` fehlschlagen, nutze den Wrapper `run_check_names.ps1` (s.o.); `run_lint_markdown.ps1` ist veraltet und verweist nur noch auf den direkten `npx`-Aufruf.

Hinweis: RP-Markdown wird bewusst "soft" validiert (H1 + optionale Typprüfungen). Szenen-Front-Matter (empfohlen): YAML mit Feldern `characters`, `locations`, `inventoryRefs`.
