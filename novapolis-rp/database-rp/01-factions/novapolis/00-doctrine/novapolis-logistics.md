---
stand: 2026-02-16 12:54
update: Maschinenlesbare Metadaten + Rollen/Transferregeln aus Bestandsdaten ergänzt; Checks PASS.
checks: "& .\\.venv\\Scripts\\python.exe scripts\\run_checks_and_report.py PASS (2026-02-16 12:54)"
category: canon
schemaVersion: 1
language: de
status: active
owners: [admin-novapolis]
tags: [rp, doctrine, logistik, inventar, novapolis]
relatedSlugs: [novapolis, novapolis-inventar, d5-inventar, c6-inventar, logistik, missionslog, c6-logistik-policy, c6, d5, pahl, nika-perez, kora-malenkov, jonas-merek]
slug: novapolis-logistics
version: "0.2"
last_updated: 2026-02-16T12:54:00+01:00
last_change: Rollen/Schnittstellen und Transferregeln (D5↔C6) konsolidiert.
---

Novapolis - Logistics
====================

Ziel
---

Ziel ist eine robuste, auditierbare Logistik: Bestände, Transfers und Ausgaben sind nachvollziehbar, und der Außenhandel bleibt strikt vom Kern (D5) getrennt.

Rollen & Schnittstellen (Bestandsdaten)
--------------------------------------

- **Quartiermeisterin (D5)**: Nika Perez – Ausgabe/Inventar/Protokolle, Priorisierung (Schnittstelle zu Ronja/Pahl).
- **Sicherheit/Freigaben (Novapolis)**: Pahl Brenner – operative Freigaben, Sicherheitslage, Einsatzkoordination.
- **Leitung C6 / Logistikknoten**: Kora Malenkov – Materialübergaben D5↔C6, Lieferfenster, Außenhandels-Übergaben.
- **Technik/Logistik (D5)**: Jonas Merek – Werkstatt, Funk, technische Abwicklung von Anforderungen.

Transferregeln D5 ↔ C6 (Kurz)
-----------------------------

- Transfers zwischen D5 und C6 laufen ausschließlich über Mission/Logistik und werden protokolliert.
- Außenhandelsgüter werden über C6 geführt; D5 bleibt nicht öffentlich zugänglich.
- Währungseinheiten (KUGELN neu/gebraucht) werden wie Inventar geführt; Abweichungen werden dokumentiert.

- Inventar (Fraktion): [Novapolis-inventar](../04-inventory/Novapolis-inventar.md)
- Inventar (D5): [D5-inventar](../04-inventory/D5-inventar.md)
- Inventar (C6): [C6-inventar](../04-inventory/C6-inventar.md)
- Handel/Diplomatie: [Relationslog-Novapolis](../06-handel-diplomatie/Relationslog-Novapolis.md)
- Admin-Logistik (Meta/Reference): [Logistik Novapolis](../../../00-admin/Logistik.md)

Stations-/Orts-Addenda
----------------------

- D5 (Location): [D5](../03-locations/D5.md)
- C6 (Location): [C6](../03-locations/C6.md)
- C6 (Policy): [C6 - Logistik-Policy](../03-locations/C6-Logistik-Policy.md)
