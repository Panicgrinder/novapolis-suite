---
last-updated: 2025-10-27T19:20:00+01:00
---

# Scenes – Konventionen

Empfohlene Front-Matter zur Validierung und Cross-Refs:

- id: eindeutige Szenen-ID (frei wählbar)
- characters: Liste der referenzierten Charakterdateien (Basename ohne .md), z. B. "Jonas-Merek"
- locations: Liste der referenzierten Location-Dateien (Basename), z. B. "Verbindungstunnel-D5-C6"
- inventoryRefs: Liste der Inventar-Referenzen (Basename), z. B. "Novapolis-inventar"

Beispiel:

---
id: scene-2025-10-27-a
characters: ["Jonas-Merek", "Ronja-Kerschner"]
locations: ["Verbindungstunnel-D5-C6"]
inventoryRefs: ["Novapolis-inventar"]
---

H1-Überschrift ist Pflicht (wird geprüft). Inhalt frei.

## Co-Occurrence (Bezugspaare)

Folgende Paare müssen in Szenen gemeinsam auftreten (wird validiert):

- Ronja-Kerschner → Reflex
- Jonas-Merek → Lumen
- Kora-Malenkov → Echo

Wenn eine Szene einen der linken Einträge enthält, muss der rechte ebenfalls in `characters` stehen.