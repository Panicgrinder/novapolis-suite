---
stand: 2026-04-29 00:47
update: "Waren-Index erweitert um weitere belegte Sammelklassen fuer Rohmaterialien, medizinische Gueter, Informationsgueter, Tarn-/Signaltechnik und Batterien."
checks: snapshot-lock PASS (2026-04-29 00:31)
slug: waren-index
category: Admin
schemaVersion: 1
language: de
status: active
owners: [admin-novapolis]
tags: [rp, economy, items, index]
relatedSlugs: [marktpreise-inventar, reference-campaign-state, missionslog, curated-konfliktliste]
items:
  - id: kugeln-neu
    name: Kugeln (neu)
    kind: currency
    unit: stk
    tags: [waehrung, munition, neu]
    seenIn: [reference-campaign-state, marktpreise-inventar, curated-konfliktliste]
    notes: "Hochwertige Währung; 1 neu ≈ 10 gebraucht (Faustregel)."
  - id: kugeln-gebraucht
    name: Kugeln (gebraucht)
    kind: currency
    unit: stk
    tags: [waehrung, munition, gebraucht]
    seenIn: [reference-campaign-state, marktpreise-inventar, freie-gruppen-inventar]
    notes: "Alltagswährung; Hauptmunition, Qualität streut."
  - id: energiezelle-standard
    name: Energiezelle (Standard)
    kind: consumable
    unit: stk
    tags: [energie, zelle]
    seenIn: [marktpreise-inventar, reference-campaign-state]
    notes: "Richtwert über Baseline; Preis folgt Knappheit/Route/Trust."
  - id: luftfilter-gasmasken
    name: Luftfilter (Gasmasken)
    kind: consumable
    unit: stk
    tags: [filter, luft, gasmaske]
    seenIn: [marktpreise-inventar, reference-campaign-state]
    notes: "Richtwert ueber Baseline; Verbrauch nach Einsatzlage."
  - id: luftfilter-einrichtungen
    name: Luftfilter (Einrichtungen)
    kind: consumable
    unit: stk
    tags: [filter, luft, einrichtung]
    seenIn: [marktpreise-inventar, reference-campaign-state]
    notes: "Richtwert ueber Baseline; Wartungsintervalle variieren."
  - id: wasserfilter-portabel
    name: Wasserfilter (portabel)
    kind: consumable
    unit: stk
    tags: [filter, wasser, portabel]
    seenIn: [marktpreise-inventar, reference-campaign-state]
    notes: "Richtwert ueber Baseline; Einsatz im Feld/auf Tour."
  - id: filtermaterial-stationaer
    name: Filtermaterial (stationaere Filteranlagen)
    kind: consumable
    unit: stk
    tags: [filter, wasser, filtermaterial, stationaer]
    seenIn: [marktpreise-inventar, reference-campaign-state]
    notes: "Richtwert ueber Baseline; Austausch nach Last/Qualitaet."
  - id: werkzeugtasche-fundstueck
    name: Werkzeugtasche (Fundstueck)
    kind: tool
    unit: stk
    tags: [werkzeug, fundstueck]
    seenIn: [scene-2025-10-27-g]
    notes: "Ownership offen; Inhalt tbd nach Beleg."
  - id: messausruestung
    name: Messausruestung (allgemein)
    kind: tool
    unit: set
    tags: [messung, ausruestung]
    seenIn: [scene-2025-10-27-ad]
    notes: "Bedarf fuer Vor-Ort-Messungen; konkrete Geraete tbd."
  - id: statikpruefset
    name: Statikpruef-Set (Tunnel)
    kind: tool
    unit: set
    tags: [statik, tunnel, pruefung]
    seenIn: [scene-2025-10-27-a, scene-2025-10-27-c]
    notes: "Material fuer Statikpruefung; Details tbd."
  - id: funkausruestung
    name: Funkausruestung (stabil)
    kind: tool
    unit: set
    tags: [funk, kommunikation]
    seenIn: [scene-2025-10-27-ae, scene-2025-10-27-ak]
    notes: "Funkstabilisierung; Reichweite/Qualitaet tbd."
  - id: sensoren-set
    name: Sensoren-Set (Monitoring)
    kind: tool
    unit: set
    tags: [sensoren, monitoring]
    seenIn: [scene-2025-10-27-p]
    notes: "Monitoring-Erweiterung; Spezifikation tbd."
  - id: gasmaske
    name: Gasmaske
    kind: tool
    unit: stk
    tags: [schutz, luft, gasmaske]
    seenIn: [raw-canvas-2025-10-16t12-00-00-000z]
    notes: "Persoenliche Schutzausruestung; Filter separat."
  - id: atemschutz
    name: Atemschutz (funktionstuechtig)
    kind: tool
    unit: stk
    tags: [schutz, luft, atemschutz]
    seenIn: [raw-canvas-2025-10-16t03-12-00-000z]
    notes: "Atemschutz-Geraet; genaue Spezifikation tbd."
  - id: atemfilter
    name: Atemfilter
    kind: consumable
    unit: stk
    tags: [filter, luft, atemschutz]
    seenIn: [raw-canvas-2025-10-16t12-00-00-000z]
    notes: "Filter fuer Atemschutz/Gasmasken."
  - id: werkzeugkit
    name: Werkzeugkit
    kind: tool
    unit: set
    tags: [werkzeug]
    seenIn: [raw-canvas-2025-10-16t12-00-00-000z]
    notes: "Basis-Set fuer Reparaturen."
  - id: ersatzteile-set
    name: Ersatzteile-Set
    kind: component
    unit: set
    tags: [ersatzteile, reparatur]
    seenIn: [raw-canvas-2025-10-16t12-00-00-000z]
    notes: "Kupferdraht/Schweisspaste/Sicherungen (Set)."
  - id: akkuzelle
    name: Akkuzelle (geladen)
    kind: consumable
    unit: stk
    tags: [energie, akku]
    seenIn: [raw-canvas-2025-10-16t12-00-00-000z]
    notes: "Kleine Energiezelle; nicht mit Energiezelle (Standard) verwechseln."
  - id: rationen
    name: Rationen
    kind: consumable
    unit: stk
    tags: [nahrung]
    seenIn: [raw-canvas-2025-10-16t12-00-00-000z]
    notes: "Standardrationen."
  - id: wasser-trink
    name: Wasser (Trinkwasser)
    kind: consumable
    unit: stk
    tags: [wasser]
    seenIn: [raw-canvas-2025-10-16t12-00-00-000z]
    notes: "Trinkwasser; genaue Einheiten variieren."
  - id: lampe
    name: Lampe (betriebsbereit)
    kind: tool
    unit: stk
    tags: [licht, ausruestung]
    seenIn: [raw-canvas-2025-10-16t12-00-00-000z]
    notes: "Standardlampe."
  - id: multimeter
    name: Multimeter
    kind: tool
    unit: stk
    tags: [messung, elektronik]
    seenIn: [raw-canvas-2025-10-16t12-00-00-000z]
    notes: "Elektronikdiagnose; Messgeraet."
  - id: union-ersatzteilkiste
    name: Union-Ersatzteilkiste
    kind: component
    unit: stk
    tags: [ersatzteile, kiste]
    seenIn: [raw-canvas-2025-10-16t12-00-00-000z]
    notes: "Kiste mit Ersatzteilen (Stationsgut)."
  - id: filterkartusche-leer
    name: Filterkartusche (leer)
    kind: component
    unit: stk
    tags: [filter, leer]
    seenIn: [raw-canvas-2025-10-16t12-00-00-000z]
    notes: "Leere Kartusche; Wiederaufbereitung tbd."
  - id: ersatzrohr
    name: Ersatzrohr
    kind: component
    unit: stk
    tags: [rohr, ersatzteil]
    seenIn: [raw-canvas-2025-10-16t12-30-00-000z]
    notes: "Stationsersatzteil."
  - id: ventilkomponente
    name: Ventilkomponente
    kind: component
    unit: stk
    tags: [ventil, ersatzteil]
    seenIn: [raw-canvas-2025-10-16t12-00-00-000z]
    notes: "Ventil-/Armaturenkomponente."
  - id: kabelspule
    name: Kabelspule
    kind: component
    unit: stk
    tags: [kabel, energie]
    seenIn: [raw-canvas-2025-10-16t12-30-00-000z]
    notes: "Energie-/Datenkabel (Spule)."
  - id: schmieroel
    name: Schmieroel
    kind: consumable
    unit: stk
    tags: [wartung]
    seenIn: [raw-canvas-2025-10-16t12-30-00-000z]
    notes: "Wartungsmaterial."
  - id: strommodul
    name: Strommodul
    kind: component
    unit: stk
    tags: [energie, modul]
    seenIn: [raw-canvas-2025-10-16t12-30-00-000z]
    notes: "Energiekomponente."
  - id: wasserkanister
    name: Wasserkanister
    kind: consumable
    unit: stk
    tags: [wasser, kanister]
    seenIn: [raw-canvas-2025-10-16t12-30-00-000z]
    notes: "Groessere Wassereinheit."
  - id: wasserflasche
    name: Wasserflasche
    kind: consumable
    unit: stk
    tags: [wasser]
    seenIn: [raw-canvas-2025-10-16t12-30-00-000z]
    notes: "Trinkwasser in Flaschenform."
  - id: wartungsschluessel
    name: Wartungsschluessel
    kind: tool
    unit: stk
    tags: [werkzeug, wartung]
    seenIn: [raw-canvas-2025-10-16t12-30-00-000z]
    notes: "Stationswerkzeug."
  - id: druckmesser
    name: Druckmesser
    kind: tool
    unit: stk
    tags: [messung, druck]
    seenIn: [raw-canvas-2025-10-16t12-30-00-000z]
    notes: "Messgeraet fuer Druck."
  - id: schweissgeraet
    name: Schweissgeraet
    kind: tool
    unit: stk
    tags: [werkzeug, schweisstechnik]
    seenIn: [raw-canvas-2025-10-16t12-30-00-000z]
    notes: "Schweissgeraet; stationaer einsetzbar."
  - id: sensorpaket
    name: Sensorpaket
    kind: tool
    unit: set
    tags: [sensoren, monitoring]
    seenIn: [raw-canvas-2025-10-16t12-30-00-000z]
    notes: "Paket fuer Monitoring/Installation."
  - id: schutzanzug
    name: Schutzanzug
    kind: tool
    unit: stk
    tags: [schutz, ausruestung]
    seenIn: [raw-canvas-2025-10-16t12-30-00-000z]
    notes: "Schutzanzug fuer Einsaetze."
  - id: ersatzmaske
    name: Ersatzmaske
    kind: tool
    unit: stk
    tags: [schutz, maske]
    seenIn: [raw-canvas-2025-10-16t12-30-00-000z]
    notes: "Ersatzmaske fuer Atemschutz."
  - id: schaltplaene-technische-doku
    name: Schaltplaene & technische Doku
    kind: component
    unit: set
    tags: [doku, technik]
    seenIn: [raw-canvas-2025-10-16t12-00-00-000z]
    notes: "Fragmentarische technische Dokumentation."
  - id: reparaturstation-defekt
    name: Reparaturstation (defekt)
    kind: component
    unit: stk
    tags: [reparatur, stationaer]
    seenIn: [raw-canvas-2025-10-16t12-00-00-000z]
    notes: "Stationaere Einheit; reaktivierung tbd."
  - id: artefakt-7a
    name: Artefakt 7A
    kind: component
    unit: stk
    tags: [artefakt, einzigartig]
    seenIn: [scene-2025-10-27-d]
    notes: "Einzigartig; erst inventarisieren, dann Details."
  - id: datenkern-stationaer
    name: Datenkern (stationaer)
    kind: component
    unit: stk
    tags: [daten, artefakt, einzigartig]
    seenIn: [scene-2025-10-27-x]
    notes: "Einzigartig; am Fundort/Stationsinventar gebunden."
  - id: datenkern-tragbar
    name: Datenkern (tragbar)
    kind: component
    unit: stk
    tags: [daten, artefakt, einzigartig, tragbar]
    seenIn: [raw-canvas-2025-10-16t12-30-00-000z]
    notes: "Einzigartig; versiegelt, Funktion unbekannt."
  - id: adapter-dn60
    name: Adapter / Fitting (DN60)
    kind: component
    unit: stk
    tags: [adapter, fitting, dn60]
    seenIn: [marktpreise-inventar, reference-campaign-state]
    notes: "Sonderteil; Preis folgt Knappheit/Route/Trust."
  - id: schweissausruestung-kompakt
    name: Schweißausrüstung (kompakt)
    kind: tool
    unit: set
    tags: [werkzeug, schweisstechnik]
    seenIn: [marktpreise-inventar, reference-campaign-state]
    notes: "Werkstattbedarf; kompakte Ausführung."
  - id: werkzeugsatz-mechanik
    name: Werkzeugsatz (Mechanik)
    kind: tool
    unit: set
    tags: [werkzeug, mechanik]
    seenIn: [marktpreise-inventar]
    notes: "Basis für Reparaturen/Projekte."
  - id: hydrofilter-behaelter
    name: Hydrofilter-Behälter (Reserve)
    kind: component
    unit: stk
    tags: [wasser, filter, behaelter]
    seenIn: [reference-campaign-state]
    notes: "Reservebauteil; in D5 inventarisiert."
  - id: medkit-standard
    name: Medkit (Standard)
    kind: consumable
    unit: set
    tags: [medizin, erste-hilfe, feld]
    seenIn: [missionslog, reference-campaign-state]
    notes: "Basis-Set fuer Erstversorgung im Feldeinsatz."
  - id: verbandmaterial-set
    name: Verbandmaterial (Set)
    kind: consumable
    unit: set
    tags: [medizin, verband, erste-hilfe]
    seenIn: [missionslog, reference-campaign-state]
    notes: "Wundversorgung; Verbrauch lageabhaengig."
  - id: desinfektionsmittel
    name: Desinfektionsmittel
    kind: consumable
    unit: stk
    tags: [medizin, hygiene, versorgung]
    seenIn: [reference-campaign-state]
    notes: "Hygiene-/Wundbehandlung; stationaer und mobil nutzbar."
  - id: antibiotika-basis
    name: Antibiotika (Basis)
    kind: consumable
    unit: stk
    tags: [medizin, medikament]
    seenIn: [reference-campaign-state]
    notes: "Grundstock fuer bakterielle Infektionen; Verfügbarkeit variabel."
  - id: schmerzmittel-basis
    name: Schmerzmittel (Basis)
    kind: consumable
    unit: stk
    tags: [medizin, medikament]
    seenIn: [reference-campaign-state]
    notes: "Basisanalgetika; Verbrauch bei Einsaetzen erhoeht."
  - id: sicherungssatz
    name: Sicherungssatz
    kind: component
    unit: set
    tags: [energie, elektrik, ersatzteile]
    seenIn: [marktpreise-inventar, reference-campaign-state]
    notes: "Ersatzsicherungen fuer Verteilung/Module."
  - id: dichtungsmanschette
    name: Dichtungsmanschette
    kind: component
    unit: stk
    tags: [wartung, dichtung, ersatzteile]
    seenIn: [marktpreise-inventar, missionslog]
    notes: "Abdichtung von Leitungen/Anschluessen; kritisch bei Leckagen."
  - id: kabelanschnitt
    name: Kabelanschnitt
    kind: component
    unit: abschnitt
    tags: [kabel, energie, montage]
    seenIn: [d5-inventar, c6-inventar, novapolis-inventar, draisine-transportmodul]
    notes: "Kleiner abgehaengter Kabelabschnitt fuer Montage, Reparatur oder Leitungsfuehrung; meist aus vorhandener Kabelspule gezogen statt als ganze Spule verbucht."
  - id: kuhlmittel-industrie
    name: Kühlmittel (Industrie)
    kind: consumable
    unit: stk
    tags: [wartung, kuehlung, energie]
    seenIn: [reference-campaign-state]
    notes: "Fuer Aggregate/Leistungseinheiten; Qualitätsstreuung möglich."
  - id: lagerfett-technik
    name: Lagerfett (Technik)
    kind: consumable
    unit: stk
    tags: [wartung, mechanik]
    seenIn: [marktpreise-inventar]
    notes: "Grundmaterial fuer mechanische Instandhaltung."
  - id: druckluftkartusche
    name: Druckluftkartusche
    kind: consumable
    unit: stk
    tags: [technik, druck, wartung]
    seenIn: [missionslog, reference-campaign-state]
    notes: "Nutzbar fuer Pneumatik/Werkzeuge; Logistikbedarf schwankend."
  - id: metallprofil-lang
    name: Metallprofil (lang)
    kind: component
    unit: stk
    tags: [stuetzbau, metallprofil, lang]
    seenIn: [nordlinie-01-stuetzbaukasten, d5-inventar]
    notes: "Tragendes Laengenteil fuer groessere Spannweiten oder schräge Abstuetzung."
  - id: metallprofil-mittel
    name: Metallprofil (mittel)
    kind: component
    unit: stk
    tags: [stuetzbau, metallprofil, mittel]
    seenIn: [nordlinie-01-stuetzbaukasten, d5-inventar]
    notes: "Standardprofil fuer die meisten behelfmaessigen Tunnelstuetzen."
  - id: metallprofil-kurz
    name: Metallprofil (kurz)
    kind: component
    unit: stk
    tags: [stuetzbau, metallprofil, kurz]
    seenIn: [nordlinie-01-stuetzbaukasten, d5-inventar]
    notes: "Kurzteil fuer Versteifung, Querzug oder lokale Unterfuetterung."
  - id: stuetzklemme
    name: Stuetzklemme
    kind: component
    unit: stk
    tags: [stuetzbau, klemme, verbindung]
    seenIn: [nordlinie-01-stuetzbaukasten, d5-inventar]
    notes: "Schnelle Fixierung und Verspannung an vorbereiteten Punkten."
  - id: lasche-knotenblech
    name: Lasche / Knotenblech
    kind: component
    unit: stk
    tags: [stuetzbau, lasche, knotenblech]
    seenIn: [nordlinie-01-stuetzbaukasten, d5-inventar]
    notes: "Flaechige Verbindung oder Lastverteilung zwischen Profilen."
  - id: ausgleichsplatte
    name: Ausgleichsplatte
    kind: component
    unit: stk
    tags: [stuetzbau, ausgleich, platte]
    seenIn: [nordlinie-01-stuetzbaukasten, d5-inventar]
    notes: "Unterlage oder Distanzstueck fuer unruhige Auflagepunkte."
  - id: klebmasse-schwach
    name: Klebmasse (schwach)
    kind: consumable
    unit: kartusche
    tags: [stuetzbau, klebmasse, fixierung]
    seenIn: [nordlinie-01-stuetzbaukasten, d5-inventar]
    notes: "Nur fuer Ansetzen, Ausrichten oder leichte Fixierung; nie primaere Endverbindung."
  - id: schraubensatz-mittel
    name: Schraubensatz (mittel)
    kind: component
    unit: set
    tags: [stuetzbau, schrauben, verbindung]
    seenIn: [nordlinie-01-stuetzbaukasten, d5-inventar]
    notes: "Mittlere Sicherung fuer behelfmaessige, kontrollierbare Verbindung."
  - id: bolzen-mutter-satz-stark
    name: Bolzen-Mutter-Satz (stark)
    kind: component
    unit: set
    tags: [stuetzbau, bolzen, muttern, verbindung]
    seenIn: [nordlinie-01-stuetzbaukasten, d5-inventar]
    notes: "Starke mechanische Verbindung fuer hoeher belastete Baugruppen."
  - id: schienenprofil
    name: Schienenprofil
    kind: component
    unit: m
    tags: [trasse, schiene, metall, bau]
    seenIn: [missionslog, d5-inventar, c6-inventar, novapolis-inventar]
    notes: "Laengenmaterial fuer Trassen- und Leitungsfuehrung im Tunnelkorridor; im aktuellen RP als belegte Verbrauchsklasse von Nordlinie 01 gefuehrt."
  - id: betonplatte
    name: Betonplatte
    kind: component
    unit: m2
    tags: [bau, platte, tunnel]
    seenIn: [missionslog, d5-inventar, c6-inventar, novapolis-inventar]
    notes: "Bauplatte fuer Unterbau, Lastverteilung oder staerkere Sicherungszonen; im aktuellen RP als belegte Verbrauchsklasse von Nordlinie 01 gefuehrt."
  - id: notdecke
    name: Notdecke
    kind: consumable
    unit: stk
    tags: [evakuierung, versorgung, waerme]
    seenIn: [c6-inventar]
    notes: "Leichte Waerme-/Notversorgung fuer Evakuierungs- und Schlaflagen."
  - id: wechselkleidung-set
    name: Wechselkleidung (Set)
    kind: consumable
    unit: set
    tags: [evakuierung, kleidung, versorgung]
    seenIn: [c6-inventar]
    notes: "Konservativer Sammelposten fuer tragbare Ersatzkleidung."
  - id: hygienepaket-basis
    name: Hygienepaket (Basis)
    kind: consumable
    unit: set
    tags: [evakuierung, hygiene, versorgung]
    seenIn: [c6-inventar]
    notes: "Basispaket aus Waschartikeln und kleinen Pflegeguetern."
  - id: kochgeschirr-set
    name: Kochgeschirr (Set)
    kind: tool
    unit: set
    tags: [versorgung, kueche, evakuierung]
    seenIn: [c6-inventar]
    notes: "Kleines Koch-/Essgeschirr fuer Schicht- oder Gruppenversorgung."
  - id: nahrungsmittel-grundbedarf
    name: Nahrungsmittel (Grundbedarf)
    kind: consumable
    unit: paket
    tags: [nahrung, handel, grundbedarf]
    seenIn: [relationslog_novapolis_v1, haendlerbund-inventar, caravan-moves]
    notes: "Belegte Handelsklasse fuer Grundversorgung im Austauschpfad Novapolis <-> Haendlerbund; bewusst grob, solange keine feinere Packlisten- oder Stationsinventarlinie vorliegt."
  - id: grundbedarfsgueter
    name: Grundbedarfsgueter
    kind: consumable
    unit: paket
    tags: [versorgung, handel, grundbedarf]
    seenIn: [relationslog_novapolis_v1, haendlerbund-inventar, caravan-moves]
    notes: "Breite Sammelklasse fuer nichtluxurioese Alltagsgueter im H-47-/C6-Austauschpfad; bleibt absichtlich oberhalb einzelner Verbrauchsartikel, bis konkrete Packlisten vorliegen."
  - id: rohmaterialien
    name: Rohmaterialien
    kind: component
    unit: paket
    tags: [handel, material, rohstoff]
    seenIn: [relationslog_novapolis_v1]
    notes: "Breite Importklasse fuer noch nicht weiter zerlegte Grund- und Baustoffe; im aktiven Novapolis-Handelsbedarf bereits als eigener Korridor benannt, aber noch ohne feinere Materialsplitterung."
  - id: medizinische-gueter
    name: Medizinische Gueter
    kind: consumable
    unit: paket
    tags: [medizin, handel, versorgung]
    seenIn: [relationslog_novapolis_v1, novapolis-markets]
    notes: "Breite Handels- und Versorgungsklasse oberhalb einzelner Medkits, Antibiotika oder Desinfektionsposten; dient als kanonischer Sammelanker fuer importierte medizinische Versorgung."
  - id: informationsgueter
    name: Informationsgueter
    kind: component
    unit: paket
    tags: [handel, information, trust]
    seenIn: [novapolis-markets, fluesterkollektiv-inventar]
    notes: "Nichtstoffliche, aber tauschbare Sammelklasse fuer Geruechte, Kontakte, Zugangscodes oder vergleichbare Wissensgueter; bleibt bewusst grob, solange keine feinere Handelslinie belegt ist."
  - id: tarn-signaltechnik
    name: Tarn-/Signaltechnik
    kind: tool
    unit: set
    tags: [technik, signal, tarnung]
    seenIn: [fluesterkollektiv-inventar]
    notes: "Breite Technikklasse fuer kleine Signal-, Abschirm- und Tarnmittel des Fluesterkollektivs; bewusst ohne Einzelgeraete, solange keine konkrete Stueckliste vorliegt."
  - id: batterien
    name: Batterien
    kind: consumable
    unit: stk
    tags: [energie, verbrauch, mobil]
    seenIn: [fluesterkollektiv-inventar]
    notes: "Allgemeine mobile Stromquelle fuer kleine Geraete und Feldtechnik; im aktuellen RP bislang nur als belegter Verbrauchsanker innerhalb breiter Verbrauchsmaterial-Klassen gefuehrt."
---

Waren-Index (weltweit)
======================

Zweck
-----
Weltweite Übersicht über im RP bereits aufgetauchte Waren/Güter. Dient als SSOT für IDs, Tags und Querverweise. Preise/Knappheit siehe Baseline: `marktpreise-inventar`.

Hinweise
--------
- ID ist der slug in `items[].id` (stabil, slug-only-Regel). Benennung: kleinschreibung, minus-getrennt.
- `seenIn` referenziert Dokument-slugs (nicht Dateinamen).
- Preise werden nicht hier gepflegt, sondern in `marktpreise-inventar` und fraktionsbezogen in 01-factions/*/06-handel-diplomatie/.
- Erweiterung nur um Items, die im RP/Logs/Szenen oder in aktiven Inventar-/Handels-SSOTs bereits als eigenstaendige Klasse vorgekommen sind; neue Detailwaren zuerst im Missionslog/Scenes belegen.
- Breite Sammelklassen sind zulaessig, wenn sie im aktiven Handel, in Fraktionsinventaren oder Markt-SSOTs bereits als eigener Gueterkorridor benannt werden und noch keine feinere Packliste belastbar ist.

Unique-Items (Empfehlung)
-------------------------
- Einzigartige Items bleiben im `Waren-Index` sichtbar, sollen aber konsequent mit Tag `einzigartig` geführt werden.
- Für KI-Runtime und Suche ist ein dedizierter Ableger `Unique-Waren-Index.md` sinnvoll, sobald mindestens 8-10 eindeutige Unikate mit eigener Historie vorliegen.
- Bis dahin: eine Quelle (`Waren-Index`) beibehalten und den Unique-Ableger erst als gefilterte Sicht ergänzen, um Drift zu vermeiden.

Kurzübersicht (menschlich lesbar)
---------------------------------
- Kugeln (neu) [kugeln-neu] — Währung; 1 neu ≈ 10 gebraucht
- Kugeln (gebraucht) [kugeln-gebraucht] — Alltagswährung; Qualität streut
- Energiezelle (Standard) [energiezelle-standard]
- Luftfilter (Gasmasken) [luftfilter-gasmasken]
- Luftfilter (Einrichtungen) [luftfilter-einrichtungen]
- Wasserfilter (portabel) [wasserfilter-portabel]
- Filtermaterial (stationaere Filteranlagen) [filtermaterial-stationaer]
- Werkzeugtasche (Fundstueck) [werkzeugtasche-fundstueck]
- Messausruestung (allgemein) [messausruestung]
- Statikpruef-Set (Tunnel) [statikpruefset]
- Funkausruestung (stabil) [funkausruestung]
- Sensoren-Set (Monitoring) [sensoren-set]
- Gasmaske [gasmaske]
- Atemschutz (funktionstuechtig) [atemschutz]
- Atemfilter [atemfilter]
- Werkzeugkit [werkzeugkit]
- Ersatzteile-Set [ersatzteile-set]
- Akkuzelle (geladen) [akkuzelle]
- Rationen [rationen]
- Wasser (Trinkwasser) [wasser-trink]
- Lampe (betriebsbereit) [lampe]
- Multimeter [multimeter]
- Union-Ersatzteilkiste [union-ersatzteilkiste]
- Filterkartusche (leer) [filterkartusche-leer]
- Ersatzrohr [ersatzrohr]
- Ventilkomponente [ventilkomponente]
- Kabelspule [kabelspule]
- Schmieroel [schmieroel]
- Strommodul [strommodul]
- Wasserkanister [wasserkanister]
- Wasserflasche [wasserflasche]
- Wartungsschluessel [wartungsschluessel]
- Druckmesser [druckmesser]
- Schweissgeraet [schweissgeraet]
- Sensorpaket [sensorpaket]
- Schutzanzug [schutzanzug]
- Ersatzmaske [ersatzmaske]
- Schaltplaene & technische Doku [schaltplaene-technische-doku]
- Reparaturstation (defekt) [reparaturstation-defekt]
- Artefakt 7A [artefakt-7a]
- Datenkern (stationaer) [datenkern-stationaer]
- Datenkern (tragbar) [datenkern-tragbar]
- Adapter DN60 [adapter-dn60]
- Schweißausrüstung (kompakt) [schweissausruestung-kompakt]
- Werkzeugsatz (Mechanik) [werkzeugsatz-mechanik]
- Hydrofilter-Behälter [hydrofilter-behaelter]
- Medkit (Standard) [medkit-standard]
- Verbandmaterial (Set) [verbandmaterial-set]
- Desinfektionsmittel [desinfektionsmittel]
- Antibiotika (Basis) [antibiotika-basis]
- Schmerzmittel (Basis) [schmerzmittel-basis]
- Sicherungssatz [sicherungssatz]
- Dichtungsmanschette [dichtungsmanschette]
- Kabelanschnitt [kabelanschnitt]
- Kühlmittel (Industrie) [kuehlmittel-industrie]
- Lagerfett (Technik) [lagerfett-technik]
- Druckluftkartusche [druckluftkartusche]
- Metallprofil (lang) [metallprofil-lang]
- Metallprofil (mittel) [metallprofil-mittel]
- Metallprofil (kurz) [metallprofil-kurz]
- Stuetzklemme [stuetzklemme]
- Lasche / Knotenblech [lasche-knotenblech]
- Ausgleichsplatte [ausgleichsplatte]
- Klebmasse (schwach) [klebmasse-schwach]
- Schraubensatz (mittel) [schraubensatz-mittel]
- Bolzen-Mutter-Satz (stark) [bolzen-mutter-satz-stark]
- Schienenprofil [schienenprofil]
- Betonplatte [betonplatte]
- Notdecke [notdecke]
- Wechselkleidung (Set) [wechselkleidung-set]
- Hygienepaket (Basis) [hygienepaket-basis]
- Kochgeschirr (Set) [kochgeschirr-set]
- Nahrungsmittel (Grundbedarf) [nahrungsmittel-grundbedarf]
- Grundbedarfsgueter [grundbedarfsgueter]
- Rohmaterialien [rohmaterialien]
- Medizinische Gueter [medizinische-gueter]
- Informationsgueter [informationsgueter]
- Tarn-/Signaltechnik [tarn-signaltechnik]
- Batterien [batterien]

Links
-----
- Baseline-Preise → ../04-inventory/Marktpreise-inventar.md
- Währung (Kugeln) → ./Reference-Campaign-State.md
- Missionslog (Belege) → ./Missionslog.md
- Konfliktliste (Kontext/Decisions) → ./Curated-Konfliktliste.md
