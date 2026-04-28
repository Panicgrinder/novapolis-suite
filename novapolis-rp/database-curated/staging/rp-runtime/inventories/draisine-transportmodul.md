---
stand: 2026-04-29 00:47
update: Das Draisine-Transportmodul fuehrt jetzt einen eigenen Runtime-Inventartraeger mit getrennter Lesart fuer gebundenen Prototypbestand, Verbrauchsrahmen und vom Tunnelbedarf getrennte offene Fehlstellen.
checks: snapshot-lock PASS (2026-04-28 22:39)
---

Runtime Inventory - Draisine-Transportmodul
==========================================

Status
------

- slug: draisine-transportmodul
- holder_or_location: D5 / Draisine auf den Bahnsteiggleisen
- state: Arbeitsstand
- review_state: working

Entries
-------

- item: Schmieroel
  amount: `1 gebunden / 3 Rest in D5`
  unit: Einheit
  source: `database-rp/01-factions/novapolis/05-projects/Draisine-Transportmodul.md`; `database-rp/01-factions/novapolis/04-inventory/D5-inventar.md`; `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 11
  confidence: SSOT- und Runtime-belegt als aktueller Prototypbestand; Werkstattbindung, kein Feldverbrauch
- item: Lagerfett (Technik)
  amount: `1 gebunden / 2 Rest in D5`
  unit: Einheit
  source: `database-rp/01-factions/novapolis/05-projects/Draisine-Transportmodul.md`; `database-rp/01-factions/novapolis/04-inventory/D5-inventar.md`; `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 11
  confidence: SSOT- und Runtime-belegt als aktueller Prototypbestand; Werkstattbindung, kein Feldverbrauch
- item: Sicherungssatz
  amount: `1 Set gebunden / 3 Sets Rest in D5`
  unit: Set
  source: `database-rp/01-factions/novapolis/05-projects/Draisine-Transportmodul.md`; `database-rp/01-factions/novapolis/04-inventory/D5-inventar.md`; `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 11
  confidence: SSOT- und Runtime-belegt als aktueller Prototypbestand; Werkstattbindung, kein Feldverbrauch
- item: Dichtungsmanschette
  amount: `1 gebunden / 5 Rest in D5`
  unit: Einheit
  source: `database-rp/01-factions/novapolis/05-projects/Draisine-Transportmodul.md`; `database-rp/01-factions/novapolis/04-inventory/D5-inventar.md`; `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 11
  confidence: SSOT- und Runtime-belegt als aktueller Prototypbestand; Werkstattbindung, kein Feldverbrauch

Runtime Split
-------------

- Dieser Traeger fuehrt nur den Draisine-Eigenbestand und den kleinen Werkstattverbrauchsrahmen des Prototyps.
- Tunnel- und Nordlinie-Bedarf werden hier nicht als Draisine-Verbrauch umgebucht.
- `Schweißgeraet` und `Adapter / Fitting (DN60)` bleiben deshalb getrennt im Nordlinie-/D5-Bedarf statt als lokaler Draisine-Bestand.

Verbrauchsrahmen
----------------

- review: Pro Werkstattblock liegt der konservative Verbrauchsrahmen fuer die Draisine bei `0-1` Schmieroel, `0-1` Lagerfett (Technik) und `0-1` Sicherungssatz; episodisch `0-1` Dichtungsmanschette oder `Kabelanschnitt`.
- Dieser Rahmen stammt aus SSOT und ist noch keine zusaetzliche Runtime-Ist-Buchung ueber die aktuell vier gebundenen Posten hinaus.

SSOT-linked Project Scope
-------------------------

- Noch nicht als eigener Draisine-Ist-Verbrauch gebucht, aber fuer den laufenden Projektkontext bereits SSOT-gebunden anschlussfaehig sind:
  - `Kabelanschnitt` aus `Kabelspule`: in D5 belegt als Stationsgut; im Draisine-SSOT bereits als episodisch moeglicher Werkstattposten angelegt und jetzt auch als eigene Warenklasse im SSOT lesbar.
  - `Werkzeugkit`: in D5 belegt, traegt den aktiven Werkstattkontext der Draisine mit, ohne bisher als eigener Draisine-Abgang gebucht zu sein.
  - `Werkzeugsatz (Mechanik)`: in D5 belegt, fachlich naheliegender Projektkontext fuer Radaufnahme, Sicherung und Schienenfixpunkte.
  - `Wartungsschluessel` und `Druckmesser`: in D5 belegt und als Werkzeug-/Messkontext fuer laufende Montage- und Pruefarbeit verfuegbar, aber noch nicht als eigener Draisine-Verbrauch abgebucht.
- Diese Klassen erweitern die Runtime-Warenauswahl der Draisine bewusst ohne neue freie Bindung: verfuegbar als Projektumfeld, aber erst bei expliziter Runtime-Evidenz als gebunden oder verbraucht promoten.

Open Needs
----------

- Draisine-Eigenbedarf:
  - belegt: Fuer den naechsten kleinen Bauschritt ist der Kernsatz vor Ort.
  - offen: Die Reserve ist knapp; ein weiterer konkreter Zusatzposten ueber die vier gebundenen Werkstattgueter hinaus ist aktuell noch nicht belastbar benannt.
  - offen: `Kabelanschnitt`, `Werkzeugkit`, `Werkzeugsatz (Mechanik)`, `Wartungsschluessel` und `Druckmesser` sind als SSOT-gebundener Projektkontext lesbar, aber noch nicht als eigener gebundener Draisine-Abgang belegt.
- Getrennter Tunnel-/Projektbedarf:
  - `Schweißgeraet`
  - `Adapter / Fitting (DN60)`
- Diese beiden Posten bleiben harte Nordlinie-Blocker, aber kein bereits gebuchter Draisine-Eigenverbrauch.

Recent Changes
--------------

- Turn 11 bestaetigt runtime-seitig erstmals ausdruecklich, dass Jonas und Pahl den Prototyp auf den D5-Bahnsteiggleisen fuehren und dabei nur einen kleinen, ehrlichen Materialzwischenstand geben.
- Die bisher nur ueber Projektblatt, D5-Inventar und Szene verteilte Werkstattbindung der Draisine wird deshalb ab jetzt in einem eigenen Runtime-Traeger gefuehrt.
- Der Trennschnitt ist absichtlich hart: gebundener Prototypbestand hier, D5-/Nordlinie-Tunnelbedarf weiter in `inventories/d5.md` und den Projekt-/State-Traegern.
- Die Warenauswahl der Draisine fuehrt jetzt zusaetzlich die naechsten SSOT-gebundenen Projektklassen als noch ungebundene Werkzeug- und Materialumgebung, damit spaetere echte Abgaenge nicht erst wieder aus Fliesstext rekonstruiert werden muessen.

Evidence Chain
--------------

- `database-rp/00-admin/Waren-Index.md`
- `database-rp/00-admin/Warenueberblick-T0.md`
- `database-rp/01-factions/novapolis/04-inventory/D5-inventar.md`
- `database-rp/01-factions/novapolis/05-projects/Draisine-Transportmodul.md`
- `database-rp/00-admin/Waren-Index.md`
- `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 11
- `state/d5.md`
- `state/nordlinie-01.md`

Promotion Notes
---------------

- Zusaetzliche Draisine-Posten erst dann als Runtime-Ist-Buchung nachziehen, wenn sie im laufenden RP-Zug als real gebunden, verbaut, geliefert oder verbraucht belegt sind.
- `Schweißgeraet` und `DN60` nur dann hier aufnehmen, wenn sie spaeter tatsaechlich als der Draisine selbst zugeordneter Bestand oder Verbrauch belegt werden; bis dahin bleiben sie Projektblocker der Nordlinie.
- Die jetzt sichtbar gefuehrten Projektklassen `Kabelanschnitt`, `Werkzeugkit`, `Werkzeugsatz (Mechanik)`, `Wartungsschluessel` und `Druckmesser` bleiben Umgebungsklassen, bis ein Folgezug daraus echte Draisine-Bindung macht.
