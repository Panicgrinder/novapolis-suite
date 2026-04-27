---
stand: 2026-04-28 01:22
update: Der Freshness-Scope deckt jetzt Root, Governance, Dev, Agent, RP, Sim und die Tree-Artefakte ueber konkrete Pfade, Globs und passende Pruefmodi samt Max-Alter-Overrides ab.
checks: snapshot-lock PASS (2026-04-28 01:22); doc-freshness PASS (scope_rows=46, checked_docs=262, findings=0, 2026-04-28 01:17)
---

Doc Freshness Scope
===================

Ziel
----

- Kanonische Scope-Quelle fuer den workspaceweiten Freshness-Check.
- Der Scope soll nicht nur den Dev-Hub, sondern die fuehrenden Doku- und Navigationspfade aus Root, Governance, Agent, RP, Sim und den Tree-Artefakten abdecken.

Modi
----

- `frontmatter`: `stand` aus YAML-Frontmatter.
- `legacy-header`: `stand:` aus dem historischen Kopfblock ohne YAML-Frontmatter.
- `mtime`: Dateialter ueber Dateisystem-Zeitstempel fuer generierte oder nicht-frontmatter-basierte Artefakte.
- `max_age_days`: optionaler Override fuer langsam rotierende Governance-, Referenz- oder Reportpfade; `-` nutzt die Default-SLA des `surface`-Werts.

Scope
-----

| Path | surface | mode | max_age_days | owner | notes |
| --- | --- | --- | --- | --- | --- |
| `README.md` | ACTIVE | frontmatter | - | root-governance | Root-Einstieg |
| `WORKSPACE_INDEX.md` | ACTIVE | frontmatter | - | root-governance | Root-Navigation |
| `WORKSPACE_STATUS.md` | ACTIVE | frontmatter | - | root-governance | Laufender Betriebsstatus |
| `DONELOG.md` | ACTIVE | frontmatter | - | root-governance | Root-Summary |
| `todo.root.md` | ACTIVE | frontmatter | - | root-governance | Root-Backlog |
| `.github/copilot-instructions.md` | REFERENCE | legacy-header | - | governance | Kern-SSOT |
| `.github/copilot-instructions-headings.md` | REFERENCE | frontmatter | - | governance | Headings-Index |
| `.github/instructions/*.instructions.md` | REFERENCE | mtime | 180 | governance | Scoped Instructions |
| `novapolis-dev/README.md` | REFERENCE | frontmatter | - | dev-governance | Dev-Hub-Einstieg |
| `novapolis-dev/docs/active-surface-index.md` | REFERENCE | frontmatter | - | dev-governance | Dev-Klassifikation |
| `novapolis-dev/docs/donelog.md` | ACTIVE | frontmatter | - | dev-governance | Operativer Dev-Log |
| `novapolis-dev/docs/todo.index.md` | ACTIVE | frontmatter | - | dev-governance | Modulindex |
| `novapolis-dev/docs/todo.dev.md` | ACTIVE | frontmatter | - | dev-governance | Dev-Board |
| `novapolis-dev/docs/todo.rp.md` | ACTIVE | frontmatter | - | rp-governance | RP-Board |
| `novapolis-dev/docs/todo.agent-board.md` | ACTIVE | frontmatter | - | agent-governance | Agent-Board |
| `novapolis-dev/docs/todo.sim.md` | ACTIVE | frontmatter | - | sim-governance | Sim-Board |
| `novapolis-dev/docs/index.md` | REFERENCE | frontmatter | - | dev-governance | Dev-Hub-Navigation |
| `novapolis-dev/docs/naming-policy.md` | REFERENCE | frontmatter | - | dev-governance | Naming-SSOT |
| `novapolis-dev/docs/tests.md` | REFERENCE | frontmatter | - | qa-governance | Test- und Checkleitfaden |
| `novapolis-dev/docs/dataset-provenance.md` | REFERENCE | frontmatter | - | data-governance | Datenherkunft |
| `novapolis-dev/docs/copilot-vscode-usage.md` | REFERENCE | frontmatter | - | tooling-governance | Guidance-Doku |
| `novapolis-dev/docs/readme_decisions.md` | REFERENCE | frontmatter | - | dev-governance | README-Entscheidungen |
| `novapolis-dev/docs/readme.hub.md` | REFERENCE | frontmatter | - | dev-governance | README-Hub |
| `novapolis-dev/docs/architecture-summary-local-ai.md` | REFERENCE | frontmatter | - | architecture | Architekturueberblick |
| `novapolis-dev/docs/process/**/*.md` | REFERENCE | frontmatter | 180 | process-governance | Aktive Prozess-SSOTs |
| `novapolis-dev/docs/specs/**/*.md` | REFERENCE | frontmatter | 180 | domain-maintainers | Aktive Spezifikationen |
| `novapolis-dev/docs/meta/**/*.md` | REFERENCE | frontmatter | 180 | dev-governance | aktive Meta-Dokus |
| `novapolis_agent/README.md` | REFERENCE | frontmatter | - | agent-governance | Modul-Einstieg |
| `novapolis_agent/docs/runbook.md` | REFERENCE | frontmatter | - | agent-governance | Operatives Runbook |
| `novapolis_agent/docs/training.md` | REFERENCE | frontmatter | 180 | agent-governance | Training-Leitfaden |
| `novapolis_agent/docs/REPORTS.md` | REFERENCE | mtime | 180 | agent-governance | Report-Ueberblick |
| `novapolis_agent/docs/provenance-register.md` | REFERENCE | mtime | 180 | agent-governance | Provenienzregister |
| `novapolis_agent/docs/DONELOG.txt` | ACTIVE | mtime | 30 | agent-governance | Modul-DONELOG |
| `novapolis-rp/README.md` | REFERENCE | frontmatter | - | rp-governance | Modul-Einstieg |
| `novapolis-rp/database-rp/00-admin/**/*.md` | REFERENCE | mtime | 120 | rp-governance | Admin- und Kanonrahmen |
| `novapolis-rp/database-rp/**/README.md` | REFERENCE | mtime | 120 | rp-governance | Struktur- und Teilindexpfade |
| `novapolis-rp/database-rp/**/*Index*.md` | REFERENCE | mtime | 120 | rp-governance | Fuehrende Indexpfade |
| `novapolis-rp/database-curated/*.md` | REFERENCE | mtime | 120 | rp-governance | Curation-Leitpfade |
| `novapolis-rp/database-curated/staging/*.md` | REFERENCE | mtime | 120 | rp-governance | Staging-Leitpfade |
| `novapolis-rp/database-curated/staging/rp-runtime/**/*.md` | ACTIVE | mtime | 30 | rp-governance | Aktive RP-Runtime-Doku |
| `novapolis-rp/database-raw/99-exports/*.md` | REFERENCE | mtime | 120 | rp-governance | RAW-Export-Policy |
| `novapolis-rp/coding/tools/**/*.md` | REFERENCE | mtime | 120 | rp-governance | Tool- und Validator-Doku |
| `novapolis-sim/README.md` | REFERENCE | frontmatter | - | sim-governance | Modul-Einstieg |
| `workspace_tree.txt` | ACTIVE | mtime | 30 | root-governance | Aktiver Reader-Baum |
| `workspace_tree_dirs.txt` | ACTIVE | mtime | 30 | root-governance | Aktive Verzeichnis-Summary |
| `workspace_tree_full.txt` | REFERENCE | mtime | 60 | root-governance | Forensischer Vollbaum |

Pflege
------

- Neue fuehrende Doku- oder Navigationspfade werden hier im selben Lauf nachgezogen, in dem sie in den aktiven Workspace-Rahmen aufgenommen werden.
- Globs sind hier ausdruecklich erlaubt und werden vom Freshness-Check zu konkreten Dateien expandiert; sie dienen nicht nur als manuelle Gruppenmarkierung.
- Root- und Dev-Navigation, Modul-Runbooks sowie Tree-Artefakte sollen damit in einem gemeinsamen Scope liegen, damit ein gruener Lauf nicht mehr still nur ein Dev-Subset bedeutet.
- Die hier gesetzten `max_age_days`-Overrides sind bewusst sparsam und dokumentieren langsam rotierende Governance-, Report- und RP-Referenzpfade explizit statt sie still aus dem Scope zu entfernen.