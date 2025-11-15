---
stand: 2025-11-16 00:19
update: Erstanlage Minimaländerungs-Prinzip.
checks: keine
state: active
---

Regel 410 – R-SAFE
===================

Zweck
-----
Nur das Nötige ändern, alles andere unberührt lassen.

Definition
---------
- Minimaler Diff; keine unbeteiligten Umformatierungen/Umbenennungen.

Tat
---
- Patches auf das Problem fokussieren; Stil/Struktur unverändert lassen, sofern nicht nötig.

Geltungsbereich
---------------
- Alle Code-/Dokupatches.

Beispiele
--------
### Korrekt
- Nur die fehlerhafte Funktion korrigieren.

### Anti-Beispiel
- Komplettes File reformatten, obwohl nur eine Zeile betroffen ist.
