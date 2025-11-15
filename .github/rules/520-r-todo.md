---
stand: 2025-11-16 00:19
update: Erstanlage TODO/DONELOG-Konsistenz (Propagation test).
checks: keine
state: experimental
---

Regel 520 – R-TODO
===================

Zweck
-----
Konsistente Pflege von TODO/DONELOG-Einträgen; automatische Propagation ist derzeit im Teststatus.

Definition
---------
- Formate und Pflichtfelder in TODO/DONELOG einhalten.
- Automatische Übernahme neu erkannter TODOs (Propagation) ist optional (test), bis zur Aktivierung nur dokumentieren.

Tat
---
- TODO/DONELOG strukturiert pflegen; Propagation nur nach expliziter Freigabe.

Geltungsbereich
---------------
- Root- und modulare TODO/DONELOG-Dateien.

Beispiele
--------
### Korrekt
- Neues TODO im Root erfassen, Format einhalten.

### Anti-Beispiel
- Freie Textnotizen ohne Pflichtfelder; ungeprüfte automatische Propagation.
