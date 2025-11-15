---
stand: 2025-11-15 10:15
update: Erstanlage Wrapper-Policy.
checks: keine
state: active
---

Regel 310 – R-WRAP
===================

Zweck
-----
Sichere, reproduzierbare Ausführung komplexer Abläufe mittels Skript-Wrapper.

Definition
---------
- Mehrschritt-Prozesse ausschließlich über „pwsh -File <skript.ps1>“.
- Inline „-Command“ nur für echte Einzeiler (max. ein Prozessaufruf, höchstens eine Pipe).

Tat
---
- Bei mehrschrittigen Tasks Skript anlegen/nutzen; keine langen Inline-Kommandos.

Geltungsbereich
---------------
- Lint/Typen/Tests/Coverage, Build/CI, Artefakt-Erzeugung.

Beispiele
--------
### Korrekt
- `pwsh -File scripts\\run_checks_and_report.ps1`

### Anti-Beispiel
- Verschachtelte, mehrzeilige `-Command`-Blöcke mit mehreren Schritten.
