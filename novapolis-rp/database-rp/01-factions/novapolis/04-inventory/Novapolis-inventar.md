---
stand: 2026-04-20 21:22
update: Das Fraktionsinventar fuehrt Novapolis jetzt im Delta-/Bilanzformat; der D5->C6-Lauf ist als belegte Prozessspur mit Verantwortlichen und Empfangsbestaetigung verankert.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260420_210436.md
canvas: Inventar Novapolis
last_updated: 2026-03-31T08:46:44+02:00
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

Delta-/Bilanzformat (belegt)
----------------------------

Transfer
--------

| Status | Von | Nach | Warengruppe | Menge | Prozessanker | Verantwortliche | Beleg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| belegt, mengenoffen | D5-Materiallager unter Bahnsteig und/oder Werkstattbestand | C6-Empfang -> Baustellenverteilung | `Bauteile`, `Werkzeuge`, `Versorgungsgueter` | `tbd` | `Entnahme/Packen -> Abmeldung in D5 -> manueller Transport mit ReflexAssist -> Eintreffen in C6 -> Bestandsaufnahme -> Empfangsbestaetigung` | Ronja Kerschner, Reflex | `RAW-chat-export-2025-10-27T09-16-00-188Z.txt`, `RAW-canvas-2025-10-16T13-05-00-000Z.txt`, [Missionslog-Novapolis](../05-projects/Missionslog-Novapolis.md) |
| belegt, richtungsoffen | C6 | D5 | `Materialrueckfuehrung` | `tbd` | generischer Ruecklauf im RAW-Logistikcanvas | `tbd` | `RAW-canvas-2025-10-16T13-05-00-000Z.txt`, [Logistik](../../../00-admin/Logistik.md) |

Verbrauch
---------

| Status | Zeitraum | Delta | Menge | Standortsplit | Beleg |
| --- | --- | --- | --- | --- | --- |
| belegt | Tag 12 -> 13 | Baustoffe | `1,3 t` | `Verbrauchsort C6-/Nordlinie-Baustellenumfeld; D5-Quellabgang je Posten bleibt tbd` | `database-curated/staging/chat-export.normalized.txt`, [Missionslog-Novapolis](../05-projects/Missionslog-Novapolis.md) |
| belegt | Tag 12 -> 13 | Schienenprofil | `120 m` | `Verbrauchsort C6-/Nordlinie-Baustellenumfeld; D5-Quellabgang je Posten bleibt tbd` | `database-curated/staging/chat-export.normalized.txt`, [Missionslog-Novapolis](../05-projects/Missionslog-Novapolis.md) |
| belegt | Tag 12 -> 13 | Betonplatten | `18 m2` | `Verbrauchsort C6-/Nordlinie-Baustellenumfeld; D5-Quellabgang je Posten bleibt tbd` | `database-curated/staging/chat-export.normalized.txt`, [Missionslog-Novapolis](../05-projects/Missionslog-Novapolis.md) |
| belegt | Tag 12 -> 13 | Beschaedigte Werkzeuge | `2` | `Schadensort C6-/Nordlinie-Baustellenumfeld; D5-Quellabgang je Posten bleibt tbd` | `database-curated/staging/chat-export.normalized.txt`, [Missionslog-Novapolis](../05-projects/Missionslog-Novapolis.md) |

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

Bedarf (belegt, noch nicht gedeckt)
-----------------------------------

- D5: Schweißausrüstung sowie Adapter/Fitting `DN60` bleiben priorisierter Bedarf ohne belastbaren lokalen Bestand. Quelle: [D5-inventar](./D5-inventar.md).
- C6: Adapter/Fittings `DN60`, Schweißausrüstung und belastbare Lagerstruktur bleiben offener Bedarf fuer Betriebsaufnahme und Reparatur. Quelle: [C6-inventar](./C6-inventar.md).
- Fraktionsweit: harte Restmengen fuer D5/C6 bleiben `tbd`, bis Verbrauch, Zielseite und Ruecklauf nicht mehr nur prozessuell, sondern auch mengenmaessig belegt sind.

Offene Restmengen
-----------------

- Harte Fraktionssummen bleiben `tbd`, solange D5/C6 nur Fruehanker plus Prozesskette, aber keine vollstaendige Mengenbuchung fuehren.
- Der standortscharfe Split des Materialverbrauchs Tag 12 -> 13 ist konservativ als `C6-/Nordlinie-Baustellenumfeld` bei D5-seitiger Quell-/Transferlast lesbar; offen bleiben die konkrete D5-Abbuchung je Posten und der konkrete C6-Lagerabgang.
- Konkrete C6-Einlagerung zwischen Primaer- und Sekundaerlager bleibt `tbd`.

Links
-----
- Logistik-Policy C6 → ../03-locations/C6-Logistik-Policy.md
- Logistik (Admin) → ../../../00-admin/Logistik.md
- Missionslog → ../05-projects/Missionslog-Novapolis.md
- Währung "Kugeln" (Reference) → ../../../00-admin/Reference-Campaign-State.md


