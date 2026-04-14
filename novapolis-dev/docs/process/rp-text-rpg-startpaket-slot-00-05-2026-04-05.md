---
stand: 2026-04-14 21:08
update: Das Startpaket fuehrt jetzt den verbindlichen Slot-00-Startanker und die belegte Weltbindung fuer den Sim-vor-RP-Einstieg auf denselben Sessionvertrag.
checks: markdownlint=PASS; frontmatter=PASS; todo-index-sync=PASS
---

RP-Produktpfad: Spielstartpaket und Slot-00-05-Korridor
========================================================

Ziel
----

Dieses Arbeitsblatt zerlegt den offenen RP-Produktpfad fuer den ersten spielbaren Novapolis-Slice in eine belastbare, evidence-first Struktur.

- Kein neuer Kanon ohne Beleg.
- Keine verdeckte Zweit-SSOT.
- Fokus ist die Festschreibung von Startpaket, Reveal-Grenzen und einem ersten Mehrslot-Korridor fuer spaetere Agent-/Sim-Umsetzung.

Nicht-Ziele dieses Laufs
------------------------

- Keine neue Missionsszene erfinden.
- Keine neue Faktensetzung fuer Artefakte, Anomalien oder Fremdfraktionen.
- Keine automatische Promotion von offenen RAW-Fragen zu Kanon.

Evidenzbasis (harte Anker)
--------------------------

- D5 als aktiver, bewohnter Hauptstandort mit Werkstatt-/Kontrollraumkern: `novapolis-rp/database-rp/01-factions/novapolis/03-locations/D5.md`
- C6 als teilaktiver Aussenposten mit Kernzone A/B/C und C6-Helper-Rahmen: `novapolis-rp/database-rp/01-factions/novapolis/03-locations/C6.md`
- Laufender Projektpfad Nordlinie D5-C6 mit getrennten Kennzahlen Erkundung/Sicherung/Betrieb: `novapolis-rp/database-rp/01-factions/novapolis/05-projects/Nordlinie-01.md`
- Belegter Material- und Missionspfad D5 -> C6: `novapolis-rp/database-rp/01-factions/novapolis/05-projects/Missionslog-Novapolis.md`
- Fruehe D5-Startanker: `scene-2025-10-27-g.md`, `scene-2025-10-27-h.md`, `scene-2025-10-27-ah.md`, `scene-2025-10-27-ai.md`
- Parallele C6-Arbeitsanker: `scene-2025-10-27-d.md`, `scene-2025-10-27-e.md`
- Kuratierte Leitplanken fuer D5/C6, Knowledge, Secrecy, World Turns, Reflex und Pahl: `novapolis-dev/docs/process/rp-canvas-rescue/resolved.md`
- Charakter-SSOTs fuer Startkern: `Ronja-Kerschner.md`, `Reflex.md`, `Jonas-Merek.md`, `Pahl-Brenner.md`, `Kora-Malenkov.md`
- Fraktions- und Stationsrahmen fuer Mehrfachstarts: `novapolis-rp/database-rp/00-admin/Fraktionen-Taxonomie.md`, `novapolis-rp/database-rp/00-admin/Stationskontroll-Matrix.md`, `novapolis-rp/database-rp/00-admin/Metrokarte-T0.md`
- Freie-Gruppen-Anker fuer fraktionslose Starts: `novapolis-rp/database-rp/04-inventory/Freie-Gruppen-inventar.md`
- Externe Fraktions- und Ortsanker fuer Bereichsstarts: `G7.md`, `H12.md`, `A1.md`, `B2.md`, `F9.md`, `K4.md`
- Start-Chooser und konkrete Startboegen: `novapolis-dev/docs/process/rp-start-chooser.ssot.md`, `novapolis-dev/docs/process/rp-startbogen-novapolis-d5.ssot.md`, `novapolis-dev/docs/process/rp-startbogen-novapolis-c6.ssot.md`, `novapolis-dev/docs/process/rp-startbogen-arkologie-a1.ssot.md`, `novapolis-dev/docs/process/rp-startbogen-schienenbund-b2.ssot.md`, `novapolis-dev/docs/process/rp-startbogen-eisenkonklave-h12.ssot.md`, `novapolis-dev/docs/process/rp-startbogen-schattenbund-f9.ssot.md`, `novapolis-dev/docs/process/rp-startbogen-fluesterkollektiv-k4.ssot.md`, `novapolis-dev/docs/process/rp-startbogen-freie-gruppen-a2.ssot.md`, `novapolis-dev/docs/process/rp-startbogen-haendlerbund-g7.ssot.md`

Vertrags- und Weltanker fuer den Sim-vor-RP-Start
-------------------------------------------------

- Dieses Startpaket ist die aktive RP-Zielquelle fuer produktive Neueinstiege bei `slot_00` bis `slot_05`.
- Der Sim-vor-RP-Einstieg darf deshalb keine freie Vorszene ausserhalb dieses Korridors aufziehen, sondern muss denselben Sessionvertrag mit `campaign_id`, `session_id`, `scene_id`, `slot_id` und `turn_id` auf diese Startanker legen.
- Der Default-Start bleibt weltseitig bei den belegten Novapolis-Kernraeumen `D5` und `C6`; weitere Startgebiete duerfen nur ueber ihren belegten Startbogen und den Start-Chooser an denselben Vertragsrahmen angeschlossen werden.
- `slot_00` ist der kanonische Neueinstiegsanker; spaetere Resume- oder Folgepfade werden nicht aus diesem Startpaket erfunden, sondern ueber die jeweiligen Folgekorridor- oder Handover-SSOTs fortgesetzt.
- Der Weltbezug des Startpakets bleibt dadurch auf die hier belegten Orts-, Projekt-, Reveal- und Charakterquellen beschraenkt; freie Sim-Startwelten ohne RP-Anker sind ausgeschlossen.

Startpaket v0 (belegt/offen getrennt)
-------------------------------------

### 1. Primäre PC-Linse

- Belegt: Der frueheste voll tragfaehige Einstieg mit hoher Dichte liegt in D5 bei Ronja.
- Belegt: Reflex ist als aktive, an Ronja gekoppelte Schutz-/Sensorinstanz im derzeit staerksten Startkern praesent.
- Belegt: Jonas und Pahl sind D5-seitig verfuegbare Folgefiguren fuer Werkstatt-, Funk- und Sicherheitskontext.
- Belegt: Kora und Echo bilden die parallele C6-Linse, aber nicht denselben unmittelbaren Default-Startanker wie Ronja/Reflex in D5.
- Belegt: Die globale RP-SSOT kennt neben Novapolis weitere Fraktionsraeume und Kontrollstationen, daher darf der Produktpfad nicht dauerhaft auf genau einen Start reduziert bleiben.
- Offen: Ob der erste spielbare POV dauerhaft nur Ronja bleibt oder spaeter einen kontrollierten POV-Wechsel braucht, ist noch nicht kanonisch festgezogen.

### 2. Startort und Ausgangslage

- Belegt: D5 ist stabil, bewohnt und operativ der sicherste Kernstandort.
- Belegt: C6 ist nicht leer, sondern teilaktiv mit begrenzter Kernzone, laufender Sicherung und externer Belastung.
- Belegt: Der Tunnel D5-C6 ist kein freier Normalverkehr, sondern ein aktives Wiederinbetriebnahmeprojekt mit Friktionspotenzial.
- Belegt: Material, Funk, Wartung und Sicherheitspruefung sind fuer den Default-Slice die derzeit dichtesten Startachsen.
- Belegt: Ueber `Fraktionen-Taxonomie`, `Stationskontroll-Matrix` und `Metrokarte-T0` existieren aber mehrere weitere kontrollierte oder neutrale Startbereiche, die fuer einen spaeteren Startbaukasten eingeplant werden koennen.

Mehrfachstarts und Gebietswahl v0
---------------------------------

### Leitprinzip

- Der Produktpfad soll mehrere Startoptionen tragen.
- Diese Startoptionen muessen nicht alle sofort dieselbe Kanon- und Szenentiefe haben.
- Es wird daher zwischen `voll tragfaehigem Slice`, `Rahmenstart` und `fraktionslosem Neutralstart` getrennt.

### 1. Voll tragfaehiger Slice

- Novapolis / D5 ist jetzt als eigener Default-Startbogen festgezogen.
- C6 ist jetzt als eigenstaendiger paralleler Novapolis-Startbogen gegen D5 abgegrenzt.
- Erweiterungsraum innerhalb desselben Fraktionsraums bleibt danach E3 und spaetere Folgefenster.

### 2. Fraktionsgebundene Rahmenstarts

- Belegt als Fraktions- und Basisanker vorhanden:
  - Novapolis: `D5`, `C6`, `E3`
  - Haendlerbund: `G7`
  - Eisenkonklave: `H12`
  - Arkologie-A1: `A1`
  - Schienenbund: `B2`
  - Schattenbund: `F9`
  - Fluesterkollektiv: `K4`
- Bewertung 2026-04-05:
  - `D5/C6/E3/G7` haben bereits mehr operative Kontextdichte.
  - `A1/B2/F9/H12/K4` sind als reale Startbereiche belegt, aber in den aktuellen Orts-SSOTs oft noch nur als Rahmenknoten mit `tbd`-Feldern vorhanden.
- Produktfolge: Diese Fraktionsstarts duerfen als Startoptionen vorgesehen werden, muessen aber im UI/Produktpfad nur dann als `Rahmenstart` markiert bleiben, wenn lokale Mindestboegen fehlen.
- Fortschritt 2026-04-05: Fuer `G7`, `A1`, `B2`, `H12`, `F9` und `K4` liegen jetzt eigene Minimal-Startboegen vor.

### 3. Fraktionsloser Start

- Belegt: Die RP-SSOT kennt `Freie Gruppen` explizit als Sammelkategorie fuer fraktionslose NPC.
- Belegt: `Freie-Gruppen-inventar.md` fuehrt dafuer einen eigenen globalen Scope.
- Belegt: `Fraktionen-Taxonomie.md` fuehrt `Freie Gruppen` ausdruecklich als eigene Nicht-Hauptfraktions-Kategorie.
- Konsequenz: Ein fraktionsloser Start ist kein Sonderwunsch ausserhalb des Modells, sondern bereits mit einem echten SSOT-Anker vereinbar.
- Fortschritt 2026-04-05: `A2` fuehrt jetzt den ersten konkreten Neutralstartbogen fuer `Freie Gruppen`.

### 4. Frei waehlbarer Startbereich

- Belegt: `Stationskontroll-Matrix.md` und `Metrokarte-T0.md` fuehren nicht nur Fraktionsbasen, sondern auch viele `Neutral/Transit`-Stationen als Puffer- und Austauschzonen.
- Konsequenz: Der spaetere Start-Chooser sollte Startbereich und Fraktionsmodus voneinander trennen.
- Evidence-first Klassen fuer die Gebietswahl:
  - Fraktionskern: `D5`, `C6`, `E3`, `G7`, `H12`, `A1`, `B2`, `F9`, `K4`
  - Neutral/Transit: z. B. `A2`, `B1`, `C1`, `D1`, `E2`, `F1`, `G3`
  - Unterbereiche innerhalb eines Startgebiets: z. B. `D5-Werkstatt`, `D5-Funkraum`, `C6-Schleuse`, `C6-Lagerhalle`
- Guardrail: Freie Gebietswahl ueber die gesamten 54 Stationen ist als Produktziel plausibel, aber noch nicht fuer alle Stationen lokal gleich tief ausmodelliert.

### 5. Empfohlenes Produktmodell fuer den Start-Chooser

1. Schritt: Startmodus waehlen.
   - `Novapolis-Default`
   - `Fraktionsstart`
   - `Fraktionslos / Freie Gruppen`
2. Schritt: Startbereich waehlen.
   - Fraktionskernstation
   - Neutral-/Transitstation
   - lokaler Unterbereich, falls vorhanden
3. Schritt: Sichtbarkeit und Startbogen aus dem jeweiligen Dichtegrad ableiten.
   - `voll tragfaehiger Slice`
   - `Rahmenstart mit begrenzter Tiefe`
   - `Neutralstart mit spaeterem Fraktionsanschluss`

### 3. Sofortige Stakes des Startlaufs

- D5-intern: Unklare Werkzeugtasche, Wartungsauftrag, vorsichtiger Wartungsgang.
- D5/System: Terminal/Port/System-Link mit Risiko von Dämpfung bzw. Kontrollverlust.
- Team-intern: Reflex-Schutz, Ronjas Arbeitsfokus, Jonas-Werkstattkontext, Pahls Freigabe- und Sicherheitsrolle.
- Welt-intern: C6 laeuft parallel weiter; was dort geschieht, ist nicht automatisch PC-sichtbar.
- Projektseitig: Nordlinie 01 und der Materialpfad D5 -> C6 erzeugen Zeit- und Ressourcen-Druck, ohne schon einen Hard-Fail zu erzwingen.

### 4. Startkern-Besetzung

- Direkt am D5-Start: Ronja, Reflex, Jonas, Pahl.
- Parallelfaden / spaeterer Reveal: Kora, Echo, C6-Helper, C6-N3-Kontext.
- Bewusst nicht im ersten Kern: externe Fraktionen ausserhalb des bereits belegten Hintergrundraums.
- Fuer Mehrfachstarts offen: externe Fraktionskerne und freie Gruppen brauchen je einen eigenen Startkern statt bloesser Stationsnamen.

### 5. Startrelevante SSOT-Luecken

- Mind-Cluster fuer den Novapolis-Kerncast, den direkten Anschlusscast `Arlen/Lumen/Marven/Marei/Lyra/Senn` und die externen Full-Slice-Kerne `A1/B2/H12/F9/K4` liegen jetzt als eigene SSOTs vor.
- Die Reveal-/Secrecy-Regeln des Startkorridors liegen jetzt in `novapolis-dev/docs/process/rp-startkorridor-reveal-matrix.ssot.md`.
- Knowledge-/Actions-Abdeckung ist jetzt fuer `D5`, `C6`, `Nordlinie-01`, `Missionslog-Novapolis` und den Kerncast startkorridor-tauglich gebuendelt.
- Die externen Fraktionskerne fuehren jetzt je einen eigenen Minimal-Startbogen; lokale Tiefenschaerfe und Nebenstart-Hooks werden ueber ihre Startboegen und Orts-SSOTs enger gefasst.
- Der fraktionslose Start besitzt jetzt mit `rp-startbogen-freie-gruppen-a2.ssot.md` einen ersten belastbaren Neutralstart; offen bleibt vor allem der spaetere Anschluss an weitere Fraktionspfade.
- Mehrere Szene-Dateien verlinken auf eine T+0-Timeline-Datei, die am erwarteten Pfad derzeit nicht aufloesbar ist; das ist ein Strukturhinweis, kein neuer Kanon.

### 6. Frisch geschlossene SSOT-Bloecke

- Mind-Cluster-SSOTs: Kerncast `Ronja/Reflex/Jonas/Pahl/Kora/Echo`, Anschlusscast `Arlen/Lumen/Marven/Marei/Lyra/Senn` sowie die Full-Slice-Kerne von `A1/B2/H12/F9/K4` liegen jetzt als eigene Cluster-Dateien vor.
- Scheduler-ready Startkorridor-Scope: `D5.md`, `C6.md`, `Nordlinie-01.md`, `Missionslog-Novapolis.md`, `Ronja-Kerschner.md`, `Reflex.md`, `Jonas-Merek.md`, `Pahl-Brenner.md`, `Kora-Malenkov.md`, `Echo.md`.
- Reveal-SSOT: `novapolis-dev/docs/process/rp-startkorridor-reveal-matrix.ssot.md`.
- Reveal-SSOTs: `rp-startkorridor-reveal-matrix.ssot.md` fuer `D5/C6` und `rp-startgebiete-reveal-matrix.ssot.md` fuer `A1/B2/H12/F9/K4/G7/A2/B1/C1/C3/D1/E2/F1`.
- Folgekorridor-SSOT: `novapolis-dev/docs/process/rp-folgekorridor-slot-00-05.ssot.md`.
- Folgekorridor-Erweiterung: `novapolis-dev/docs/process/rp-folgekorridor-slot-06-10.ssot.md`.
- Langzeit-Folgekorridor: `novapolis-dev/docs/process/rp-folgekorridor-slot-11-15.ssot.md`.
- Kampagnen-Folgekorridor: `novapolis-dev/docs/process/rp-folgekorridor-slot-16-20.ssot.md`.
- Weiterer Kampagnen-Folgekorridor: `novapolis-dev/docs/process/rp-folgekorridor-slot-21-25.ssot.md`.
- Neutrale Orts-SSOTs fuer den Pufferpfad: `novapolis-rp/database-rp/03-locations/A2.md`, `B1.md`, `C3.md`.
- Weitere neutrale Startboegen: `rp-startbogen-freie-gruppen-b1.ssot.md`, `rp-startbogen-freie-gruppen-c3.ssot.md`.
- Zusaetzliche neutrale Orts- und Start-SSOTs: `novapolis-rp/database-rp/03-locations/C1.md`, `D1.md`, `rp-startbogen-freie-gruppen-c1.ssot.md`, `rp-startbogen-freie-gruppen-d1.ssot.md`.
- Weitere neutrale Orts- und Start-SSOTs: `novapolis-rp/database-rp/03-locations/E2.md`, `F1.md`, `rp-startbogen-freie-gruppen-e2.ssot.md`, `rp-startbogen-freie-gruppen-f1.ssot.md`.

Reveal- und Wissensgrenzen v0
----------------------------

### PC-direkt im Startpaket

- D5-Wartungsauftrag, Werkzeugtasche, Beobachtungsmodus im Wartungsgang.
- Suche nach Terminal/Port/System-Link in D5.
- Reflex als aktiver Schutz- und Reaktionsfaktor im unmittelbaren Nahbereich.
- Jonas und Pahl als D5-seitige Folgekontakte fuer Werkstatt, Sicherheit, Freigaben und Reha-/Belastungslogik.

### Allies-only / kontrollierter Reveal

- Monitoring- und E3-Risiko-Infos aus dem Missionslog.
- C6-Status, soweit er ueber abgesicherte Log-/Funkpfade nach D5 gespiegelt wird.
- Echo-/Kora-Kontext, wenn Ronja bzw. das D5-Team ihn ueber bestaetigte Meldungen erhaelt.

### World-only / nicht ungeprueft an den PC

- Arbeitsdetails aus C6-N3 inklusive Artefaktmarkierung `7A`, sofern sie nicht sauber gespiegelt wurden.
- Verdeckte oder rohe Sphaeren-/Mind-Cluster-Zustaende.
- Unsichere oder offene Anomalie-Interpretationen.
- Fraktions- und Routenwissen ausserhalb des bereits freigegebenen Novapolis-/C6-Rahmens.

### Geruecht / Signalrauschen

- Hinweise auf "Lebewesen" im Untergrund von C6 bleiben Geruecht/Signalrauschen, bis eine neue Admin-Freigabe oder belastbare Evidenz vorliegt.

Slot-00-05-Arbeitskorridor v0
-----------------------------

Hinweis: Die folgenden Slots sind ein Arbeitskorridor fuer spaetere Kanonisierung. Sie ordnen vorhandene T+0-Anker in eine spielbare Sequenz, setzen aber keine neue harte Uhrzeit oder exakte Tick-Protokolle.

### Slot 00 - D5: Wartungsauftrag und vorsichtige Beobachtung

- Primärlinse: PC-direkt.
- Evidenz: `scene-2025-10-27-g.md`.
- Spielkern: Ronja prueft Unregelmaessigkeit statt sofortiger Konfrontation.
- Entscheidungsklassen:
  - vorsichtig beobachten,
  - Werkzeugtasche sichern oder markieren,
  - Jonas/Pahl frueh einbinden,
  - allein weitergehen.
- Fail-forward: Auch ein vorsichtiger Fehlgriff erzeugt hoechstens Zeitverlust, Misstrauen oder Zusatzkontrolle, nicht das Ende des Laufs.

### Slot 01 - D5: Terminal/Port/System-Link

- Primärlinse: PC-direkt.
- Evidenz: `scene-2025-10-27-h.md`.
- Spielkern: Nutzen gegen Risiko ausbalancieren.
- Entscheidungsklassen:
  - tiefer in den Link gehen,
  - Reflex Schutz priorisieren lassen,
  - Jonas als technischen Rueckhalt holen,
  - auf sichere Analyse vertagen.
- Fail-forward: Ein riskanter Zugriff darf Belastung, Dämpfung oder Informationsrauschen erzeugen, aber nicht die Session unbrauchbar machen.

### Slot 02 - D5: Werkstatt-/Funk-Weiterlauf und Pahl-Kontext

- Primärlinse: PC-direkt, mit teaminterner Verzweigung.
- Evidenz: `scene-2025-10-27-ah.md`, `D5.md`, `Pahl-Brenner.md`, `Jonas-Merek.md`.
- Spielkern: D5 bleibt nicht statisch; Ronja/Reflex arbeiten, waehrend Jonas/Pahl den Sicherheits- und Werkstattpfad tragen.
- Entscheidungsklassen:
  - Funk priorisieren,
  - Pahl um Freigabe/Regelhilfe bitten,
  - Werkstatt-/Schacht-Kontext aufziehen,
  - C6-Status aktiv abfragen.
- Fail-forward: Bei schlechter Priorisierung verschiebt sich nur, welcher Folgepfad spaeter teurer wird.

### Slot 03 - C6: Sicherung/Markierung als paralleler Weltfaden

- Primärlinse: world-only, spaeter allies-only oder pc-reveal.
- Evidenz: `scene-2025-10-27-d.md`, `C6.md`.
- Spielkern: C6 arbeitet parallel an Sicherung vor Analyse/Bergung.
- Reveal-Regel: Dieser Faden wird nur ueber bestaetigte Log-/Funk-/Instanzpfade an D5 ausgespielt.
- Fail-forward: Kein Dead End; ein verspaeteter Reveal verschiebt nur Informationsstand und Risikoabschaetzung.

### Slot 04 - C6: Abschluss/Übergabe und Echo-Moment

- Primärlinse: allies-only mit optionalem PC-Reveal.
- Evidenz: `scene-2025-10-27-e.md`.
- Spielkern: C6 konsolidiert einen Abschluss-/Uebergabemoment, waehrend Echo als Status- oder Schutzsignal wirkt.
- Reveal-Regel: Keine freie Ausgestaltung; nur das, was sauber in Missionslog, Log oder Folge-SSOT gespiegelt wird, darf Richtung PC wandern.

### Slot 05 - D5: Grundriss-/Systemordnung und Nordlinie-Entscheidungsfenster

- Primärlinse: PC-direkt mit Projektbezug.
- Evidenz: `scene-2025-10-27-ai.md`, `Nordlinie-01.md`, `Missionslog-Novapolis.md`.
- Spielkern: Ordnung, Planbarkeit und naechster Fokus werden festgezogen.
- Entscheidungsklassen:
  - D5 erst stabilisieren,
  - Tunnel/Nordlinie pushen,
  - Materiallauf vorbereiten,
  - C6-Reveal systematisch nachziehen.
- Fail-forward: Die Konsequenz ist Schwerpunktverschiebung, nicht Abbruch. Kosten laufen ueber Zeit, Sicherheit, Ressourcen oder Sichtbarkeit.

Konsequenzklassen fuer den ersten Korridor
-----------------------------------------

- Zeitkosten: Verzoegerung, zusaetzlicher Slot-Verbrauch, spaetere Freigabe.
- Sicherheitskosten: hoeherer Schutzbedarf, staerkere Pahl-/Reflex-Intervention, strengere Freigaben.
- Ressourcenkosten: Material-/Filter-/Werkzeugverbrauch, Tunnel- oder Funkaufwand.
- Beziehungskosten: Misstrauen, mehr Kontrolle, engere Beobachtung, aber kein sofortiger Beziehungsbruch ohne weitere Kette.
- Wissenskosten: weniger Klarheit, spaeterer Reveal, unsaubere Lageeinschaetzung.

Arbeitsreihenfolge fuer die naechsten RP-Laeufe
-----------------------------------------------

1. Den Folgekorridor hinter `slot 30` auf `slot 31-35` oder eine bewusst modulare Episodenform ausbauen.
2. Sessionvertrag, Produkt-Gate und spaetere Replay-Pfade technisch an denselben RP-Produktpfad anbinden.
3. Reveal- und Folgekorridor-Logik spaeter auf weitere Kern- und Puffergebiete jenseits des aktuellen Full-Slice-Sets ausdehnen.

Definition of Done fuer diesen Planungsschritt
----------------------------------------------

- Der erste Startkorridor ist evidence-first und nicht mehr nur als lose TODO-Formulierung beschrieben.
- Mehrere Startoptionen und ein fraktionsloser Pfad sind jetzt evidence-first im Arbeitsblatt verankert, ohne ueber den aktuellen Kanon hinauszugehen.
- Belegte Startanker, Reveal-Grenzen und offene Kanon-Luecken sind getrennt benannt.
- Der weitere RP-Pfad ist auf echte SSOT-Dateien und nicht auf freie Chat-Erinnerung abgestuetzt.
