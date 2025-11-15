---
stand: 2025-11-15 10:15
update: Erstanlage der Regelbeschreibung (STOP-Gate Hard/Soft).
checks: keine
state: active
---

Regel 001 – R-STOP
===================

Zweck
-----
Das STOP-Gate erzwingt vor sicherheits- oder modusrelevanten Aktionen eine explizite Bestätigung, um unbeabsichtigte oder riskante Ausführungen zu verhindern.

Definition
---------
- Klassen:
  - Hard-Trigger (Mutation/Sicherheit): Code-/Script-Änderungen, Validator-/Testläufe mit Seiteneffekten, Policy-/SSOT-Anpassungen.
  - Soft-Trigger (Mehrdeutigkeit/Konflikt): Unklare Quellen, widersprüchliche Regeln, Moduskonflikte, unspezifizierte Pfade.
- Gemeinsame Regeln: Für Code und Redaktion; triviale Gespräche ausgenommen. Hard hat Vorrang; RAW/noisy/staging Bereiche: nur Soft, solange keine Mutation.

Tat
---
- Vor Hard-Triggern explizite Bestätigung einholen; ohne Freigabe nicht ausführen.
- Bei Soft-Triggern kurz Optionen darstellen, Bestätigung einholen, erst dann fortfahren.
- Eine mutierende Aktion niemals ohne vorherige STOP-Gate-Bewertung starten.

Geltungsbereich
---------------
- Alle Code-/Script-Änderungen, Tests mit Seiteneffekt, Policy-/SSOT-Anpassungen, unklare/konfliktäre Situationen.

Beispiele
--------
### Korrekt
- „Bevor ich Tests mit Seiteneffekt starte, benötige ich Ihre Freigabe.“
- „Regelkonflikt erkannt (R-WRAP vs. R-WRAP-Ausnahme). Fortfahren?“

### Anti-Beispiel
- Ohne Rückfrage Dateien löschen oder Refactor mit breiter Wirkung beginnen.
- Bei unklaren Quellen eigenmächtig fortfahren.
