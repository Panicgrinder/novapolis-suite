---
stand: 2025-11-16 00:19
update: Erstanlage Kontextquellen-Regel.
checks: keine
state: active
---

Regel 020 – R-CTX
=================

Zweck
-----
Sicherstellen, dass vor jeder Aktion die maßgeblichen Steuer-/Kontextdateien geladen und referenziert werden.

Definition
---------
- Kontextquelle (R-CTX): Relevante Steuerdateien (mind. `.github/copilot-instructions.md` und betroffene Arbeitsdateien) sind vor Aktionen zu laden und im Kontext zu referenzieren.

Tat
---
- Vor Mutationen die Governance lesen und die konkret betroffenen Dateien nennen/verlinken.
- In Receipts die Quellenpfade absolut aufführen.

Geltungsbereich
---------------
- Alle agentischen Aktionen mit Bezug zur Projektgovernance oder zu betroffenen Dateien.

Beispiele
--------
### Korrekt
- „Quellen: F:\\VS Code Workspace\\Main\\.github\\copilot-instructions.md; ...“

### Anti-Beispiel
- Änderungen ohne Referenz auf die Governance oder betroffene Dateien.
