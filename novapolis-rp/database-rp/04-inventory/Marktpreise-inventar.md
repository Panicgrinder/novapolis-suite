---
stand: 2026-02-10 22:45
update: Markdownlint-Fix (Leerzeilen um Tabelle).
checks: "not run (not requested)"
canvas: Marktpreise - Baseline
last_updated: 2026-01-14T08:56:04+01:00
category: inventory
slug: marktpreise-inventar
owner: market
scope: global
version: "0.1"
tags: [handel, baseline]
---

Marktpreise - Baseline
======================

Zweck
-----
Diese Seite ist eine SSOT-Baseline für Preisgefühl und Knappheit im Setting.
Sie ersetzt keine fraktionsspezifischen Inventare, sondern liefert eine gemeinsame Referenz,
wenn Szenen Handel, Tausch oder Beschaffung dokumentieren.

Währung (Kurz)
--------------
- Standard: "Kugeln" (neu/gebraucht)
- Faustregel: 1 neu ≈ 10 gebraucht (Qualität streut)

Baseline-Preise (Richtwerte)
----------------------------
- Energiezelle (Standard): Richtwert ohne Zahl; Preis folgt Modifikatoren (Knappheit/Route/Trust)
- Luftfilter (Gasmasken): Richtwert ohne Zahl; Preis folgt Modifikatoren (Knappheit/Route/Trust)
- Luftfilter (Einrichtungen): Richtwert ohne Zahl; Preis folgt Modifikatoren (Knappheit/Route/Trust)
- Wasserfilter (portabel): Richtwert ohne Zahl; Preis folgt Modifikatoren (Knappheit/Route/Trust)
- Filtermaterial (stationaer): Richtwert ohne Zahl; Preis folgt Modifikatoren (Knappheit/Route/Trust)
- Adapter / Fittings (DN60 / Sonder): Richtwert ohne Zahl; Preis folgt Modifikatoren (Knappheit/Route/Trust)
- Schweißausrüstung (kompakt): Richtwert ohne Zahl; Preis folgt Modifikatoren (Knappheit/Route/Trust)
- Werkzeugsatz (Mechanik): Richtwert ohne Zahl; Preis folgt Modifikatoren (Knappheit/Route/Trust)

Skalen (maschinenlesbar)
------------------------
- Verfuegbarkeit: hoch | mittel | niedrig | selten | extrem
- Tauschwert: niedrig | mittel | hoch | sehr-hoch | sonder

Item-Skalen (kompakt)
---------------------

| item_id | name | verfuegbarkeit | tauschwert | notes |
| --- | --- | --- | --- | --- |
| kugeln-neu | Kugeln (neu) | mittel | hoch | waehrung, baseline |
| kugeln-gebraucht | Kugeln (gebraucht) | hoch | niedrig | waehrung, baseline |
| energiezelle-standard | Energiezelle (Standard) | mittel | hoch | baseline |
| luftfilter-gasmasken | Luftfilter (Gasmasken) | mittel | hoch | baseline |
| luftfilter-einrichtungen | Luftfilter (Einrichtungen) | niedrig | hoch | baseline |
| wasserfilter-portabel | Wasserfilter (portabel) | mittel | hoch | baseline |
| filtermaterial-stationaer | Filtermaterial (stationaer) | niedrig | hoch | baseline |
| werkzeugtasche-fundstueck | Werkzeugtasche (Fundstueck) | selten | hoch | fundstueck |
| messausruestung | Messausruestung (allgemein) | niedrig | sehr-hoch | spezialbedarf |
| statikpruefset | Statikpruef-Set (Tunnel) | niedrig | sehr-hoch | tunnel-check |
| funkausruestung | Funkausruestung (stabil) | niedrig | hoch | kommunikation |
| sensoren-set | Sensoren-Set (Monitoring) | niedrig | hoch | monitoring |
| gasmaske | Gasmaske | niedrig | hoch | schutz |
| atemschutz | Atemschutz (funktionstuechtig) | mittel | hoch | schutz |
| atemfilter | Atemfilter | mittel | hoch | filter |
| werkzeugkit | Werkzeugkit | mittel | hoch | basis-set |
| ersatzteile-set | Ersatzteile-Set | mittel | hoch | reparatur |
| akkuzelle | Akkuzelle (geladen) | mittel | hoch | akku |
| rationen | Rationen | hoch | niedrig | nahrung |
| wasser-trink | Wasser (Trinkwasser) | hoch | niedrig | nahrung |
| lampe | Lampe (betriebsbereit) | mittel | mittel | licht |
| multimeter | Multimeter | niedrig | hoch | messung |
| union-ersatzteilkiste | Union-Ersatzteilkiste | selten | hoch | ersatzteile |
| filterkartusche-leer | Filterkartusche (leer) | niedrig | niedrig | leer |
| ersatzrohr | Ersatzrohr | niedrig | mittel | ersatzteil |
| ventilkomponente | Ventilkomponente | niedrig | mittel | ersatzteil |
| kabelspule | Kabelspule | niedrig | mittel | kabel |
| schmieroel | Schmieroel | mittel | mittel | wartung |
| strommodul | Strommodul | niedrig | hoch | energie |
| wasserkanister | Wasserkanister | mittel | mittel | wasser |
| wasserflasche | Wasserflasche | hoch | niedrig | wasser |
| wartungsschluessel | Wartungsschluessel | mittel | mittel | werkzeug |
| druckmesser | Druckmesser | niedrig | hoch | messung |
| schweissgeraet | Schweissgeraet | niedrig | sehr-hoch | schweisstechnik |
| sensorpaket | Sensorpaket | niedrig | hoch | monitoring |
| schutzanzug | Schutzanzug | niedrig | hoch | schutz |
| ersatzmaske | Ersatzmaske | niedrig | hoch | schutz |
| schaltplaene-technische-doku | Schaltplaene & technische Doku | selten | hoch | doku |
| reparaturstation-defekt | Reparaturstation (defekt) | selten | hoch | stationaer |
| artefakt-7a | Artefakt 7A | extrem | sonder | einzigartig |
| datenkern-stationaer | Datenkern (stationaer) | extrem | sonder | einzigartig |
| datenkern-tragbar | Datenkern (tragbar) | extrem | sonder | einzigartig |
| adapter-dn60 | Adapter / Fitting (DN60) | niedrig | sehr-hoch | baseline |
| schweissausruestung-kompakt | Schweissausruestung (kompakt) | niedrig | hoch | baseline |
| werkzeugsatz-mechanik | Werkzeugsatz (Mechanik) | mittel | hoch | baseline |
| hydrofilter-behaelter | Hydrofilter-Behaelter (Reserve) | niedrig | hoch | ersatzteil |

Modifikatoren
-------------
- Knappheit: +20% bis +80%
- Bulk (Mengenrabatt): -10% bis -25%
- Risiko/Route (Tunnel/Anomalien): +10% bis +50%
- Beziehung/Trust: -10% bis -30% (oder Alternativ: bessere Qualität statt Preis)

Logging-Konvention (für Szenen)
-------------------------------
- Jede Szene, die Handel beeinflusst, verlinkt auf die betroffenen Inventare.
- Bestandsänderungen werden in den jeweiligen Inventaren unter "Bewegungen (Log)" nachgezogen.
- Verhandlungen/Beziehungen werden im jeweiligen Relationslog dokumentiert.

Links
-----
- Logistik (Admin) → ../00-admin/Logistik.md
- Missionslog → ../00-admin/Missionslog.md
- Währung "Kugeln" (Reference) → ../00-admin/Reference-Campaign-State.md
