---
stand: 2025-11-16 00:19
update: Erstanlage Workspace-Scan-Policy.
checks: keine
state: active
---

Regel 110 – R-SCAN
===================

Zweck
-----
Begrenzung von Live-Scans zur Minimierung von Seiteneffekten und Rauschen.

Definition
---------
- R-SCAN: Workspace-Scan standardmäßig nur Root-Ebene (aktiv).
- Rekursiv nur für Artefakt-Erzeugung (Snapshots) zulässig.

Tat
---
- Live-Scans am Root begrenzen; Rekursion nur, wenn explizit als Artefaktlauf vorgesehen.

Geltungsbereich
---------------
- Workspace-Scans und zugehörige Tools.

Beispiele
--------
### Korrekt
- Root-only Scan für Statusaufnahme.

### Anti-Beispiel
- Unkoordinierter, rekursiver Live-Scan des gesamten Repos.
