---
stand: 2026-02-26 05:17
update: TTS-Model-Track konkretisiert (Policy, Trainingsziel, Evaluationsmetriken, Runtime-Adapter-Plan).
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-dev/docs/todo.agent-board.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' 'novapolis_agent/README.md' 'novapolis_agent/docs/tts-model-track.md' 'novapolis_agent/docs/DONELOG.txt' PASS (2026-02-25 22:56); .\.venv\Scripts\python.exe scripts/check_frontmatter.py 'novapolis-dev/docs/todo.agent-board.md' 'novapolis-dev/docs/todo.index.md' 'novapolis-dev/docs/donelog.md' 'novapolis_agent/README.md' 'novapolis_agent/docs/tts-model-track.md' 'novapolis_agent/docs/DONELOG.txt' PASS (EXITCODE=0, 2026-02-25 22:56)
---

TTS Model Track (Chronistin)
============================

Zweck
-----

- Dieses Dokument konkretisiert den offenen TTS-Model-Track aus dem Agent-Board.
- Fokus: Entscheidungsgrundlage und Umsetzungsleitplanken, keine Laufzeitimplementierung in diesem Schritt.

1) Daten- und Rechte-Policy
---------------------------

- Zulassung nur fuer Datensaetze mit nachvollziehbarer Herkunft, Lizenzstatus und Nutzungsfreigabe.
- Sprache zuerst `de` (Chronistin-Zielprofil); Mischdaten nur mit expliziter Kennzeichnung.
- Pflicht-Metadaten pro Paket: Quelle, Lizenztyp, Freigabestatus, Datum, verantwortliche Stelle.
- Harte Ausschluesse: ungeklaerte Rechte, TOS-gebundene Modelle ohne Nachweis, nicht-kommerzielle/no-derivatives Quellen fuer produktiven Pfad.
- Kopplung an bestehende Governance: deny-by-default-Ansatz analog zur Model-Allowlist.

2) Trainingsziel
----------------

- Zielbild kurzfristig: Finetune eines bestehenden offenen Basismodells (CLI-first), kein eigenes Foundation-Modell.
- Zielbild mittelfristig: optionaler Vergleich zweier Pfade
  - Pfad A: Finetune/Adapter-Strategie (LoRA) fuer schnelle Iteration,
  - Pfad B: erweitertes Modelltraining nur nach stabiler Daten-/Eval-Reife.
- Operationaler Default fuer naechste Iterationen: LoRA-basierter Finetune-Track mit reproduzierbaren Parametern.

3) Evaluationsmetriken
----------------------

- Gate-Metriken vor Training:
  - Datenqualitaet: Dupe-Rate, Mindestlaenge, Filterquote,
  - Strukturqualitaet: Pflichtfelder (`id`, `slug`, `tags`) und Validator-Status,
  - Policy-Status: Rechte/Freigabe dokumentiert.
- Gate-Metriken nach Training:
  - Aufgabenbezogene Pass-Rate auf definierten Eval-Suites,
  - Fehl-Cluster (Top fehlgeschlagene Check-Typen),
  - Stabilitaet ueber wiederholte Kurzlaeufe (kein Einmalluck).
- Akzeptanz nur bei dokumentierter Verbesserung ohne Verschlechterung kritischer Baselines.

4) Runtime-Adapter-Plan (hinter Schritt 7)
------------------------------------------

- Adapter-Reihenfolge:
  1. `dummy/null` (bereits vorhanden) als Testanker,
  2. ein produktiver Primäradapter (TTS-Synthese) fuer MVP,
  3. optionale Sekundaeradaper fuer Vergleich/Failover.
- Vertragsprinzip:
  - Einheitliche Provider-Schnittstelle bleibt stabil,
  - Runtime-Adapter duerfen API/Auth/Rate-Limit/Cache-Vertraege nicht umgehen,
  - Fehlerpfade werden kontrolliert und beobachtbar ausgegeben (kein Silent-Fail).

5) Umsetzungsgrenzen
--------------------

- CLI-first bleibt verbindlich fuer Trainings-/Build-Prozesse.
- UI/Tasking darf orchestrieren, aber nicht den kanonischen Ausfuehrungspfad ersetzen.
- Dieses Dokument ist eine Architekturkonkretisierung; Umsetzungspunkte bleiben im Agent-Board priorisiert.
