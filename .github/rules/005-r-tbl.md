---
stand: 2025-11-16 00:19
update: Neue Grundregel zur Tabellenstruktur angelegt.
checks: keine
state: active
---

Regel 005 – R-TBL
==================

Zweck
-----
Einheitliche, maschinenfreundliche Tabellenstruktur im gesamten Regelkatalog sicherstellen.

Definition
---------
- Jede Tabelle innerhalb des Regelkatalogs muss dieselbe Struktur einhalten.
- Die erste Spalte ist immer „Status“.
- Es ist nicht erlaubt, eine Regel-ID, eine Tat oder eine Checkliste als Tabellenüberschrift zu verwenden.
- Überschriften benennen Abschnitte, niemals Regeln.

Tat
---
- Tabellen grundsätzlich mit der Spalte „Status“ als erster Spalte anlegen.
- Abschnittsüberschriften neutral benennen (keine Regel-IDs, keine Taten, keine „Checkliste“ als Titel einer Regel-Tabelle).

Geltungsbereich
---------------
- Alle Tabellen im Regelkatalog, insbesondere im Patch-Dokument und den referenzierten Übersichtstabellen.

Beispiele
--------
### Korrekt
- Überschrift: „STOP-Gates“; Tabelle: erste Spalte „Status“, danach inhaltliche Spalten.
- Überschrift: „Checkliste für Doku-Update-Prozess“; Tabelle mit „Status“ als erster Spalte.

### Anti-Beispiel
- Überschrift direkt als Regel-ID (z. B. „R-STOP“), oder als Tat/Checkliste.
- Tabelle ohne „Status“-Spalte.
