---
stand: 2025-11-15 10:15
update: Erstanlage Timestamp-Konvention.
checks: keine
state: active
---

Regel 050 – R-TIME
===================

Zweck
-----
Einheitliche, lokale Zeitstempel sichern Reproduzierbarkeit und Nachverfolgbarkeit.

Definition
---------
- Zeitformat: `YYYY-MM-DD HH:mm` (lokale Zeit, Europe/Berlin in der Governance beschrieben).
- Pro Ereignis frisch via Systemzeit (PowerShell `Get-Date`) ermitteln; kein Reuse.

Tat
---
- Frontmatter `stand` und Postflight-Zeitstempel stets frisch setzen.

Geltungsbereich
---------------
- Frontmatter, Postflight-Blocks, Statusnotizen, Logs.

Beispiele
--------
### Korrekt
- `stand: 2025-11-15 10:15`

### Anti-Beispiel
- Veraltete oder wiederverwendete Zeitstempel.
