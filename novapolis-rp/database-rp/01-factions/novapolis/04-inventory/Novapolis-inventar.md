---
stand: 2026-04-29 00:47
update: Das Fraktionsinventar fuehrt jetzt zusaetzlich den konservativen Betriebskorridor T0 fuer D5, C6 und den aktiven D5-C6-Pfad.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260427_022916.md
canvas: Inventar Novapolis
last_updated: 2026-04-27T02:24:00+02:00
category: inventory
slug: novapolis-inventar
owner: novapolis
scope: faction
version: "0.1"
---
Inventar - Novapolis (Fraktion)
================================

Hinweis: Fraktionsinventare strikt getrennt (Policy Y.1). Abrechnung im Wochenzyklus.

- Transfers zwischen D5 und C6 nur via Mission/Logistik.
- Waehrung "Kugeln" wird als Inventar-Item gefuehrt (neu/gebraucht).

Betriebskorridor T0
-------------------

- Das konservative Betriebsmodell fuehrt `D5` als aktive Kernbasis, `C6` als teilaktiven Aussenposten und `D5 <-> C6` als belegten Arbeitskorridor desselben Novapolis-Blocks; siehe [novapolis-betriebsmodell-t0](../00-doctrine/novapolis-betriebsmodell-t0.md) und [novapolis-nahraum-t0](../00-doctrine/novapolis-nahraum-t0.md).
- Inventarseitig folgt daraus: belastbar sind D5 als Fraktionskern, C6 als Verbrauchs- und Stagingschwerpunkt und der Transferpfad dazwischen; `E3` begruendet weiterhin kein aktives Inventarcluster.

Delta-/Bilanzformat (belegt)
----------------------------

Transfer
--------

| Status | Von | Nach | Warengruppe | Menge | Prozessanker | Verantwortliche | Beleg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| belegt, mengenoffen | D5-Materiallager unter Bahnsteig und/oder Werkstattbestand | C6-Empfang -> Bestandsaufnahme -> C6-Staging -> Baustellenverteilung | `Bauteile`, `Werkzeuge`, `Versorgungsgueter` | `tbd` | `Entnahme/Packen -> Abmeldung in D5 -> manueller Transport mit ReflexAssist -> Eintreffen in C6 -> Bestandsaufnahme -> Empfangsbestaetigung -> spaeterer Baustellenabgang nach Personaleinteilung` | Ronja Kerschner, Reflex | `RAW-chat-export-2025-10-27T09-16-00-188Z.txt`, `RAW-canvas-2025-10-16T13-05-00-000Z.txt`, [Missionslog-Novapolis](../05-projects/Missionslog-Novapolis.md) |
| review, klein aber konkret | D5-Stuetzbaukasten / Werkstattbestand | D5-seitiger Nordlinie-Abschnitt | `Stuetzbaukasten-Komponenten` | `2x metallprofil-mittel, 4x metallprofil-kurz, 4x stuetzklemme, 2x lasche, 2x ausgleichsplatte, 4x schraubensatz, 1x bolzen-mutter-satz, 1x klebmasse` | `Werkstattvorbereitung -> kleiner Turn-7-Abgang -> Tragen/Setzen im Tunnel` | Jonas Merek, Pahl Brenner, Ronja Kerschner, Reflex | [Nordlinie-01](../05-projects/Nordlinie-01.md), `database-curated/staging/rp-runtime/sessions/d5-c6-nordlinie-sanierung-01/scene-log.md` |
| belegt, richtungsoffen | C6 | D5 | `Materialrueckfuehrung` | `tbd` | generischer Ruecklauf im RAW-Logistikcanvas | `tbd` | `RAW-canvas-2025-10-16T13-05-00-000Z.txt`, [Logistik](../../../00-admin/Logistik.md) |

Verbrauch
---------

| Status | Zeitraum | Delta | Menge | Standortsplit | Beleg |
| --- | --- | --- | --- | --- | --- |
| belegt | Tag 12 -> 13 | Baustoffe | `1,3 t` | `Verbrauchsort C6-/Nordlinie-Baustellenumfeld; D5-Quellabgang je Posten bleibt tbd` | `database-curated/staging/chat-export.normalized.txt`, [Missionslog-Novapolis](../05-projects/Missionslog-Novapolis.md) |
| belegt | Tag 12 -> 13 | Schienenprofil | `120 m` | `Verbrauchsort C6-/Nordlinie-Baustellenumfeld; D5-Quellabgang je Posten bleibt tbd` | `database-curated/staging/chat-export.normalized.txt`, [Missionslog-Novapolis](../05-projects/Missionslog-Novapolis.md) |
| belegt | Tag 12 -> 13 | Betonplatten | `18 m2` | `Verbrauchsort C6-/Nordlinie-Baustellenumfeld; D5-Quellabgang je Posten bleibt tbd` | `database-curated/staging/chat-export.normalized.txt`, [Missionslog-Novapolis](../05-projects/Missionslog-Novapolis.md) |
| belegt | Tag 12 -> 13 | Beschaedigte Werkzeuge | `2` | `Schadensort C6-/Nordlinie-Baustellenumfeld; D5-Quellabgang je Posten bleibt tbd` | `database-curated/staging/chat-export.normalized.txt`, [Missionslog-Novapolis](../05-projects/Missionslog-Novapolis.md) |

Projektbuchungen (konservativ, 2026-04-27)
------------------------------------------

| Status | Projekt | Quelle | Bindung / Transfer | Einsatz / Verbrauch | Reststand |
| --- | --- | --- | --- | --- | --- |
| review | Nordlinie 01 | D5-Stuetzbaukasten | `2x metallprofil-mittel, 4x metallprofil-kurz, 4x stuetzklemme, 2x lasche, 2x ausgleichsplatte, 4x schraubensatz, 1x bolzen-mutter-satz, 1x klebmasse` | `2x mittel, 3x kurz, 4x klemme, 2x lasche, 1x ausgleichsplatte, 3x schraubensatz, 1x bolzen-mutter-satz, 1x klebmasse` im Turn-7-Zug eingesetzt | Tunnelrest vor Ort: `1x metallprofil-kurz, 1x ausgleichsplatte, 1x schraubensatz`; D5-Rest siehe [D5-inventar](./D5-inventar.md) |
| review | Draisine-Transportmodul | D5-Werkstattbestand | `1x schmieroel, 1x lagerfett, 1x sicherungssatz, 1x dichtungsmanschette` im Prototyp gebunden | noch kein Feldverbrauch, aber Werkstattbestand ist dem Prototyp zugeordnet | verfuegbarer D5-Rest: `3x schmieroel, 2x lagerfett, 3x sicherungssatz, 5x dichtungsmanschette` |

Verbrauchsrahmen gesamt (konservativ, offene Projekte)
------------------------------------------------------

Hinweise

- Harte Fraktionssummen bleiben jenseits der aktuell gebuchten Kleinmengen weiter `tbd`; der folgende Rahmen beschreibt den derzeit beleg- und arbeitsnahen Gesamtdruck.
- Offene Projekte im Sinn dieses Rahmens sind [Nordlinie-01](../05-projects/Nordlinie-01.md) und [Draisine-Transportmodul](../05-projects/Draisine-Transportmodul.md).

Stationen

| Status | Bereich | Rhythmus | Konservativer Verbrauch | Fraktionslesart |
| --- | --- | --- | --- | --- |
| review | D5 Basisbetrieb | pro Tag | `3-4` Rationenaequivalente, `1` Wasserkanister, geringe Hygiene-/Mednutzung | D5 bleibt stabiler Kern, verliert unter Druck zuerst Reserve und Redundanz |
| review | C6 Basisbetrieb | pro Tag | `8-12` Rationen aus Reserve-/Schnellverpflegung, `1-2` Wasserkanister plus `6-10` Wasserflaschen mobile Reserve | C6 ist der klare Verbrauchsschwerpunkt der Fraktion |

Offene Projekte

| Status | Projekt | Rhythmus | Konservativer Verbrauch | Fraktionslesart |
| --- | --- | --- | --- | --- |
| belegt plus review | Nordlinie 01 | belegter Bautag und laufende Sicherungsbloecke | belegt: `1,3 t Baustoffe`, `120 m Schienenprofil`, `18 m2 Betonplatten`, `2` beschaedigte Werkzeuge; laufend review: D5-seitig kleiner Stuetzbaukasten, C6-seitig Schutz-/Verschleissgut | Nordlinie bleibt der groesste materielle Verbrauchstreiber |
| review | Draisine-Transportmodul | je Werkstattblock | `0-1` Schmieroel, `0-1` Lagerfett, `0-1` Sicherungssatz; episodisch `0-1` Dichtungsmanschette oder `Kabelanschnitt` | kleiner, aber stetiger Werkstattdruck auf D5-Technikposten |

Fraktionsverbrauch (arbeitsnaher Gesamtblick)

| Status | Bereich | Aussage | Beleg |
| --- | --- | --- | --- |
| review | Versorgung | Der hoechste laufende Fraktionsverbrauch sitzt aktuell nicht in D5, sondern in C6 als Kombination aus Personenlast, Evakuierungsfolge und Baustellennaehe. | [C6-inventar](./C6-inventar.md), [C6](../03-locations/C6.md) |
| review | Bau / Technik | Der groesste materielle Projektdruck sitzt in Nordlinie plus dem kleineren, aber konstanten D5-Werkstattdruck der Draisine. | [Nordlinie-01](../05-projects/Nordlinie-01.md), [Draisine-Transportmodul](../05-projects/Draisine-Transportmodul.md) |
| review | Gesamt | Novapolis verbraucht aktuell verteilt: D5 langsam-stabil im Basisbetrieb, C6 schnell-angespannt in Reserveguetern, Nordlinie hoch bei Baustoff und Werkzeugverschleiss, Draisine niedrig bis mittel bei Technikposten. | [D5-inventar](./D5-inventar.md), [C6-inventar](./C6-inventar.md) |

Bilanz
------

| Status | Konto | Delta | Vor-/Nachher-Stand | Beleg |
| --- | --- | --- | --- | --- |
| belegt | Novapolis gesamt - Energiezellen | `-12 Nettoverlust` | `tbd` | `database-curated/staging/chat-export.normalized.txt`, [Logistik](../../../00-admin/Logistik.md) |
| belegt | D5 Energiefluss | `+10 Produktion - 8 Grundlast - 12 Export = -10` | `tbd` | [D5-inventar](./D5-inventar.md), [Logistik](../../../00-admin/Logistik.md) |
| belegt | C6 Energiefluss | `+10 Zufuhr - 12 Verbrauch = -2` | `tbd` | [C6-inventar](./C6-inventar.md), [Logistik](../../../00-admin/Logistik.md) |

Handel
------

| Status | Item / Klasse | Menge | Notiz | Beleg |
| --- | --- | --- | --- | --- |
| belegt, mengenoffen | Kugeln (neu) | `tbd` | hochwertiges Fraktions-Item; `1 neu ≈ 10 gebraucht` | `database-curated/staging/chat-export-complete.finalgate.md`, [Logistik](../../../00-admin/Logistik.md) |
| belegt, mengenoffen | Kugeln (gebraucht) | `tbd` | Alltags-/Hauptmunition, Qualitaet streut | `database-curated/staging/chat-export-complete.finalgate.md`, [Logistik](../../../00-admin/Logistik.md) |
| belegt, mengenoffen | Nahrungsmittel (Grundbedarf) | `tbd` | belegte Importklasse im H-47-/C6-Aufbaupfad; noch ohne Packliste oder Stationssplit | [Relationslog-Novapolis](../06-handel-diplomatie/Relationslog-Novapolis.md), [Haendlerbund-inventar](../../haendlerbund/04-inventory/Haendlerbund-inventar.md) |
| belegt, mengenoffen | Grundbedarfsgueter | `tbd` | breite Importklasse fuer alltaegliche Versorgungsware im H-47-/C6-Austauschpfad | [Relationslog-Novapolis](../06-handel-diplomatie/Relationslog-Novapolis.md), [Haendlerbund-inventar](../../haendlerbund/04-inventory/Haendlerbund-inventar.md) |

Bedarf (belegt, noch nicht gedeckt)
-----------------------------------

- D5: Schweißausrüstung sowie Adapter/Fitting `DN60` bleiben priorisierter Bedarf ohne belastbaren lokalen Bestand. Quelle: [D5-inventar](./D5-inventar.md).
- C6: Adapter/Fittings `DN60`, Schweißausrüstung und belastbare Lagerstruktur bleiben offener Bedarf fuer Betriebsaufnahme und Reparatur. Quelle: [C6-inventar](./C6-inventar.md).
- Fraktionsweit: harte Restmengen fuer D5/C6 bleiben `tbd`, bis Verbrauch, Zielseite und Ruecklauf nicht mehr nur prozessuell, sondern auch mengenmaessig belegt sind; das gilt auch fuer die Importklassen `Nahrungsmittel (Grundbedarf)` und `Grundbedarfsgueter`.
- Fraktionsweit: Der Verbrauchsrahmen ist jetzt fuer den kleinen Nordlinie-Turn-7-Satz und die aktuelle Draisine-Werkstattbindung in konkrete Abgaenge und Reststaende gezogen; die vollstaendige Summenbuchung ueber alle Folgezuege bleibt offen.

Offene Restmengen
-----------------

- Harte Fraktionssummen bleiben `tbd`, solange D5/C6 nur Fruehanker plus Prozesskette, aber keine vollstaendige Mengenbuchung fuehren.
- Der standortscharfe Split des Materialverbrauchs Tag 12 -> 13 ist konservativ als `C6-/Nordlinie-Baustellenumfeld` bei D5-seitiger Quell-/Transferlast lesbar; offen bleiben die konkrete D5-Abbuchung je Posten und der konkrete C6-Lagerabgang.
- Konkrete C6-Einlagerung zwischen Primaer- und Sekundaerlager bleibt `tbd`.
- Harte Fraktionssumme ueber alle offenen Projekte bleibt `tbd`, auch wenn der kleine Nordlinie-Turn-7-Satz und die aktuelle Draisine-Werkstattbindung jetzt konkret gebucht sind; offen bleiben weitere Folgezuege, Ruecklaeufe und der historische Split groesserer Baustoffmengen.

Links
-----
- Logistik-Policy C6 → ../03-locations/C6-Logistik-Policy.md
- Logistik (Admin) → ../../../00-admin/Logistik.md
- Missionslog → ../05-projects/Missionslog-Novapolis.md
- Währung "Kugeln" (Reference) → ../../../00-admin/Reference-Campaign-State.md


