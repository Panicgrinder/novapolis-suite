---
stand: 2026-04-17 01:04
update: Der Start-Chooser bindet jetzt auch Spielhauptmenue und Charakterstart als OOC-Vorschaltpfad an die RP-Startanker bei slot_00.
checks: snapshot-lock PASS (2026-04-17 01:04); markdownlint=PASS; frontmatter=PASS
---

RP Start-Chooser SSOT
=====================

Zweck
-----

Diese SSOT definiert, wie der spaetere Produktpfad mehrere Startoptionen anbietet, ohne ueber die aktuelle Beleglage hinauszugehen.

- Sie ersetzt keine Lore- oder Orts-SSOT.
- Sie ist die verbindliche Auswahl- und Freigabeschicht zwischen Produkt-UI, RP-SSOT und spaeterer Spielleiter-Orchestrierung.

Quellenbasis
------------

- `novapolis-rp/database-rp/00-admin/Fraktionen-Taxonomie.md`
- `novapolis-rp/database-rp/00-admin/Stationskontroll-Matrix.md`
- `novapolis-rp/database-rp/00-admin/Metrokarte-T0.md`
- `novapolis-rp/database-rp/04-inventory/Freie-Gruppen-inventar.md`
- `novapolis-dev/docs/process/rp-text-rpg-startpaket-slot-00-05-2026-04-05.md`
- `novapolis-dev/docs/specs/text-rpg-session-contract-v1.md`
- `novapolis-dev/docs/process/rp-startbogen-novapolis-d5.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-novapolis-c6.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-arkologie-a1.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-schienenbund-b2.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-eisenkonklave-h12.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-schattenbund-f9.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-fluesterkollektiv-k4.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-freie-gruppen-a2.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-freie-gruppen-b1.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-freie-gruppen-c1.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-freie-gruppen-c3.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-freie-gruppen-d1.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-freie-gruppen-e2.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-freie-gruppen-f1.ssot.md`
- `novapolis-dev/docs/process/rp-startbogen-haendlerbund-g7.ssot.md`

Grundmodell
-----------

Der Start-Chooser trennt vier Ebenen:

1. Startmodus
2. Startbereich
3. Startdichte
4. Sichtbarkeits- und Reveal-Regel

Startmodi
---------

### `novapolis_default`

- Beschreibung: dichter Default-Slice um Ronja/Reflex in D5.
- Status 2026-04-05: voll tragfaehig mit eigener Start-SSOT `novapolis_d5`.

### `faction_start`

- Beschreibung: Start in einem realen Fraktionskern.
- Status 2026-04-05: fuer alle aktuell freigegebenen Kernstationen mit Startbogen belegt.
- Eigenstaendiger Novapolis-Fraktionsstart vorhanden: `novapolis_c6`.
- Aktuell konkrete Startboegen vorhanden: `haendlerbund_g7`, `arkologie_a1`, `schienenbund_b2`, `eisenkonklave_h12`, `schattenbund_f9`, `fluesterkollektiv_k4`.

### `factionless_start`

- Beschreibung: Start ohne feste Fraktionsbindung unter `Freie Gruppen`.
- Status 2026-04-05: mehrere konkrete Neutralstarts vorhanden.
- Aktuell konkrete Startboegen vorhanden: `freie_gruppen_a2`, `freie_gruppen_b1`, `freie_gruppen_c1`, `freie_gruppen_c3`, `freie_gruppen_d1`, `freie_gruppen_e2`, `freie_gruppen_f1`.

### `neutral_start`

- Beschreibung: Start in einer neutralen Transit- oder Pufferstation.
- Status 2026-04-05: als Gebietsklasse aktiv; konkrete spielbare Auspraegung derzeit ueber `freie_gruppen_a2`, `freie_gruppen_b1`, `freie_gruppen_c1`, `freie_gruppen_c3`, `freie_gruppen_d1`, `freie_gruppen_e2` und `freie_gruppen_f1` belegt.

Gebietswahl
-----------

Der Startbereich wird getrennt vom Startmodus gewaehlt.

### Gebietsklassen

- `faction_core`: fraktionskontrollierte Kernstation
- `neutral_transit`: neutrale Transit- oder Pufferstation
- `subarea`: lokaler Unterbereich innerhalb eines Startgebiets

### Aktuell freigegebene Kerngebiete

- Novapolis: `D5`, `C6`, `E3`
- Haendlerbund: `G7`
- Arkologie-A1: `A1`
- Schienenbund: `B2`
- Eisenkonklave: `H12`
- Schattenbund: `F9`
- Fluesterkollektiv: `K4`

### Aktuell freigegebene neutrale Gebiete

- `A2`, `B1`, `C1`, `D1`, `E2`, `F1`, `G3`

### Aktuell freigegebene Unterbereiche

- `D5-Werkstatt`
- `D5-Funkraum`
- `C6-Schleuse`
- `C6-Lagerhalle`

Dichtegrad
----------

### `full_slice`

- Eigener Startbogen vorhanden
- Startkern, Stakes, erster Entscheidungsraum und Anschluss an Reveal-Regeln vorhanden
- Beispiel: `novapolis_d5`, `haendlerbund_g7`, `freie_gruppen_a2`, `freie_gruppen_b1`

### `framing_start`

- Fraktion und Gebiet belegt, aber lokaler Startbogen noch nicht ausformuliert
- Darf im Produkt erscheinen, muss aber als begrenzte Tiefe oder "im Aufbau" markiert werden
- Beispiel: reservierte oder spaeter freigegebene Kerne ohne Startbogen

### `locked`

- Gebiet theoretisch im T0-Modell vorhanden, aber noch ohne Startfreigabe
- Darf noch nicht als vollwertige Auswahl angeboten werden

Sichtbarkeit und Reveal
-----------------------

Die Startauswahl aendert nicht die globalen Reveal-Regeln.

- `pc_visible`: direkter Einstiegstext, unmittelbare Optionen, sichtbare Gefahren
- `allies_only`: vertrauliche Gruppen- oder Funk-/Log-Informationen
- `world_only`: verdeckte Welt- und SL-Informationen
- `rumor`: ungesicherte Geruechte, Signalrauschen, nicht verifizierte Hinweise

Produktregeln fuer die Auswahl
------------------------------

1. Jeder angezeigte Start braucht einen belegten Stations- oder Fraktionsanker.
2. Ein `full_slice` braucht einen eigenen Startbogen.
3. Ein `framing_start` darf keine Scheintiefe vortaeuschen.
4. Ein `factionless_start` muss auf `Freie Gruppen` oder einen gleichwertigen fraktionslosen SSOT-Anker zeigen.
5. Gebietswahl bleibt an reale Kontroll- und Topologie-SSOTs gebunden.

Vertragsanker fuer Sim-Voraufbau
--------------------------------

- Der Start-Chooser ist nur die Freigabeschicht fuer kanonische RP-Startanker; er ist kein freier Sprunggenerator in beliebige spaetere Slots oder Weltbereiche.
- Jeder freigegebene Start muss auf denselben Sessionvertrag zeigen und deshalb mindestens mit `campaign_id`, `scene_id`, `slot_id` und belegtem Startgebiet verknuepfbar sein.
- Produktive Neueinstiege fuer den Sim-vor-RP-Pfad starten auf den RP-Ankern des Startpakets bei `slot_00`; spaetere Resume-Einstiege hinter `slot 30` laufen ueber den Slice-2-Handover und nicht ueber den Start-Chooser.
- Die Weltbindung des Starts bleibt auf die durch Startbogen, Reveal-Matrix und Topologie belegten Gebiete beschraenkt; der Chooser darf keine freie Parallelkontinuitaet zu nicht belegten Raeumen erzeugen.

Produktiver Einstiegsfluss
--------------------------

- Der Start-Chooser liegt fachlich im Spielhauptmenue hinter dem Hub und nicht direkt auf der Operator-Oberflaeche.
- Neueinstieg bedeutet deshalb: `Hub -> Spielhauptmenue -> Start-Chooser -> RP-Startanker bei slot_00`.
- Wenn fuer den gewaehlten RP-Startanker noch keine laufende Figur oder Session existiert, fuehrt derselbe Pfad zuerst in einen OOC-Charakterstart statt direkt in eine Inworld-Szene.
- Dieser OOC-Charakterstart bleibt auf den minimalen Produktumfang beschraenkt: Startoption, Schwierigkeitsgrad und Bindung an den gewaehlten RP-Startanker.
- Der Charakterstart erzeugt keine freie Vorszene und keinen Parallel-Slot vor `slot_00`, sondern bereitet nur denselben kanonischen Neueinstieg fuer das Startpaket vor.

Freigegebene Startkandidaten 2026-04-05
---------------------------------------

| Key | Modus | Bereich | Dichtegrad | Belegstatus |
| --- | --- | --- | --- | --- |
| `novapolis_d5` | `novapolis_default` | `D5` | `full_slice` | eigener Startbogen vorhanden |
| `novapolis_c6` | `faction_start` | `C6` | `full_slice` | eigener Startbogen vorhanden |
| `haendlerbund_g7` | `faction_start` | `G7` | `full_slice` | eigener Startbogen vorhanden |
| `freie_gruppen_a2` | `factionless_start` | `A2` | `full_slice` | eigener Startbogen vorhanden |
| `freie_gruppen_b1` | `factionless_start` | `B1` | `full_slice` | eigener Startbogen vorhanden |
| `freie_gruppen_c1` | `factionless_start` | `C1` | `full_slice` | eigener Startbogen vorhanden |
| `freie_gruppen_c3` | `factionless_start` | `C3` | `full_slice` | eigener Startbogen vorhanden |
| `freie_gruppen_d1` | `factionless_start` | `D1` | `full_slice` | eigener Startbogen vorhanden |
| `freie_gruppen_e2` | `factionless_start` | `E2` | `full_slice` | eigener Startbogen vorhanden |
| `freie_gruppen_f1` | `factionless_start` | `F1` | `full_slice` | eigener Startbogen vorhanden |
| `arkologie_a1` | `faction_start` | `A1` | `full_slice` | eigener Startbogen vorhanden |
| `schienenbund_b2` | `faction_start` | `B2` | `full_slice` | eigener Startbogen vorhanden |
| `eisenkonklave_h12` | `faction_start` | `H12` | `full_slice` | eigener Startbogen vorhanden |
| `schattenbund_f9` | `faction_start` | `F9` | `full_slice` | eigener Startbogen vorhanden |
| `fluesterkollektiv_k4` | `faction_start` | `K4` | `full_slice` | eigener Startbogen vorhanden |

Offene Folgearbeit
------------------

- Weitere Neutralstarts jenseits `A2/B1/C1/C3/D1/E2/F1` konkretisieren.
- Sekundaere Stationsstarts jenseits der Kernknoten konkretisieren, z. B. `E3`, `A3`, `F7`, `G6`, `H1`.
