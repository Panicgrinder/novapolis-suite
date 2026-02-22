---
stand: 2026-02-22 01:49
update: Tags-Taxonomie als Referenz und Abschnitts-ID ergänzt.
checks: npm --prefix novapolis-rp/coding/tools/validators run validate:rp PASS (2026-02-22 01:37); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/00-admin/index-rules.md' PASS (2026-02-22 01:37); .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py 'novapolis-rp/database-rp/00-admin/index-rules.md' PASS (2026-02-22 01:37)
slug: index-rules
category: Admin
schemaVersion: 1
language: de
status: active
owners: [admin-novapolis]
tags: [rp, rules, index]
relatedSlugs: [reference-campaign-state, process-workflow, sim-state-schema, tags-taxonomie]
---

Index: Regeln, Policies und FSM
===============================

Zweck: Zentrale Übersicht aller Regel-/Policy-Sektionen und Entscheidungsanker (IDs), um menschliche und KI-basierte Verwaltung zu erleichtern.

Quelldatei (Aggregator)
-----------------------
- reference: `reference-campaign-state` → ./Reference-Campaign-State.md
- reference: `process-workflow` → ./Process-Workflow.md
- reference: `sim-state-schema` → ./Sim-State-Schema.md
- reference: `tick-regeln-simulation` → ./Tick-Regeln-Simulation.md
- reference: `tags-taxonomie` → ./Tags-Taxonomie.md

Abschnitts-IDs (interne Anker für KI)
-------------------------------------
- process-workflow → Prozess/Workflow (Curation, Validation, Export, Simulation)
- sim-state-schema → Sim-State Schema (maschinenlesbar, RP-World-State)
- tags-taxonomie → zentrale gültige Tag-Liste und Startersets
- fsm-campaign → Kampagnen-Zustandsmaschine
- rule-se-pools → Symbiose-Energie (SE) – Pools
- rule-instances → Instanzen: Wissensstand & Persönlichkeit
- rule-proximity → Nähe-Kopplung (PROXIMITY)
- rule-reflex-speech → Reflex Sprache/Audio (REFLEX-SPEECH)
- rule-reflex-control → Schutz-Übernahme (REFLEX-CONTROL)
- rule-detach → Detachment & Beweglichkeit (REFLEX-DETACH)
- rule-jealousy-gloves → Kontakt-Guard / Eifersuchts-Guard (JEALOUSY-GLOVES)
- policy-new-entities → Admin/Canon-Policy: Neue Entitäten
- economy-kugeln → Währung: „Kugeln“ (neu vs gebraucht)
- project-draisine → Projekt: Draisine-/Transportmodul (D5)

Decision-IDs (kanonische Festlegungen)
--------------------------------------
- DEC-2026-02-09-01 → `REFLEX-CONTROL`: Rückgabe/Entkopplung erst bei "Sicher"
- DEC-2026-02-09-02 → `PROXIMITY`: Distanzfenster (Startwerte) als Default

RP-Referenzstandard (slug-only)
-------------------------------

- Semantische ID ist immer `slug` (auch in `characters`, `locations`, `dependencies`, `owners`).
- Dateiname/Ordnername ist nur Ablageform und darf nie als Referenz-Token verwendet werden.
- Markdown-Links dienen der Navigation; semantische Validierung läuft über `slug`.

Hinweis
-------
- Die obigen IDs sind als HTML-Kommentare in der Quelldatei markiert (z. B. `<!-- id: rule-proximity -->`).
- Für klickbare Navigation nutze die Abschnittsüberschriften in `Reference-Campaign-State.md`.
