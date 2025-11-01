---
stand: 2025-11-01 09:44
update: YAML-Frontmatter eingeführt (Snapshot-Regel) – Kopf migriert.
checks: keine
---

<!-- markdownlint-disable MD013 -->
# Novapolis Agent – ToDo & Roadmap

Kurzfristige Ziele (Heute)

- [x] Eval-Profile festziehen
  - Ziel: Reproduzierbare Läufe via `eval/config/profiles.json` (quiet default, temp, optionale Checks).
  - Status: Done (UI lädt Profile; Meta-Header vollständig; kurzer ASGI-Lauf konsistent).
- [x] Eval-UI: Profile-/Quiet-/ASGI-/Skip-Preflight-Integration
  - Ziel: Läufe steuerbar über Profile, reduzierte Logs, In-Process-ASGI, Preflight optional.
  - Status: Done (Menü integriert, Flags wirksam, Trends/Exports ok).
- [x] Synonym-Overlay (privat) einführen und mergen
  - Ziel: `eval/config/synonyms.local.json` (gitignored) automatisch mit `synonyms.json` mergen.
  - Status: Done (Loader-Merge, Sample-Datei, Doku in README & eval/README, .gitignore ergänzt).
- [x] Eval-Pfade harmonisieren & Meta-Header erweitern
  - Ziel: Nutzung von `eval/datasets|results|config`, Meta mit overrides (model/host/temperature).
  - Status: Done (Runner/UI angepasst, Ergebnisse validiert).
stand: 2025-11-01 17:55
update: Redirect-Stub – bitte `novapolis-dev/docs/todo.agent.md` verwenden (SSOT)
checks: keine
<!-- Redirect-Stub: Bitte diese Datei nicht mehr pflegen. Die Single Source of Truth liegt unter: -->
## Weiterleitung

- SSOT: `../../novapolis-dev/docs/todo.agent.md`
- Bitte Änderungen ausschließlich dort vornehmen.
