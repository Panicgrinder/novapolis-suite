---
stand: 2025-11-16 06:52
update: Erstanlage Sicherheitsprinzip.
checks: keine
state: active
---

Regel 400 – R-SEC
==================

Zweck
-----
Risikominimierung bei Änderungen und Abläufen.

Definition
---------
- Keine destruktiven Änderungen ohne vorherige WhatIf-Phase.
- Minimalinvasive Diffs, keine automatischen Löschungen außerhalb klarer Skriptkontexte.

Tat
---
- Vor potenziell destruktiven Schritten WhatIf/Cleanup-Strategie prüfen; Löschungen nur kontrolliert.

Geltungsbereich
---------------
- Datei-/Repo-Operationen, automatisierte Aufräumprozesse.

Beispiele
--------
### Korrekt
- WhatIf-Plan dokumentiert, danach gezielter Cleanup.

### Anti-Beispiel
- Breite, automatische Löschläufe ohne Absicherung.
