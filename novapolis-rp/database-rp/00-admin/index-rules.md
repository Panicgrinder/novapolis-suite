---
stand: 2026-02-22 04:16
update: T0-Operativreferenzen (Metrokarte, Stationskontroll-Matrix, Warenueberblick) als globale Admin-Anker ergänzt.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-02-22 02:26); .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py 'novapolis-rp/database-rp/00-admin/index-rules.md' 'novapolis-rp/database-rp/00-admin/Current-State.md' 'novapolis-rp/database-rp/00-admin/Logistik.md' 'novapolis-rp/database-rp/00-admin/Metrograph.md' 'novapolis-rp/database-rp/00-admin/Ortsgraph.md' 'novapolis-rp/database-rp/00-admin/Canvas-Admin-Day-Switch-Debug.md' 'novapolis-rp/database-rp/00-admin/Kernkonversationen.md' 'novapolis-rp/database-rp/00-admin/Metrokarte-T0.md' 'novapolis-rp/database-rp/00-admin/Stationskontroll-Matrix.md' 'novapolis-rp/database-rp/00-admin/Warenueberblick-T0.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-22 02:27)
slug: index-rules
category: Admin
schemaVersion: 1
language: de
status: active
owners: [admin-novapolis]
tags: [rp, rules, index]
relatedSlugs: [reference-campaign-state, process-workflow, sim-state-schema, tags-taxonomie, metrokarte-t0, stationskontroll-matrix, warenueberblick-t0]
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
- reference: `metrokarte-t0` → ./Metrokarte-T0.md
- reference: `stationskontroll-matrix` → ./Stationskontroll-Matrix.md
- reference: `warenueberblick-t0` → ./Warenueberblick-T0.md

Abschnitts-IDs (interne Anker für KI)
-------------------------------------
- process-workflow → Prozess/Workflow (Curation, Validation, Export, Simulation)
- sim-state-schema → Sim-State Schema (maschinenlesbar, RP-World-State)
- tags-taxonomie → zentrale gültige Tag-Liste und Startersets
- metrokarte-t0 → operativer T0-Netzblick (Linien, Knoten, Engpasshinweise)
- stationskontroll-matrix → Zuständigkeiten je Station (wer kontrolliert, wie sicher)
- warenueberblick-t0 → standortgetrennter Güter-Überblick ohne Mengenretcon
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
