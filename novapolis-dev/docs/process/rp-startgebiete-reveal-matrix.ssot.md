---
stand: 2026-04-05 19:43
update: Die Startgebiete-Matrix deckt jetzt auch die neutralen Startknoten `E2` und `F1` samt F1-Klarstellung im C6-Kontext ab.
checks: snapshot-lock PASS (2026-04-05 19:33); markdownlint PASS; frontmatter PASS
---

RP Startgebiete Reveal Matrix SSOT
==================================

Zweck
-----

Diese SSOT erweitert die Reveal-Logik ueber den Novapolis-Startkorridor hinaus auf die weiteren aktuell freigegebenen Startgebiete `A1`, `B2`, `H12`, `F9`, `K4`, `G7` und `A2` sowie die neutralen Puffer- und Startknoten `B1`, `C1`, `C3`, `D1`, `E2` und `F1`.

Quellenbasis
------------

- `novapolis-dev/docs/process/rp-startbogen-arkologie-a1.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-schienenbund-b2.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-eisenkonklave-h12.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-schattenbund-f9.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-fluesterkollektiv-k4.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-haendlerbund-g7.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-freie-gruppen-a2.ssot.md`
- `novapolis-rp/database-rp/03-locations/A2.md`
- `novapolis-rp/database-rp/03-locations/B1.md`
- `novapolis-rp/database-rp/03-locations/C1.md`
- `novapolis-rp/database-rp/03-locations/C3.md`
- `novapolis-rp/database-rp/03-locations/D1.md`
- `novapolis-rp/database-rp/03-locations/E2.md`
- `novapolis-rp/database-rp/03-locations/F1.md`
- `novapolis-rp/database-rp/01-factions/arkologie-a1/03-locations/A1.md`
- `novapolis-rp/database-rp/01-factions/schienenbund/03-locations/B2.md`
- `novapolis-rp/database-rp/01-factions/eisenkonklave/03-locations/H12.md`
- `novapolis-rp/database-rp/01-factions/schattenbund/03-locations/F9.md`
- `novapolis-rp/database-rp/01-factions/fluesterkollektiv/03-locations/K4.md`
- `novapolis-rp/database-rp/01-factions/haendlerbund/03-locations/G7.md`
- `novapolis-rp/database-rp/00-admin/Stationskontroll-Matrix.md`
- `novapolis-rp/database-rp/00-admin/Metrokarte-T0.md`

Regelkerne
----------

1. `pc_visible` bleibt unmittelbarer Start-, Raum- oder Auftragskontext der jeweiligen Linse.
2. `allies_only` umfasst die interne Leitungs-, Freigabe- und Kanalhygiene der jeweiligen Fraktion.
3. `npc_only` deckt lokale Einzelabsichten und Innenlagen ab, die nicht automatisch in Gruppenwissen uebergehen.
4. `world_only` bleibt Welt- oder Gegenspielerwissen und taucht nie ungefiltert als PC-Fakt auf.
5. `rumor` bleibt unsicher, bis eine bestaetigte Quelle denselben Inhalt hebt.
6. Startgebietsspezifische Mind-Cluster bleiben Rohmaterial fuer SL/NPC-Verhalten und werden nur indirekt ausgespielt.

Reveal-Klassen
--------------

| Klasse | Bedeutung | Zulaessige Ausspielung |
| --- | --- | --- |
| `pc_visible` | direkter Wahrnehmungs-, Auftrags- oder Raumkontext | PC-Text, Optionen, `pc_log` |
| `allies_only` | bestaetigtes Gruppenwissen im Startgebiet | Funk, Freigabe, Log, Besprechung |
| `npc_only` | situative Innenlage einzelner Figuren | NPC-Reaktion, nie roh im PC-Text |
| `world_only` | verdeckte Lage, fremde Ziele, rohe Innenwerte | nur SL, Debug, `world_log` |
| `rumor` | schwaches Signal, Geruecht, ungesicherter Hinweis | als Geruecht markieren, nie als Fakt |

Matrix
------

| Startgebiet | Objekt | Klasse | Reveal-Pfad | Guardrail |
| --- | --- | --- | --- | --- |
| `A1` | Sicherheitsauflagen, Tauschfenster, Vorzone `A2` | `pc_visible` | lokale Ansage, Leitungsbriefing | keine freien Novapolis-Kontakte behaupten |
| `A1` | Validierungs- und Freigabekette zwischen Forschung, Handel und Sicherheit | `allies_only` | Leitungslog, Screeningprotokoll | kein Weltgesetz aus interner Arkologie-Logik machen |
| `A1` | ungepruefte Anomaliedeutungen und Gegenfraktionslesen | `world_only` | nur SL | keine unvalidierten Forschungsdeutungen in PC-Text heben |
| `B2` | Trassenlage `B1 -> B2 -> C3`, Reparaturdruck, Freigabefenster | `pc_visible` | Kommandoknoten, Leitstand, lokale Beobachtung | keine freien Liefermengen oder Diplomatiebeziehungen setzen |
| `B2` | interne Sperr- und Durchsatzlogik | `allies_only` | Leitstand, Betriebslog | Sperrlogik nicht still zu Globalrecht aufblasen |
| `H12` | Schadenskorridor `H3 -> H12`, Handelsfenster, Sicherheitsdruck | `pc_visible` | Kommandobunker, Leitstand, Lagebriefing | keine freien Waffen-, Konvoi- oder Archivlisten setzen |
| `H12` | Kommandokette und konkrete Freigabepfade | `allies_only` | Kommandolog, Sicherheitsfreigabe | keine offenen Kontakte ohne Freigabebeleg |
| `H12` | tiefe Archivziele, unverifizierte Fremdplaene | `world_only` | nur SL | keine Rohziele im PC-Text |
| `F9` | Abschirmung, Beschaffungsdruck, aktiver `G6`-Korridor | `pc_visible` | lokale Beobachtung, Einsatzansage | keine offenen Gegenparteien oder Routen erfinden |
| `F9` | Kanal- und Gegenaufklaerungslogik | `allies_only` | Sicherheitszentrale, Zellbriefing | kein Leak-Verdacht ohne Marker zu Fakt machen |
| `F9` | tiefe Tarnstrukturen und verdeckte Gegenparteien | `world_only` | nur SL | keine Tarnstruktur unmarkiert revealen |
| `K4` | Kontaktfenster, Signalfragen, Freigaben | `pc_visible` | Leitstand, Kanalpruefung, lokale Beobachtung | keine bestaetigten Novapolis-Kontakte ohne Beleg |
| `K4` | Kanaltrennung und Einflussprioritaeten | `allies_only` | interne Kanalhygiene, Freigabelog | keine Netzlogik ohne Quelle nach aussen kippen |
| `K4` | eigentliche Absichten und tiefe Netzlogik | `world_only` | nur SL | keine Zielbilder ohne Validierung |
| `G7` | Route `G7 <-> C6`, Dealfragen, sichtbare Sicherheitsbedenken | `pc_visible` | direkte Beobachtung, Konvoibriefing | keine Manifeste oder Lagersummen behaupten |
| `G7` | interne Konvoilogik und Rueckzugsregeln | `allies_only` | Konvoilog, Crewabsprache | keine stillschweigende Novapolis-Vollintegration |
| `G7` | fremde Langfristziele hinter `H3/H12` | `world_only` | nur SL | keine tiefe Fraktionsabsicht als Fakt ausspielen |
| `A2` | lokale Knappheit, Wegeoptionen, sichtbare Kontakte | `pc_visible` | direkte Beobachtung | keine festen NPC oder A2-Lore ohne Ortsbogen setzen |
| `A2` | erste Gruppenbildung nach aktivem Anschluss | `allies_only` | Kontaktgruppe, Tauschgespraech | kein impliziter Fraktionsbeitritt ohne Entscheidung |
| `A2` | verdeckte Fraktionsabsichten um den Pufferraum | `world_only` | nur SL | keine unsichtbaren Konfliktplaene im PC-Text |
| `A2` | Geruechte ueber sichere Anschluesse `A1` oder `B1` | `rumor` | Geruecht, Transitgespraech | nie als bestaetigten Korridor ausgeben |
| `B1` | neutraler Vorpuffer vor `B2`, partieller Weiterlauf | `pc_visible` | Wegwahl, direkte Beobachtung | keine lokale Crew oder Diplomatie ohne Beleg |
| `B1` | Uebergangslogik zwischen offenem Transit und `B2`-Sperrdruck | `allies_only` | situative Absprache, Reise- oder Kontaktlog | keine implizite Schienenbund-Freigabe annehmen |
| `C1` | aktiver Transit zwischen `C2` und `D1` | `pc_visible` | Wegwahl, direkte Beobachtung | keine feste Schutzstruktur oder Crew ohne Beleg |
| `C1` | situative Reise- und Richtungsabstimmung im offenen Neutralraum | `allies_only` | Reise- oder Tauschabsprachen | keine implizite Stationsordnung annehmen |
| `C3` | teilaktiver Zwischenraum, Mikro-Kollaps-Risiko Richtung `D3` | `pc_visible` | Beobachtung, Wegentscheidung | Hazard nicht frei zu groesserem Ereignis aufblasen |
| `C3` | tieferes Risiko- oder Folgewissen hinter `D3` | `world_only` | nur SL | keine unsichtbaren Anschlusslagen direkt revealen |
| `D1` | aktiver Uebergangsraum vor dem partiellen `D2`-Weiterlauf | `pc_visible` | Wegwahl, direkte Beobachtung | keine Details zu `D2` ohne Beleg vorziehen |
| `D1` | situative Rueckzugs- oder Weiterlaufabstimmung | `allies_only` | Reise- oder Rueckzugsabsprachen | keine stabilen Rechte aus dem Transit ableiten |
| `E2` | aktiver Neutralraum mit geschaedigtem E3-Bezug | `pc_visible` | Beobachtung, Wegwahl, sichtbarer Schadendruck | keine freien Gasunfall- oder E3-Details erfinden |
| `E2` | Warn- und Reiseabsprachen am Schadensaum | `allies_only` | Warnung, Reiseabsprache | keine tieferen Ursachen ohne Quelle als Fakt ausgeben |
| `F1` | realer Neutralraum mit partiellem `F3`-Weiterlauf | `pc_visible` | Beobachtung, Wegwahl | keine Direktverbindung zu C6 behaupten, die T0 nicht traegt |
| `F1` | tiefere Linien- oder Netzkontexte hinter dem C6-Bezug | `world_only` | nur SL | keine unbelegten Netzpfade revealen |

Reveal-Pfade
------------

### Lokale Beobachtung

- Sichtbare Stationsteile, Leitstandsansagen, konkrete Freigaben, unmittelbare Korridorlage.

### Leitungs- und Freigabelog

- Interne Ketten fuer Forschung, Handel, Sicherheit, Transit und Screening.
- Hebt Inhalte nur in den jeweiligen Verbund, nicht automatisch an den PC.

### Konvoi-, Kontakt- und Kanalbriefing

- G7-, K4- und F9-nahe Linien duerfen sichtbare Einsatz- und Kontaktlogik transportieren.
- Kein Briefing ersetzt Sichtbarkeitsmarkierung.

### Geruecht und Signalrauschen

- Unsichere Wege, Kontaktgeruechte, unvalidierte Signale.
- Bleibt sprachlich unsicher und darf nur ueber Bestaetigung steigen.

Verbotene Kurzschluesse
-----------------------

- Kein Mind-Cluster-Rohwert wird in irgendeinem der erweiterten Startgebiete direkt zum PC-Text.
- Kein `rumor` wird ohne Bestaetigung zu `pc_visible` promoted.
- Keine interne Freigabelogik einer Fraktion wird automatisch als globales Systemgesetz behandelt.
- Keine verdeckte Fraktionsabsicht wird allein aus Startprämisse oder Konfliktlabeln direkt revealbar.