---
title: "Novapolis Agent - ToDo & Roadmap (SSOT)"
date: 2025-11-12 08:59
tags: [doc]
stand: 2025-11-16 06:52
update: Frontmatter auf Governance-Format umgestellt.
checks: keine
---
<!-- markdownlint-disable MD012 MD022 MD041 -->
Novapolis Agent - ToDo & Roadmap (SSOT)
---------------------------------------

Hinweis
------
- Dies ist die zentrale ToDo-Datei (Single Source of Truth) für das Agent-Modul.
- Bestehende Inhalte werden schrittweise aus `novapolis_agent/docs/TODO.md` hierher migriert.
- Bis zur vollständigen Migration verweist die alte Datei als Redirect-Stub auf diese Seite.

Platzhalter
 - [ ] Abgleich mit Root Coverage-Gate (R-COV) und Aufnahme fehlender Prüfsteps (Receipt-Formate) in diesen Plan

Neue Aufgaben - TTS & Tools (2025-11-01 22:24)
----------------------------------------------

- [ ] Coqui-Exporter (Build-Time, Planung): Script `scripts/tts_coqui_export.py` (Text→WAV→OGG, Hash-Cache, Voice-Mapping), Zielordner `novapolis-sim/assets/voiceovers/de/`.
- [ ] Mini-Service (Runtime, Planung): FastAPI-Wrapper (Text→WAV/OGG), simple Auth/Rate-Limit, lokaler Cache; nur Schnittstelle/Mappings definieren.
- [ ] VS Code Tasks (Planung): „TTS: export (coqui)“, „TTS: clean cache“, „TTS: check voices“. Umsetzung erst nach Spec-Freigabe.
- [ ] Templates bereitstellen: Beispiel-YAML für `knowledge:`/`actions:` in Agent-README verlinken (Quelle: Dev-Annotation-Spec).

Archivierte Blöcke (Agent)
--------------------------
- Kurzfristige Ziele (Heute) - archiviert am 2025-11-01 19:16 → `novapolis-dev/archive/todo.agent.archive.md`




