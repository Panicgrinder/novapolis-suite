---
stand: 2026-03-11 03:57
update: Projektkontext-Bruecke als SSOT geplant; Phase 1 gestartet (Manifest + Index-Build-Skript).
checks: .\.venv\Scripts\python.exe novapolis_agent\scripts\build_project_context_index.py PASS (indexed_sources=10, n_docs=10, vocab=2807, 2026-03-10 17:05); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-dev/docs/process/project-context-bridge.ssot.md' 'novapolis_agent/docs/runbook.md' 'novapolis-dev/docs/donelog.md' 'novapolis_agent/docs/DONELOG.txt' PASS (2026-03-10 17:05); .\.venv\Scripts\python.exe scripts/check_frontmatter.py 'novapolis-dev/docs/process/project-context-bridge.ssot.md' 'novapolis_agent/docs/runbook.md' 'novapolis-dev/docs/donelog.md' 'novapolis_agent/docs/DONELOG.txt' PASS (EXITCODE=0, 2026-03-10 17:05)
---
Project Context Bridge (SSOT)
=============================

Ziel
----

Diese SSOT definiert den offiziellen Implementierungspfad fuer einen projektbewussten Chatmodus der lokalen KI im Novapolis-Workspace.

Scope
-----

- Runtime/Bedienung: `novapolis_agent/`
- Kontextquellen: Root + `novapolis-rp/` + `novapolis-dev/`
- Governance: `.github/copilot-instructions.md` und aktive scoped instructions

Ist-Stand (belegt)
------------------

- Kontextnotizen-Injektion ist vorhanden (`CONTEXT_NOTES_*` + `[Kontext-Notizen]` Injektion im Chat-Flow).
- RAG-Injektion ist vorhanden (`RAG_ENABLED`, `RAG_INDEX_PATH`, `RAG_TOP_K` + `[RAG]` Injektion im Chat-Flow).
- Ein TF-IDF-Retriever ist vorhanden (`novapolis_agent/utils/rag.py`).
- Ein Basis-Indexer ist vorhanden (`novapolis_agent/scripts/rag_indexer.py`).
- Eval-Infrastruktur und Suite-Tasks sind vorhanden (neutral/rpg/rp_content + strict validator).

Zielbild
--------

Ein opt-in Modus "chat with project context" nutzt einen kanonischen, versionierten Kontextquellenkatalog und injiziert Retrieval-Snippets kontrolliert in den bestehenden Chat-Flow.

- Keine stillen Seiteneffekte
- Keine neue Parallelarchitektur im MVP
- Reproduzierbarer Build- und Betriebsweg ueber Skript + Runbook

Phasenplan
----------

1. Phase 1 (MVP Start)
   - Kanonische Quellenliste versionieren
   - reproduzierbares Build-Skript fuer Kontextindex
   - Runbook-Betriebsweg dokumentieren
2. Phase 2 (Retrieval-Qualitaet)
   - Chunking/Scoring verbessern, Quellengewichtung nach Surface-Klasse
3. Phase 3 (Eval/Gates)
   - Bridge-spezifische Eval-Pakete + KPI-Auswertung
4. Phase 4 (Bedienbarkeit)
   - Root-Tasking, Betriebsmodi, konsistente Operator-Doku

Phase 1 Ergebnis (dieser Lauf)
------------------------------

- Neues Quellenmanifest: `novapolis_agent/eval/config/context.bridge.sources.json`
- Neues Build-Skript: `novapolis_agent/scripts/build_project_context_index.py`
- Runbook-Abschnitt fuer Bedienung: `novapolis_agent/docs/runbook.md`

Akzeptanzkriterien Phase 1
--------------------------

- Quellenliste ist versioniert und maschinenlesbar.
- Index-Build funktioniert reproduzierbar ueber `.venv`-Python.
- Runbook beschreibt den minimalen Betriebsweg fuer den Kontextmodus.

Out of Scope (Phase 1)
----------------------

- Kein neuer API-Endpunkt
- Kein Embedding-/Vector-Backend
- Kein Fine-Tuning
