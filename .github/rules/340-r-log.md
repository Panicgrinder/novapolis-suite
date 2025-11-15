---
stand: 2025-11-15 10:15
update: Erstanlage Receipt-/Postflight-Pflicht.
checks: keine
state: active
---

Regel 340 – R-LOG
==================

Zweck
-----
Vollständige, nachvollziehbare Dokumentation jeder Mutation.

Definition
---------
- Nach jeder Dateiänderung oder Skript-/Testausführung genau EIN Postflight-Block.
- Enthält Meta (Modus, Modell, Pfade, Versionen), Prüfzusammenfassung, Regel-IDs, Todos/Zeitpunkte, Ende-Timestamp.

Tat
---
- Postflight am Ende der Nachricht anfügen; keine Zwischen-Postflights.

Geltungsbereich
---------------
- Alle mutierenden Aktionen.

Beispiele
--------
### Korrekt
- Ein Postflight mit klaren Feldern und Abschluss-Zeit.

### Anti-Beispiel
- Mehrere Postflights für Teilaktionen oder ganz ohne Receipt.
