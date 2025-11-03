## Korrekturen / Beschlüsse – Namen

- [NAME-RONJA] Nachname von Ronja
	- Evidenz: `database-raw/99-exports/RAW-canvas-2025-10-16T11-45-00-000Z.txt` (Sidecar-Flags: vorsichtig_behandeln, korrupt) enthält „Ronja Vallin“; Canon-Datei: `database-rp/02-characters/Ronja-Kerschner.md`.
	- Beschluss: Canon ist „Ronja Kerschner“. Vorkommen „Vallin“ gelten als fehlerhafte Quelle und werden bei Ingest normalisiert („Vallin“ → „Kerschner“) mit Review-Hinweis.

# Unklarheiten / Entscheidungsbedarf (vorläufig)

Hinweis: Diese Liste basiert auf den Chunks part-011 und part-022 (neueste Passagen). Markiere, was gilt, oder gib Alternativen vor.

## Fraktionen / Benennungen
- [x] [NAME] „Schatten“/„Lumen“/weitere – Welche Benennung ist gültig? (Canvas-Drift vermutet)
	- Beschluss: Keine der Benennungen („Schatten“/„Lumen“) wird verwendet; streichen zur Drift-Bereinigung.
- [x] [SET] Vier Hauptfraktionen bestätigen? (Eiserne Enklave, Akologie, Händlerbund, Schienenbund) + „Novapolis“, „Freie Gruppen“
	- Evidenz: #1824 bekräftigt 4 Hauptfraktionen + Novapolis/Freie Gruppen.
	- Beschluss: Kanonisch sind 4 Hauptfraktionen + Novapolis/Freie Gruppen.
 - [x] [GHOST-FACTION] „Neue/Unbekannte Fraktion“ in gelöschtem Bericht – existiert sie tatsächlich? Falls nein: Ursachenanalyse Drift und Bereinigung.
	- Evidenz: #1761–#1763 Hinweis auf unbekannte Fraktion in gelöschtem Bericht.
    - Beschluss: Existiert nicht; als Drift markieren und bereinigen.
 - [x] [COUNT] Anzahl Hauptfraktionen klären: 4 vs. 5 – welche ist kanonisch, wie heißen sie?
	- Evidenz: #1427 (fordert 5), #1824 (nennt 4 + Novapolis/Freie Gruppen).
    - Beschluss: 4 Hauptfraktionen (Eiserne Enklave, Akologie, Händlerbund, Schienenbund) + Novapolis/Freie Gruppen.

- [x] [EK-LEADERSHIP] Führung/Struktur Eisenkonklave: Kommandant Varek Solun als Kanon bestätigen; Rollen/Vertretung klären (Militär/Operativ vs. Zivil/Logistik).
	- Evidenz: `database-raw/99-exports/RAW-canvas-2025-10-16T03-25-00-000Z.txt` (char_varek_solun_v1), `database-raw/99-exports/RAW-canvas-2025-10-16T16-55-00-000Z.txt` (Cluster „eisenkonklave_operativ“ führt `char_varek_solun_v1`).
	- Beschluss: A.2 – Varek Solun führt Militär + Zivil; Stellvertretung: Lyra Hest (Zivil/Logistik). Verlinkungen in Fraktions-/Missions-/Relations‑Canvas setzen.

- [x] [EK-TAXONOMY] Standort‑Codierung der Eisenkonklave harmonisieren (H12 vs. Sektor_H3) und mit Cluster/Logistik/Events konsistent machen.
	- Evidenz: char‑Canvas (H12), Cluster‑Index (Sektor_H3), Ereignislog (H‑47 Route).
	- Beschluss: B.1 – Endgültig „H12“. Alias „Sektor_H3“ bleibt als Redirect.

- [x] [ARKO-RESEARCH] Arkologie A1 – Forschungsrat/Leitung und Signal‑Mapping: Dr. Liora Navesh als Leiterin Forschungsrat/Chefärztin Biotechnologie bestätigen; „SÜDFRAGMENT“/H‑47 gegen Ereignislog mappen.
	- Evidenz: `database-raw/99-exports/RAW-canvas-2025-10-16T03-25-10-000Z.txt` (char_liora_navesh_v1), `database-raw/99-exports/RAW-canvas-2025-10-16T05-34-00-000Z.txt` (Ereignislog v1: südliches Signalfragment, H‑47 Route), Cluster‑Index (Arkologie_A1 vorhanden; Führungsrolle dort: char_lys_annar_v1).
	- Beschluss: C.1 – Dr. Liora Navesh bestätigt. „SÜDFRAGMENT“ bleibt vorerst ohne H‑47‑Mapping (bestätigt). [FR-KNOWLEDGE] strikt: A1 kennt Novapolis/D5 nicht.

- [x] [ARKO-TAXONOMY] Arkologie_A1 Standort‑/System‑Taxonomie konsistent halten (Arkologie_A1 vs arkologie_a1, Relations/Cluster‑IDs, Sicherheitsprotokolle A‑9 Referenz).
	- Evidenz: char_liora_navesh_v1 (Arkologie_A1), Cluster‑Index (arkologie_a1), relationslog_arkologie_v1.
	- Beschluss: D.3 – Schreibschema „Arkologie A1“ (Titel‑Case, Leerzeichen) als Anzeige; System‑ID „Arkologie_A1“. Redirects aus `arkologie_a1` setzen.

## Orte / Stationen
- [x] [D5] D5 als Basis von Novapolis, einziger Reaktor, 100% Zustand – endgültig bestätigen?
	- Beschluss: D5 ist Basis von Novapolis, einziger Reaktor, aktuell 100%.
- [x] [C6] C6: Händlerkarawane ansässig, Algen/Pilz, Strom von D5, Kreuzungsstation, Tunnel D5–C6 in Reparatur – bestätigen?
	- Beschluss: Bestätigt. Einige Bewohner stammen ursprünglich aus einer Händlerkarawane; Algen/Pilz aktiv; C6 erhält teilweise Strom von D5; Kreuzungsstation; Tunnel D5–C6 in Reparatur.
 - [x] [N7] „N7“ vollständig entfernen/ignorieren? (keine Referenzen mehr zulassen)
	- Beschluss: Nicht entfernen. Als Anomalie-Ort beibehalten; Umbenennung auf „C6‑Nord“ zur Verwechslungsminimierung.
- [x] [LAYOUT] Fixe Umgebungsbeschreibungen und Maße festlegen (Eingang vom Tunnel aus, Wegeführung, Lichtverhältnisse, Raumgrößen/SQM je Raum, Schlafkammern, Lagerräume).
	- Evidenz: #1694 (fixe Beschreibungen + Maße), #1698 (Raumgrößen), #1712 (C6-SQM-Zuteilungen), #1696 (Beleuchtung Reparatur, Linienabgänge: D5, E3, F1, +1 unbekannt).
	- Beschluss: Layout-Minimum festschreiben inkl. „Kleines Lazarett“. Detailwerte werden im C6-Canvas hinterlegt.
- [x] [LIFT] D5: Lastenaufzug unter Bahnsteig mit 2t Traglast wiederherstellen.
	- Evidenz: #1700 (Aufzug zurücksetzen).
	- Beschluss: Wiederherstellung beschlossen; Status: angestoßen.
- [x] [WORKSHOP] D5: Entstehungsort Reflex – kleine Werkstatt/Wartungsraum unter Kontrollbereich D5 – exakt verorten und beschreiben.
	- Evidenz: #1209 (Entstehung/Ort Reflex).
	- Beschluss: Westseitiger Wartungsschacht, hinter dem Signalraum (unter Kontrollbereich D5).
- [x] [POP] Einwohnerzahl konsolidieren: Max ~29 humanoide (Karawane 6, E3 20, + Jonas, Pahl); C6 20 Flüchtlinge + 4 Karawane; Abweichungen korrigieren.
	- Evidenz: #1511–#1519 (Bewohnerlisten, Archivierung Nia/Rell), #1519 (Obergrenze).
	- Beschluss: Bestätigt – Karawane 6, Flüchtlinge 20, plus Jonas, Pahl, Ronja ⇒ ~29 Gesamt. Abweichungen in Canvas korrigieren.
- [x] [C6-LINES] C6 Liniennetz und Zugänge finalisieren: D5‑Linie, verschütteter Trakt, F1‑Verbindung, Karawanenlinie, Wandtunnel (Fußgängerzugang) – Bezeichnungen und Status.
	- Evidenz: #1345–#1349 (Linien/Wandtunnel), #1696 (4 Linienhinweis, part‑020).
	- Beschluss: Linie D5–C6 „aktiv, in Reparatur“; F1‑Verbindung „eingestürzt, reaktivierbar“; E3‑Verbindung „offen, begehbar, nicht instandgesetzt; vermutlich befahrbar (Karawanenroute)“; Karawanenlinie „operativ, geringe Kapazität“; Wandtunnel „begehbar, riskant“; C6–C7 „offen, begehbar, nicht instandgesetzt; vermutlich befahrbar (wie E3)“.
- [x] [E3-E2] Gasunfallstation klären: E3 oder E2? Zusammenhang mit Jonas’ Herkunft und Tunnel‑Abzweig verifizieren.
	- Evidenz: #1215 (Unfallsstation unsicher, E3/E2), #1391–#1397 (E3‑Evakuierung).
	- Beschluss: E2 ist die Gasunfall‑Station. Zusammenhang mit Jonas’ Herkunft entsprechend anpassen; Tunnel‑Abzweig verifizieren.

- [x] [C6-SQM] C6 nutzbare Fläche konservativ validieren (Startwert 440 m²?) und Ausbau‑Roadmap; Aufteilung A/B/C nachvollziehbar machen.
	- Evidenz: #805–#808 (konservativer Start), #855 (Reinit: 440 m², A/B/C, „Gelb‑Rot“).
	- Beschluss: Startnutzfläche 440 m² (konservativ). Flächenaufteilung: A 30% / B 40% / C 30% (Start).
- [x] [MAPS] Canvas „Pläne von Novapolis“: schematische Karten zulassen (D5/C6/Territorium) mit striktem Hinweis „nicht als Referenz“; Versionierung/Layering.
	- Evidenz: #1091–#1104 (Kartenwunsch, schematischer Hinweis, V1.2), #1099–#1101 (Ebenen andeuten).
	- Beschluss: Schematische Karten zulässig, mit deutlichem Hinweis „nicht als Referenz“ und Versionierung/Layern.

## Projekte / Tunnel Nordlinie
 - [x] [PROGRESS] Letzter Baufortschritt 40% – bestätigen oder korrigieren?
    - Beschluss: 40% bestätigt.
 - [x] [METHOD] Fortschrittsrechnung: Differenzbasiert vs. Tagesleistung (% pro Tag/Person) – gewünschte Methode?
	 - Beschluss: Tagesleistung (m/Tag/Team), skaliert mit Teamgröße/Erschöpfung; speist Fortschrittsbalken.
 - [x] [LENGTH] Fixe Tunnel-Gesamtlänge festlegen (ggf. aus Reisezeit herleiten) und für Fortschrittsberechnung verwenden.
	- Evidenz: #1694 (Tunnel-Länge ableiten aus Reisezeit).
    - Beschluss: Gesamtlänge 2 600 m (fix) für Fortschrittsberechnungen.

- [x] [PARALLEL] Parallele Arbeiten von C6-Seite starten, sobald Quarantäne Ende bestätigt.
	- Evidenz: #1573 (Prüfung auf Ende Quarantäne, paralleler Start).
    - Beschluss: Start ja, sobald Quarantäneende bestätigt.
 - [x] [EVAL] Technische Bewertung Tunnel (Ziele präzisieren, Personalbedarf aus C6, realistischer Zeit- und Materialaufwand mit Referenzen) vor Freigabe festlegen.
	- Evidenz: #1488–#1489 (Anmerkungen zur Präzisierung/Mittelung).
    - Beschluss: Checkliste aktiv – Ziele/Abschnitte, Blocker, Personal aus C6, Zeit-/Materialbedarf mit Referenzen; plus Ereignisprotokoll (Störungen/Unfälle) als Freigabe-Kriterium.

## Energie / Inventar
 - [x] [ENERGY] Energieformel „D5 -8 / C6 -12 = -20; D5 +10 = -10“ – gültig/ungültig? Quelle/Regel festlegen.
	- Evidenz: #1806 (Formel-Frage), #1757–#1759 (Reaktor-Produktion, Logistik-Verknüpfungen, Zellensoll ggf. 2 statt 4).
    - Beschluss: Dynamische Tagesbilanz pro Knoten; das Format „D5 -8 / C6 -12 = -20; D5 +10 = -10 (Zellen)“ ist als Darstellung zulässig. Beispielwerte aktuell: D5 Verbrauch 8, C6 Verbrauch 12, D5 Produktion +10 → Nettoverbrauch 10 Zellen bei Verbundbetrieb und laufender Sanierung.
 - [x] [LOG-LINKS] Logistik-Canvas-Verlinkungen robust machen (Generator/Energie-Konten), Lazy-Load vs. dauerhaft aktiv klären.
	- Evidenz: #1759 (Verknüpfungs-/Lazy-Load-Problematik).
    - Beschluss: Hybrid – Kernkonten dauerhaft aktiv; periphere/temporäre Konten via Lazy-Load mit Health-Check.
 - [x] [RECHARGE] D5-Reaktor lädt Zellen; C6 teilweise durch D5 versorgt – Umfang/Regeln bestätigen und verlinken.
 	 - Evidenz: #1658 (Aufladung in D5; C6-Teilversorgung durch D5 prüfen).
	 - Beschluss: Zellen werden in D5 geladen; C6 ist teilweise über D5 versorgt (Regeln in Logistik verlinken).
     - Erweiterung: Versorgung ist infrastrukturlimitiert; theoretisch könnte D5 mehr versorgen, praktisch begrenzen Leitungs-/Schaltzustand und Reaktorkapazität den Umfang.

- [x] [CARRY] Tragekapazität pro Person modellieren (Richtwert ~50 kg; dynamisch nach Größe/Training/Gesundheit); Missions‑Inventarableitung festlegen.
	- Evidenz: #1213 (Tragekapazität ~50 kg, dynamisch).
	- Beschluss: Richtwert 50 kg pro Person; dynamische Anpassung nach Größe/Training/Gesundheit. Missions‑Inventar wird aus Team‑Tragekapazität abgeleitet.

- [x] [UNITS] Harte Einheiten für Inventare/Bestände (Tonnen/Meter/Volumen) verbindlich festlegen und pflegen (Vorratsindex u. a.).
	- Evidenz: #1527 (Anforderung Einheiten), #1529 (keine unbelegten Bestände).
    - Beschluss: Masse kg/t; Länge m; Fläche m²; Volumen m³; Energie kWh; Zellen in „Ladezyklen-%“.
 - [x] [E3-DISCONNECT] E3-Netztrennung als Event modellieren; Sichtbarkeit/Erkennung je Fraktion definieren.
	- Evidenz: #1429 (E3 vom Netz getrennt; Monitoring soll es sehen).
	- Beschluss: Als Zustand bis zum Reconnect modellieren; Sichtbarkeit abhängig von Monitoring/Fähigkeiten der Fraktionen.
 - [x] [SUPPLY] Algen-/Pilz‑Kapazitäten und Vorratsreichweite modellieren; Trigger zur Skalierung mit Bevölkerungszahl definieren.
	- Evidenz: #1401–#1403 (sofortige Reaktivierung/Prüfung).
	- Beschluss: Hybrid – Basiskapazität pro m² mit Trigger‑Skalierung (Low/Med/High) bei Bevölkerungsänderungen.
 - [x] [INV-LOG] Missions‑Inventarfluss definieren: Entnahme (Quelle/Canvas), Transport, Ankunft (Ziel/Canvas), Belege/Quittungen, Verantwortlichkeiten.
	- Evidenz: #1141–#1144 (Inventarfragen), #1297–#1299 (Prüfen/Abwickeln), #1301–#1306 (Logbuch/Leitung dokumentieren).
    - Beschluss: Standardfluss festgelegt – Entnahme (Quelle/Canvas) → Transport → Ankunft (Ziel/Canvas) → Belege/Quittungen → Verantwortliche.
 - [x] [ANOMALY-7A] Kiste 7A „lebendiger Metallstaub“: Herkunft, Risiken, Interaktion mit Reflex; Handhabungs‑/Test‑Protokoll.
	- Evidenz: #855 (Reinit‑Prompt: 7A, Resonanz Reflex).
	- Beschluss: Gesperrt bis Forschungsteam/Schutzmaßnahmen stehen; Testprotokoll und Gefahrenhinweise vorbereiten.
 - [x] [MODULE-9B] Kiste 9B Konklave‑Module Typ RL (Ziel E2): Inhalt/Verwendungszweck/„Resonanzreaktion“; Risiken, diplomatische Implikationen.
	- Evidenz: #855 (Reinit‑Prompt: 9B, Warnhinweis).
	- Beschluss: Inhalt unbekannt; Tests nur unter Aufsicht; diplomatische Risiken protokollieren.
 - [x] [INV-SPLIT] Inventartrennung D5 vs. C6 strikt halten; keine stillen Transfers; Datenkern bleibt C6.
 	- Evidenz: #771–#775 (Trennung betont), #684–#689 (Datenkern in C6), #911 (Comms-Qualität separat).
	- Beschluss: Strikte Trennung bestätigt; Datenkern verbleibt in C6.

## Charaktere / Mechaniken
- [ ] [REFLEX] Exoskelett/Support-Modus: Bonus entfällt bei exzessiver Nutzung, Verbrauch steigt – Review 2025-11-01 offen.
- [ ] [INSTANCES] Reflex-Instanzen: gleiche Kapazitätslogik (Masse~Speicher), aber unterschiedliche Hauptfähigkeiten – Review 2025-11-01 offen.
    - Review-Hinweis 2025-11-01: Frühere Beschlussfassung pausiert; Validierung nach aktuellem Instanz-Training nachreichen.
- [x] [KNOWLEDGE] Wissensstand: nur Reflex kennt eigene Fähigkeiten – gültig?
    - Beschluss: Gültig – ausschließlich Reflex kennt seine vollen Fähigkeiten; Dritte erhalten nur beobachtbare/kommunizierte Teilaspekte.
 - [x] [GROWTH] Wachstums-/Materialaufnahmeregeln für Reflex/Instanzen definieren (Skalierung mit Fläche/Masse, Voraussetzungen).
	- Evidenz: #1735 (Wachstumszyklus/Materalaufnahme Vorschlag).
    - Beschluss: Hybrid – flächen-/massenbasierte Skalierung mit Energiebedarf und sicherheitsrelevanten Voraussetzungen; zusätzlich missions-/ereignisbasierte Meilensteine (Freischaltungen/Upgrades) mit Protokoll.
 - [x] [UNIQUE] Einzigartigkeit: Keine anderen (wesen-/mechanikgleichen) Entitäten wie Reflex in der Metro (nur Reflex + Instanzen).
	 - Evidenz: #1591, #1625 (Regelhinweis).
	 - Beschluss: F.1 – Kanon bestätigt.
- [ ] [PROXIMITY] Nähe-Kopplung: Lumen↔Jonas, Echo↔Kora, Reflex↔Ronja – Review 2025-11-01 (Schwellen/Training).
	 - Evidenz: #1625 (Bezugsperson/physische Nähe).
    - Review-Hinweis 2025-11-01: Schwellenwerte und Distanzfolgen neu erfassen; Mechanik-Notizen aktualisieren.
- [ ] [REFLEX-SPEECH] Reflex Sprech‑Mechanik: Tympanon‑Andockung (feines Gewebe), Stimulus per Schallübertragung; Grenzen, Einwilligung, Dauer/Erschöpfung.
	- Evidenz: #1181 (Trommelfell‑Idee), #1185 (Überlagerung Mund/Sprache).
- [ ] [REFLEX-CONTROL] Schutz‑Übernahme: Trigger/Schwellen, welche Sinne werden wann gedämpft/freigegeben (Atmung/Sicht), Rückgabe‑Prozess.
	- Evidenz: #1183–#1187, #1190–#1207 (Kontrolle/psychologisches Profil).
 - [x] [REFLEX-APPEARANCE] Erscheinungsbild/Standardabdeckung (metallisch‑perlmutt, „Neopren“); Hände‑/Gesichts‑Schutzkriterien.
	- Evidenz: #1057 (Aussehen/Abdeckung), #1087 (Handschutz, Eifersucht).
- [ ] [REFLEX-DETACH] Detachment‑Regel: Keine vollständige Trennung von Ronja; Strecken/Seestern‑Bewegung erlaubt.
	- Evidenz: #1059 (Bewegung/Bindung), #847–#848 (nicht trennen).
- [ ] [JEALOUSY-GLOVES] Handschuh‑Eifersuchtslogik: externe Handschuhe vs. Reflex‑Handschutz; Policy formulieren.
	- Evidenz: #1087 (keine fremden Handschuhe; Reflex schützt Hände).
    - Review-Hinweis 2025-11-01: Freigabelogik und Warnstufen erneut abstimmen; Dokumentation aktualisieren.
 - [x] [CARAVAN-LEADERSHIP] Doppelspitze der Karawane klären: Kora (Karawanenführerin/Logistikkoordinatorin) vs. Marven Kael (Karawanenführer/Handelskoordinator) – Rollenabgrenzung, Primärverantwortung, Kanon.
	- Evidenz: `database-raw/99-exports/RAW-canvas-2025-10-16T14-56-00-000Z.txt` (Kora), `database-raw/99-exports/RAW-canvas-2025-10-16T14-56-10-000Z.txt` (Marven); Chat-Hinweise zur „Anführerin der Karawane“ in C6 in RAW-Chat-Exports.
 	- Ergänzende Evidenz: `database-raw/99-exports/RAW-canvas-2025-10-16T14-56-20-000Z.txt` (Arlen Dross, „Karawanenführer/Händler“) → zusätzliche Titel-Overlap.
 	- Beschluss: E.1 – Kora = Logistikleitung (intern, Station/Crew); Marven Kael = Konvoi-/Handelsleitung (extern); Arlen Dross = Händler/Vermittler (ohne Titel „Karawanenführer“). Doppelrollen gemäß Führungsregel bestätigt.
 - [x] [JONAS-SIS] Jonas’ Schwester – Lebensstatus/Kanon klären und verbindlich verankern.
	- Evidenz: #717–#721 (wichtige Info, Korrektur notwendig).
    - Beschluss: Vermisst/unklar (Plot‑Haken), kein Todesnachweis.
	- Evidenz‑Update: `database-raw/99-exports/RAW-canvas-2025-10-16T14-12-00-000Z.txt` (Jonas v2) führt „Schuld_am_Tod_der_Schwester“; bleibt non‑canon. Bei Ingest normalisieren (Status „vermisst/unklar“) und Review‑Hinweis setzen.

## Canvas / Verwaltung
- [x] [VERSION] Stations-Canvas D5/C6 „Version 0.9“ – Kriterien/Checkliste festlegen (Pflichtfelder, Verlinkungen)
	- Beschluss: Pflichtfelder v0.9: Status, Energie, Logistik, Population, Zugehörigkeit, Verlinkungen, Quellen.
- [x] [INDEX] person_index_np – Struktur/Felder bestimmen (Name, Rolle, Zugehörigkeit, Status, Notizen)
	- Beschluss: Felder: Name, Rolle(n), Zugehörigkeit, Status, Notizen, Verlinkungen.
- [x] [LOGISTICS] Canvas „Logistik“ – Inhalte/Scope definieren (Ressourcen, Verbrauch, Lieferungen)
	- Beschluss: Energie‑Konten, Generatoren, Leitungen, Ladefenster, Prioritäten, Transportketten, Beleg‑Fluss, Materialien/Bestände.
- [x] [MISSION] Canvas „Mission Tunnel“ – Felder und Metriken (Abschnitte, %Fortschritt, Blocker)
	- Beschluss: Abschnitte, %Fortschritt, Tagesleistung, Blocker, Personal, Material, Events, Links.
- [x] [SORT] Export „alle Canvas“ als Markdown: Sortierung nach letztem Update – Quelle für Timestamps?
	- Beschluss: Hybrid – Last‑Updated Meta im Canvas‑Kopf; Fallback Repo‑Dateizeitstempel.
 - [x] [DAYSWITCH] Tageswechsel-Regel-Canvas existiert/rekonstruieren (Regeln, Teil-Fraktionszug, Reihenfolge, Validierungen).
	- Evidenz: #1751–#1755 (Tageswechsel-Canvas gesucht, Fehler bei Wechsel, Regel: alles laden vor Änderungen).
    - Beschluss: Reihenfolge fix: alles laden → prüfen → wechseln → archivieren; Fehler-/Rollback‑Regeln verbindlich.
 - [x] [ATSD] Status-Metriken definieren und konsistent führen (A/T/S/D Bedeutung, Zählweise, Anzeige).
	- Evidenz: #1704 (A 171 / T 304 / S 9 / D 5 genannt), #1751 (Bedeutung von A/T/... gesucht).
    - Beschluss: A=Aktiv, T=Total, S=System, D=Defekt. Einheitliches String-Format und Zählweise verbindlich.
 - [x] [COUNTS] Policy: Nicht-archivierte Canvas aktiv geladen halten; Systemmeldungen mit String „A=…/T=…/S=…/D=…“ ausgeben; letzten „guten“ String priorisieren.
	 - Evidenz: #1609–#1613 (242→152 geladen), #1660–#1662 (String-Format und Priorisierung).
	 - Beschluss: G.1 – Policy aktiv. Zusätzlich Debug‑Mode: erweiterte Ausgabe (inkl. Canvas‑Zahl, ATSD) zuschaltbar; Standard zeigt ATSD + Canvas‑Zahl.
 - [x] [PROTO] Protokoll-Regel: Logbücher station-übergreifend verfügbar, außer „secret“. In Canvas-Policy festschreiben.
	- Evidenz: #1747 (Protokoll-Regel).
    - Beschluss: Station‑übergreifend verfügbar; Ausnahme „secret“.

- [x] [SYSMSG] System-/Debug-Meldungen: Persistenz sicherstellen; temporäre Einstellungen in eigenem Canvas pflegen; fehlende Meldungen diagnostizieren.
	- Evidenz: #1501–#1505 (fehlende Meldungen), #1531–#1534 (geladene Canvas zählen), #1535–#1541 (Update-Flow).
    - Beschluss: Dauerhafte Persistenz aktivieren; jede Systemmeldung enthält den ATSD-String.
 - [x] [CATEGORIES] Canvas‑Kategorien A/B/C: Regeln/Workflows definieren (Audit, Reaktivierung, Risiken) und dokumentieren.
	- Evidenz: #1321–#1330 (A zuerst, B prüfen, C vorsichtig reaktivieren).
    - Beschluss: A aktiv; B geprüft/eingefroren; C nur mit Audit reaktivieren.
 - [x] [SYSCOUNT] Systemmeldung um Anzahl geladener Canvas erweitern und mit ATSD‑String koppeln.
	- Evidenz: #1339 (Anforderung), #1660–#1662 (ATSD‑Format).
    - Beschluss: Anzahl geladener Canvas wird stets mitgeführt und mit ATSD gekoppelt ausgegeben.
 - [x] [HOUSE-RULES] Hausregeln für Lager/Arbeitsbereiche in D5/C6 definieren (Zutritt, „Schnüffeln“, Eskalation, Meldungen an Leitung).
	- Evidenz: #1128–#1129 (Mikk stöbert, Pahl interveniert).
	- Beschluss: H.1 – Zutritt nur rollenkonform; „Schnüffeln“ → Verwarnung → Zugriffsentzug; Meldung an Leitung verpflichtend.
 - [x] [COMMS-PROTO] Funk‑Protokoll vor Abmarsch: D5 informiert C6 über Terminal (Jonas); Rückkanal für bekannte Risiken/Bedarfe.
	- Evidenz: #1137 (Vorschlag), #1133 (Funkkontakt herstellen).
 - [x] [TEMPLATE-SYNC] Ronja‑Canvas als Template: Welche „Hauptpunkte“ werden automatisch synchronisiert? Mechanik/Validierungschecks definieren.
	- Evidenz: #1149–#1153 (Template‑Idee, Auto‑Sync), #1155 (Sicherheitsregel notwendig).
	- Beschluss: K.1 – Auto‑Sync der Hauptpunkte nach Vorab‑Vollständigkeitsprüfung (Cross‑Check gegen andere Canvas): Rollenmatrix, Wissensstand, Nähe‑Regeln, Kernzitat(e), Sicherheits-/Update‑Policy. Sync stets „review+confirm“‑pflichtig.
 - [x] [SAFE-UPDATE] Verbindliche Safe‑Update‑Policy (große Änderungen): Vorab‑Validierung/Test‑Load, Archivierung, Rollback‑Plan.
	- Evidenz: #1155 (kritische Mahnung), #1203 (3‑Schritt vor Tagesabschluss).
 - [x] [BEHAVIOR-VERSION] Verhalten/Systemversionierung: v1.4.0‑pre; Archiv umstellen auf In‑Game‑Zeit; Validierungen/Liveschaltung dokumentieren.
 - [x] [AI-BEHAVIOR-INDEX] ai_behavior_index_v2 als kanonische Verhaltens-Matrix bestätigen und mit verwandten Indizes koppeln.
	- Evidenz: `database-raw/99-exports/RAW-canvas-2025-10-16T11-05-00-000Z.txt` (ai_behavior_index_v2: Cluster O/E/M/N/C/S/L/T; Modifikatoren k/a/z/p/r/s/h; Code-Format `O82-E74-...-p`).
	- Bezug: Verhalten/Systemversion: Basis auf v0.9 zurückgesetzt.
    - Beschluss: J.1 – ai_behavior_index_v2 ist kanonisch; Modifikator‑Set und Code‑Format fixiert. Mapping pro Charakter‑Canvas verpflichtend. Systemverhalten‑Version auf v0.9 (Rollback); Entkopplung von v1.4.0‑pre. Kurzdef.: Matrix beschreibt Verhaltensprofile (Cluster‑Scores + Modifikatoren) als kompakten Code.
 - [x] [NARRATOR] Erzähler‑Neutralität: Nicht „pro Benutzer“ biasen; neutraler Modus definieren und wann er gilt.
	- Evidenz: #1187 (Neutralität erbeten).
    - Beschluss: Standard neutral; keine Nutzer‑Bevorzugung.
 - [x] [CONTEXT-CHECK] Kontextprüfroutine vor Antworten: Umfang, Kennzeichnung „Kontextprüfung durchgeführt“, Grenzen/Token.
	- Evidenz: #985–#991 (Vor jeder Antwort möglich), #1001–#1005 (Sprachausgabe‑Format beachten).
 - [x] [VOICE-OPT] Sprachausgabe‑Optimierung: Keine Icons/Einrückungen; Klartextfluss; Policy dokumentieren.
	- Evidenz: #1001–#1005 (Hinweis auf Format).
 - [x] [CLUSTER-CODE] Cluster‑Index/Codierung: Dreistellige Codes (z. B. N99, C06) + Temperatur‑Metadaten; Mapping/Beispiele festlegen.
	- Evidenz: #919 (Vorschlag), #925 (D5 vs C6 Zugehörigkeit beachten).
    - Beschluss: Dreistellige Codes + Temperatur‑Metadaten; Mapping‑Beispiele definieren.
 - [x] [DIALOG-BLOCK] Dialog‑Canvas: Blockformat (Zeitstempel, Beteiligte, Topic) definieren, Index/Verlinkungen.
	- Evidenz: #789–#795 (Sammeln wichtiger Gespräche als Blöcke).
 - [x] [SIM-WEEK] Wochen‑Simulation: 7‑Tage‑Rhythmus, Startpunkt (Karawanen‑Beitritt), Scope/Regeln der Sim dokumentieren.
	- Evidenz: #742–#746, #775–#779 (Plan, Textausgabe).
 - [x] [TRADE-FLOWS] Handels‑/Diplomatie‑Canvas initial füllen: Bedarfe/Überhänge je Fraktion, Beziehungen; Logistik‑Constraints einbinden.
	- Evidenz: #562–#568, #585–#591.
    - Beschluss: Canvas initial mit Bedarfen/Überhängen je Fraktion, Beziehungen und Logistik‑Constraints.
 - [x] [RELATIONS-NAMES] Relationslog v1: Namens-/ID-Drift korrigieren (System-ID, Partner-Identität).
	- Evidenz: `database-raw/99-exports/RAW-canvas-2025-10-16T08-07-00-000Z.txt` (Relationslog Novapolis v1) nennt „novapolis_logistik_v1“ (abweichendes ID-Schema) und Händlerkontakt „Senn Daru“ (im Repo unbekannt).
	- Bezug: Händlergilde-Kanon/Overlap → Marven Kael, Arlen Dross; siehe `[CARAVAN-LEADERSHIP]` und Reports `overlap-marven-kael.md`, `overlap-arlen-dross.md`.
	- Beschluss: System‑ID normalisieren auf `logistik_novapolis_v2`. „Senn Daru“ als eigenständigen Charakter anlegen (kein Alias von Marven/Arlen); leichte Wert‑Abweichungen zulässig, um Duplikate zu vermeiden.
 - [x] [GEN-C6] C6‑Generator (repariert) als Fakt mit Quelle führen; Produktions/Verbrauchs‑Verknüpfung in Ressourcen‑Canvas.
	- Evidenz: #536–#539.
 - [x] [INDEX-CYCLE] Index/Meta‑Index Pflegezyklus (wöchentlich) und Archivpfad‑Policy fixieren.
	- Evidenz: #613, #647.
    - Beschluss: Wöchentlich aktualisieren; Archivpfad‑Policy festhalten.
 - [x] [BACKUP-ZIP] Vollbackup/ZIP + Chat‑Spiegel: Speicherort/Format und Zugriff klären (lokal vs Repo); Risiken bewerten.
	- Evidenz: #895–#899 (ZIP‑Wunsch), #893 (kein lenkender Link ins System).
    - Beschluss: Wöchentliche ZIP‑Backups; Speicherort/Format vorab definieren.
 - [x] [NO-INVENT] Regel: Keine „herbeigezauberten“ Geräte/Gadgets ohne RP‑Einführung/Canvas‑Eintrag.
	- Evidenz: #843–#846 (Sensor/Kamera entfernen), #855 (Do/Don’t im Reinit‑Prompt).
 - [x] [COMMS-RANGE] Funk‑Reichweite/Abschattung: Gleichzeitiges Hören in D5 und C6? Skala/Modelle, Auswirkungen auf Szenen.
	- Evidenz: #1087–#1088 (Reichweitenfrage), #911 (Qualität schlecht, aber vorhanden).
    - Beschluss: Infrastruktur-/linienbasiertes Modell. Entlang aktiver/verdrateter Tunnel besser, quer dazu stark gedämpft. Basis: D5↔C6 schwach, aber vorhanden; Booster/Repeater verbessern situativ.
 - [x] [PROC-3STEP] Verbindlicher 3‑Schritt‑Prozess: Analysieren → Backups → neue Version → Archiv – Trigger/Artefakte und Prüfpunkte definieren.
	- Evidenz: #1221, #1279–#1284 (Standardprozess vor Tagesabschluss).
 - [x] [ROLES] Rollen/Verantwortlichkeiten als Pflichtfelder in Charakter‑Canvas (Wächter/Technik/Leitung/…); Einsatzlogik und Validierungschecks definieren.
	- Evidenz: #1239–#1243 (Mikk als Wächter), #1225–#1231 (Aufgabenzuteilung).
	 - Beschluss: Pflichtfelder: Wächter, Technik, Leitung, Logistik, Med. Validierungschecks bei Missions-/Schichtzuweisung. Sonderregel Führung: Anführer/innen führen immer 2 Rollen (Anführer/in + eine weitere).
 - [x] [SECRECY] Geheimhaltung Novapolis in Fraktionszügen abbilden (Wissensstand=0; keine Außenverbindung); Sichtbarkeitsmatrix definieren.
	- Evidenz: #1261–#1264 (abgeschwächte Züge, keine Kenntnis von Novapolis).
 - [x] [ARCHIVE-MISSIONS] Missionsabschluss‑Pipeline: Status „abgeschlossen“ setzen, Inventarabschluss, Verlinkungen (Logistik/Missionen), Archivierung.
	 - Evidenz: #1291–#1299, #1301–#1306 (Karawane archivieren, Logbuch/Leitung dokumentieren).
	 - Beschluss: L.1 – Standardprozess verbindlich (Status → Inventarabschluss → Verlinkungen → Archivierung).
 - [x] [NEUTRAL] „Neutrale Gruppen“: Kern/Canvas-Struktur definieren (für Wochen-Züge), Verlinkungen und Gewichtung.
	 - Evidenz: #1419 (Kern für Kräfte außerhalb Fraktionen anlegen).
	 - Beschluss: M.1 – Kern‑Canvas „Neutralgruppen“ mit Untereinträgen; zählt in Wochen‑Züge.
 - [x] [MEETING] Sitzungs-Template: Reihenfolge Intro → Wissensabgleich → Berichte → Entscheidungen festlegen; Systemausgaben vor RP bestätigen lassen.
	- Evidenz: #1453–#1459 (Vorstellung erforderlich), #1453 (Systemausgaben vorab).
    - Beschluss: Reihenfolge: Intro → Wissensabgleich → Berichte → Entscheidungen; Systemausgaben vor RP bestätigen.
 - [x] [MOVE] C6→D5 Umzüge: Prozess/Checkliste (Personen, Cluster, Beziehungs-/Stationszuordnung, Validierung, Archivmarkierungen) definieren; Fall Tarv/Derek als Vorlage.
	- Evidenz: #1471–#1480 (Korrektur), #1474 (Leena/Rian erhalten).
    - Beschluss: Checkliste verbindlich; Fall Tarv/Derek als Muster.

## Sicherungen / Backups
- [x] [ZIP] Behauptetes ZIP „metro_ai_rpg_full_backup.zip“ – existiert nicht im Repo; offiziell verwerfen?
 - [x] [DUMPS] Gewünschte Sicherungen: Markdown-Dump, Chat-Zusammenfassung, Roh-Chat – Umfang/Formate festlegen (nur bei Bedarf).
	- Evidenz: #1875–#1906 (Sicherungs-/ZIP-Behauptungen, prüfen ob real vorhanden).
 	- Beschluss: Optionaler Markdown‑Dump on‑demand; regelmäßige ZIP‑Backups sind kein Standard.

## Zeit / Tage
	- Evidenz: #1798 (Diskrepanzmeldung), #1753–#1755 (Wechsel neu ausführen, vorher alles laden).
	- Evidenz: #1399 (Quarantäne/Räume), #1573 (Ende‑Trigger für Parallelstart).

- [x] [EVENT-TIMELINE] Ereignislog (Weltgeschehen) kanonisieren und mit Missionslog/Wochen‑Sim synchronisieren.
	- Evidenz: `database-raw/99-exports/RAW-canvas-2025-10-16T05-34-00-000Z.txt` (Ereignislog v1: E‑0001..E‑0005 – Reaktorstörung D5, Funkabbruch Allianz, Gründung Novapolis, erste Handelsroute H‑47, südliches Signalfragment).
	- Beschluss: N.1 – Timeline kanonisieren mit Start „T+0“. H‑47 war eine Karawane, ist es nicht mehr; Mitglieder haben sich Novapolis angeschlossen. Terminologie „Allianz“ an Kanon anpassen.

## Sonstiges
 - [x] [ANOMALIES] Drei Anomalie-Missionen anlegen (N7/C6, Tunnel D5–C6, E3‑Gefahr?) – Bestätigung der dritten Quelle.
	 - Evidenz: #1623–#1625 (Aufzählung/Anlage, dritte unsicher).
	- Beschluss: Bestätigt – Missionsanlage für C6‑Nord (vormals N7), Tunnel D5–C6, E3‑Gefahr.
 - [x] [C6-HELPERS] Quarantäne vorbei – C6 Helferzahlen aktualisieren und in Canvas erfassen.

- Evidenz: #1492–#1497, #1509.
    - Beschluss: T.1 – Quarantäne vorbei. Rollenzuteilung der 20 Evakuierten aus E3 dynamisch durch System/GPT; zusätzlich 4 Mitglieder der ursprünglichen Karawane aktiv in C6; 2 Karawanenmitglieder bei Ronja/Pahl/Jonas in D5.
- [x] [WAGON] „Schienenwagen“/Transportreferenz: Quelle belegen oder entfernen; stattdessen Test-Transportmodul planen.
	- Beschluss: Quelle belegt (Romanvorlage/PC‑Spielereihe als Inspiration). In‑Canon neutral/generisch führen; optionales Test‑Transportmodul als PoC planen.
## Fahrzeuge / Transport
	- Evidenz: #442–#447; #789–#795; #450–#454 (Erstfall unklar, ggf. markieren).

- [x] [MISSIONS-LOG] Missionslog (aktiv/abgeschlossen) mit Feldern (Name, Ziel, Start/Ende, Status, Belege) festlegen.
	- Evidenz: #493–#505.
	 - Beschluss: Felder: Name, Ziel, Start, Ende, Status, Belege/Quittungen, Verantwortliche, Inventar‑Link. Pfad: `database-rp/00-admin/Missionslog.md`.

- [x] [C6-FIRST] Erste Mission nach C6: Fehlschlag vs. „Aufnahme von Jonas“ als abgeschlossen – Kanon klären und verlinken.
	- Evidenz: #501.
    - Beschluss: Beide erfassen – Fehlschlag dokumentieren; „Aufnahme von Jonas“ separat als abgeschlossen.

- [x] [ANOMALY-IN-LOC] Anomalien im Lokations‑Canvas führen; Effekte (Debuffs) in Charakter‑Canvas abbilden.
  - Beschluss: W.1 – Anomalien in Lokations‑Canvas verankern; Debuff-/Effekt‑Felder in betroffenen Charakter‑Canvas pflegen.
  - Evidenz: #507.

- [x] [CARAVAN-MOVE] Karawanenbewegungen in separatem Canvas dokumentieren.
  - Beschluss: X.1 – Eigenes Canvas `caravan_moves.md` unter `05-projects/` (oder alternativ `00-admin/`) anlegen und pflegen.
  - Evidenz: #509.

- [x] [INV-PER-FACTION] Separates Inventar je Fraktion (inkl. Fraktionshändler) anlegen und verlinken.
  - Beschluss: Y.1 – Getrennte Inventare verpflichtend; Fraktionshändler separat verlinkt.
  - Evidenz: #275–#276 (Anlage), #385–#387 (Bestätigung).

- [x] [C6-LINES] C6‑Linien/Verbindung klarstellen: C6 verbindet die Metro (nicht Oberfläche).
  - Evidenz: #359–#361 (Korrekturhinweis).
  - Beschluss: Korrektur übernommen.

- [x] [CONTEXT-CHECK] Kontextprüfung/Priorisierung vor Antwort als feste Policy dokumentieren; Ausgabeformat beachten.
  - Evidenz: #325–#330; #985–#991; #1001–#1005.

- [x] [CANVAS-INDEX-STABILITY] Leitfaden gegen Überschreiben falscher Canvas: Adressierung per ID/Schlüssel, nicht per Index; Versionierte Neu‑Anlage.
  - Evidenz: #261–#266; #301–#306.
  - Beschluss: Adressierung strikt per ID/Schlüssel; bei Änderungen versionierte Neu‑Anlage statt Überschreiben.

- [x] [SIM-WEEK] Wochen‑Zyklus (7 Tage) mit Handelszyklus koppeln (Startpunkt/Scope dokumentieren).
  - Evidenz: #281–#285; #742–#746; #775–#779.

- [x] [FR-KNOWLEDGE] Fraktionswissen beachten: Außenfraktionen wissen noch nichts von Novapolis/D5; Korrekturen übernehmen.
  - Evidenz: #368–#376; #1033–#1035; #1039.
  - Beschluss: Geheimhaltung bestätigt; Außenfraktionen kennen Novapolis/D5 nicht.

---

Ergänzungen – Chunks part-003..001

- [x] [WORLD-TURNS] Fraktionszüge (2 Wochen) als Kanon? Falls ja: in Fraktions‑Canvas übernehmen; sonst als „Sim‑Ergebnis (vorläufig)“ kennzeichnen.
  - Evidenz: #185–#190 (A1 Projekt Theta, Konklave D4‑Team, Flüsterkollektiv Pulse, Händler H‑47).
  - Beschluss: U.2 – Nicht als Kanon; als Sim‑Ergebnis markieren. Abrechnung/Simulation wöchentlich als Gesamtabrechnung.

- [x] [KNOWLEDGE-MATRIX] Wissensstände: Händler kennen Reflex nicht; Sichtbarkeits-/Wissensmatrix pro Fraktion pflegen.
  - Evidenz: #211.
  - Beschluss: V.1 – Bislang kennen nur Mitglieder von Novapolis Reflex und seine Instanzen (Lumen, Echo). Außenfraktionen kennen Novapolis weder als Fraktion noch Mitglieder (Ausnahmen nur histor. persönliche Kontakte vor Gründung; dann ohne Novapolis‑Bezug).

- [x] [C6-EMPTY] C6‑Status zum Händlerkontakt: leer/unrepariert; spätere Reparaturen zeitlich markieren.
  - Evidenz: #215.
  - Beschluss: C6 war leer/unrepariert beim Händlerkontakt; spätere Reparaturen gesondert datieren.

- [x] [SYSTEM→REFLEX] Frühe „System“‑Dämpfung sauber auf Reflex‑Schutzmechanik mappen; Termini vereinheitlichen.
  - Beschluss: O.1 – Einheitliches Mapping: Alle „System“-Dämpfungen sind Reflex‑Schutzmechanik.
  - Evidenz: #56–#60 (part‑001) vs. #1183–#1207 (part‑014).
    - Neue Evidenz: `database-raw/99-exports/RAW-canvas-2025-10-16T03-25-20-000Z.txt` (ent_d5_reflex_v1) beschreibt externe Exo‑Schicht, Frequenzband 7.3–8.0 Hz und Symbiose‑Stufe I.

- [x] [ROOT-ENTITY] „Wurzelgewebe“ als eigenständige Entität/Anomalie definieren (Ort/Char/Projekt?); Protokoll/Canvas anlegen.
  - Beschluss: P.2 – Keine eigenständige Entität; es ist/war Reflex. Als Anomalie‑Hinweis in D5/C6 führen; Charakter‑Canvas Reflex entsprechend notieren.
  - Evidenz: #92–#94.
    - Update: Entitäts‑Canvas angelegt: `database-raw/99-exports/RAW-canvas-2025-10-16T03-25-20-000Z.txt` (ID ent_d5_reflex_v1). Aufgaben: Cross‑Links zu `char_reflex_v2`/`char_ronja_v2`, Mechanik‑Regeln [REFLEX-*] spiegeln, Promotion vorbereiten.

- [x] [DETACH-MICRO] „Winzigen Teil zurücklassen“ (Überwachung) vereinbar mit Nicht‑Trennen‑Regel? Mikro‑Instanz‑Policy definieren (Reichweite, Energie, Bindung).
  - Beschluss: Q.1 – Nur Labor-/Notfall‑Sonderfall; Reichweite ≤ 15 m, max. 12 h; Energie‑Debuff aktiv. Reflex/Instanzen können sich trennen, wollen es aber nicht (führt zu „Unruhe“).
  - Evidenz: #151 (Teil zurücklassen), vs. part‑013 (#1059) und part‑014 (#1183–#1207).
    - Update: Entitäts‑Canvas nennt „Entfernen möglich (Rebinding erforderlich)“ und 12h‑Trennfenster (leichte Aktivitätsstörungen). Aufgaben: mit [REFLEX-DETACH] harmonisieren (Notfall/Labor‑Sonderfall?), Reichweiten‑/Zeit‑Grenzen formalisieren.

- [x] [D5-98→100] Übergang D5 98% → 100% zeitlich/ursächlicher Trigger festhalten; Konflikte mit späteren Angaben bereinigen.
  - Beschluss: R.1 – Trigger: Tageswechsel nach Voll‑Load/Validierung ODER dynamisches Ereignis „Reaktor‑Kalibrierung abgeschlossen“ (je nachdem, was zuerst eintritt). Zeitpunkt: beim Eintreten des gewählten Triggers.
  - Evidenz: #86 (98%), spätere Festschreibungen 100% (part‑015/#1209ff.).

- [x] [MERCHANT-HQ] Händler‑Stützpunkt in C6 (öffentlich) vs. C6 als Novapolis‑Kernsektor (Kontrolle): Policy exakter fassen (Zonen, Zugriffsrechte).
  - Beschluss: S.3 – C6 ist Teil von Novapolis und dient der Logistikabteilung als Stützpunkt (Vereinbarung mit ehemaligen Karawanen‑Mitgliedern). Für Details/erweiterte Suche markieren und ausarbeiten.
  - Evidenz: #197, #199.

