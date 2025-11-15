---
stand: 2025-11-15 10:15
update: Erstanlage Coverage-Gate.
checks: keine
state: active
---

Regel 330 – R-COV
==================

Zweck
-----
Mindesttestabdeckung gewährleisten.

Definition
---------
- Coverage-Gate: Mindest-Coverage ≥ 80 % vor Merge.

Tat
---
- Tests mit Coverage laufen lassen; unter 80 % nicht mergen.

Geltungsbereich
---------------
- Test-/CI-Pipelines des Projekts.

Beispiele
--------
### Korrekt
- Pytest mit Coverage-Report, Gate erfüllt.

### Anti-Beispiel
- Merge bei 60 % Coverage ohne Freigabe.
