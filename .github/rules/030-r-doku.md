---
stand: 2025-11-15 10:15
update: Erstanlage Doku-Update-Pflicht (true).
checks: keine
state: active
---

Regel 030 – R-DOKU
===================

Zweck
-----
Alle relevanten Arbeitsdokumente nach wirksamen Änderungen synchron halten.

Definition
---------
- Doku-Update (true): Pflichtschritte nach relevanten Änderungen.
  - TODOs aktualisieren (Root/Module), erledigte abhaken, neue Nacharbeiten erfassen.
  - DONELOG ergänzen (Wer/Was/Wann/Kontext).
  - READMEs/Indexseiten synchronisieren (Links/Anker/Zählungen).
  - Frontmatter pflegen (`stand/update/checks`), Delimiter unverändert lassen.
  - Lint/Validator laufen lassen und Ergebnis notieren.
  - Strukturänderungen dokumentieren (workspace_tree_*.txt, WORKSPACE_STATUS.md).

Tat
---
- Nach jeder relevanten Änderung alle obigen Punkte abarbeiten und kurz protokollieren.

Geltungsbereich
---------------
- Alle Änderungen mit dokumentarischer/strukturierter Wirkung (Code, Skripte, Workflows, Doku).

Beispiele
--------
### Korrekt
- Nach Patch: DONELOG-Eintrag, Index aktualisiert, Frontmatter mit frischem `stand`, markdownlint ausgeführt/ergebnis notiert.

### Anti-Beispiel
- Feature geändert, aber TODO/DONELOG/Index/Frontmatter/Lint ignoriert.
