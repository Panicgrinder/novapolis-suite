---
stand: 2025-11-07 07:54
update: Abgeschlossen; ins Archiv verschoben.
checks: keine
refs: .github/copilot-instructions.md, scripts/check_frontmatter.py
affected: .github/copilot-instructions.md
archived_at: 2025-11-07 07:51
---

Copilot-Instructions Erweiterungs-ToDos (Archiv)
================================================

Kurzfassung: Ergänzungen zur Zentraldatei `.github/copilot-instructions.md`, um erkannte Lücken (Scope, Gates, Setup, Governance) zu schließen.

Offene Punkte (geplant)
-----------------------
1. [x] Geltungsbereich präzisieren
   - Umsetzung: Abschnitt „Dateipfad & Geltungsbereich“ ergänzt (2025-11-07 06:50), deckt Chat, Inline, Apply-Patch und Agent-Funktionen ab.
2. [x] Kanonischer Pfad klarstellen
   - Umsetzung: Selber Abschnitt nennt `.github/copilot-instructions.md` explizit als einzig gültigen Speicherort.
3. [x] Zeitstempel- & TZ-Policy
   - Umsetzung: Abschnitt „Update-Logistik“ legt Format `YYYY-MM-DD HH:mm` fest, beschreibt lokale Standardzeit + UTC-Option (`ToUniversalTime()`); Validator-Anpassung bei `Z` bleibt als separater Folgepunkt offen.
4. [x] Validator Skip-Pfade dokumentieren
   - Umsetzung: Frontmatter-Schutz-Abschnitt listet Skip-Pfade vollständig.
5. [x] Line-Endings / BOM / Final-Newline
   - Umsetzung: Neuer Abschnitt „Dateiformat & EOL“ deckt BOM, Abschluss-Newline und LF/Git-Hinweis ab.
6. [x] Markdownlint-Overrides
   - Umsetzung: Zentraler Markdownlint-Abschnitt nennt `.markdownlint-cli2.jsonc` als einzige Quelle und verweist auf Review-Pflicht.
7. [x] CI/Gate-Charakter
   - Umsetzung: Frontmatter-Schutz-Abschnitt markiert Validator als hartes Gate (Pre-Commit & CI).
8. [x] Coverage-Policy
   - Umsetzung: Abschnitt „Prüf- und Release-Checks“ ergänzt Coverage-Gate ≥80 % (Task `Tests: coverage (fail-under)`).
9. [ ] Neue VS Code Tasks (übertragen)
   - Offene Umsetzung als Root-Aufgabe in `single-root-todo.md` nachgeführt; diese Liste ist damit vollständig dokumentiert.
10. [x] Onboarding/Setup
    - Umsetzung: Abschnitt „Onboarding & Setup“ beschreibt Venv, Requirements und erste Checks.
11. [x] Definition of Done (DoD)
    - Umsetzung: Neuer DoD-Abschnitt für Code & Docs ergänzt.
12. [x] Security / Dependencies
    - Umsetzung: Abschnitt „Security & Dependencies“ aufgenommen (monatliches `pip-audit`, Pinning, Secrets).
13. [x] Release / Versionierung
    - Umsetzung: Abschnitt „Release & Versionierung“ eingefügt (Version-Flow, DONELOG, Gates).
14. [x] Klarere Priorisierung mehrfacher Behavior-Dokumente
    - Umsetzung: Liste unter „Primäre Behaviour-Quellen“ priorisiert global → RP → Agent.
15. [x] Frontmatter-Migrationsstatus
    - Umsetzung: Hinweis im Frontmatter-Abschnitt verweist auf dieses ToDo-Dokument als Fortschrittsquelle.

Annahmen / Noch zu klären
-------------------------
- Zeitzonenentscheidung (lokal vs. UTC) - Entscheidung offen.
- Ob `Z` Suffix in Validator integriert werden soll.
- Aggregat-Task Namenskonvention (`Checks: full` vs. `Checks: all`).

Abschlussnotiz
--------------
- Primäre Ergänzungen an `.github/copilot-instructions.md` sind umgesetzt.
- Offene Restarbeit (VS-Code-Tasks) befindet sich jetzt im Root-Tracker `single-root-todo.md` und wird dort weiterverfolgt.
- Dieses Dokument gilt damit als abgeschlossen und bleibt als Nachweis der durchgeführten Anpassungen bestehen.

Langfristig (optional)
----------------------
- CI erweitern (Matrix nach Python-Versionen), Security-Scan-Step in CI.
- Optionaler Auto-Lint-Fix im Pre-Commit (separater Hook, bewusst opt-in).
- Flaky-Test-Tracking (Liste/Marker, regelmäßige Review).
- Logging-/Observability-Policy (PII-Redaktion, Rotationsintervalle, sensible Felder ausschließen).
- Shared-Package-Migration/De-Dup-Checkliste für `packages/novapolis_common` (Risiko: Doppelpfade).
- Alle Punkte kurz und prägnant; kein überfrachteter Abschnitt.
- Keine Änderung an bestehenden funktionalen Codepfaden.
- Keine widersprüchliche Terminologie.

(Ende)

