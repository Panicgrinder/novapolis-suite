---
stand: 2025-11-08 23:20
update: Überschriftenliste aktualisiert; Vorschläge für neue Regel-IDs ergänzt
checks: keine
---

Hinweis: Diese Datei ist eine Extrakt‑Referenz. Sie enthält die aus
`.github/copilot-instructions.md` extrahierten Überschriften und ist
selbst unter dem Pfad `.github/copilot-instructions-headings.md` im
Repository abzulegen.

Aktuelle Überschriften (Extrakt)
================================

Hinweis: Extraktion basiert auf Stand `Timestamp: 2025-11-08 23:02` der Datei `.github/copilot-instructions.md`.

- LLM-Dokumentenheader (nicht löschen)
- Kurzreferenz aller Überschriften dieser Anleitung
- Dateipfad & Geltungsbereich
- Primäre Behaviour-Quellen
- Gemeinsamer Arbeitsstil
- Onboarding & Setup
- Cheat Sheet (pwsh‑Kommandos)
- Kanonische Prüfabläufe (pwsh)
- Workspace‑Tree‑Artefakte (Zuordnung)
- YAML-Frontmatter (kompakt & LLM-freundlich)
- Frontmatter‑Schutz (true)(robust gegen Delimiter‑Verlust)
- Dateiformat & EOL
- Definition of Done (Code & Docs)
- Security & Dependencies
- Meta- / Systeminfo-Protokollierung (Preflight & Postflight, kompakt)
- Semantische Regeln
- Kompakter Meta-Block für normale Antworten
- Definition der Regel-IDs (zur Verwendung im Feld „Regeln: IDs=…“)
- STOP-Gates & Modi
- Essentials (konzentriert)
- Repositoryweiter Rahmen
- Prüf- und Release-Checks
- Release & Versionierung
- Novapolis Agent (Backend)
- Novapolis-RP
- Workspace-Instructions (kompakt)
- Diagnose‑Playbook bei Lint‑FAIL (pwsh, konservativ)
- Mirrors/Redirect‑Stubs
- Export/Importer
- Ziele

Abgeleitete neue Regel-ID Vorschläge (nicht bindend)
---------------------------------------------------
- ID R-COV: Coverage-Gate (Mindest-Coverage ≥80% vor Merge durchsetzen)
- ID R-IDX: Headings-Index-Pflege (Aktualisierung bei strukturrelevanten Änderungen)
- ID R-COMM: Kommunikationsstil (prägnant, deutsch, keine Füllphrasen)
- ID R-RED: Redundanz-Handling (Duplikate nur mit Freigabe entfernen, vorher melden)
- ID R-TODO: Konsistenz von TODO/DONELOG-Einträgen (Format, Pflichtfelder)
- ID R-TIME: Timestamp-Konvention (lokales Format yyyy-MM-dd HH:mm; Quelle pwsh Get-Date)
- ID R-SAFE: Minimaländerungen ohne semantischen Eingriff (nur Orthografie/Lint, wenn eingeschränkt erlaubt)

(Ende des Extrakts)
