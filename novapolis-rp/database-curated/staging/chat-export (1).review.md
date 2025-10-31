# Review – chat-export (1).txt

Quelle: `database-raw/99-exports/chat-export (1).txt`
Status: pending
Erstellt: 2025-10-27

Arbeitsnotizen
- Vermutung: Testexport, potenzielle Doppler und Lücken.
- Querprüfung: Gegen PDF und andere RAW-Exporte (stichprobenartig).
 - Hinweis: Alle Fakten aktuell vorläufig → als [FACT?] markiert und unter [OPEN] zu verifizieren.

Checkliste
- [ ] Grobe Deduplizierung erledigt
- [ ] Normalisierung erstellt (`chat-export (1).normalized.txt`)
- [ ] JSONL erzeugt (`chat-export (1).jsonl`) – optional
- [ ] Extrakte erstellt (Szenen/Fakten)
- [ ] Stichprobe (≥10%) gegen PDF geprüft
- [ ] Offene Punkte dokumentiert ([OPEN])

Szenenanker [SCENE]
- 

Kanon-Fakten [FACT]
- 

Charaktere [CHAR]
- 

Orte [LOC]
- 

Projekte [PROJ]
- 

Inventar [INV]
- 

Offen [OPEN]
- 

## Chunk part-011 (global 10001–10819) – Neueste Nachrichten

- Kontext: Meta-/Recovery-Phase, Fokus auf Canvas-Konsistenz, Fraktionsnamen, Backup und Tagesabschluss.
- Referenz: Nachrichten-ID-Bereich ca. #1765–#1906.

Szenenanker [SCENE]
- [SCENE] Recovery/Debug-Session: Prüfung Fraktionen/Canvas, Backup-Anforderung, Tagesabschluss-Workflow (Msgs ~#1765–#1906, part-011).

Kanon-Fakten [FACT?]
- [FACT?] Vier Hauptfraktionen (vorläufig): 1. Eiserne Enklave, 2. Akologie, 3. Händlerbund, 4. Schienenbund; außerdem „Novapolis“ und „Freie Gruppen“ (Msg #1824).
- [FACT?] D5 (vorläufig): Basis Novapolis; einziger Reaktor in der Metro; U‑Bahn‑Schacht; 100% Zustand; Jonas’ Werkstatt (Geburtsort Reflex); Bewohner u. a. Ronja, Reflex, Jonas, Lumen, Pahl (Msg #1846, Abschnitt „ort 1. d5“).
- [FACT?] C6 (vorläufig): Ehem. Händlerkarawane ansässig; Pilzkulturen/Algen; Strombezug von D5; Kreuzungsstation; Tunnelverbindung D5–C6 in Reparatur; Draisine im Bau (Jonas & Pahl) (Msg #1846, „ort 2. C6“).
- [FACT?] „N7“ soll im Spiel nicht mehr existieren; alle Bezüge löschen/ignorieren (Msg #1846, Klammerhinweis) – vorläufig zu prüfen.
- [FACT?] Baufortschritt Tunnel zuletzt 40% (Msg #1848, Punkt 3) – vorläufig.
- [FACT?] Wissensstand: Aktuell weiß nur Reflex über seine Fähigkeiten Bescheid (Msg #1818) – vorläufig.

Charaktere [CHAR]
- [CHAR] Ronja + Reflex: Exoskelett‑Testlauf; Ronja kann schwere Objekte (Betonpfeiler) heben → Balancing erforderlich (Msg #1814, Einleitung).
- [CHAR] Reflex „Support‑Modus“: Bei exzessiver Nutzung soll Energiebonus entfallen und Verbrauch ansteigen; Speicher/Kapazität als Funktion der Masse (Msg #1814, Vorschlag).
- [CHAR] Reflex‑Instanzen: Einheitliche Speicherlogik (Masse ~ Kapazität), aber andere Hauptfähigkeiten für die zwei weiteren Instanzen (Msg #1816).

Orte [LOC]
- [LOC] D5: siehe FACT oben; „Stationen‑Canvas“ D5/C6 auf Version 0.9 markieren (Msg #1856–#1860).
- [LOC] C6: siehe FACT oben; direkte Koppelung an D5 über Energieversorgung und Tunnel.

Projekte [PROJ]
- [PROJ] Nordlinie/Tunnel D5–C6: 40% Fortschritt; Rechenmethodik zur Tagesleistung diskutiert (Msgs #1804–#1808, #1848).
- [PROJ] Konsistenzprüfung Missionsfortschritt und Ressourcenkonten (Msg #1804, #1810–#1812).

Inventar/Verbrauch [INV]
- [INV] Energieverbrauchsfrage: „Energie D5 -8 / C6 -12“ → Klärung/Validierung erforderlich (Msg #1806, Punkt 1.1).

Offen/Prüfaufträge [OPEN]
- [OPEN] Canvas‑Drift/Umbenennungen prüfen: Fraktions‑ und Canvas‑Namen (Schatten/Lumen etc.), interne Flags, archivierte Versionen getrennt laden (Msgs #1768–#1774, #1822–#1826).
- [OPEN] Zeit-/Datumsinkonsistenzen prüfen: „letztes eines Tages“ vs. „nächstes des Folgetags“ (Msg #1798).
- [OPEN] Vollständiger Canvas‑Reload (inkl. Archiv) und Abgleich gegen Gesprächsverlauf/Kontext (Msgs #1820, #1866–#1871).
- [OPEN] Erstellung „unumstößlicher“ Kanon‑Canvas mit Priorität 1 (Msg #1846 Einleitung; „wird immer zuerst geladen“).
- [OPEN] Backup/Export: Gesamter Chat als Markdown/JSON; ZIP‑Paket; Zählung der Nachrichten; Persistenz nach Kontext‑Reset verifizieren (Msgs #1875–#1906).

## Chunk part-022 (global 10501–10819) – Neueste Nachrichten (II)

- Kontext: Administrative Konsolidierung, Sicherungen/Exporte, Wiederherstellungsschritte, Setup für weitere Prüfung.
- Referenz: Nachrichten-ID-Bereich ca. #1849–#1906.

Szenenanker [SCENE]
- [SCENE] Sicherungs-/Exportphase: „freigegeben“, Speichern/Neu‑Laden, Kontext‑Reset, Erstellung von Markdown‑ und JSON‑Sicherungen, ZIP‑Paket (Msgs #1850, #1879–#1906).
- [SCENE] Vorbereitende Canvas‑Arbeit: Stations‑Canvas D5/C6 laden und auf 0.9 markieren; person_index_np laden; Logistik/Mission „Tunnel“ laden (Msgs #1854–#1863).
- [SCENE] „Agent Mode“ aktiviert; Wunsch nach Wiedereinstiegspunkt nach Troubleshooting (Msg #1864).

Kanon-Fakten [FACT?]
- [FACT?] Es existieren Stations‑Canvas für D5 und C6; gewünschter Status: Version 0.9 (Msgs #1854–#1860).
- [FACT?] person_index_np ist ein existierendes Personenverzeichnis/Index (Msg #1856).
- [FACT?] Eigenständige Canvas „Logistik“ und „Mission Tunnel“ sind vorgesehen (Msg #1862).
- [FACT?] Geplante/erforderte Sicherungen: eine Markdown‑Sicherung aller Canvas (inkl. archivierter), eine Chat‑Zusammenfassung, eine Rohfassung des gesamten Chatverlaufs, sowie JSON‑Splits (Hinweis: „fünf .json“) (Msgs #1866, #1881–#1899).
- [FACT?] Anspruch/Behauptung des Systems: Bereitstellung eines ZIP‑Backups („metro_ai_rpg_full_backup.zip“) mit JSON/Markdown/Canvas (Msg #1906) – muss verifiziert werden.

Charaktere [CHAR]
- [CHAR] – keine neuen inhaltlichen Charakterdetails in diesem Chunk; Fokus liegt auf Verwaltung/Backup.

Orte [LOC]
- [LOC] – indirekt: D5/C6‑Canvas (Verwaltungsebene), keine neuen Ortsfakten inhaltlich.

Projekte [PROJ]
- [PROJ] Mission/Projekt „Tunnel“ (D5–C6) soll geladen und geprüft werden (Msg #1862).

Inventar [INV]
- [INV] – keine neuen Inventardaten in diesem Chunk.

Offen/Prüfaufträge [OPEN]
- [OPEN] Verifizieren, ob die behaupteten Sicherungsartefakte (Markdown‑Dump, Chat‑Zusammenfassung, Rohfassung, JSON‑Splits, ZIP) tatsächlich existieren (im ursprünglichen Chat‑System gab es evtl. nur Placebo‑Ausgaben).
- [OPEN] Konkrete Definition „Version 0.9“ für D5/C6: Welche Kriterien? (Felder/Abschnitte/Validierungs‑Checkliste definieren.)
- [OPEN] Wiedereinstiegspunkt („Agent Mode“) formal festlegen: Wo abgelegt? Welche Trigger/Checkliste?
- [OPEN] Reihenfolge/Namensschema für „alle Canvas“ bei Markdown‑Export: Sortierung nach letztem Aktualisierungszeitpunkt (wie gewünscht) – Metadatenbasis klären.
- [OPEN] JSON‑Splits: Falls genutzt, eindeutige message_id‑Strategie und Mapping zu globalen Zeilen festlegen (nur wenn später nötig).

## Chunk part-021 (global 10001–10500) – Fraktions-/Canvas-Debug, Energie/Progress-Methodik

- Kontext: Intensive Canvas-/Fraktionsprüfung, Aufsetzen eines „unumstößlichen“ Canvas, Rechen-/Methodikfragen zu Energie und Baufortschritt.
- Referenz: Nachrichten-ID-Bereich ca. #1764–#1848.

Szenenanker [SCENE]
- [SCENE] Canvas-Debug/Recovery: Alle Canvas temporär laden (archivierte separiert), Inhalte vergleichen, Änderungen zusammenfassen, veraltete Versionen zur Archivierung vorbereiten (Msgs #1768–#1788, #1792–#1796).
- [SCENE] Prüfroutine Zeit/Energie/Progress: Tagesgrenzen prüfen, Ressourcenverbrauch und Tunnel-Fortschritt gegentesten (Msgs #1798–#1808, #1804–#1806).
- [SCENE] „Unumstößlich“-Canvas anlegen: Core-Kanon soll immer zuerst geladen werden (Msg #1846).

Kanon-Fakten [FACT?]
- [FACT?] Vier Hauptfraktionen (vorläufig): 1. Eiserne Enklave, 2. Akologie, 3. Händlerbund, 4. Schienenbund; zusätzlich „Novapolis“ und „Freie Gruppen“ (Msg #1824).
- [FACT?] „Unumstößlich“-Canvas: Ein dediziertes Canvas mit höchster Priorität soll die unverrückbaren Grundtatsachen halten und stets zuerst geladen werden (Msg #1846).
- [FACT?] D5 (vorläufig, aus Msg #1846): Basis von Novapolis; einziger Reaktor der Metro; U-Bahn-Schacht; 100% Zustand; Jonas’ kleine Werkstatt (Geburtsort Reflex); Bewohner u. a. Ronja, Reflex, Jonas, Lumen, Pahl.
- [FACT?] C6 (vorläufig, aus Msg #1846): Ehemalige Händlerkarawane ansässig; Pilz-/Algennutzung; Strombezug von D5; Kreuzungsstation; Tunnel D5–C6 in Reparatur; Draisine im Bau (Jonas & Pahl).
- [FACT?] „N7“ wird aus dem Spiel entfernt; alle historischen Bezüge löschen/ignorieren (Msg #1846). Hinweis: Frühere Nennung „N7“ in Prüfung (Msg #1844, #1806) → Konflikt bereinigen.
- [FACT?] Tunnel-Fortschritt zuletzt 40% (Msg #1848).

Charaktere [CHAR]
- [CHAR] Exoskelett/Support-Modus (Balancing-Vorschlag): Bei exzessiver Nutzung entfällt Energiebonus und Verbrauch steigt; Kapazität an Masse gekoppelt (Msg #1814).
- [CHAR] Reflex-Instanzen: Gleiche Speicher-/Kapazitätslogik (Masse ~ Speicher), aber unterschiedliche Hauptfähigkeiten für die zwei weiteren Instanzen (Msg #1816).
- [CHAR] Wissensstand: Aktuell kennt nur Reflex seine eigenen Fähigkeiten (Msg #1818).

Orte [LOC]
- [LOC] D5/C6 – siehe Fakten oben; Kopplung über Energieversorgung und Instandsetzungstunnel; „Unumstößlich“-Canvas soll D5/C6-Grundlagen stabilisieren (Msg #1846).

Projekte [PROJ]
- [PROJ] Mission „Tunnel D5–C6“: Methodikdiskussion zur Fortschrittsberechnung (Differenzbasiert vs. Tagesleistung/Person), Ziel: RP-taugliche Geschwindigkeit (Msgs #1808, #1802).
- [PROJ] Konsistenzprüfungen Ressourcen-/Verbrauchstabellen (Msgs #1804, #1810–#1812).

Inventar/Verbrauch [INV]
- [INV] Energiefrage: „D5 -8 / C6 -12 = -20; D5 +10 = -10“ – Formeln/Regelwerk verifizieren (Msg #1806).

Offen/Prüfaufträge [OPEN]
- [OPEN] Fraktions-/Canvas-Drift: Namenswechsel („Schatten“/„Lumen“ etc.) und Flags historisch nachvollziehen; alle Canvas laden, Unterschiede listen (Msgs #1768–#1774, #1780–#1784).
- [OPEN] N7-Konsistenz: Frühere Referenzen identifizieren (Msgs #1806, #1844) und gemäß Beschluss (Msg #1846) bereinigen/entfernen.
- [OPEN] Energie-Formel und Konten definieren: Verbräuche/Erträge je Station; Abgleich mit Logistik-/Verbrauchs-Canvas (Msgs #1810–#1812, #1806).
- [OPEN] Fortschrittsmethode festlegen: Differenz vs. %/Tag/Person; RP-taugliche Richtwerte (0,5–1% je Kopf als Startpunkt) entscheiden (Msg #1808).
- [OPEN] Tagesgrenzen-Check: „letztes eines Tages“ vs. „nächstes des Folgetags“ korrigieren/markieren (Msg #1798, #1802).
- [OPEN] Prozess: Archivieren/Ersetzen nur mit Sichtprüfung/Diff (Anforderung: vor jeder Archivierung Anzeige und Gegenüberstellung, Msg #1786).

## Chunk part-020 (global 9501–10000) – Setup RP‑Modus, Draisinen‑Specs, Stationen fixieren

- Kontext: Admin/Setup für sauberen RP‑Start (Temporär‑Nachrichten, Snapshots, Reindex/Sync), Draisinen‑Spezifikation, feste Stations‑Beschreibungen inkl. Maße, Logistik/Verknüpfungen.
- Referenz: Nachrichten-ID-Bereich ca. #1671–#1763.

Szenenanker [SCENE]
- [SCENE] RP‑Modus Vorbereitung: Temporäre Morgen‑Nachricht, Snapshots, „freigeben:reindex/sync/snapshot“, Gewichtung/Archivierung überprüfen (#1678, #1688–#1690, #1710).
- [SCENE] Stations‑Fixierung: D5/C6/Verbindungstunnel beschreiben (vom Tunnel‑Eingang aus), Maße und Licht definieren (#1694, #1696, #1698).
- [SCENE] Tageswechsel‑Routine: Regeln/Canvas prüfen, fehlerhaften Wechsel zurückrollen, alles neu laden (#1751, #1753–#1755).

Kanon-Fakten [FACT?]
- [FACT?] Draisinen‑Projekt aktiv: Konstruktion für Tunnelbetrieb geplant; Kapazität/Abmessungen/Antrieb noch zu spezifizieren (#1680, #1727).
- [FACT?] D5 verfügt über Lastenaufzug (unter dem Bahnsteig), Zielzustand: 2t Traglast (wiederherstellen) (#1700).
- [FACT?] C6 nutzbare Fläche aktuell „~400+“ m²; frühere höhere Zahlen wurden korrigiert; Station mit 4 Linienabzweigen (D5, E3, F1, +1 unbekannt) – vorläufig (#1696, #1712).
- [FACT?] Protokoll: Logbücher stationenweit zugänglich außer „secret“ (#1747).

Charaktere [CHAR]
- [CHAR] Rollen/Zuordnung: Jonas, Pahl und Lumen an der Draisine; Ronja/Reflex im Tunnel; C6‑Bewohner‑Canvas sollen geladen/aktualisiert werden (#1727, #1729, #1724).
- [CHAR] Reflex‑Cluster: Echo ist Reflex‑Instanz; Kerncharakteristika teilen sich, Wachstumssystem vorgeschlagen (#1735).

Orte [LOC]
- [LOC] D5: Jonas’ Werkstatt (Geburtsort Reflex) und Zugang über schmalen Schacht – verifizieren und im Canvas fixieren (#1696).
- [LOC] C6: Beleuchtung wurde früh renoviert; Raumgrößen/SQM pro Raum fehlen, bitte ergänzen (#1696, #1698).

Projekte [PROJ]
- [PROJ] Draisine: Spezifikation und Baufortschritt dokumentieren; Antrieb (Elektro/Brennstoff) entscheiden (#1680, #1727).
- [PROJ] Tageswechsel‑Regeln: Canvas für Wechsel mit Validierungen/Teil‑Fraktionszug definieren (#1751, #1753).

Inventar/Verbrauch [INV]
- [INV] Energie/Logistik: Verknüpfungen zu Generator/Produktion im Logistik‑Canvas sicherstellen; Lazy‑Load vs. dauerhaft aktiv klären (#1757–#1759).

Offen/Prüfaufträge [OPEN]
- [OPEN] Draisinen‑Spezifikation fixieren: Spurbreite/Platz (≈10 Pers.), Länge (~6 m), Masse realistisch, Antrieb festlegen; Referenzen (Metro Spiele/Romane) nutzen (#1680).
- [OPEN] Stations‑Beschreibungen und Maße fix: D5/C6/Tunnel (Eingang, Wege, Licht, Raum‑SQM), inklusive Aufzug 2t in D5 (#1694, #1698, #1700).
- [OPEN] C6 Linien‑Abgänge: D5, E3, F1, +1 unbekannt – letzte Linie identifizieren (#1696).
- [OPEN] A/T/S/D‑Metriken klären und konsistent führen; aktuelle Zählung „A 171 / T 304 / S 9 / D 5“ verifizieren (#1704, #1751).
- [OPEN] Tageswechsel‑Canvas/Regeln wiederherstellen; Wechsel nur nach Komplett‑Load; Validierungscheckliste festlegen (#1751, #1753–#1755).
- [OPEN] Energie‑Bilanz: Reaktorproduktion, Soll‑Zellen und Logistik‑Verlinkungen prüfen, damit Tagesabrechnung korrekt erfolgt (#1757–#1759).

## Chunk part-019 (global 9001–9500) – Weekly‑Sim/Canvas‑Audit, Reflex‑Regeln, Anomalien

- Kontext: Übergang zu Systemmodus für Wochen‑Simulation (Tag 7–11), umfassender Canvas‑Audit, Regeln/Policies, RP‑Fortsetzung mit konsistenter Datenbasis.
- Referenz: Nachrichten-ID-Bereich ca. #1582–#1670.

Szenenanker [SCENE]
- [SCENE] Weekly‑Simulation und Audit: Simulation bis Morgen von Tag 11; aktive Canvas prüfen, Archivkandidaten markieren; Token‑Kosten im Blick (#1595–#1605).
- [SCENE] Canvas‑Integrity: Voll‑Reload, Struktur‑ und Verweisprüfung, Gruppierte Auflistung (Bewohner/Orte/Missionen …) (#1611–#1614).
- [SCENE] Abschlussrituale: Tägliche Abschlussbesprechung D5/C6; Logbucheinträge von Ronja; kleine Fraktionszüge (#1593–#1595, #1640, #1644, #1652, #1654).

Kanon-Fakten [FACT?]
- [FACT?] Arbeiten von D5 hatten begonnen; Logbucheintrag für Tag 9 existiert/e (#1583).
- [FACT?] Reflex ist körperlich an Ronja anliegend (wie Neoprenanzug), kein separater Arm; frühere Formulierungen waren widersprüchlich (#1607).
- [FACT?] Nähebedürfnis/Kopplung: Lumen↔Jonas und Echo↔Kora spiegeln Ronja↔Reflex (Bezugsperson und Nähe) (#1625).
- [FACT?] N7 ist Bereich innerhalb C6; dort wurde eine Anomalie gefunden (frühe Renovierungen) (#1623).

Charaktere [CHAR]
- [CHAR] Fokuswechsel: Kurzszenen zu Jonas und Lumen; Ronja priorisiert Tunnelarbeit nach Anomalie‑Protokoll (#1587, #1591).
- [CHAR] Darek vor Ort bei Exo‑Test; Reaktionen von NPCs erwünscht (#1648).

Orte [LOC]
- [LOC] D5↔C6: Tunnel begehbar, noch nicht befahrbar (Klarstellung) (#1636).

Projekte [PROJ]
- [PROJ] Missionsanlage (vorerst unpriorisiert): 1) Anomalie N7 (C6), 2) Tunnel‑Anomalie D5–C6, 3) E3‑Gefahr? – dritte Mission zu verifizieren (#1623–#1625).
- [PROJ] Transportmodul: Testreferenz streichen; Vorschlag: Pahl/Jonas/Lumen bauen ein Test‑Transportmodul (morgen) (#1642).
- [PROJ] Daily‑Routine‑Canvas: Tägliche Prüf‑/Ablauf‑Checkliste maschinenlesbar, inkl. Cluster/Verlinkungen/Temporär‑Einstellungen (#1664–#1666).

Inventar/Verbrauch [INV]
- [INV] Energie: D5‑Reaktor ermöglicht Zellaufladung; C6 wird teilweise von D5 versorgt – prüfen und im Logistik‑Canvas verlinken (#1658).
- [INV] Verbrauchsberechnung am Tagesende prüfen; r_usage_v1 Canvas anlegen (#1656, #1658).

Offen/Prüfaufträge [OPEN]
- [OPEN] Quarantäne vorbei: C6‑Helferzahl aktualisieren; Personalverteilung in D5/C6 anpassen (#1634).
- [OPEN] Fortschritt widersprüchlich (>60% vs. <40%): gültigen Stand verifizieren (vermutlich <40%) (#1634).
- [OPEN] Canvas‑Policy: Nicht‑archivierte Canvas aktiv geladen halten; Abriss der Zählung erklären (242→152) und korrigieren (#1609–#1613).
- [OPEN] Fraktionsset/Divergenzen: Hauptfraktionen gegen Archiv/Reports abgleichen; N7‑Status als Bereich in C6 fixieren (#1615–#1617, #1623).
- [OPEN] A/T/S/D‑String in Systemmeldungen aufnehmen; Bedeutung definieren und letzten „guten“ String hoch werten (#1660–#1662).

## Chunk part-018 (global 8501–9000) – Mission 2 Planung, Bestandsaufnahmen, System‑Update‑Vorbereitung

- Kontext: Vorbereitung Mission 2 (Aufklärung äußere Linien), Inventar/Bestandsaufnahmen D5/C6, Bevölkerungsklärung/Archivierungen, temporäre Einstellungen/System‑Update, Debug-/Systemmeldungen.
- Referenz: Nachrichten-ID-Bereich ca. #1492–#1581.

Szenenanker [SCENE]
- [SCENE] Missionsplanung „Aufklärung der äußeren Linien“: Ronja+Reflex melden sich; Geleit (2 Wachen, 3 Träger); Handelswaren vorbereiten (Inventar/Logistik) (#1492–#1497).
- [SCENE] Bestandsaufnahmen: C6 und D5 führen umfassende Bestandsprüfungen durch; RP setzt dort fort (#1499, #1509).
- [SCENE] System‑Pflege: Debug/Systemmeldungen prüfen; temporäre Einstellungen im Canvas sammeln; Vorbereitung Prompt für System‑Update (#1501–#1505, #1535–#1541, #1537–#1539).

Kanon-Fakten [FACT?]
- [FACT?] Missionsregeln: Diplomatische Außenmission startet erst nach Tunnel‑Renovierung; Mission 2 wird vorgeplant, nicht gestartet (#1509, #1492).
- [FACT?] Bevölkerung Novapolis (vorläufige Obergrenze): max. ~29 humanoide Bewohner aus Karawane (6), E3 (20), plus Jonas und Pahl; Abgleich/Verdichtung erforderlich (#1519).
- [FACT?] Zwei Karawanenmitglieder Nia/Rell waren fälschlich in D5; Archivierung veranlasst (#1515–#1519).

Charaktere [CHAR]
- [CHAR] Wissensstände/Beziehungs‑Cluster sollen in allen Charakter‑Canvas gepflegt werden; späterer Abgleich gegen Ronjas Canvas‑Struktur (#1565, #1577–#1581).

Orte [LOC]
- [LOC] C6/D5: Bestandsaufnahme beschlosssen; Prüfung Bewohnerlisten (C6 20 Flüchtlinge + 4 Karawanenmitglieder, D5 mit Jonas/Pahl) (#1511–#1519).

Projekte [PROJ]
- [PROJ] Mission 2 „Aufklärung äußere Linien“: Ronja+Reflex + 2 Wachen + 3 Träger; Handelsware mitnehmen; Inventar/Logistik‑Canvas zuvor aktualisieren (#1492, #1497).
- [PROJ] System‑Update: Temporäre Einstellungen sammeln; Prompt prüfen; Update durchführen und Validierung danach (#1535–#1541, #1545–#1553).
- [PROJ] Bevölkerungsauswertung/Canvas‑Audit: Bewohner‑Canvas auf neue Version heben; Archivierungen mit Drei‑Schritte‑Plan (#1521–#1525).

Inventar/Verbrauch [INV]
- [INV] Inventardaten konsistent mit harten Einheiten (Tonnen/Meter/Volumen); Vorratsindex „Stahl“ u. a. (#1527).
- [INV] Energiezellen/Materialmengen prüfen; keine unbelegten Bestände „erdichten“ (#1529).

Offen/Prüfaufträge [OPEN]
- [OPEN] C6/D5‑Bewohnerlisten final klären; Nia/Rell archiviert; Max‑Bewohnerzahl gegen Lore bestätigen (#1511–#1519).
- [OPEN] Debug-/Systemmeldungen: Persistenz sicherstellen; temporäre Einstellungen Canvas pflegen; fehlende Systemmeldungen Ursache beheben (#1501–#1505, #1531–#1534).
- [OPEN] Schienenwagen/Transport: Quelle belegen oder entfernen; vorläufig Test‑Transportmodul erst planen, nicht als existent ausgeben (#1575, Bezug zu #1642 in part‑019/020).
- [OPEN] Quarantäne‑Ende und Start paralleler Arbeiten von C6‑Seite validieren (vermutlich Tag 10) (#1573).

## Chunk part-017 (global 8001–8500) – C6‑Führung, Rückweg nach D5, Fraktions‑Züge, Missionsplanung

- Kontext: Tag 6–7: Quarantäne‑Tag 2 Organisation (Marei/Kora/Ronja), Echo‑Verhalten, Wochen‑Sim (Fraktionen/Nicht‑Fraktionen), Rückkehr Ronja+Reflex nach D5 mit zwei Begleitern, Datenkonsolidierung und Sitzungen.
- Referenz: Nachrichten-ID-Bereich ca. #1405–#1491.

Szenenanker [SCENE]
- [SCENE] C6‑Organisation: Marei (E3) + Kora (C6) + Ronja (Novapolis) koordinieren Aufgaben (Quarantäne‑Tag 2) (#1407).
- [SCENE] Abend Tag 6: Gespräch Ronja/Reflex/Kora/Echo; Echo anhänglich zu Kora betonen (#1417).
- [SCENE] Wochen‑Simulation (Tag 7): Züge aller Fraktionen und neutraler Gruppen; Metadaten‑Ausgabe gewünscht (#1419–#1429, #1431).
- [SCENE] Abschied/Echo: Abschiedsszene, Systemmeldungen reparieren und sichern (#1443–#1447).
- [SCENE] Ankunft D5: Tunnel‑Bestandsaufnahme auf dem Rückweg; Empfang und Info an C6 (#1447–#1451).
- [SCENE] Vorstellungs‑/Wissens‑Abgleich: Meeting aller Beteiligten; erst Vorstellung, dann Berichte; Wissensstände angleichen (#1453–#1459).

Kanon-Fakten [FACT?]
- [FACT?] Echo (Reflex‑Instanz) zeigt wie Reflex starke Nähe zur Bezugsperson (Kora) und sucht Körperkontakt (Konsistenzregel) (#1417, #1463–#1465).
- [FACT?] Zwei Personen wechseln von C6 nach D5; korrekter Satz: Tarv und Derek (spätere Korrektur) (#1471–#1480).
- [FACT?] N7 bleibt versiegelt; keine aktive Bedrohung; Wochen‑Züge laufen trotzdem weiter (#1419).
- [FACT?] E3 ist vom Netz getrennt; Energiefluktuationen sollten Fraktionen mit Monitoring auffallen (#1429).

Charaktere [CHAR]
- [CHAR] Neue Bewohner: Für neue Bewohner einzelne Charakter‑Canvas anlegen; Verlinkungen in Cluster/Logistik herstellen (#1405).
- [CHAR] Ronja: Planung Rückzug nach D5 sobald C6 100% bereit ist; Büro‑Übergabe an Kora (#1409).
- [CHAR] Kora/Marei: C6‑Führung/Delegation; Kora wählt 2 Personen für D5‑Umzug (#1407, #1435).

Orte [LOC]
- [LOC] D5: Ankunft zweier C6‑Bewohner, Begrüßung durch Jonas/Lumen/Pahl; Wissenslücken schließen (#1451–#1455).
- [LOC] D5/C6‑Tunnel: fortlaufende Bestandsaufnahme während Rückweg (#1447).

Projekte [PROJ]
- [PROJ] Mission „Tunnelinstandsetzung“: Ziele präzisieren (Schienenverkehr wieder nutzbar machen), mehr Personal (C6 anfordern), höherer Zeit‑ und Materialaufwand; separate technische Bewertung erstellen (#1488–#1489).
- [PROJ] Mission 2 „Aufklärung äußere Linien“: Ronja+Reflex melden sich; 2 Wachen, 3 Träger; Handelswaren; nur temporär geplant bis Finalfreigabe (#1492, #1488).
- [PROJ] Neutral‑Gruppen Kern anlegen für Wochen‑Züge/Sim (#1419).

Inventar/Verbrauch [INV]
- [INV] Inventare aktualisieren; Konsistenz prüfen (#1405, #1497).
- [INV] Handelswaren für Mission 2 vorbereiten; Logistik/Inventar‑Canvas nutzen (#1492).

Offen/Prüfaufträge [OPEN]
- [OPEN] Fraktionen‑Anzahl klären: „vier“ vs. „fünf Hauptfraktionen“ – Konflikt bereinigen (#1427 vs. #1824).
- [OPEN] Systemmeldungen/Debug: fehlende Meldungen immer wieder – Persistenz sichern und Diagnose protokollieren (#1445–#1447, #1491).
- [OPEN] Umzug C6→D5: Sicherstellen, dass Tarv und Derek korrekt verschoben wurden; Leena/Rian bleiben erhalten; alle Cluster/Beziehungen/Standorte aktualisieren (#1471–#1480, #1474).
- [OPEN] E3‑Netztrennung: Monitoring‑Implikationen für Fraktionen definieren (wer merkt es, welche Canvas) (#1429, Anschluss an Energie‑Policy).

## Chunk part-016 (global 7501–8000) – System‑Last/Canvas‑Kategorien, C6‑Linien, Echo‑Kora, E3‑Evakuierung

- Kontext: Admin‑Themen (Tokenverbrauch, alle nicht‑archivierten Canvas aktiv laden, Systemmeldung mit Canvas‑Zahl, Kategorien A/B/C Reaktivierung), RP‑Fokus auf C6 (Zugänge/Linien), Karawanen‑Test, Echo‑Instanzbindung an Kora, Kontakt zu E3 und Evakuierung, Quarantäne/Versorgung in C6.
- Referenz: Nachrichten-ID-Bereich ca. #1307–#1403.

Szenenanker [SCENE]
- [SCENE] Admin/Setup: Temporäre Einträge für nächstes Update; vollständige Tages‑Simulation (Token); Policy „alle nicht‑archivierten Canvas geladen“; Systemmeldung inkl. Canvas‑Anzahl (#1307–#1339).
- [SCENE] C6‑Morgen: Ronja/Reflex Aufbruch in die Station; Team‑Besprechung vorbereiten (#1341–#1344).
- [SCENE] Linien/Wege C6: Zugänge und Linienführung klären; Logistik‑Canvas mit Gleiszuständen füttern (#1345–#1349).
- [SCENE] Karawanen‑Test: Gruppe bricht von C6 auf; Echo als Instanz Kora zuordnen; Reise ohne Fracht (#1353–#1365, #1359–#1363).
- [SCENE] E3: Kontaktaufnahme, Bewertung (minimale Bevölkerung), Evakuierungsentscheidung, Transfer nach C6, Quarantäne in Gemeinschaftsbereich (#1376–#1399, #1391–#1397).
- [SCENE] Versorgung: Algen‑/Pilzfarmen reaktivieren und Kapazität prüfen (#1401–#1403).

Kanon-Fakten [FACT?]
- [FACT?] Betriebsmodus: Alle nicht‑archivierten Canvas sollen aktiv geladen sein; Systemmeldungen sollen die Anzahl geladener Canvas anzeigen (#1317–#1339).
- [FACT?] C6 Zugänge/Linien (vorläufig):
	- U‑Bahn‑Station mit 2 Gleisen; ein Gleis Richtung verschütteter Trakt, das andere Richtung D5.
	- Zusätzliche Linie Verbindung F1↔(andere Richtung) für Karawanentransport.
	- Ein „Wandtunnel“ (Fußgängerzugang) existiert und war der historische Zugang der Karawane (#1345–#1349).
- [FACT?] Echo ist Reflex‑Instanz bei Kora; Lumen ist die Instanz bei Jonas; Echo kann nicht „fliegen“ und muss physisch aufschließen (#1355, #1375, #1359–#1363).
- [FACT?] E3 wurde vor Evakuierung gewarnt; danach Netztrennung/Evakuierung → Ankunft C6; Quarantäne angewandt (#1391–#1397, #1399).

Charaktere [CHAR]
- [CHAR] Echo: neue Instanz‑Canvas anlegen/aktualisieren; Bezugsperson Kora, Näheverhalten wie Reflex (#1359–#1361).
- [CHAR] Kora/Marei: leiten Bestandsaufnahmen, Quarantäne und Versorgung (#1385–#1391, #1399–#1403).

Orte [LOC]
- [LOC] C6: Liniennetz/Wege und Wandtunnel dokumentieren; Gleiszustände im Logistik‑Canvas führen (#1345–#1349).
- [LOC] E3: als Quellstation der 20 Evakuierten modellieren; nach Evakuierung vom Netz getrennt (#1391–#1397).

Projekte [PROJ]
- [PROJ] Canvas‑Kategorien A/B/C: Reaktivierungs‑/Audit‑Prozess definieren (A zuerst, B nach Prüfung, C nur mit harten Regeln) (#1321–#1330).
- [PROJ] Karawanen‑Test: Pfad, Personal, Energiegrenzen für Echo; Zielstationen und Protokoll (Kontakt, Log‑Eintrag) (#1369–#1375).

Inventar/Verbrauch [INV]
- [INV] Logistik/Inventare: Gleiszustände, Algen/Pilz‑Kapazitäten, Vorräte mit Einheiten erfassen; Datenaustausch D5↔C6 (Jonas) etablieren (#1349, #1389, #1401–#1403).

Offen/Prüfaufträge [OPEN]
- [OPEN] C6‑Linien exakter bestimmen: Anzahl/Bezeichnungen, Abzweige (D5, F1, verschütteter Trakt, Karawanenlinie) und Wandtunnel‑Status verbindlich festlegen; Konflikte zu früheren 4‑Linien‑Angaben auflösen (#1345–#1349 vs. #1696/part‑020).
- [OPEN] Canvas‑Kategorien Prozess verschriftlichen: Kriterien/Aktionen für A/B/C, Validierung, Archiv‑Policy (#1321–#1330).
- [OPEN] Systemmeldung: Formatstring mit Canvas‑Zahl standardisieren und persistieren (Verknüpfung zu A/T/S/D‑String) (#1339).
- [OPEN] E3‑Evakuierung/Policy: Trigger, Ablauf, Ressourcenwirkung (Energie frei für D5/C6), Sichtbarkeitsregeln für Fraktionen dokumentieren (#1391–#1397).

## Chunk part-015 (global 7001–7500) – Rückkehr C6, Rollen/Leitung, Admin‑Prozess, D5‑Slice‑of‑Life

- Kontext: Rückblick/Neuaufnahme RP‑Faden: Ankunft/Bestandsaufnahme C6, Aufgaben‑Zuordnung durch Kora, Admin‑3‑Schritt‑Prozess, Fraktionszüge (abgeschwächt), D5‑Zwischenszene Jonas↔Reflex‑Instanz, Korrektur Karawanen‑Missionsstatus.
- Referenz: Nachrichten‑ID‑Bereich ca. #1209–#1306.

Szenenanker [SCENE]
- [SCENE] C6‑Ankunft/Bestandsaufnahme: Material sichten, Aufgaben gemäß Fähigkeiten zuweisen; Kora übernimmt Leitung von C6 (Msgs #1219, #1221–#1229, #1231).
- [SCENE] Admin‑Routine: „Analysieren → Backups → neue Version → alte archivieren“ als Standardprozess; Kern‑Canvas aktualisieren vor Tagesabschluss (Msgs #1221, #1279–#1284).
- [SCENE] Rollenklärung: Wächter Mikk nicht für fachfremde Aufgaben einteilen; Rollen/Funktionen in Charakter‑Canvas prüfen/angleichen (Msgs #1239–#1243, #1241).
- [SCENE] D5‑Slice: Jonas benennt/erprobt Reflex‑Instanz (Lautsprecher), Pahl einbezogen; Funkverbindung bereits repariert (Msgs #1267–#1276).
- [SCENE] Fraktionszüge (abgeschwächt): Alle nötigen Canvas laden; Novapolis nach außen unbekannt; keine Außenverbindung aktiv (Msgs #1261–#1264).

Kanon‑Fakten [FACT?]
- [FACT?] Reflex‑Ursprung: In kleiner Werkstatt/Wartungsraum unter dem Kontrollbereich von D5 entstanden, als Folge der Lösung der Ronja‑Verschmelzung (#1209).
- [FACT?] C6‑Leitung: Kora übernimmt formal die Stationsleitung; Ronja unterstützt, bleibt Anführerin von Novapolis (#1229–#1231).
- [FACT?] Admin‑3‑Schritt‑Prozess ist Standard: Analysieren → Backups → neue Version → Archivierung (#1221, #1279–#1284).
- [FACT?] Karawanen‑Mission ist abgeschlossen und zu archivieren; erneuter Aufbruch wurde NICHT angeordnet (#1291–#1296).
- [FACT?] Novapolis ist extern unbekannt; physische Außenverbindung theoretisch über C6, aber faktisch noch ohne Außenkontakt (#1263).

Charaktere [CHAR]
- [CHAR] Rollenmatrix pflegen: Mikk als Wächter; Aufgabenverteilung an übliches Profil anlehnen und im Canvas verankern (#1239–#1243).
- [CHAR] Jonas↔Reflex‑Instanz („Lumen“): Instanz spricht über Lautsprecher; Tests mit Pahl; Instanz als aktiver Canvas (#1267–#1273, #1269–#1271).
- [CHAR] Ronja↔Reflex: Nähe/Kopplung; Reflex zeigt Eigenaktivität während Ronja schläft; Schutz hat Priorität (#1285–#1287).

Orte [LOC]
- [LOC] D5: Kleine Werkstatt/Wartungsraum unter Kontrollbereich als Entstehungsort von Reflex dokumentieren (#1209).
- [LOC] Tunnel D5↔C6: Gut erschlossen; kleiner Wartungsgang mit drei Leichen; weiterer Abzweig nach E3 (ggf. E2) verschüttet – verifizieren (#1215).

Projekte [PROJ]
- [PROJ] C6‑Instandsetzung: Luftfilter/Beleuchtung priorisiert; Arbeitszuteilung durch Kora; Material von Versorgungsgruppe sichten (#1231).
- [PROJ] Fraktionszüge: Abgeschwächt, unter Wahrung der Novapolis‑Geheimhaltung; erst nach vollständigem Canvas‑Load (#1261–#1264).
- [PROJ] Archiv‑Pfad: Karawanen‑Mission als „abgeschlossen“ markieren, Inventare verbuchen, alte Version archivieren (#1291–#1299).

Inventar/Verbrauch [INV]
- [INV] Tragekapazität Versorgungsgruppe: Ziel ~50 kg p. P. (dynamisch je Person: Größe/Training); Material für C6‑Reparatur priorisiert (#1213).
- [INV] Bestandsaufnahme C6 und Charakter‑Inventare synchronisieren; Datenaustausch D5↔C6 sicherstellen (#1219, #1297–#1299).

Offen/Prüfaufträge [OPEN]
- [OPEN] Gasunfall E3 vs. E2 klären; Station des Unfalls und Jonas’ Herkunft eindeutig festlegen (#1215).
- [OPEN] Rollen/Verantwortlichkeiten als Pflichtfelder im Charakter‑Schema verankern (Wächter, Techniker, Leitung …) (#1239–#1243).
- [OPEN] Admin‑3‑Schritt‑Prozess als verbindliche Policy dokumentieren (inkl. Triggers/Artefakte) (#1221, #1279–#1284).
- [OPEN] Novapolis‑Geheimhaltung in Fraktionszügen modellieren (Wissen/Erkennung → 0) (#1261–#1264).
- [OPEN] Karawanen‑Mission sauber archivieren, inkl. Inventarabschluss und Verlinkungen (Canvas „Logistik“/„Missionen“) (#1291–#1299, #1301–#1306).

## Chunk part-014 (global 6501–7000) – D5‑Zwischenfall, Rollen/Regeln, Inventar‑Prozess, System‑Update, Reflex‑Kontrolle

- Kontext: D5‑Intermezzo (Mikk stöbert, Pahl führt), Vorschlag: Reflex‑Instanz als Guide, Versorgungsmission für C6 vorbereiten (Inventar/Comms), Rollen-/Canvas‑Konsolidierung, Behavior/Archiv‑Update, tiefe Szene Ronja↔Reflex (Schutz/Übernahme der Kontrolle).
- Referenz: Nachrichten‑ID‑Bereich ca. #1128–#1208.

Szenenanker [SCENE]
- [SCENE] D5‑Lager/Kommandokette: Mikk durchsucht Kisten; Pahl hat Kommando, solange Ronja/Reflex abwesend (#1128–Intro).
- [SCENE] Reflex‑Instanz‑Führung: Vorschlag, Jonas um Leihgabe der Instanz zu bitten, um D5 zu zeigen; Persönlichkeit des „kleinen Reflex“ sichtbar (#1129–#1131).
- [SCENE] Versorgung C6: Vorräte übergeben und Aufbruch; Funkkontakt zu C6 herstellen (vermutlich Kora antwortet) (#1133).
- [SCENE] Konsistenz/Diagnose: Analyse der Abweichungen; manuelles Laden/Prüfen relevanter Canvas (#1135–#1136).
- [SCENE] Status C6: Verbliebene Personen gelistet; Comms via D5‑Terminal vor Abmarsch (Jonas) (#1137).
- [SCENE] Canvas‑Pflege: Fehlende Novapolis‑Charaktere anlegen; Prüf-/Validierungslauf (#1137).
- [SCENE] Systempflege: Admin‑Prompt/Update, Validierungsfragen, Umstellung Archiv‑Zyklus auf In‑Game‑Zeit (#1163–#1167).
- [SCENE] Anomalie‑Moment: Ronja scannt; Reflex schützt, übernimmt Kontrolle, dämpft Sinne, gibt Atem/Sicht zurück; tiefer psychologischer Blick (#1175–#1207).

Kanon‑Fakten [FACT?]
- [FACT?] Pahl führt in D5, wenn Ronja/Reflex abwesend sind (#1128).
- [FACT?] Reflex‑Instanz bei Jonas zeigt Bindungs-/Näheverhalten analog zu Reflex↔Ronja; bleibt i. d. R. bei Jonas (#1128, #1131, #1135).
- [FACT?] Comms D5↔C6 wurden zuvor repariert/optimiert; vor Abmarsch informiert Jonas per Terminal C6 (#1139, #1137).
- [FACT?] C6‑Besetzung zu diesem Zeitpunkt: Ronja, Reflex, Kora, Sima, Tarv, Derek (#1137).
- [FACT?] Rollenpräferenz: Mikk eher Wächter/Sicherheit; Lira Richtung Logistik/Technik (nicht „zu viele Techniker“) (#1147).
- [FACT?] Ronja‑Canvas soll als Template dienen; Hauptpunkte synchron in andere Charakter‑Canvas übertragen (#1149–#1153).
- [FACT?] Verbindliche Safe‑Update‑Policy für große Canvas‑Änderungen erforderlich (3‑Schritt + Validierung) (#1155, #1203).
- [FACT?] Behavior/System: Vorbereitung v1.4.0‑pre; Archivierungszyklus auf In‑Game‑Zeit (#1163–#1167).
- [FACT?] Reflex‑Mechanik: Kann über feines Gewebe am Trommelfell Sprache übertragen; in Gefahr kann Reflex zur Vollschutz‑Hülle werden und Sinne dämpfen (#1181, #1185, #1183–#1187, #1190–#1207).

Charaktere [CHAR]
- [CHAR] Mikk (Wächter): Aufgabenprofil Richtung Sicherheit; eigenständige Entscheidungen nur im Rahmen der Rolle (#1147, #1145).
- [CHAR] Lira (Logistik/Technik): Canvas erweitern, um eigenständige Entscheidungen zu ermöglichen (#1145–#1147).
- [CHAR] Ronja/Reflex: Nähe/Kopplung, Reflex übernimmt situativ Kontrolle, gibt minimale Sinne zurück (Atmung/Sicht) (#1183–#1207).
- [CHAR] Jonas/Instanz: Instanz spricht via Lautsprecher möglich; bleibt an Jonas gebunden (#1269 aus part‑015, Kontext hier #1129–#1135).

Orte [LOC]
- [LOC] D5: Lager, Jonas’ Werkstatt, Kommunikations‑Terminal; Führungsstruktur (Pahl) bei Abwesenheit von Ronja/Reflex (#1128, #1129, #1137).
- [LOC] C6: Empfang von Funkmeldungen vor Abmarsch; Besetzungsliste (#1133, #1137).

Projekte [PROJ]
- [PROJ] Versorgungsmission C6: Inventaraufnahme, Quell-/Ziel‑Inventare, Funkabgleich Bedarf, Abreise‑Protokoll (#1141–#1144, #1133, #1137).
- [PROJ] Canvas‑Standardisierung: Ronja‑Template, Auto‑Sync der Kernfelder (#1149–#1153).
- [PROJ] System‑Update: Admin‑Prompt, Validierung, In‑Game‑Archivierung (#1163–#1167, #1165–#1166).

Inventar/Verbrauch [INV]
- [INV] Inventar‑Pfad definieren: „Wieviel von was entnommen? Aus welchem Inventar? In welches Ziel‑Inventar verbucht?“ – Prozess/Canvas festschreiben (#1141).
- [INV] Bedarfsabfrage via Funk an C6 vs. eigenständige Auswahl durch Team (#1143).

Offen/Prüfaufträge [OPEN]
- [OPEN] Hausregeln Lager/„Schnüffeln“ definieren; Sanktions‑/Hinweisprozess (Mikk‑Fall) (#1128–#1129).
- [OPEN] Leihgabe Reflex‑Instanz: Policy im Einklang mit Bindung/Bezugsperson (Jonas) festlegen (#1129–#1135).
- [OPEN] Fehlende Novapolis‑Charakter‑Canvas anlegen und validieren (Codierung, Aktualität, Verweise) (#1137).
- [OPEN] Missions‑Inventar: Einheitliche Buchungs‑Pipeline (Quelle/Ziel, Belege, Verantwortliche) spezifizieren (#1141–#1144).
- [OPEN] Mikk/Lira‑Canvas so erweitern, dass autonome Entscheidungen plausibel/rollenkonform sind (#1145–#1147).
- [OPEN] Ronja‑Template‑Sync: Automatische Übernahme „Hauptpunkte“ definieren, Risiken/Drift vermeiden (#1149–#1155).
- [OPEN] Safe‑Update‑Regel dokumentieren und in Verwaltung‑Canvas verankern (Validierungen vor Live‑Änderung) (#1155, #1203).
- [OPEN] Verhalten v1.4.0‑pre: Prüfen, ob alles übernommen/kompatibel ist; Narrator‑Neutralität konfigurierbar? (#1167–#1173, #1187).
- [OPEN] Reflex‑Sprechmechanik/Trommelfell: Grenzen, Zustimmung, Erschöpfung; Schutz‑Trigger/Schwellen definieren (#1181, #1183–#1187, #1190–#1207).

## Chunk part-013 (global 6001–6500) – Reflex‑Profil/Verhalten, D5‑Layout/Pläne, Comms/Tunnel, Kontext‑Reload

- Kontext: Vertiefung Reflex‑Charakter (Aussehen/Bewegung/Bindung), Korrekturen zu Symbiose‑Stufen, D5‑Struktur/Skizzen‑Canvas, Comms/Tunnel‑Details, Systemkontext neu laden, Führungsrollen klären.
- Referenz: Nachrichten‑ID‑Bereich ca. #1046–#1127.

Szenenanker [SCENE]
- [SCENE] Reflex‑Profil: Aussehen wie „metallisch‑perlmutt“ Neoprenanzug; bedeckt i. d. R. bis Handgelenke/Hals; Hände bei Bedarf; Gesicht bisher nie (#1057, #1087).
- [SCENE] Bewegung/Bindung: Reflex kann sich seesternartig bewegen/strecken, trennt sich aber nicht komplett von Ronja; kindlich, besitzergreifend, Verlustangst (#1059).
- [SCENE] D5‑Struktur: Werkstatt unter schmalem Wartungsschacht; oben Kommando‑/Gemeinschaftsbereich mit Büro; Reaktor/Versorgung; Kommunikationszentrale; Lager; Bahnsteig (#1089).
- [SCENE] „Pläne von Novapolis“: Skizzen/Pläne‑Canvas (schematisch, nicht als Referenz) mit Versionierung; Bildanalyse/Korrekturen; Ebene andeuten (#1091–#1103, #1099–#1101).
- [SCENE] Comms/Tunnel: D5‑Funkzentrale vorhanden; regulärer (beschädigter) U‑Bahntunnel, zu Fuß begehbar; kein Wartungstunnel; Reichweitenfragen (#1081, #1069, #1111, #1109, #1127).
- [SCENE] Kontext‑Reload/Validation: Neu laden Chat+Canvas; Systemische Korrekturen; Fokus auf RP‑Reihenfolge (#1115–#1121).

Kanon‑Fakten [FACT?]
- [FACT?] Reflex‑Aussehen: metallisch‑perlmutt, wirkt wie Neoprenanzug; trägt Ronja unter Kleidung; Standardabdeckung bis Handgelenke/Hals (#1057).
- [FACT?] Reflex trennt sich nicht; Bewegung via Strecken/„Seestern“ möglich; Sprache möglich (Hauptinstanz) (#1059, #1067–#1069, #1087).
- [FACT?] Eifersucht/Schutz: Handschuhe werden durch Reflex‑Hände‑Schutz ersetzt („keine fremden Handschuhe“) (#1087).
- [FACT?] D5‑Layout: Werkstatt unter Wartungsschacht; darüber Gemeinschaft/Büro; separater Reaktor/Versorgung; Funkzentrale; Lager; Bahnsteig (#1089).
- [FACT?] „Pläne von Novapolis“ Canvas: schematische Darstellung, nicht als Referenz zu verwenden; Version 1.2 mit Hinweis (#1101–#1104).

Charaktere [CHAR]
- [CHAR] Ronja: Ordnung/Planung; führt, bleibt Fraktionsleiterin (Kora führt nur lokal/temporär) (#1111).
- [CHAR] Reflex: Kindlich, besitzergreifend, Schutz vor Trennung; zeigt starke Nähe, übernimmt Hände‑Schutz (#1059, #1087).

Orte [LOC]
- [LOC] D5: zweistufige Struktur mit Werkstatt unten; Funkzentrale; Lager; Bahnsteig (#1089, #1099–#1101).
- [LOC] C6↔D5: regulärer Tunnelabschnitt, fußläufig (beschädigt), nicht wartungsspezifisch (#1109, #1111).

Projekte [PROJ]
- [PROJ] D5‑Pläne: Canvas „Pläne von Novapolis“ pflegen; Ebenen eindeutig andeuten; Bildversionierung/Notiz „schematisch“ (#1091–#1104).

Inventar/Verbrauch [INV]
- [INV] Keine neuen Inventarfakten; Fokus auf Vermeiden „herbeigezauberter“ Gegenstände (#1109–#1110).

Offen/Prüfaufträge [OPEN]
- [OPEN] D5‑Karte finalisieren: Ebenen/Durchgänge und Maße prüfen; Werkstatt‑/Schaftposition bestätigen (#1097–#1101).
- [OPEN] Comms‑Reichweite: Gleichzeitiges Hören in beiden Stationen plausibilisieren; Reichweiten-/Dämpfungsmodell definieren (#1087–#1088).
- [OPEN] Neid/Handschuhe‑Regel: Situationslogik und Grenzen dokumentieren (#1087).

## Chunk part-012 (global 5501–6000) – Codes/Cluster, Kontextprüfung, Backups, Schwierigkeitsgrad, Fraktionswissen

- Kontext: Integrationsarbeit an Codierungssystemen, wiederholte Kontextprüfungen, Backup‑Strategie, Vorbesprechung Versorgungsmission, Schwierigkeitsgrad/Outcome‑Gewichtung, Cluster‑Index‑Idee.
- Referenz: Nachrichten‑ID‑Bereich ca. #955–#1045.

Szenenanker [SCENE]
- [SCENE] Codes vereinheitlichen: Händlergilde/Eisenkonklave Codes korrigieren; mehrere Codierungen in Einklang bringen (#957–#965, #963).
- [SCENE] Kontextprüfung: Vor jeder Antwort optional automatisch; Vermerk „Kontextprüfung durchgeführt“; Doku und Probeläufe (#985–#991, #1001–#1005).
- [SCENE] Backup: Vollständiges Canvas‑Backup + Chat‑Spiegelung als ZIP (lokal) gewünscht (#891–#899, #895–#897).
- [SCENE] Fraktionswissen korrigieren: Händlerfraktion weiß noch nichts von Novapolis; nur Energiespitzen/Missing Caravan (#1033–#1035, #1039).
- [SCENE] Tunnelstatus präzisiert: regulärer Tunnelabschnitt, fußläufig; kein Brücken/Wartungstunnel (#981–#983).
- [SCENE] Schwierigkeitsgrad: Outcome stärker an Spieler/NPC‑Entscheidungen koppeln; Phase‑2 anheben (#917–#919).
- [SCENE] Cluster‑Index Vorschlag: dreistellige Codes (z. B. N99, C06), Temperatur‑Meta zur Nähe/Verwendung (#919).

Kanon‑Fakten [FACT?]
- [FACT?] Kontextprüfroutine kann vor Antworten laufen; Kennzeichnung „Kontextprüfung durchgeführt“ (#987–#991).
- [FACT?] Backup‑ZIP lokal gewünscht; Chat‑Spiegelung als Canvas/Datei (#895–#899).
- [FACT?] Fraktionswissen: Händler kennen Novapolis nicht direkt; nur Energieschwankungen und vermisste Karawane (#1033–#1035, #1039).

Charaktere [CHAR]
- [CHAR] – systemisch; keine neuen Charakterdetails.

Orte [LOC]
- [LOC] D5↔C6: Tunnelabschnitt zu Fuß begehbar; kein Brückenabschnitt (#983).

Projekte [PROJ]
- [PROJ] Codes/Cluster‑Harmonisierung; Doku anlegen (#963–#967, #997–#1000).
- [PROJ] Backup‑Pipeline: Export/ZIP; Doku/Anleitung (#895–#899, #1009).

Inventar/Verbrauch [INV]
- [INV] – keine neuen Inventardaten.

Offen/Prüfaufträge [OPEN]
- [OPEN] Codierungen (2 Systeme + Verhaltenscodierung) sauber mappen; Konflikte/laufende Migration dokumentieren (#963–#967).
- [OPEN] Kontextprüfung als feste Policy in Admin‑Canvas festschreiben; Schwellen/Umfang (#985–#991, #1001–#1005).
- [OPEN] Backup‑ZIP: Format/Ort/Downloadpfad festlegen (Repo vs. extern) (#893–#899).
- [OPEN] Cluster‑Index: Konkrete 3‑stellige Syntax + Temperaturmetadaten definieren (#919).

## Chunk part-011 (global 5001–5500) – Vorbesprechung Versorgung, Comms‑Reparatur, Canvas‑Ladung, Fraktionsblöcke

- Kontext: Missionseinordnung, C6/D5‑Besetzungen klären, Comms‑Reparatur priorisieren, Canvas‑Ladung/Blöcke‑Update, Backup‑Thema, RP‑Fortsetzung.
- Referenz: Nachrichten‑ID‑Bereich ca. #870–#954.

Szenenanker [SCENE]
- [SCENE] Missionslage: D5 ist zentral; C6 mit 3 Freiwilligen; Ronja/Reflex in C6 (Instandsetzung), wohnen D5 (#874–#875).
- [SCENE] Comms: Ronja/Reflex stabilisieren Verbindung vor Abmarsch; C6 informiert; C6‑Gruppe laden (#879–#886, #883).
- [SCENE] Kontext/Canvas laden: Fraktionen‑Hauptcanvas einbeziehen; RP‑relevante Daten priorisieren (#889–#909).
- [SCENE] Erinnerung: Funk war bereits repariert, aber schlecht (#911).
- [SCENE] Backup/Export: Wunsch nach ZIP/Spiegelung (anschließend wieder RP‑Fokus) (#893–#906).
- [SCENE] Balancing: Schwierigkeit Phase 2; Entscheidungen stärker gewichten (#917–#919).

Kanon‑Fakten [FACT?]
- [FACT?] C6‑Bewohner (freiwillig) = 3; Ronja/Reflex gehören D5 an (#875).
- [FACT?] Comms repariert, Zustand schlecht; Stabilisierung läuft (#911, #883).

Charaktere [CHAR]
- [CHAR] – keine neuen individuellen Details.

Orte [LOC]
- [LOC] D5 zentrale Fraktion Novapolis; C6 als Außenposten im Aufbau (#874–#875).

Projekte [PROJ]
- [PROJ] Blöcke‑Update (Fraktionen/NPC): in Gruppen laden und 3‑Schritt‑Update befolgen (#933–#949, #951–#954 in Anschlussbereichen).

Inventar/Verbrauch [INV]
- [INV] – keine neuen Inventardaten.

Offen/Prüfaufträge [OPEN]
- [OPEN] Schwierigkeit/Outcome‑Gewichtung operationalisieren (Regeln, Schwellen, Rückkopplung in Canvas) (#917–#919).
- [OPEN] Comms‑Qualitätsschema (Skala, Effekte auf Szenen) definieren (#911–#913).

## Chunk part-010 (global 4501–5000) – C6‑Raumplanung, Bewohner/Caravan‑Canvas, Reflex‑Vorstellung, Anomalie‑Kisten, Reinit‑Prompt

- Kontext: Morgen in C6, Frühstück und Stationsaufteilung, belastbare Nutzfläche und Limitierungen, Gruppen‑Canvas, Reflex‑Vorstellung, Fracht/Kisten, interne Gänge sichern, Geräte‑Erfindungen strikt vermeiden, Kontext‑Reset + Reinit‑Prompt mit festen Weltzuständen.
- Referenz: Nachrichten‑ID‑Bereich ca. #801–#869.

Szenenanker [SCENE]
- [SCENE] C6‑Nutzfläche: belastbare m²‑Angaben und konservative Startwerte gewünscht; schrittweise Ausbau (#805–#808).
- [SCENE] Aufteilung C6: 1/3 Händler (Novapolis), 1/3 Verwaltung/Werkstatt (Ronja), 1/3 Gemeinschaft/Besucher (provisorisch) (#811–#812).
- [SCENE] Bewohner/Caravan‑Canvas: keine Einzel‑Canvas für 6 NPCs; zwei Gruppen‑Canvas (Bewohner C6; Karawanengruppe Kora) (#815).
- [SCENE] Reflex‑Vorstellung: Hauptinstanz verbal; Vorstellung in C6‑Runde (#821–#823).
- [SCENE] Fracht/Kisten: Sichtung/Dokumentation; Objektivität + Würfelelement (#825–#828, #831).
- [SCENE] Interne Erkundung: interne Gänge freiräumen und sichern; vorsichtig, keine Gadgets aus dem Nichts (#833–#846).
- [SCENE] Kontext‑Reset/Reinit: Ausführlicher Reinit‑Prompt mit Weltzuständen/Regeln (#855).

Kanon‑Fakten [FACT?]
- [FACT?] C6 m² konservativ ansetzen; Ausbau erforderlich (Anfangs‑Limit) (#807–#808).
- [FACT?] Gruppen‑Canvas für Bewohner/Caravan statt Einzel‑Canvas (#815).
- [FACT?] Symbiose Stufe 1: nur direkte/verbale Kommunikation; Reflex bleibt an Ronja; Fortbewegung möglich, kein vollständiges Lösen (#831, #847–#848).
- [FACT?] Reinit‑Prompt schlägt feste Weltzustände vor (vorläufig):
	- station_c6_v2.3: 440 m²; Abschnitte A/B/C; Status Gelb‑Rot.
	- Mission Freilegung_C6_Nord aktiv.
	- Fracht: Kiste 7A „lebendiger Metallstaub“ resoniert mit Reflex; Kiste 9B Konklave‑Module RL (Ziel E2), Warnhinweis.
	- Reflex‑Regeln: Hauptkörper sprachfähig, gebunden; Nebeninstanz D5 nicht sprachfähig.
	- Keine „herbeigezauberten“ Geräte (#855, #843–#846).

Charaktere [CHAR]
- [CHAR] Kora/Händlerführung: Aufteilung/Bedarfe abstimmen (#811–#819).
- [CHAR] Ronja/Reflex: Vorstellung/Kommunikation; Vorsicht beim Erkunden (#821–#841).

Orte [LOC]
- [LOC] C6: drei Abschnitte A/B/C; interne teils verschüttete Gänge (#811–#812, #833–#841).

Projekte [PROJ]
- [PROJ] Reinit/Reset: Feste Zustände/Checkliste als Admin‑Baustein festhalten (#855).
- [PROJ] C6‑Aufteilung/Nutzfläche: Canvas aktualisieren, konservativ beginnen (#805–#812).

Inventar/Verbrauch [INV]
- [INV] Fracht‑Dokumentation: Kisten sichten/dokumentieren; keine neuen Gegenstände ohne RP‑Einführung (#825–#846).

Offen/Prüfaufträge [OPEN]
- [OPEN] C6 m² und Abschnittsaufteilung final bestätigen; Ausbauplan zeitlich staffeln (#805–#812).
- [OPEN] Reinit‑Prompt Inhalte in Admin/Unumstößlich‑Canvas prüfen/übernehmen; Evidenz/Versionierung (#855).
- [OPEN] Anomalie‑Kisten (7A/9B): Herkunft, Risiken, Interaktion mit Reflex; Öffnung nur mit Beschluss/Protokoll (#825–#833, #855).

## Chunk part-009 (global 4001–4500) – Core‑Chars Update, Kora‑Rollenfix, Woche‑1‑Sim, D5‑Slice Jonas/Pahl, Inventar‑Trennung

- Kontext: Backup↔Neue Version‑Vergleiche, Jonas/Pahl‑Canvas mit psych. Profil, Kora‑Rollenklärung (Novapolis‑Karawane vs. Händlergilde), Backups archivieren, erste Wochen‑Simulation aufsetzen, D5‑Alltag Jonas/Pahl mit Reflex‑Instanz, Dialog‑Canvas anlegen, Inventare D5/C6 strikt trennen.
- Referenz: Nachrichten‑ID‑Bereich ca. #706–#800.

Szenenanker [SCENE]
- [SCENE] Canvas‑Pflege: Jonas laden, psychologisches Profil ergänzen, Version vergleichen; danach Pahl identisch (#710–#729).
- [SCENE] Kora‑Rolle: Führt Novapolis‑Karawane, nicht Händlergilde‑Karawane in C6; fehlerhafte Version verwerfen (#736–#741).
- [SCENE] Wochen‑Simulation (Woche 1): Backups archiviert, Quer‑Verweise validiert, im 7‑Tage‑Rhythmus planen (#742–#746, #744).
- [SCENE] D5‑Slice: Jonas+Pahl, Reflex‑Nebeninstanz zeigt Eigenleben/Hilfe, Charakterisierung anbahnen (#779–#787).
- [SCENE] Dialog‑Canvas: Wichtige Gespräche als Blöcke sammeln (#789–#795).
- [SCENE] Inventar‑Trennung: D5 vs. C6 strikt; Datenkern gehört C6‑Stationsinventar (#771–#775, #684–#689 Verweise).

Kanon‑Fakten [FACT?]
- [FACT?] Kora ist Anführerin der Novapolis‑Karawane in C6 (nicht Gilde) (#736–#741).
- [FACT?] Wochen‑Zyklen (7‑Tage) für Sim angestrebt; Startpunkt nahe Karawanen‑Beitritt (#742–#746, #775–#779).
- [FACT?] D5 und C6 Inventare bleiben getrennt; Transfers nur via Mission/Logistik (#771–#775).
- [FACT?] D5: Jonas + Pahl + Reflex‑Nebeninstanz anwesend (#779–#787).

Charaktere [CHAR]
- [CHAR] Jonas/Pahl: Canvas aktualisiert inkl. psych. Profil, Abgleich gegen Backup (#710–#729).
- [CHAR] Reflex‑Nebeninstanz (D5): eigener Canvas erwünscht; mobil im Nahbereich, nicht sprachfähig (#782–#787).
- [CHAR] Kora: Rollenklärung als Karawanen‑Lead Novapolis (#736–#741).

Orte [LOC]
- [LOC] D5: Werkstatt (Jonas), Gemeinschaftsbereich (Pahl verletzt), Alltag/Ordnung thematisiert (#779–#783).

Projekte [PROJ]
- [PROJ] Woche‑1‑Sim: Parameter/Start festlegen; Ergebnisse textuell (Sprachausgabe) (#777–#779).
- [PROJ] Dialog‑Canvas: Blockformat mit Zeitstempel/Beteiligten (#789–#795).

Inventar/Verbrauch [INV]
- [INV] Datenkern in C6‑Stationsinventar belassen; keine stille Verschiebung (#771–#775, #684–#689).

Offen/Prüfaufträge [OPEN]
- [OPEN] Jonas’ Schwester: Lebensstatus verifizieren und konsistent verankern (#717–#721).
- [OPEN] Woche‑Sim‑Parameter (Zyklen, Scope, Grenzen) definieren (#742–#746, #775–#779).
- [OPEN] Dialog‑Canvas‑Blockformat/Index finalisieren (#789–#795).

## Chunk part-008 (global 3501–4000) – Indexe/Archive, Maschinenformat, Stations‑Ressourcen, Handel+Diplomatie, Logistik

- Kontext: Index/Meta‑Index anlegen (Novapolis, Händler, Meta Rest), Archivpfad trennen, Maschinenformat für Canvas, Station‑getrennte Ressourcen/Produktion, C6‑Generator (repariert), Handels/Diplomatie‑Canvas, Logistik mit Tunnel‑Restriktionen, Fraktionshandelsbeziehungen.
- Referenz: Nachrichten‑ID‑Bereich ca. #611–#700.

Szenenanker [SCENE]
- [SCENE] Indexe: Novapolis‑Index, Händler‑Index, Meta‑Index Rest; archivierte Versionen in separatem Pfad (#611–#617, #627–#633, #597–#605 Verweise aus part‑007).
- [SCENE] Maschinenformat: Canvas maschinenoptimiert, Ausgabe weiterhin formatiert (#605–#610).
- [SCENE] Ressourcen/Produktion: station‑getrennte Canvas (D5/C6 etc.) (#526–#529 Verweis, fortgeführt #611–#642).
- [SCENE] C6‑Generator: vorhanden und durch Ronja repariert; als Fakt in Ressourcen/Logistik führen (#536–#539).
- [SCENE] Handel/Diplomatie: gemeinsame Canvas; Handelsbeziehungen der Fraktionen andeuten (#540–#568).
- [SCENE] Logistik: Tunnelzustand als Constraint; Vermerk in Handels‑Canvas, Logistik‑Canvas anlegen (#585–#591, #589–#591).

Kanon‑Fakten [FACT?]
- [FACT?] Archivpfad für alte Versionen separat; Indexe einzeln, nicht monolithisch (#613, #627–#633).
- [FACT?] Canvas maschinenoptimiert speichern; Sprachausgabe separat formatieren (#605–#610).
- [FACT?] C6 verfügt über Generator; Ronja hat ihn repariert (vorläufig) (#536–#539).

Charaktere [CHAR]
- [CHAR] – keine neuen persönlichen Details, Fokus auf Admin/Struktur.

Orte [LOC]
- [LOC] C6: Generatorstatus gepflegt; Logistikpfade/Tunnel in Canvas verankern (#536–#539, #589–#591).

Projekte [PROJ]
- [PROJ] Handels+Diplomatie Canvas etablieren; Fraktionsbeziehungen/Bedarfe/Überfluss skizzieren (#540–#568).
- [PROJ] Logistik‑Canvas: Neben‑/Wartungsgänge dokumentieren (#589–#591).

Inventar/Verbrauch [INV]
- [INV] Handelslog pro Fraktion/Novapolis; monatliche Simulation optional (#560–#566).

Offen/Prüfaufträge [OPEN]
- [OPEN] Index‑Wöchentest: Automatische Prüfung, ob Cluster/Index die Wirklichkeit spiegelt (#647).
- [OPEN] Handelsbeziehungen initialisieren: Bedarfe/Überhänge je Fraktion; Diplomatie‑Gewichte (#562–#568).
- [OPEN] Logistik‑Verknüpfung in Handelsregeln formal machen (#585–#591).

## Chunk part-007 (global 3001–3500) – Fracht/ Missionen, Stations‑Trennung, Index/Meta‑Index, Maschinenformat‑Policy

- Kontext: Fracht der Karawane definieren und Missions‑Canvas aktualisieren; Vorschlag station‑gebundener Ressourcen‑Canvas; Handelslogs/‑Diplomatie aufsetzen; Logistik‑Canvas; Index/Meta‑Index; Policy „Canvas maschinenoptimiert“.
- Referenz: Nachrichten‑ID‑Bereich ca. #511–#610.

Szenenanker [SCENE]
- [SCENE] Fracht definieren; Missions‑Canvas aktualisieren; Reihenfolge strikt nacheinander, nicht parallel (#517–#525).
- [SCENE] Stationen trennen: Ressourcen/Produktion je Station (D5/C6) (#526–#529).
- [SCENE] Handels/Diplomatie‑Canvas etablieren; Fraktionen durchgehen (#540–#579).
- [SCENE] Logistik/Pläne: Nebengänge/Schacht in Logistik‑Canvas markieren (#589–#591 Hinweise in 009/008 fortgeführt).
- [SCENE] Index/Meta‑Index: Überblicks‑Canvas, nach Zugehörigkeit sortiert (#643–#647, #595–#603 in 008/007 Kontext).
- [SCENE] Maschinenformat‑Policy: Canvas maschinenlesbar speichern, Ausgabe formatiert (#605–#610).

Kanon‑Fakten [FACT?]
- [FACT?] Missions‑/Fracht‑Definition gehört in dedizierte Canvas; keine Parallelaktionen (#517–#525).
- [FACT?] Stationen physisch getrennt → Inventare/Produktionen trennen (#526–#529).
- [FACT?] Index/Meta‑Index für Sicht auf Personen/Fraktionen/Orte sinnvoll (#643–#647).

Charaktere [CHAR]
- [CHAR] – keine neuen individuellen Daten.

Orte [LOC]
- [LOC] D5/C6: getrennte Produktions‑/Ressourcenpfade (#526–#529).

Projekte [PROJ]
- [PROJ] Handels/Diplomatie‑Canvas und Logistik‑Canvas aufsetzen (#540–#591).

Inventar/Verbrauch [INV]
- [INV] Fracht definieren, Missionslog aktualisieren (#517–#523).

Offen/Prüfaufträge [OPEN]
- [OPEN] Maschinenformat‑Leitfaden schriftlich in Admin‑Canvas festhalten (#605–#610).
- [OPEN] Index/Meta‑Index Pflege‑Zyklus (wöchentlich) definieren (#647).

## Chunk part-006 (global 2501–3000) – Charaktere/Gruppen-Canvas, Dialog-Canvas, Reflex-Stufe, Jonas/E2, Missionslog/Anomalien

- Kontext: Konsolidierung der Canvas-Struktur (Charaktere, Gruppen), strikte Gruppenregeln für Novapolis, Dialog-Canvas mit Blockformat, Korrekturen zu Reflex-Symbiose, Jonas’ Herkunft/Aufsicht, Missionslog-Setups, Anomalien/Caravan-Logik.
- Referenz: Nachrichten-ID-Bereich ca. #419–#510.

Szenenanker [SCENE]
- [SCENE] Canvas-Aufbau: Charaktere und Gruppen anlegen/prüfen; erst Charaktere (Ronja, Reflex, Jonas …), dann Gruppen (NPC-Sammler) (#424–#466).
- [SCENE] Dialog-Canvas: Einführung eines Canvas für „wichtige Konversationen“ mit einheitlichem Blockformat (Zeit, Sprecher, @mention, Nachricht) (#442–#447).
- [SCENE] Kontext-/Fehlerkorrekturen: „erstes Aufhalten durch Reflex“ uneindeutig; Event vorerst auslassen (#450–#454).

Kanon-Fakten [FACT?]
- [FACT?] Ronja brachte D5 auf 100%; 98% bezog sich wahrscheinlich auf C6 (vorläufig) (#419).
- [FACT?] Reflex-Symbiose Stufe 1: Reflex wie „Neoprenanzug“, keine Stufe‑2‑Fähigkeiten; Kommunikation überwiegend verbal (#435, #434–#438).
- [FACT?] Jonas wurde später von einer Reflex‑Instanz beaufsichtigt; Erstfund im Tunnel auf dem Weg nach C6 (#456, #458–#459).
- [FACT?] Gruppenpolitik Novapolis: keine erfundenen Mitglieder; C6‑Einwohner‑Gruppe leer; D5 besteht aus Ronja, Reflex, Jonas, Pahl (#469).

Charaktere [CHAR]
- [CHAR] Ronja: Zitat „Pause als Beleidigung“ soll in Profil; aktuelle Position mit Reflex in C6 (Lebewesen unter Boden) prüfen (#432).
- [CHAR] Reflex: Kindlicher Touch ergänzen; bleibt an Ronja gebunden; keine Stufe‑2‑Funktionen (#437–#438, #435).
- [CHAR] Jonas: Herkunft E2 (Gasleck) im Zweifel; Schwester zurückgelassen – validieren (#456).

Orte [LOC]
- [LOC] C6: „Lebewesen unter dem Boden“ als offener Faktor; Dialog‑Canvas sammelt Kernaussagen dazu (#432, #442–#447).

Projekte [PROJ]
- [PROJ] Dialog‑Canvas: Blockformat definieren und Beispiele aus Chat extrahieren (#442–#447, #445–#449).
- [PROJ] Gruppen‑Canvas: drei Gruppen für Novapolis (Karawane, Einwohner D5, Einwohner C6) + je Fraktion „Scout <Name>“ (#464–#466).
- [PROJ] Missionslog: Aktive/Abgeschlossene Missionslogs einführen (#493–#505).

Inventar/Verbrauch [INV]
- [INV] Prüffrage: Hat D5 einen Reaktor? (Konflikt/Hinweis) (#422). Leichenverbleib (Gang/C6) – ethischer Umgang als Policy prüfen (#422).

Offen/Prüfaufträge [OPEN]
- [OPEN] D5‑Reaktor: Existenz/Regeln bestätigen; Energiemodell aktualisieren (#422).
- [OPEN] Leichen‑Handhabung: Lagerort und Ethik (Dünger‑Gedanke) klären (#422).
- [OPEN] Reflex „erstes Aufhalten“: exakte Szene/Lokation ermitteln oder als Legende kennzeichnen (#450–#454).
- [OPEN] Dialog‑Blockformat finalisieren (Zeitstempel, Name, @mention, Nachricht) und Dubletten‑Prüfung (#442–#447).
- [OPEN] Jonas’ Herkunft E2 vs. E3 und Schwester‑Status belegen (#456).
- [OPEN] Fraktionsführer (drei) benennen und in Gruppenstruktur abbilden (#460).

## Chunk part-005 (global 2001–2500) – Versionierung/Backups, C6-Korrektur, Fraktionen/Inventare, Währung/Bullets

- Kontext: Verhaltens-/Regel‑Update (Versionierung, Kontextprüfung, Archivierung), C6‑Beschreibung/Fehlerkorrektur, Fraktions‑Canvas und Inventare, Währung als „Kugeln“ mit 10:1‑Ratio, Index‑Validierung.
- Referenz: Nachrichten-ID-Bereich ca. #320–#418.

Szenenanker [SCENE]
- [SCENE] Versionierung/Policy: max. drei Backups/Versionen je Canvas; Älteres archivieren (#323, #341–#345).
- [SCENE] Kontextprüfung vor Antworten; Priorisierung/Aktualität bewerten (#325–#330).
- [SCENE] C6‑Canvas neu anlegen und korrigieren: C6 verbindet Metro (nicht Oberfläche) (#356–#361).
- [SCENE] Fraktionen/Inventare: vier Hauptfraktionen prüfen; pro Fraktion Inventar anlegen; Novapolis benennen (#366–#387, #410–#418).
- [SCENE] Währung: „Kugeln“ (Munition) als Currency‑Canvas; 10:1 neu:alt; in Fraktionsinventare eintragen (#388–#397, #401–#402).

Kanon-Fakten [FACT?]
- [FACT?] Drei Versionen/Backups je Canvas genügen; Älteres archivieren (#323).
- [FACT?] C6: Verbindung zur Metro, nicht zur Oberfläche (#359–#361).
- [FACT?] Währung „Kugeln“: fabrikneu = 10x handgefertigt; als Gegenstand in Inventaren geführt (#388–#397, #401–#402).
- [FACT?] Novapolis als Fraktionsname bestätigt; eigener Fraktions‑Canvas + Inventar (#412–#416).

Charaktere [CHAR]
- [CHAR] – keine neuen individuellen Details; Fokus auf Admin‑Policies und Fraktionen/Inventare.

Orte [LOC]
- [LOC] C6‑Beschreibung korrigiert (Metro‑Verbindung); C6‑Canvas existiert wieder (#356–#361).

Projekte [PROJ]
- [PROJ] Behavior/GPT‑Regeln: Kontextprüfung, Priorisierung, Archiv‑Zyklus in Regeln verankern (#325–#333, #339–#345).
- [PROJ] Fraktions‑Inventare: je Fraktion getrennte Inventar‑Canvas anlegen/prüfen (#385–#387, #275–#276 Verweis aus part‑004).
- [PROJ] Currency‑Canvas und System‑Index pflegen; Überschreibungsfehler validieren (#403–#409).

Inventar/Verbrauch [INV]
- [INV] Verteilung der Kugeln je Fraktion (Mengen offen); als normaler Gegenstand buchen (#391–#397, #401–#402).

Offen/Prüfaufträge [OPEN]
- [OPEN] Currency‑Canvas‑Duplikate/Überschreibung prüfen und bereinigen (#405–#409).
- [OPEN] Fraktionsbeziehungen/Wissensstände: Außenfraktionen wissen nichts von D5/Novapolis (prüfen) (#368–#376).
- [OPEN] Verteilungslogik Kugeln definieren (Startmengen, Umlauf) und dokumentieren (#388–#397).

## Chunk part-004 (global 1501–2000) – C6‑Instandsetzung, Comms‑Priorität, Sensoren/Verbrauch, Canvas‑Fehler, Wochen-/Handelszyklus

- Kontext: Vorbereitung auf C6‑Arbeiten (Materialtransport, Reflex als Exo), Priorisierung Kommunikationslink, Sensorsetup und Materialprüfung, wiederholte Canvas‑Überschreibungen und Ursache, Wochen‑Zyklus und Handelszyklus koppeln, Reflex/Ronja‑Szene vertiefen.
- Referenz: Nachrichten-ID-Bereich ca. #221–#319.

Szenenanker [SCENE]
- [SCENE] Ronja+Reflex brechen mit Material nach C6 auf; Reflex hilft als Exoskelett (#225, #229–#236).
- [SCENE] Comms zuerst: Verbindung wiederherstellen, bevor Luft/Beleuchtung (#247–#248, #243–#246).
- [SCENE] Sensoren installieren; Materialverfügbarkeit im Inventar prüfen (#251–#254).
- [SCENE] Falsches Canvas überschrieben (mehrfach: Varek Solun, Handelsprotokoll, Reflex); Ursachenanalyse angestoßen (#261–#266, #295–#303).
- [SCENE] Wochen‑Zyklus (7 Tage) und Handelszyklus koppeln (#281–#285).
- [SCENE] Reflex/Ronja: Schutz/Kindlichkeit/Komfort; Kontrollübergabe als Einigungspunkt (#287–#294).

Kanon-Fakten [FACT?]
- [FACT?] Kommunikationslink D5↔C6 hat Priorität vor Luft/Beleuchtung (#247–#248).
- [FACT?] Material-/Verbrauchsbuchung vor Fortsetzung der Wartung; Inventar korrekt zuordnen (#259–#264).
- [FACT?] 7‑Tage‑Zyklus bestätigt; Handelszyklus daran ausrichten (#281–#285).

Charaktere [CHAR]
- [CHAR] Ronja: vorsichtig/gründlich, priorisiert Vorbereitung; akzeptiert Reflex’ Schutz in belastenden Momenten (#249–#255, #287–#294).
- [CHAR] Reflex: beschützend, besitzergreifend, kindlich; zeitweise Kontrolle, Sinne dosiert zurück (#287–#294).

Orte [LOC]
- [LOC] D5↔C6: Tunnel begehbar, Materialtransport zu C6; keine Aussage über Zugbetrieb (Korrektur) (#227–#231).

Projekte [PROJ]
- [PROJ] Canvas‑Adressierung/Index: Nicht per Reihenfolge, sondern per ID/Schlüssel adressieren; Versionierte Canvas statt Überschreiben (#301–#306).
- [PROJ] Faktions‑Inventare: Gesamtes Fraktionsinventar‑Canvas anlegen; plus separates Canvas für Fraktionshändler (#267–#276).

Inventar/Verbrauch [INV]
- [INV] Verbrauch/Materiallog führen (Quelle/Ziel‑Inventar, Quittungen, Verantwortliche) vor jeder Arbeit (#259–#264).

Offen/Prüfaufträge [OPEN]
- [OPEN] Comms‑Reichweite/Qualität modellieren; Effekte auf Szenen definieren (#247–#248).
- [OPEN] Canvas‑Index‑Stabilität: Leitfaden gegen „falsches Canvas überschrieben“ festschreiben (#261–#266, #301–#306).
- [OPEN] Wochen‑/Handelszyklus formal dokumentieren (Startpunkt, Scope) (#281–#285).

## Chunk part-003 (global 1001–1500) – Fraktionsanlage, Weltzüge, Händlerkontakt C6, C6 als Puffer, Canvas‑Fehler

- Kontext: Anlage von drei Hauptfraktionen (Arkologie A1, Eisenkonklave, Flüsterkollektiv) plus Händlergilde, zweiwöchige Fraktionszüge bis Tag 20, Karawane Richtung D‑Sektor, C6 als öffentlich zugänglicher Puffersektor von Novapolis, mehrfache Canvas‑Überschreibungsfehler, Erstkontakt Reflex↔Händler in leerer C6.
- Referenz: Nachrichten-ID-Bereich ca. #179–#220.

Szenenanker [SCENE]
- [SCENE] Fraktionen & Anführer anlegen (mit verdeckten Zielen) (#179–#184, #181–#184).
- [SCENE] Fraktionszüge (2 Wochen) – verdeckte Weltreaktionen auf D5/C6‑Signale; Händlerkarawane unterwegs, Ankunft ~Tag 20 (#185–#188).
- [SCENE] Händlerkontakt: Reflex eröffnet Gespräch in leerer, unreparierter C6; Händler kennen Reflex nicht (#210–#216, #211).
- [SCENE] C6‑Policy: C6 bleibt Kernsektor von Novapolis, aber äußerer, öffentlicher Bereich für Gäste/Handel (#199).
- [SCENE] Canvas‑Verwechslungen: Händler‑Canvas vs. C6 überschrieben; Korrekturen durchgeführt (#201–#209).

Kanon-Fakten [FACT?]
- [FACT?] Vier zusätzliche Fraktionen im Spiel: Arkologie A1, Eisenkonklave, Flüsterkollektiv, Händlergilde (vorläufig; Wissensstände beachten) (#179–#186).
- [FACT?] Weltzüge: A1 „Projekt Theta“ (Aufklärung), Konklave Aufklärungsteam in D4, Flüsterkollektiv sendet Töne (F3→D5), Händlerkarawane H‑47 unterwegs (vorläufig) (#188).
- [FACT?] C6 fungiert als öffentlicher Puffer für Gäste/Handel; Novapolis behält Kontrolle (#199).

Charaktere [CHAR]
- [CHAR] Reflex: Dialogführer beim Händlerkontakt; Händler kennen Reflex zunächst nicht (#211–#214).
- [CHAR] Ronja: wahrt Vorsicht/Heimvorteil; Türen verschlossen (#191–#193).

Orte [LOC]
- [LOC] C6: leer/ unrepariert zum Zeitpunkt des Händlerkontakts; Gespräch findet in dieser leeren Station statt (#215).

Projekte [PROJ]
- [PROJ] Händler‑Stützpunkt in C6 als Idee (Handel fördern, Pufferfunktion) – in C6‑Canvas vermerken (#197, #199).
- [PROJ] Weltzüge‑Protokoll: Rückschreiben in Fraktions‑Canvas (vorläufig, zu verifizieren) (#188–#190).

Inventar/Verbrauch [INV]
- [INV] – keine neuen harten Inventarfakten; Fokus auf Handel/Bewegungen.

Offen/Prüfaufträge [OPEN]
- [OPEN] Fraktionszüge als Kanon übernehmen oder als „Sim‑Ergebnis (vorläufig)“ markieren? Quellen/Canvas‑Updates prüfen (#188–#190).
- [OPEN] Händler‑Canvas korrekt anlegen/prüfen; Überschreibungen rückgängig machen (#201–#209).
- [OPEN] Wissensmatrix: Händler kennen Reflex nicht – in Wissens‑/Sichtbarkeitsmatrix verankern (#211).
- [OPEN] C6‑Status (leer vs. später teils repariert) chronologisch konsistent führen (#215).

## Chunk part-002 (global 501–1000) – Symbiose Stufe 1, Jonas‑Einführung, C6‑Check, Nordlinie 01, Stil/Regeln

- Kontext: Präzisierung Reflex=Neoprenanzug (Stufe 1), Jonas anlegen, D5 98%‑Status (früh), C6 prüfen (Funken/Scans), Leichenhinweise, Projekt „Nordlinie 01“, Inventarupdates, Stilregel (ohne Quotes), Regellockerung zu Canvas‑Anzahl, umfassender Datenabgleich.
- Referenz: Nachrichten-ID-Bereich ca. #98–#178.

Szenenanker [SCENE]
- [SCENE] Exo‑Idee: Material/Herstellung; Festlegung „Neoprenanzug unter Kleidung“ (#103–#109).
- [SCENE] Jonas: misstrauische Befragung/Einführung, kleiner Werkstattraum unter D5 (#111–#133, #131–#132).
- [SCENE] C6‑Check: Funken/Scans nach Reaktorwarnungen; Leichenhinweis in Station (#137–#156, #153).
- [SCENE] Nordlinie 01: Projekt‑Canvas anlegen (#159–#160).
- [SCENE] Stil/Regeln: Ohne Quotes (#165); „ein Canvas pro Anfrage“ Regel gestrichen (#169–#172); Konsistenzprüfung/Abgleich (#173–#178).

Kanon-Fakten [FACT?]
- [FACT?] Symbiose Stufe 1: Reflex trennt sich nicht; eng anliegend; Kommunikation vorwiegend verbal (#123, #109).
- [FACT?] Jonas: neuer Charakter; kann Werkstatt unter D5 einrichten; ggf. unter Aufsicht Reflex‑Instanz (#125–#132).
- [FACT?] D5 Status damals 98% (früher Stand, später 100%) (#86, Folgedialoge).
- [FACT?] Projekt „Nordlinie 01“ existiert als Canvas (Tunnel D5–C6) (#159–#160).

Charaktere [CHAR]
- [CHAR] Ronja: ordnungsliebend, methodisch; priorisiert Sicherheit/Scans; pflegt Stilregeln (#165).
- [CHAR] Reflex: Schutz/dämpfende Kontrolle andeutungsweise (System‑Gefühl) (#56–#60, deckt spätere Ausgestaltung).
- [CHAR] Jonas: Einführung, Werkstatt/Beaufsichtigung (#125–#132).

Orte [LOC]
- [LOC] D5: Kontrollraum/Ordnung; Werkstatt unten (#82–#83, #131–#132).
- [LOC] C6: per Funk/Scan geprüft; unklarer Besetzungs‑/Zustandsstatus (damals) (#137–#142).

Projekte [PROJ]
- [PROJ] Nordlinie 01: Abschnittsplanung/Materialliste; Bestandsaufnahme Tunnel (#157–#160).

Inventar/Verbrauch [INV]
- [INV] Inventar‑Updates angefordert; fehlende Schweißausrüstung/Adapter DN60, Hydrofilterbehälter als Reserve (spätere Bestätigungen) (#129–#130; Kontext Folgeteile).

Offen/Prüfaufträge [OPEN]
- [OPEN] „System“ das dämpft: frühere Darstellung sauber Reflex‑Mechanik zuordnen (Terminologie bereinigen) (#56–#60 vs. part‑014 #1183–#1207).
- [OPEN] Leichen‑Lokation in C6 verifizieren (#153).
- [OPEN] Jonas‑Werkstatt/Beaufsichtigung durch Reflex‑Instanz konsistent verankern (Detachment‑Regeln beachten) (#131–#132).
- [OPEN] D5 98% → 100% Übergang zeitlich markieren und referenzieren (#86 vs. spätere Teile).

## Chunk part-001 (global 1–500) – Setup, Ronja Charakter, erste Szenen in D5, Wurzelgewebe‑Idee

- Kontext: ZIP‑Setup/Struktur, Mehrfach‑Canvas erlaubt, Ronja Charakterdaten (Skills/Inventar/Motivation/Makel), erste Erkundungsszenen in D5, „System“‑Dämpfungserlebnis, Interesse am Wurzelgewebe als eigens identifizierte Entität.
- Referenz: Nachrichten-ID-Bereich ca. #1–#97.

Szenenanker [SCENE]
- [SCENE] Setup: ZIP entpacken, Canvas‑Struktur, RP‑Start (#1–#8).
- [SCENE] Charakter Ronja: Stats/Skills/Inventar (Gasmaske, Werkzeugkit), Motivation/Makel (#12–#24, #22).
- [SCENE] Erste D5‑Szenen: Wartungsauftrag, vorsichtiges Vorgehen, Dämpfungsgefühl („System“) (#28–#60).
- [SCENE] Interesse am Wurzelgewebe (als mögliche eigene Entität), Exo‑Vorstellung (#90–#96, #92–#93).

Kanon-Fakten [FACT?]
- [FACT?] Ronja: Technikerin, 36, geübt/meist. Skills gemäß Angaben; Gasmaske/Werkzeugkit im Startinventar (#12, #14–#16, #22).
- [FACT?] Dämpfungsmechanik: frühe Darstellung als „System“ → später Reflex‑Schutzmechanik zu mappen (vorläufig) (#56–#60 vs. part‑014/#1183–#1207).
- [FACT?] Wurzelgewebe als identifizierte Besonderheit (Anomalie) – Status offen (#93).

Charaktere [CHAR]
- [CHAR] Ronja: Motivation Ordnung/Licht/Flora; Makel Sinnzweifel (#24).
- [CHAR] Reflex (proto‑Darstellung): Andeutung Schutz/Dämpfung (später verfeinert) (#56–#60).

Orte [LOC]
- [LOC] D5: erste Arbeits‑/Ordnungsszenen, Kontrollraumpflege (#80–#84).

Projekte [PROJ]
- [PROJ] D5‑Grundsanierung: Kontrollraum/Beleuchtung; später Ausbau (Verknüpfung zu Nordlinie 01 möglich) (#82–#84).

Inventar/Verbrauch [INV]
- [INV] Startinventar Ronja (Gasmaske, Werkzeugkit) (#22).

Offen/Prüfaufträge [OPEN]
- [OPEN] „System“ vs. Reflex: Terminologie vereinheitlichen (Schutzmechanik) (#56–#60, später #1183–#1207).
- [OPEN] Wurzelgewebe: Einordnung als Anomalie/Ort/Entität festlegen; Protokoll/Canvas definieren (#92–#94).

