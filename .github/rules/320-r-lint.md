---
stand: 2025-11-16 00:19
update: Erstanlage Markdownlint-Policy.
checks: keine
state: active
---

Regel 320 – R-LINT
===================

Zweck
-----
Einheitliche Dokumentationsqualität sicherstellen.

Definition
---------
- MD001–MD050 einhalten; insbesondere MD003: H1/H2 im Setext-Stil, H3+ als ATX.
- Ausführung: `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md'` (ohne pwsh -Command-Hülle).

Tat
---
- Vor Doku-Sessions Lint ausführen, bei Befunden konservativ korrigieren (keine Delimiter-Verstöße).

Geltungsbereich
---------------
- Alle Markdown-Dokumente gemäß Konfiguration/Skip-Pfade.

Beispiele
--------
### Korrekt
- H1/H2 Setext, H3 `###` ATX.

### Anti-Beispiel
- Gemischte Stilformen für dasselbe Heading-Level in einer Datei.
