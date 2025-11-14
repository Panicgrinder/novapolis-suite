---
stand: 2025-11-14 16:24
update: Vorschlagsentwurf geprüft — Frontmatter-Timestamp synchronisiert (Docs Sweep); ready for PR. Checks: PASS (Receipt: `.tmp-results/reports/checks_report_20251114_162424.md`)
checks: PASS
---

Kurzbeschreibung
- Sammlung konkreter Verbesserungsvorschläge für `.github/copilot-instructions.md`.
- Nicht-bindend; dient der Review und späteren gezielten Minimal-Patches.

TL;DR-Blöcke (Einfüge-Vorschlag)
- Semantische Regeln: 5-Punkte TL;DR (Guard-Checks nur bei WRITE/RUN; STOP hat Vorrang; Timestamps immer frisch; Quellen nennen; Reihenfolge Lint→Typen→Tests).
- Modell-Profile: 1-Zeiler, wann General/Codex/Mini zu wählen ist + 3 Heuristik-Stichpunkte.
- Doku-Update: Kurzliste der Pflichtschritte (TODO/DONELOG, Frontmatter, Lint, Status-Artefakte).
- Prüfläufe: Ein Satz pro Wrapper-Skript, keine Inline -Command für Mehrschritte.

Dedup & Ordnung
- Doppelte Hinweise zu Markdownlint konsolidieren; Hauptregel (MD003) einmal zentral, Verweise kürzen.
- Frontmatter-Schutz einmal beschreiben; in Sektionen nur verlinken.
- "Priorität"-Abschnitt vereinheitlichen: Reihenfolge 1) Global (SSOT) 2) RP-spezifisch 3) Agent-spezifisch. Zahlen im Text klarstellen.

Reihenfolge der Kapitel (Vorschlag)
1. Dateipfad & Geltungsbereich
2. Primäre Behaviour-Quellen
3. Modell-Profile & Moduswechsel (kurz + Mapping-Tabelle)
4. Semantische Regeln (kuratiert)
5. STOP-Gates & Modi
6. Kanonische Prüfabläufe (pwsh)
7. Markdownlint (zentral) + Frontmatter-Policy (kompakt)
8. Definition of Done (Code & Docs)
9. Doku-Update
10. Security & Dependencies
11. Prüfrelease & Versionierung
12. Workspace-Instructions (kompakt) inkl. .tmp-results

Tool-Policy Kurzmatrix (skizziert)
- Allowed: Lesen (read_file/grep/fetch), Analyze-only.
- STOP+Guard-Check: apply_patch/create_file/delete, run_in_terminal mit -File, install deps.
- Wrapper-Pflicht: Mehrschritt-Build/Test/Coverage → `pwsh -File` Skripte.

Konkrete Textänderungen (Prosa-Minimaldiffs)
- Semantische Regeln A.1: "Guard-Check erforderlich VOR jeder Aktion, die Dateien verändert oder Skripte/Tests startet." Klarstellen: Lesende Operationen explizit ausnehmen.
- STOP-Gate: ersten Satz verkürzen, Signalsatz "Beidseitig (Code↔Redaktion)" beibehalten.
- Zeit/Timestamps: Alle Beispiele auf lokale Zeit „YYYY-MM-DD HH:mm“ belassen; Hinweis auf Get-Date belassen.

Offene Punkte für Review
- Prüfen, ob "R-SCAN Root-only" weiterhin passend oder optional auf rekursiv schaltbar ist (test-Flag?).
- Mapping-Tabelle erweitern: Logs/Reports-Analysen mit Mini profilieren.

Nächste Schritte (nach Review)
- Minimal-Patches an den betroffenen Abschnitten anwenden.
- TL;DR-Blöcke einfügen (1-3 Sätze je Abschnitt).
