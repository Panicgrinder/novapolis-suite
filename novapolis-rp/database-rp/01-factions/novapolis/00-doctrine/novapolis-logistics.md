---
stand: 2026-02-21 22:11
update: Novapolis-Wochenzyklus, Lagerstands-Review und Tagesreport-Template ergänzt (ohne unbelegte Kennzahlen).
checks: ausstehend (nach Mutation neu ausführen)
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

Operativstand (Novapolis, belegt)
---------------------------------

Generatoren (Stationskontext)
-----------------------------

- D5-Reaktor: Status 100%, lädt Zellen.
- C6-Energieanlage: Standortstatus „Reaktor stabilisiert“ belegt; keine belastbaren Leistungs-/Instandsetzungskennzahlen dokumentiert.

Leitungen/Schaltzustände (Stationskontext)
------------------------------------------

- D5↔C6: begehbar im Reparaturbetrieb (Nordlinie); keine Vollinstandsetzung behaupten.
- Infrastruktur bleibt limitierend; Verfügbarkeit/Leistung nur mit belegter Quelle konkretisieren.

T+0 Constraints (Novapolis-Szenen)
----------------------------------

- Keine Tunnel-Instandsetzung behaupten, bis ein belegter Schritt vorliegt (u. a. [scene-2025-10-27-j](../../../06-scenes/scene-2025-10-27-j.md), [scene-2025-10-27-k](../../../06-scenes/scene-2025-10-27-k.md), [scene-2025-10-27-m](../../../06-scenes/scene-2025-10-27-m.md)).
- C6-Zustand nicht beschönigen; C6 bleibt „leer/unrepariert“, solange nichts anderes belegt ist (siehe [scene-2025-10-27-m](../../../06-scenes/scene-2025-10-27-m.md)).
- Inventar-Änderungen nur nach belegten Einträgen nachziehen (z. B. [scene-2025-10-27-l](../../../06-scenes/scene-2025-10-27-l.md)).

C6-Faktenstand (belegt, ohne Mengen)
------------------------------------

- Verbucht im C6-Kontext: Filter, Energiezellen, Werkzeuge.
- Kritisch offen im C6-Kontext: Adapter/Fittings DN60, Schweißausrüstung.
- Sonderfunde C6: Artefakt 7A markiert; Datenkern (tragbar) am Fundort belassen (nicht aufgenommen).

Wochenzyklus (Novapolis)
------------------------

- Rhythmus: täglicher Kurzabschluss (D5/C6) und wöchentliche Konsolidierung durch Leitung Logistik + Sicherheit.
- Wochenabschluss enthält mindestens:
  - Lagerstand D5/C6 (ohne erfundene Mengen)
  - offene kritische Bedarfe (z. B. Adapter/Fittings DN60, Schweißausrüstung)
  - Transfer-/Missionsdelta mit Quellenverweisen

Tagesreport (Template)
----------------------

- Datum/Marker:
- D5-Status (kurz):
- C6-Status (kurz):
- Transfers (Quelle→Ziel, mit Beleg):
- Offene Risiken/Blocker:
- Folgeaktion bis nächster Zyklus:
