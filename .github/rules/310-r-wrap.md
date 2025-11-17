---
stand: 2025-11-16 06:52
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
- Mehrschritt-Prozesse ausschließlich über Skript-Wrapper (z. B. `python <skript.py>`).
- Inline `-Command` nur für echte Einzeiler (max. ein Prozessaufruf, höchstens eine Pipe).

Tat
---
- Bei mehrschrittigen Tasks Skript anlegen/nutzen; keine langen Inline-Kommandos.

Geltungsbereich
---------------
- Lint/Typen/Tests/Coverage, Build/CI, Artefakt-Erzeugung.

Beispiele
--------
### Korrekt
- `python scripts/run_checks_and_report.py`

### Anti-Beispiel
- Verschachtelte, mehrzeilige `-Command`-Blöcke mit mehreren Schritten.
