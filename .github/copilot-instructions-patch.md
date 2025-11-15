LLM-Dokumentenheader (nicht löschen)
====================================
- Type: Copilot Instruction Set / Project Governance
- Scope: Novapolis-Suite (VS Code Workspace Main)
- Language: Deutsch
- Encoding: UTF-8 / Unix-EOL
- stand: 2025-11-15 23:48
- update: Status-Spalten in Tabellen 2/3 ergänzt; Überschrift Tabelle 3 neutralisiert; neue Grundregel 005 R-TBL hinzugefügt.
- checks: keine

ACHTUNG — REGEL 1 (Status-Filter)
---------------------------------
- Werte IMMER zuerst die erste Spalte „Status“ aus.
- Verarbeite ausschließlich Zeilen mit Status=active (oder ausdrücklich vom Benutzer aktivierte experimentelle Regeln).
- Lies die restlichen Spalten einer Zeile NICHT, wenn der Status nicht aktiv ist.

TL;DR Struktur
--------------
- Hauptregel-Tabelle: maschinenfreundlich (Status → Nummer → ID → Zweck → Kategorie → Tat → Geltungsbereich → Detail-Ref).
- STOP-Gates: separate Tabelle der Trigger mit konkreter „Tat“ und Geltungsbereich.
- Doku-Update=true: Checkliste konkreter Pflichten, jeweils mit Detail-Ref zur Regeldatei.

Hauptregel-Tabelle
------------------

| Status | Regel-Nr | Regel-ID | Kurzname/Zweck | Kategorie | Tat | Geltungsbereich | Detail-Ref |
| --- | ---: | --- | --- | --- | --- | --- | --- |
| active | 001 | R-STOP | STOP-Gate Vorrang | Fundament | Vor kritischen Aktionen explizite Bestätigung einholen; ohne Freigabe nicht ausführen | Code-/Skriptänderungen, Tests mit Seiteneffekt, Policy/SSOT-Anpassungen | .github/rules/001-r-stop.md#tat |
| active | 005 | R-TBL | Konsistente Tabellenstruktur | Fundament | Alle Regel-Tabellen haben dieselbe Struktur; erste Spalte ist "Status"; keine Regel-ID/Tat/Checkliste als Tabellenüberschrift; Überschriften benennen Abschnitte | Regelkatalog-Tabellen (Patch-Dokument, Referenztabellen) | .github/rules/005-r-tbl.md#tat |
| active | 010 | R-FM | Frontmatter-Policy | Fundament | YAML-Frontmatter (stand, update, checks) in allen MD-Dokumenten (außer Governance); Delimiter nie ändern | Docs (Markdown) | .github/rules/010-r-fm.md#tat |
| active | 020 | R-CTX | Kontextquelle laden | Fundament | Relevante Steuerdateien (.github/copilot-instructions.md etc.) vor Aktion laden/referenzieren | Alle agentischen Aktionen | .github/rules/020-r-ctx.md#tat |
| active | 030 | R-DOKU | Doku-Update-Pflicht (true) | Fundament | Nach relevanten Änderungen TODO/DONELOG/Status/Frontmatter/Index/Lint aktualisieren | Alle relevanten Änderungen | .github/rules/030-r-doku.md#tat |
| active | 050 | R-TIME | Timestamp-Konvention | Fundament | Zeitformat YYYY-MM-DD HH:mm, pro Ereignis neu via Get-Date (lokal) | Frontmatter, Postflight, Status | .github/rules/050-r-time.md#tat |
| active | 110 | R-SCAN | Workspace-Scan-Policy | Workspace | Root-only Live-Scan; rekursiv nur für Artefakte/Snapshots | Workspace-Scans | .github/rules/110-r-scan.md#tat |
| active | 200 | R-COMM | Kommunikationsstil | Interaktion | Prägnant, deutsch, kurze Sätze, klare Next Steps; keine Fülltexte | Antworten/Protokolle | .github/rules/200-r-comm.md#tat |
| active | 310 | R-WRAP | Wrapper-Policy | Qualität/Execution | Mehrschrittprozesse nur via "pwsh -File"; Inline "-Command" nur echte Einzeiler | Skript-/Taskausführung | .github/rules/310-r-wrap.md#tat |
| active | 320 | R-LINT | Markdownlint-Policy | Lint | MD001–MD050 einhalten; MD003 Setext für H1/H2; Lints via npx markdownlint-cli2 | Dokumentation | .github/rules/320-r-lint.md#tat |
| active | 330 | R-COV | Coverage-Gate | Tests | Coverage ≥ 80 % vor Merge (Pytest) | Tests/CI | .github/rules/330-r-cov.md#tat |
| active | 340 | R-LOG | Receipt-Pflicht (Postflight) | Qualität/Logging | Nach jeder Mutation genau ein Postflight-Receipt inkl. Felder/Checks | Alle Mutationen | .github/rules/340-r-log.md#tat |
| active | 400 | R-SEC | Sicherheitsprinzip | Sicherheit | Keine destruktiven Änderungen ohne WhatIf; minimalinvasiv; keine Auto-Löschungen | Datei-/Repo-Operationen | .github/rules/400-r-sec.md#tat |
| active | 410 | R-SAFE | Minimaländerungen | Sicherheit/Qualität | Nur kleinste nötige Diffs; keine unbeteiligten Änderungen | Patches/Refactors | .github/rules/410-r-safe.md#tat |
| active | 510 | R-IDX | Headings-Index-Pflege | Meta | Überschriftenindex bei Strukturänderungen pflegen | Governance-/Indexdateien | .github/rules/510-r-idx.md#tat |
| experimental | 520 | R-TODO | TODO/DONELOG-Konsistenz & Propagation | Meta | Formate einhalten; automatische Propagation derzeit optional (test) | TODOs/DONELOGs | .github/rules/520-r-todo.md#tat |
| active | 530 | R-RED | Redundanz-Handling | Meta | Duplikate nur nach Freigabe entfernen; vorher melden | Doku/Code | .github/rules/530-r-red.md#tat |

STOP-Gates
----------
 
| Status | Trigger | Hard/Soft | Tat | Geltungsbereich | Detail-Ref |
| --- | --- | --- | --- | --- | --- |
| active | Code-/Script-Änderungen, Validator-/Testläufe mit Seiteneffekten, Policy-/SSOT-Anpassungen | Hard | STOP vor Ausführung, explizite Bestätigung einholen; ohne Freigabe keine Aktion | Code & Dokumentation | .github/rules/001-r-stop.md#definition |
| active | Unklare Quellen, widersprüchliche Regeln, Moduskonflikte, unspezifizierte Pfade | Soft | Kurzstatus + Optionen; Bestätigung vor Fortsetzung | Code & Dokumentation | .github/rules/001-r-stop.md#definition |

Checkliste für Doku-Update-Prozess
----------------------------------
 
| Status | Tat | Detail-Ref |
| --- | --- | --- |
| active | TODOs aktualisieren (Root/Module), erledigte abhaken, neue Nacharbeiten erfassen | .github/rules/030-r-doku.md#tat |
| active | DONELOG ergänzen (Wer/Was/Wann/Kontext), Pfade/Module referenzieren | .github/rules/030-r-doku.md#tat |
| active | READMEs/Indexseiten synchronisieren (Links/Anker/Zählungen) | .github/rules/030-r-doku.md#tat |
| active | Frontmatter pflegen (stand/update/checks), Delimiter unverändert lassen | .github/rules/030-r-doku.md#tat |
| active | Lint/Validator laufen lassen und Ergebnis notieren (markdownlint, Frontmatter-Validator) | .github/rules/030-r-doku.md#tat |
| active | Strukturänderungen dokumentieren (workspace_tree_*.txt, WORKSPACE_STATUS.md) | .github/rules/030-r-doku.md#tat |
