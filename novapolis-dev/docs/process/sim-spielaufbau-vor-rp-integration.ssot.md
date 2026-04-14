---
stand: 2026-04-14 21:08
update: Die SSOT markiert den aktuellen Stand jetzt explizit als Ideensammlung und bindet den naechsten Schritt verbindlich an Sessionvertrag, Product Gate, Slice-Handover und bestehende RP-Produktquellen.
checks: markdownlint=PASS; frontmatter=PASS; todo-index-sync=PASS
---

Sim-Spielaufbau vor RP-Integration (SSOT)
=========================================

Zweck
-----

Diese SSOT definiert den geplanten Spielaufbau fuer den Sim-Client, bevor das RP-Modul als eigentlicher Spielmodus integriert wird. Ziel ist ein klarer, testbarer Produktpfad mit stabilen Zustandsgrenzen statt frueher Kopplung an RP-Inhalte.

Scope
-----

- Sim-Client-Struktur in Hub, Startphase, Kernloop und Resume-/Replay-Pfad.
- Integrationsgrenze zwischen Sim und RP (Datenvertrag, UI-Grenze, Triggerpunkte).
- Planungs- und DoD-Rahmen fuer die anschliessende Umsetzungsphase.

Nicht-Ziele
-----------

- Keine direkte RP-Content-Integration in diesem Dokumentlauf.
- Keine neuen RP-Lore-, Missions- oder Fraktionsannahmen.
- Keine Runtime- oder API-Retcons am bestehenden Sessionvertrag.

Status dieser Datei
-------------------

- Diese Datei ist aktuell ausdruecklich eine Ideensammlung und Planungs-SSOT fuer den Sim-Spielaufbau vor RP-Integration.
- Sie ist nicht selbst die neue Bestandsdatenquelle fuer Runtime-, RP-, Replay- oder Produktvertrag.
- Verbindlich fuer Bestandsdaten bleiben bis zur Uebernahme die bereits vorhandenen Zielquellen aus Sessionvertrag, Product Gate, Slice-Handover, RP-Start-/Folgekorridor und den belegten Runtime-Pfaden.
- Aussagen aus dieser Datei gelten erst dann als operativer Bestand, wenn sie im naechsten Schritt in diese Zielquellen uebernommen, dort konsistent gemacht und gegen den bestehenden Artefakt- und Vertragsrahmen belegt sind.

Quellenbasis
------------

- `novapolis-dev/docs/process/text-rpg-product-gate-v1.ssot.md`
- `novapolis-dev/docs/process/text-rpg-slice-2-handover-v1.ssot.md`
- `novapolis-dev/docs/specs/text-rpg-session-contract-v1.md`
- `novapolis_agent/docs/runbook.md`
- `novapolis-sim/scripts/Main.gd`

Einbindung in Bestandsdaten (Pflicht fuer den naechsten Schritt)
---------------------------------------------------------------

### Zielprinzip

- Der naechste Schritt ist keine weitere freie Erweiterung dieser Ideensammlung, sondern ihre saubere Einbindung in bestehende Bestandsdaten und belegte Produktquellen.
- Diese Datei bleibt dafuer Arbeits- und Ableitungsraum, darf aber keinen zweiten Wahrheitsrahmen neben den bereits aktiven Vertrags- und Produktdokumenten etablieren.

### Verbindliche Zielquellen

- `novapolis-dev/docs/specs/text-rpg-session-contract-v1.md` bleibt die Zielquelle fuer alle kanonischen Feld-, Zustands-, Log- und Replay-Anker rund um `campaign_id`, `session_id`, `scene_id`, `slot_id`, `turn_id`, `state_patches`, `world_log`, `pc_log` und Persistenzartefakte.
- `novapolis-dev/docs/process/text-rpg-product-gate-v1.ssot.md` bleibt die Zielquelle fuer Gate-, Verifikations- und Artefaktpflichten, sobald Teile dieser Mechanik produktrelevant oder pruefbar gemacht werden.
- `novapolis-dev/docs/process/text-rpg-slice-2-handover-v1.ssot.md` bleibt die Zielquelle fuer Resume-, Replay- und Folgepfadbindung hinter dem bestehenden Slice, falls die Sim-Mechanik dort operative Anschlussarbeit erzeugt.
- Die aktiven RP-Start- und Folgekorridor-SSOTs bleiben die Zielquellen fuer konkrete Startlagen, Slotanker, Orts- und Revealbindung; diese Datei darf dafuer keine freie Parallelkontinuitaet erzeugen.
- `novapolis_agent/docs/runbook.md` und die belegten Runtime-Pfade in Agent und Sim bleiben die Zielquellen fuer operative Umsetzung, Bedienpfade und verifizierte Ist-Aussagen.

### Einbindungsregeln

- Turn-, Tick-, Carry-Over- und Replay-Ideen aus dieser Datei duerfen nur dann in den Bestand uebergehen, wenn sie ohne Schattenstruktur auf den bestehenden Sessionvertrag abbildbar sind.
- Produktrelevante Regeln muessen vor operativer Nutzung aus dieser Datei in die passende Zielquelle uebernommen werden, statt hier als alleinstehende Wahrheit stehen zu bleiben.
- Konkrete Start-, Orts-, Rollen- oder Fortschrittsaussagen duerfen nur dann uebernommen werden, wenn sie an bereits belegte RP-SSOTs und deren Slot-/Revealrahmen angeschlossen werden.
- Falls eine Aussage weder sauber in Sessionvertrag, Product Gate, Slice-Handover, RP-SSOT noch belegten Runtime-Iststand passt, bleibt sie Idee und wird nicht als Bestandsdatum promoted.

### Erwarteter Uebernahmeschnitt

1. Vertragsfaehige Mechanikteile in Sessionvertrag und belegte Runtime-Modelle ueberfuehren.
2. Replay-, Resume- und Artefaktfolgen an Product Gate, Slice-Handover und Runbook anbinden.
3. Start-, Slot- und Weltbezug an bestehende RP-Produkt-SSOTs haengen statt hier isoliert fortzuschreiben.
4. Diese Datei danach auf verbleibende Planungsreste und offene Ableitungen reduzieren, statt sie als Dauer-Sammelort fuer operative Wahrheit wachsen zu lassen.

Zielbild (Spielaufbau)
----------------------

### Phase 0 - Hub und Runtime-Basis

- Hub bleibt operativer Einstieg fuer Serverstatus, Checks, Sessionstatus und Konfigurationspfade.
- Hub darf keine inhaltliche RP-Spielentscheidung erzwingen; nur technische Vorbedingungen sichern.

### Phase 1 - Startkontext und Session-Init

- Spieler bekommt klaren Startkontext (Session-ID, Slot, aktueller Zustand, aktive Ansicht).
- Start muss ohne RP-Modul lauffaehig sein, aber RP-faeige Felder bereits tragen.

### Phase 2 - Kernloop (Input -> Antwort -> Zustand)

- Einheitlicher Loop: Eingabe -> Agent-Antwort -> State-Update -> UI-Refresh.
- Ereignisse und Patch-Hinweise laufen ueber denselben Sessionvertrag wie im Gate-Pfad.

### Phase 3 - Resume und Replay als Erstklasse

- Resume-Anker und Replay-Manifest sind keine Zusatzansicht, sondern Kernteil des Spielaufbaus.
- Slot-/Checkpoint-Anwendung bleibt deterministisch und vertragstreu.

### Phase 4 - RP-Integrationsfenster

- RP wird erst gekoppelt, wenn Sim-Loop, Persistenz und Replay stabil und testbar sind.
- RP-Einstieg erfolgt ueber klaren Hand-off statt stiller Direktverdrahtung.

Integrationsgrenze zum RP-Modul
-------------------------------

### Sim-seitige Verantwortung vor RP

- Session-/Replay-Zustand verarbeiten und visualisieren.
- Bedienpfade fuer Turn, Resume, Replay, Slotnavigation und Checks stabil halten.
- Datenvertrag und Fehlerpfade robust gegen Teilverfuegbarkeit betreiben.

### RP-seitige Verantwortung nach Integration

- Spielinhalt, Fortschrittsregeln und modulare RP-Folgepfade liefern.
- RP-spezifische UI/Steuerung nur innerhalb des RP-Modulraums erweitern.

### Vertragliche Uebergabefelder

- `campaign_id`, `session_id`, `scene_id`, `slot_id`, `turn_id`
- `world_log`, `pc_log`, `state_patches`
- `resume_checkpoint_id`, `replay_manifest`

UI-Aufbau vor RP-Integration
----------------------------

- Hub-Topband: Runtime-/Gesundheitsstatus, Queue, Polling, Fehlerlage.
- Stage-Bereich: aktuelle Spielsicht, Logs, Sessionkontext.
- Ops-Spalte: Server/Checks, Replay/Resume, Hub-Chat.
- Modulflaechen: Agent, Checks, RP als getrennte Betriebsmodi; keine Mischsteuerung.
- Labelgrenzen bleiben eindeutig: `Hub-Chat` und `RP-Chat` sind getrennte Kontexte.

Arbeitsplan (vor RP-Integration)
--------------------------------

1. Sim-Loop-Haertung
   - Ziel: stabiler Input/Antwort/State-Refresh unter Last und Fehlerfaellen.
2. Resume-/Replay-Haertung
   - Ziel: konsistente Checkpoint-Anwendung ohne Slotdrift.
3. UI-Klarheit und Non-Overlap
   - Ziel: belastbares Layout ohne Kollisionen zwischen Ops-Komponenten.
4. Integrationsadapter RP
   - Ziel: minimale, explizite Uebergabeschicht statt direkter Main-Kopplung.

Akzeptanzkriterien vor RP-Integration
-------------------------------------

1. Sim-Spielschleife laeuft ohne RP-Modul stabil ueber mehrere Turns.
2. Resume und Replay sind vertragstreu und reproduzierbar.
3. Hub-/Ops-Layout bleibt bei gelaeufigen Aufloesungen ohne Ueberlappung.
4. RP-Einstiegspunkt ist als sauberer Adapterpfad definiert und testbar.

Mechanik-Akzeptanzkriterien
---------------------------

1. Ein Standard-Plan innerhalb von `30 Minuten` wird ohne Zusatzdialog ausspielbar bewertet und endet mit nachvollziehbarer Aufloesung.
2. Ein Plan im Bereich `30 bis 40 Minuten` fuehrt zu sichtbarer Fragmentierung mit klarer Trennung zwischen erledigt, begonnen und offen.
3. Ein Plan im Bereich `40 bis 60 Minuten` erzwingt vor der Ausspielung eine bewusste Spielerentscheidung zwischen Kuerzung und fragmentierter Bestaetigung.
4. Eine harte Blockade benennt den realen Grund, bietet wenn moeglich vorbereitende Teilhandlungen an und wird nicht nur als abstraktes Scheitern ausgegeben.
5. Ein Verdichtungswechsel wird fuer den Spieler sichtbar eingeleitet, laeuft ueber den Tick-Rahmen und fuehrt mit verbleibender Restzeit wieder sauber in den normalen Turn zurueck.
6. Carry-Over transportiert begonnene, unterbrochene und offene Arbeiten mit greifbaren Zustandsfeldern in den Folgeturn.
7. Das technische Turn- und Tick-Schema bleibt auf denselben Sessionvertrag abbildbar, ohne parallele Schattenstrukturen einzufuehren.

Pruefmatrix fuer Mechanik-Gates v0.1
-----------------------------------

1. Gegeben ein Plan mit abgeleitetem Gesamtwert `<= 30 Minuten`, wenn die Budgetpruefung abgeschlossen wird, dann wechselt der Lauf ohne bestaetigungspflichtigen Zwischendialog direkt von `turn_budget_review` nach `turn_execution`.
2. Gegeben ein Plan mit abgeleitetem Gesamtwert `31 bis 40 Minuten`, wenn der Spieler die fragmentierte Ausspielung bestaetigt, dann zeigt `execution_result` mindestens einen begonnenen oder offenen Schritt und die Spieler-Ausgabe trennt `erledigt`, `begonnen` und `offen` sichtbar.
3. Gegeben ein Plan mit abgeleitetem Gesamtwert `41 bis 60 Minuten`, wenn die Budgetpruefung abgeschlossen wird, dann endet der Lauf zwingend in `turn_confirmation_required` und bietet genau die sichtbaren Optionen `anpassen` oder `fragmentiert_bestaetigen`.
4. Gegeben ein blockierter Kernschritt, wenn die Blockadepruefung greift, dann setzt `budget_decision` den Plan auf `hard_block=true`, nennt den konkreten Blockadegrund und bietet mindestens eine vorbereitende Teilhandlung an, sofern die Lage aufloesbar ist.
5. Gegeben eine Lage mit unmittelbarer Gegenreaktion im Minutentakt, wenn waehrend `turn_execution` Verdichtungsbedarf entsteht, dann wird ein sichtbarer Verdichtungsstart ausgegeben, mindestens ein Tick-Protokoll erzeugt und anschliessend entweder in `turn_execution` mit Restzeit oder direkt in `turn_resolution` zurueckgefuehrt.
6. Gegeben ein begonnener oder unterbrochener Schritt, wenn `turn_resolution` abgeschlossen wird, dann enthaelt `carry_over` mindestens Bezeichnung, Zustand und einen konkreten Wiederaufnahmehinweis wie Fortschritt, offenen Zugang oder bereitliegendes Werkzeug.
7. Gegeben ein Turn mit oder ohne Verdichtungsfenster, wenn `turn_resume_ready` erreicht wird, dann bleiben `turn_id`, `scene_id`, `state_patches`, `world_log`, `pc_log`, `resume_checkpoint_id` und `replay_manifest` auf demselben aeusseren Sessionvertrag lesbar.

Offene Planungsfragen
---------------------

- Welcher minimale RP-Adapter-Scope wird im ersten Integrationsschnitt akzeptiert?
- Welche Sim-seitigen KPIs gelten als Gate fuer den Wechsel in den RP-Integrationslauf?
- Welche UI-Hinweise sind fuer User-Fuehrung noetig, wenn RP noch nicht aktiv ist?

Vorfestlegungen aus Antwortblock 1
---------------------------------

Die folgenden Punkte gelten fuer den aktuellen Planungsstand als vorlaeufig festgezogen, bis der detaillierte Turn-Ablauf separat konkretisiert wird.

### Einstieg und erste 5 bis 10 Minuten

- Die ersten 5 bis 10 Minuten des eigentlichen Spieleinstiegs sind fuer die Charaktererstellung reserviert.
- Zur Charaktererstellung gehoeren mindestens Startoption und Schwierigkeitsgrad.
- Die Charaktererstellung startet nicht still im Hintergrund, sondern wird durch die Erzaehler-KI aktiv vorgeschlagen und erst nach manueller Bestaetigung begonnen.

### Hauptmenue und Uebergang Hub -> Spiel

- Beim Verlassen des Hubs betritt der Nutzer nicht sofort eine laufende Szene, sondern zuerst das Hauptmenue des Spiels.
- Dieses Hauptmenue soll visuell wie ein heruntergekommener U-Bahn-Ticketschalter wirken und damit den Setting-Ton frueh tragen.
- Wenn noch kein Spielercharakter existiert, schlaegt die Erzaehler-KI dort direkt die Charaktererstellung vor.
- Wenn bereits ein Spielstand oder eine bestehende Figur vorhanden ist, wird der Nutzer von der Erzaehler-KI passend dazu begruesst.

### Rollenlogik und Rechte

- Im Hub bleibt der Nutzer auf der Systemebene Operator.
- Im laufenden Spiel ist der Nutzer Spieler seiner Figur und darf keine Adminrechte oder Hub-Sonderrechte mehr besitzen.
- Das Hauptmenue des Spiels bleibt bewusst OOC und trennt damit Operator-/Systemlogik von der eigentlichen Spielfigur-Ebene.

### Charakterstart

- Wenn noch keine Spielfigur existiert, fuehrt der Spielstart direkt in die Charaktererstellung.
- Diese Charaktererstellung ist kein versteckter Setup-Dialog, sondern der erste eigentliche Spielvorgang nach dem Eintritt in das Spielmenue.

### Kleinste spielbare Einheit

- Die kleinste spielbare Einheit ist vorlaeufig der einzelne Turn.
- Der exakte Turn-Ablauf wird im weiteren Verlauf dieser SSOT ueber `Turn-Modell v0.2`, `Zeitmodell v0.2` und `Verdichtungsregel v0.2` weiter konkretisiert.

### Eingabemodi

- Der Spielmodus soll umschaltbare Eingabeformen erlauben:
   - reiner Freitext
   - reine Vorauswahl
   - Vorauswahl mit optionaler Freitext-Ergaenzung
- Die Anzahl der angebotenen Vorgaben soll konfigurierbar sein, mit einem Zielkorridor von 2 bis 10 Vorgaben.
- Zusaetzlich soll steuerbar sein, ob Freitext parallel erlaubt oder deaktiviert ist.

### Fortschrittsbild und Realismusanspruch

- Das Spiel soll als realitaetsnahes RP angelegt sein und Fortschritt primaer ueber Weltreaktion statt ueber gamifizierte Marker vermitteln.
- Der Spieler soll Fortschritt vor allem daran erkennen, wie Welt, Fraktionen, Gruppen und Einzelpersonen auf seine Aktionen reagieren.
- Ein zweiter zentraler Fortschrittsanzeiger liegt in Tages- und Wochenabrechnungen fuer Gueter, Waren und wirtschaftliche Lage im Fraktions- bzw. Gruppenkontext.

Objektive Einordnung des aktuellen Planungsstands
------------------------------------------------

- Der bisherige Rahmen ist konsistent: Hub und Spiel sind nicht nur andere Screens, sondern unterschiedliche Rollen- und Rechteebenen.
- Der Einstieg ist bewusst gefuehrt und vermeidet einen diffusen Start ohne Figur oder Haltung.
- Die Erzaehler-KI ist als Eintrittsschwelle stark gesetzt; sie braucht spaeter jedoch klare Grenzen, damit sie den Spieler fuehrt, aber nicht System- oder Regelarbeit ueberlagert.
- Die flexible Eingabestruktur ist produktseitig stark, muss spaeter aber auf gleiche Entscheidungsqualitaet und Balancing geprueft werden, damit nicht verschiedene Modi zu unterschiedlichen Spielniveaus fuehren.
- Der realitaetsnahe Fortschrittsanspruch ist fachlich plausibel, erzeugt aber das Risiko, dass Fortschritt kurzfristig zu indirekt wirkt. Fuer den eigentlichen Turn-Ablauf werden daher zusaetzlich lokale, unmittelbar lesbare Rueckmeldesignale noetig sein.

Vorfestlegungen aus Antwortblock 2 und 3
---------------------------------------

Die folgenden Punkte konkretisieren den bisherigen Rahmen zum eigentlichen Spielzug und gelten fuer den aktuellen Planungsstand als vorlaeufig festgezogen.

### Turn-Beginn und Turn-Ende

- Ein Turn beginnt mit einem KI-Text, der die Aufloesung der Vorrunde und die daraus resultierende neue Situation beschreibt.
- Bei einem neuen Spielstand ersetzt die geschichtliche Einleitung die Aufloesung der Vorrunde und wird anschliessend mit der aktuellen Wahrnehmung der Figur verbunden.
- Ein Turn endet nicht durch Zwischenfragen, sondern erst dann, wenn der Spieler einen Aktionsplan tatsaechlich ausspielt.
- Rueckfragen, Klaerungen oder Planungsnachfragen an die KI koennen damit ausserhalb des eigentlichen Turn-Abschlusses behandelt werden.

### Grundstruktur eines Standard-Turns

1. Aufloesung der Vorrunde oder Einstiegslage.
2. Darstellung der neuen Situation und Wahrnehmung der Spielfigur.
3. Planung durch Texteingabe des Spielers.
4. Pruefung des Plans gegen das Zeitbudget.
5. Falls noetig: Hinweis auf Budgetueberschreitung und Entscheidung zwischen Bestaetigung oder Rueckkehr zur Planung.
6. Ausspielung des bestaetigten Plans.
7. Aufloesung mit erledigten, nicht erledigten, begonnenen und ausgelösten Folgen.

### Kleinste Zeiteinheit im Normalmodus

- Der Standardfall bleibt `1 Turn = 30 Minuten` Ingame-Zeit.
- Innerhalb dieses 30-Minuten-Turns darf der Spieler so viele Einzelhandlungen planen, wie realistisch in dieses Zeitfenster passen.
- Wenn einzelne Arbeiten laenger dauern, werden sie nicht kuenstlich in einen Turn gepresst, sondern als begonnen, fortgesetzt oder unvollendet in die naechste Runde uebernommen.

### Erlaubte Spielerhandlungen

- Im Grundsatz ist alles erlaubt, was die Spielfigur logisch selbst tun kann.
- Nicht erlaubt sind Powerplay, Metagaming oder Handlungen, die der Figur aus Wissen, Koerperlichkeit, Reichweite oder sozialer Position realistisch nicht zustehen.
- Die KI soll Plausibilitaet nicht nur narrativ, sondern auch ueber Zeitaufwand, Risiko und Reaktion der Umwelt absichern.

Turn-Modell v0.2
----------------

### Kernprinzip

- Der Spieler beschreibt keinen atomaren Einzelklick, sondern einen realistischen Handlungsplan fuer die naechsten 30 Ingame-Minuten.
- Die KI bewertet diesen Plan nicht ueber Bauchgefuehl, sondern ueber einen abgeleiteten Ablauf mit festen Einzelschritten und dokumentierbaren Zeitwerten.
- Bereits erledigte oder wiederkehrende Taetigkeiten sollen mit dokumentierten Grundwerten spaeter konsistenter einschaetzbar werden.

### Turn-Phasen

#### Phase 1 - Lagebild

- Die KI eröffnet jeden Turn mit einem knappen, aber relevanten Lagebild.
- Dieses Lagebild verbindet Wahrnehmung, offene Aufgaben, akute Risiken und sichtbare Veraenderungen seit der Vorrunde.

#### Phase 2 - Planung

- Der Spieler formuliert einen Aktionsplan in Freitext, Vorauswahl oder Hybridmodus.
- Der Plan kann mehrere Schritte enthalten, solange diese logisch und zeitlich in den 30-Minuten-Rahmen passen.

#### Phase 3 - Budgetpruefung

- Die KI leitet aus atomaren Handlungsschritten ab, ob der Plan in 30 Minuten passt.
- Wenn der Plan in den Rahmen passt, wird er direkt ausgespielt.
- Wenn der Plan den Rahmen sprengt, weist die KI darauf hin und bietet zwei Wege:
   - Rueckkehr zur Planung und Neuformulierung.
   - Bestaetigung, dass der Plan trotzdem so ausgespielt wird, wobei nicht erledigte Restteile offen bleiben.

#### Phase 4 - Ausspielung

- Die KI spielt den bestaetigten Plan in der gewaehlten Reihenfolge aus.
- Wenn das Zeitbudget waehrend der Abarbeitung erreicht ist, werden Restschritte nicht still verworfen, sondern als offen oder begonnen markiert.

#### Phase 5 - Aufloesung

- Die KI zeigt, was in diesem 30-Minuten-Fenster geschafft wurde.
- Gleichzeitig werden direkte Folgen, offene Restarbeiten und relevante Anschlusslage fuer den naechsten Turn sichtbar gemacht.

Zustandsmodell v0.1
-------------------

### Kernzustaende

- `turn_idle`: Der Turn ist noch nicht aktiv ausgespielt; der Spieler befindet sich in einem stabilen Lese- oder Ausgangszustand.
- `turn_briefing`: Das Lagebild fuer den neuen Turn wird angezeigt.
- `turn_planning`: Der Spieler formuliert oder ueberarbeitet seinen Plan.
- `turn_budget_review`: Der Plan wurde zerlegt und gegen das Zeitbudget geprueft.
- `turn_confirmation_required`: Die KI verlangt eine bewusste Entscheidung, weil Fragmentierung oder eine kritische Folge sichtbar geworden ist.
- `turn_execution`: Der bestaetigte Plan wird ausgespielt.
- `turn_dense_mode`: Die Lage ist in Verdichtung ueberfuehrt und laeuft im Tick-Schema.
- `turn_resolution`: Das Ergebnis des Turns, inklusive Folgen, Carry-Over und Restzeit, wird zusammengefuehrt.
- `turn_resume_ready`: Der Turn ist abgeschlossen und der Zustand ist bereit fuer Fortsetzung, Checkpoint oder Replay.

### Erlaubte Uebergaenge

- `turn_idle -> turn_briefing`
- `turn_briefing -> turn_planning`
- `turn_planning -> turn_budget_review`
- `turn_budget_review -> turn_planning`, wenn der Spieler den Plan anpasst
- `turn_budget_review -> turn_confirmation_required`, wenn Fragmentierung, harter Hinweis oder Grenzfall bestaetigt werden muss
- `turn_budget_review -> turn_execution`, wenn der Plan direkt ausspielbar ist
- `turn_confirmation_required -> turn_execution`, wenn der Spieler die Ausspielung bestaetigt
- `turn_confirmation_required -> turn_planning`, wenn der Spieler zur Ueberarbeitung zurueckkehrt
- `turn_execution -> turn_dense_mode`, wenn waehrend der Ausspielung unmittelbare Reaktionslogik entsteht
- `turn_dense_mode -> turn_execution`, wenn die verdichtete Lage endet und die Restzeit desselben Turns weiter ausgespielt werden kann
- `turn_execution -> turn_resolution`
- `turn_dense_mode -> turn_resolution`, wenn die Restzeit verbraucht oder die Lage direkt turnabschliessend geworden ist
- `turn_resolution -> turn_resume_ready`

### Zustandsregeln

- Rueckfragen und Klaerungen ohne Turn-Abschluss bleiben in `turn_planning`, solange kein bestaetigter Ausspielpfad gestartet wurde.
- `turn_confirmation_required` ist nur fuer echte Grenzfaelle gedacht und darf nicht zum Dauerzustand werden.
- `turn_dense_mode` ist immer temporaer und kehrt entweder in `turn_execution` oder direkt in `turn_resolution` zurueck.
- `turn_resume_ready` ist der einzige Zustand, aus dem Checkpoint, Resume oder Replay kanonisch weitergefuehrt werden.

### Ableitungslogik fuer mehrteilige Aktionsplaene

1. Die KI zerlegt jeden Plan zuerst in atomare Handlungsschritte.
2. Jeder atomare Schritt bekommt einen festen `Grundwert` aus einer internen Referenz.
3. Danach werden situative Modifikatoren auf den Schritt angewendet.
4. Anschliessend wird ein `Uebergangsaufschlag` fuer Sequenzverlust zwischen mehreren Schritten addiert.
5. Das Ergebnis ist keine freie Schaetzung, sondern ein abgeleiteter Gesamtwert in Minuten.

### Atomare Schrittklassen

- Bewegung innerhalb eines bekannten Bereichs wird standardmaessig als `kurz` behandelt.
- Eine einfache direkte Interaktion wird standardmaessig als `sehr kurz` behandelt.
- Technische Arbeit liegt standardmaessig zwischen `mittel` und `lang`.
- Komplexe Reparaturen oder verknuepfte Eingriffe gelten als `mehrstufig`.

### Pflicht-Modifikatoren

- Zustand der Figur, insbesondere Erschoepfung oder Verletzung.
- Umgebung, insbesondere Dunkelheit, Gefahr, Chaos oder Druck.
- Hilfsmittel, insbesondere Werkzeugverfuegbarkeit oder Improvisation.
- Unterstuetzung, insbesondere allein versus mit Hilfe.

### Sequenzverlust als Pflichtregel

- Mehrere Schritte hintereinander kosten nicht nur ihre Einzelsummen, sondern zusaetzlich Zeit fuer Uebergaenge.
- Der Uebergangsaufschlag bildet Umruesten, Neuorientierung, Suchaufwand, sinkende Aufmerksamkeit und steigende Fehlerwahrscheinlichkeit ab.
- Dadurch soll derselbe Plan bei steigender Komplexitaet konsistent ueber der blossen Einzelsumme liegen.

Zeitmodell v0.2
---------------

### Grundregel

- Jede Handlung kostet Zeit.
- Auch kleine Handlungen sind nicht kostenlos, sondern haben mindestens einen Basisaufwand.
- Die KI soll Zeit nicht dramaturgisch beliebig, sondern moeglichst konstant, wiederholbar und aus Grundwert plus Modifikatoren ableiten.

### Basislogik der Zeitschaetzung

- Jede Handlung bekommt einen `Grundwert` in Minuten.
- Dieser Grundwert wird anschliessend durch reale Einflussfaktoren modifiziert.
- Fuer wiederkehrende Taetigkeiten wird spaeter derselbe Grundwert wiederverwendet und nur durch aktuelle Umstaende angepasst.
- Bei mehrteiligen Plaenen wird die Gesamtzeit zusaetzlich um einen `Uebergangsaufschlag` erhoeht.

### Vorlaeufige Einflussfaktoren

- Faehigkeiten und Eigenschaften der Spielfigur.
- Unterstuetzung durch andere beteiligte Personen.
- Werkzeuge, Materiallage und Vorbereitung.
- Entfernung, Wegzeit und Zugangsbedingungen.
- Umgebungszustand, Stoerungen, Gefahr und Druck.
- Vertrautheit mit der Taetigkeit.
- Erschoepfung, Verletzung oder sonstige Einschraenkungen.

### Vorlaeufige Zeitklassen

- `sehr kurz`: 1 bis 3 Minuten
- `kurz`: 3 bis 10 Minuten
- `mittel`: 10 bis 20 Minuten
- `lang`: 20 bis 30 Minuten
- `mehrstufig`: mehr als 30 Minuten, also turnuebergreifend

### Referenz-Grundwerte fuer Standardhandlungen v0.1

- `kurzer Blick oder kurze verbale Reaktion`: 1 bis 2 Minuten
- `einfache direkte Interaktion`: 3 bis 5 Minuten
- `Bewegung innerhalb eines vertrauten Teilbereichs`: 5 bis 10 Minuten
- `Werkzeug oder Material im Nahbereich organisieren`: 5 bis 10 Minuten
- `kurze Sichtpruefung oder einfache Analyse`: 5 bis 10 Minuten
- `gezielte Untersuchung mit mehreren Pruefschritten`: 10 bis 15 Minuten
- `einfache manuelle Arbeit ohne Stoerung`: 10 bis 15 Minuten
- `technische Standardarbeit mit Werkzeug`: 15 bis 25 Minuten
- `komplexe Reparatur oder mehrgliedriger Eingriff`: 25 bis 30 Minuten
- `mehrstufige Arbeit mit Vorbereitung, Eingriff und Test`: ueber 30 Minuten

### Leitregeln fuer die Nutzung der Referenzwerte

- Die Referenzwerte sind keine Spielerinformation, sondern interne Systemwerte fuer konsistente Ableitungen.
- Die KI darf einen Wert nur dann stark absenken oder anheben, wenn ein konkreter Modifikator dies traegt.
- Derselbe Handlungstyp soll unter vergleichbaren Umstaenden wieder auf denselben Grundwert zurueckfallen.
- Wenn eine Handlung aus mehreren verschiedenen Handlungstypen besteht, wird sie nicht als ein Gesamtblock gewertet, sondern in Einzelschritte zerlegt.

### Modifikator-Matrix fuer die Zeitableitung v0.1

#### Zustand der Figur

- `ausgeruht und handlungssicher`: `-2 Minuten`, mindestens jedoch nicht unter `1 Minute` fuer den jeweiligen Schritt
- `leicht erschoepft oder leicht angeschlagen`: `+2 Minuten`
- `deutlich erschoepft oder verletzt`: `+5 Minuten`
- `stark eingeschraenkt`: `+10 Minuten` oder harte Blockade, wenn die Handlung real nicht mehr plausibel ist

#### Umgebung und Druck

- `ruhig, hell, geordnet`: `0 Minuten`
- `dunkel, eng oder unaufgeraeumt`: `+2 Minuten`
- `chaotisch, laut oder unsicher`: `+5 Minuten`
- `akute Gefahr, Beschuss, Panik oder massiver Zeitdruck`: `+10 Minuten` oder Wechsel in Verdichtung, wenn unmittelbare Reaktionslogik wichtiger wird als Planlogik

#### Hilfsmittel und Materiallage

- `passendes Werkzeug und Material voll verfuegbar`: `0 Minuten`
- `Werkzeug muss erst geholt oder vorbereitet werden`: `+3 Minuten`
- `behelfsmessig oder improvisiert`: `+5 Minuten`
- `notwendiges Werkzeug oder Material fehlt`: harte Blockade oder Plan muss umformuliert werden

#### Unterstuetzung

- `allein`: `0 Minuten`
- `gezielte Hilfe durch eine geeignete Person`: `-3 Minuten`
- `mehrere koordinierte Helfer`: `-5 Minuten`, sofern die Arbeit parallelisierbar ist
- `ungeeignete oder stoerende Hilfe`: `+3 Minuten`

#### Vertrautheit und Routine

- `Routinehandlung im vertrauten Umfeld`: `-2 Minuten`
- `bekannt, aber nicht eingespielt`: `0 Minuten`
- `ungewohnt oder selten`: `+3 Minuten`
- `erstmals oder nur theoretisch bekannt`: `+6 Minuten`

#### Leitregeln fuer die Modifikatoren

- Die Modifikatoren werden pro atomarem Schritt und nicht nur auf den Gesamtplan angewendet.
- Gleichartige Modifikatoren duerfen sich addieren, solange die Begruendung pro Schritt sichtbar bleibt.
- Wenn ein Modifikator eine Handlung praktisch unmoeglich macht, ersetzt die harte Blockade jede weitere Minutenrechnung.
- Negative Modifikatoren duerfen einen Schritt beschleunigen, aber nie auf `0 Minuten` senken.

### Prioritaetslogik fuer Modifikatoren v0.1

1. Harte Blockade pruefen: Wenn Koerperlichkeit, Werkzeug, Zugang, Wissen oder soziale Position die Handlung real unmoeglich machen, endet die Auswertung ohne weitere Minutenrechnung.
2. Verdichtungsbedarf pruefen: Wenn unmittelbare Gegenreaktionen, akute Gefahr oder parallele Akteure die Lage bestimmen, wechselt die Auswertung von Planlogik auf Tick-Logik.
3. Zeitmodifikatoren anwenden: Nur wenn die Handlung weiter planbar bleibt, werden Minutenmodifikatoren auf den atomaren Schritt gerechnet.
4. Sequenzverlust addieren: Erst nach Schrittbewertung wird der Uebergangsaufschlag fuer Mehrschrittplaene addiert.

### Eskalationsregeln fuer Verdichtung v0.1

- Ein Modifikator `akute Gefahr, Beschuss, Panik oder massiver Zeitdruck` zwingt nicht automatisch in Verdichtung, sondern nur dann, wenn dadurch unmittelbare Reaktionsfolgen im Minutentakt relevant werden.
- Ein sozialer oder physischer Konflikt mit moeglicher direkter Gegenreaktion hat Vorrang vor normaler Minutenrechnung und wird in Verdichtung ueberfuehrt.
- Reine Schwierigkeit ohne unmittelbare Gegenreaktion bleibt im normalen Turn und erzeugt nur Minutenaufschlaege.
- Eine Lage kann waehrend der Ausspielung von normaler Turn-Logik in Verdichtung kippen, wenn aus dem Resultat heraus ploetzlich unmittelbare Reaktionen entstehen.

### Harte Blockade-Regeln v0.1

- `koerperlich unmoeglich`: Die Figur kann die Handlung in ihrem aktuellen Zustand real nicht ausfuehren.
- `werkzeugseitig unmoeglich`: Ein zwingend notwendiges Werkzeug oder Material fehlt vollstaendig.
- `zugangsseitig unmoeglich`: Der Zielort oder das Zielobjekt ist ohne vorherige Zusatzhandlung nicht erreichbar.
- `wissensseitig unmoeglich`: Die Figur kann die Handlung mangels Wissen, Kontext oder Bedienkenntnis nicht plausibel beginnen.
- `sozial unmoeglich`: Die Handlung scheitert bereits an Autoritaet, Rolle oder fehlender sozialer Zugriffsebene.

### Leitregeln fuer harte Blockaden

- Eine harte Blockade beendet die aktuelle Planbewertung fuer den betroffenen Schritt sofort.
- Harte Blockaden sollen konkret benannt werden und nicht nur als abstraktes `geht nicht` erscheinen.
- Wenn eine Blockade durch vorbereitende Teilhandlungen aufloesbar ist, soll die KI diese Teilhandlungen statt der blockierten Zielhandlung anbieten.
- Wenn die gesamte Handlungskette auf einem blockierten Kernschritt beruht, gilt der Gesamtplan als `unspielbar`.

### Turn-Feedback-Mindestset v0.1

- Jeder abgeschlossene Turn muss mindestens sichtbar machen, was erledigt wurde.
- Jeder abgeschlossene Turn muss sichtbar machen, was offen oder begonnen bleibt.
- Jeder abgeschlossene Turn muss mindestens ein unmittelbares Rueckmeldesignal enthalten: Zustandsaenderung, Reaktion, Risiko oder neuer Anschluss.
- Wenn keine direkte Weltreaktion sichtbar ist, muss stattdessen klar benannt werden, welche spaetere Folge angestossen wurde.
- Der Spieler soll nach jedem Turn wissen, was jetzt anders ist, was noch laeuft und worauf der naechste Schritt aufsetzt.

### Vorlaeufige Regelauslegung

- Wenn der geplante Gesamtaufwand bis `30 Minuten` liegt, gilt der Plan als innerhalb des Turn-Rahmens.
- Wenn der geplante Gesamtaufwand zwischen `30 und 40 Minuten` liegt, gilt der Plan als knapp drueber.
- Wenn der geplante Gesamtaufwand zwischen `40 und 60 Minuten` liegt, gilt der Plan als deutlich drueber.
- Wenn der geplante Gesamtaufwand ueber `60 Minuten` liegt, gilt der Plan als zeitlich unspielbar.
- Wenn eine Einzeltaetigkeit fuer sich bereits ueber 30 Minuten liegt, wird sie als Mehrturn-Aktion behandelt.
- Wiederkehrende Taetigkeiten sollen mit dokumentiertem Grundwert gespeichert werden; modifiziert wird dann nur noch die konkrete Situation.

### Schwellenlogik fuer die Budgetpruefung

- `innerhalb des Rahmens` bedeutet `<= 30 Minuten` und wird ohne Sonderdialog ausgespielt.
- `knapp drueber` bedeutet `30 bis 40 Minuten` und wird nur mit sichtbarer Fragmentierung ausgespielt: letzte Schritte fallen weg oder bleiben begonnen und offen.
- `deutlich drueber` bedeutet `40 bis 60 Minuten` und fuehrt zu einem klaren Hinweis, dass der Plan nicht sauber in den Turn passt; der Spieler muss kuerzen oder die Fragmentierung bewusst bestaetigen.
- `unspielbar` bedeutet entweder `> 60 Minuten` oder logisch unmoeglich; in diesem Fall greift eine harte Blockade.

### Realitaetsgruende fuer harte Blockaden

- fehlende Mittel
- falsche Annahmen ueber die Lage
- physikalische oder soziale Unmoeglichkeit

Persistenz offener Handlungen v0.1
---------------------------------

### Pflichtzustaende

- `begonnen`: Die Handlung wurde gestartet, Fortschritt existiert und die Arbeit kann im naechsten Turn fortgesetzt werden.
- `unterbrochen`: Die Handlung wurde aktiv gestoert oder abgebrochen und kann Nebenfolgen wie Fehler, Schaden oder Risiko tragen.
- `offen`: Die Handlung war geplant, wurde in diesem Turn aber nicht begonnen.

### Konkrete Persistenzfelder

- Jede offene oder laufende Arbeit soll mit einer konkreten Bezeichnung gespeichert werden.
- Der Persistenzzustand soll mindestens Fortschritt, vorbereitete Mittel, geoeffnete Zugaenge und sichtbare Blocker benennen.
- Ziel ist keine vage Notiz wie `Reparatur laeuft noch`, sondern ein Zustand nach dem Muster `Ventil C6 reparieren: 40 Prozent, Werkzeug liegt bereit, Zugang offen`.

### Prioritaetsvererbung und Wiederaufnahme

- Begonnene Arbeiten bleiben mental und praktisch im Raum und erhalten dadurch Prioritaetsvererbung fuer den Folgeturn.
- Die Wiederaufnahme einer begonnenen Arbeit kostet weniger Zeit als ein kompletter Neustart, solange Vorbereitung, Werkzeuglage und Zugang noch gueltig sind.
- Unterbrochene Arbeiten koennen zusaetzliche Wiederanlaufkosten oder Risiken erzeugen, wenn die Unterbrechung den Zustand verschlechtert hat.

Technisches Antwortschema fuer Turn-Mechanik v0.1
------------------------------------------------

### Ziel des Turn-Schemas

- Die Turn-Mechanik soll spaeter nicht nur narrativ, sondern auch als strukturierter Ausgabeblock vorliegen.
- Dieser Block dient der Budgetpruefung, der sichtbaren Fragmentierung und der Wiederaufnahme offener Arbeiten.
- Die Felder sind als internes Vertragsziel zu verstehen, auch wenn die endgueltige API-Form spaeter in den Sessionvertrag eingezogen wird.

### Pflichtbloecke

- `plan_analysis`: Zerlegte Handlungsschritte mit Grundwert, Modifikatoren und Gesamtzeit.
- `budget_decision`: Klassifikation des Plans als innerhalb des Rahmens, knapp drueber, deutlich drueber oder unspielbar.
- `execution_result`: Welche Schritte erledigt, begonnen, unterbrochen oder offen geblieben sind.
- `carry_over`: Welche offenen Arbeiten mit welchem Zustand in den naechsten Turn uebergehen.
- `time_state`: Verbrauchte Zeit, Restzeit und gegebenenfalls Verdichtungszeit.

### Turn-Referenzschema

```json
{
   "plan_analysis": {
      "steps": [
         {
            "step_id": "step_01",
            "label": "Werkzeug organisieren",
            "base_minutes": 8,
            "modifiers": [
               {"kind": "environment", "effect": "+4", "reason": "dunkel und unaufgeraeumt"}
            ],
            "transition_surcharge_minutes": 2,
            "estimated_minutes": 14
         }
      ],
      "estimated_total_minutes": 37
   },
   "budget_decision": {
      "class": "knapp_drueber",
      "hard_block": false,
      "player_options": ["anpassen", "fragmentiert_bestaetigen"]
   },
   "execution_result": {
      "completed_step_ids": ["step_01"],
      "started_step_ids": ["step_02"],
      "interrupted_step_ids": [],
      "open_step_ids": ["step_03"]
   },
   "carry_over": [
      {
         "task_id": "repair_c6_valve",
         "state": "begonnen",
         "progress_percent": 40,
         "prepared_assets": ["werkzeug bereit", "zugang offen"],
         "resume_modifier": "verkuerzt_wiederaufnahme"
      }
   ],
   "time_state": {
      "turn_budget_minutes": 30,
      "consumed_minutes": 30,
      "remaining_minutes": 0,
      "dense_mode_minutes": 12
   }
}
```

### Semantische Regeln fuer das Schema

- `base_minutes` kommt immer aus der Referenzlogik und nicht aus einem freien Schaetzwert.
- `estimated_minutes` ist die Summe aus `base_minutes`, Modifikatoren und `transition_surcharge_minutes`.
- `class` in `budget_decision` darf nur einen der vier festen Werte `innerhalb_des_rahmens`, `knapp_drueber`, `deutlich_drueber`, `unspielbar` tragen.
- `carry_over` muss nur Eintraege enthalten, die im Folgeturn real weiterwirken.
- `dense_mode_minutes` bleibt `0`, solange kein Verdichtungsmodus aktiv war.
- Eine harte Blockade muss in `budget_decision` als `hard_block=true` plus konkretem Grund sichtbar werden.

### Mapping auf den bestehenden Sessionvertrag v0.1

- `turn_id` bleibt der kanonische aeussere Identifikator fuer den aktuellen 30-Minuten-Turn.
- `scene_id` markiert die sichtbare Lageeinheit, innerhalb derer Turn und Verdichtungsfenster stattfinden.
- `state_patches` bleiben der produktive Kanal fuer sichtbare Zustandsaenderungen aus `execution_result`, `carry_over` und Tick-Resultaten.
- `resume_checkpoint_id` darf nur aus `turn_resume_ready` erzeugt oder sichtbar neu gesetzt werden.
- `replay_manifest` fuehrt Turn-Ausspielung und Verdichtungsfenster als zusammenhaengenden Nachvollzugspfad, ohne dass Ticks einen eigenen Konkurrenzvertrag zu `turn_id` erzeugen.
- `world_log` und `pc_log` bleiben die sichtbaren Nachvollzugskanaele fuer Sofortfolgen, Spaetfolgen und turnbezogene Wahrnehmung.

### Mapping-Regeln

- Ein Verdichtungsfenster ist kein eigener Turn, sondern ein Turn-internes Reaktionssegment.
- Ticks duerfen als Replay-Unterstruktur erscheinen, aber nicht den aeusseren Sessionrahmen aus `turn_id` und `scene_id` ersetzen.
- Carry-Over aus einem Turn muss im Folgeturn wieder ueber denselben Sessionvertrag lesbar sein und darf nicht nur als lokale UI-Merkhilfe existieren.
- Checkpoints werden an stabilen Turn-Grenzen gesetzt; ein laufendes Verdichtungsfenster ist ohne explizite Sonderregel kein eigener Minimal-Checkpoint.

### Replay- und Checkpoint-Grenzen v0.1

- Jeder abgeschlossene Turn schreibt genau einen aeusseren Replay-Abschnitt unter derselben `turn_id`; Verdichtung bleibt darin ein eingebettetes Segment und erzeugt keinen konkurrierenden Hauptabschnitt.
- Ein Verdichtungsfenster erzeugt im `replay_manifest` einen markierten Teilblock mit `segment_kind=dense_mode`, Startminute, Endminute, Tick-Anzahl und Ruecksprungpunkt in den normalen Turn.
- Pro Tick muessen mindestens Wahrnehmung, Spieleraktion, Gegenreaktion und die daraus entstandenen `state_patches` oder Patch-Hinweise lesbar bleiben, auch wenn sie im Replay nur als Unterstruktur des Turns erscheinen.
- `world_log` traegt die sichtbare Weltreaktion des gesamten Turns; `pc_log` traegt Wahrnehmung, Entscheidungsdruck und Rueckmeldung aus Turn und Verdichtung, ohne dass dafuer ein separater Tick-Kanal eingefuehrt wird.
- `resume_checkpoint_id` darf nur gesetzt oder ersetzt werden, wenn der Lauf `turn_resume_ready` erreicht hat; ein mitten in Verdichtung abgebrochener Zustand bleibt ein unsauberer Zwischenstand und ist ohne explizite Sonderregel kein kanonischer Resume-Anker.
- Wenn ein Turn mehrere Verdichtungsfenster enthaelt, werden sie als geordnete Teilsegmente desselben Replay-Abschnitts gefuehrt und jeweils mit ihrer verbrauchten Turn-Restzeit dokumentiert.
- Ein Replay muss nach dem Laden eindeutig rekonstruieren koennen, welche Minuten im normalen Turn, welche im Verdichtungsfenster und welche als Carry-Over in den Folgeturn gewandert sind.

Sofortige und verzoegerte Folgen
--------------------------------

### Sofortige Folgen im selben Turn

- Akute Gefahrenlage.
- Unfaelle oder unmittelbare Komplikationen.
- Direkte NPC-Reaktionen.
- Sichtbare Veraenderungen im Raum oder am Zustand einer laufenden Aufgabe.
- Direkt ausgeloeste logische Konsequenzen einer Handlung.

### Verzoegerte Folgen in spaeteren Turns

- Warenfluss und Transportfolgen mit Laufzeit.
- Fortschritt oder Rueckstand bei Wartung, Instandsetzung und offenen Arbeitsketten.
- Reaktionen von Fraktionen, Gruppen und Einzelpersonen, die nicht sofort sichtbar werden.
- Geruechte, Rufveraenderungen, politische oder soziale Nachwirkungen.
- Sekundaere Sicherheits-, Logistik- oder Versorgungseffekte.

### Grundsatz fuer die Darstellung

- Nicht jede Folge muss im selben Turn sichtbar werden.
- Fuer ein realitaetsnahes RP soll zwischen direkter Auswirkung und spaeterer Nachwirkung bewusst getrennt werden.
- Der Turn-Abschluss soll daher sowohl Sofortfolgen als auch offene oder anlaufende Spaetfolgen kenntlich machen.

Verdichtungsregel v0.2
----------------------

### Trigger

- Die Verdichtungsregel greift nicht bei jeder Interaktion, sondern nur dann, wenn unmittelbare Reaktionstakte relevant werden.
- Ein Trigger liegt vor, wenn mindestens eines der folgenden Kriterien erfuellt ist:
   - direkte Reaktion wird sofort erwartet, etwa im Gespraech, bei einer Drohung oder bei einem Befehl
   - Zeitkritik entsteht, etwa durch Konflikt, Gefahr oder akuten Druck
   - mehrere Akteure koennen gleichzeitig handeln oder reagieren

### Moduswechsel

- Im Verdichtungsmodus wird der normale 30-Minuten-Turn sichtbar in einen feineren Reaktionstakt ueberfuehrt.
- Die KI muss den Wechsel klar signalisieren: Zeit wird feiner, Entscheidungen werden kleiner und das Geschehen wird unmittelbarer.
- Im Verdichtungsmodus kann ein normaler 30-Minuten-Turn in bis zu `30 Ticks` zerlegt werden.
- Ein Tick entspricht durchgaengig `1 Minute`.

### Zweck der Verdichtung

- Direkte Interaktionen sollen nicht durch den Stundenmodus grob oder unplausibel werden.
- Gleichzeitig soll der Normalfall weiter der 30-Minuten-Turn bleiben, damit Logistik, Wirtschaft, Arbeit und Alltag nicht unnötig verlangsamt werden.

### Tick-Logik im Verdichtungsmodus

- Jeder Tick bildet die Reihenfolge `Wahrnehmung -> Entscheidung -> Reaktion` ab.
- Handlungen werden im Verdichtungsmodus atomar behandelt und nicht mehr als kompletter Stundenplan abgegeben.
- Typische Tick-Handlungen sind Antworten, Beobachten, kurzes Entscheiden, Deckung suchen, Drohen, Nachgeben oder unmittelbares Nachsetzen.

Technisches Tick-Schema fuer Verdichtung v0.1
---------------------------------------------

### Ziel des Schemas

- Der Verdichtungsmodus soll nicht nur atmosphaerisch beschrieben, sondern als eigener strukturierter Entscheidungsrahmen gefuehrt werden.
- Das Tick-Schema verbindet unmittelbare Wahrnehmung, Aktion, Gegenreaktion und Rueckfuehrung in den 30-Minuten-Turn.
- Es dient spaeter als Vorlage fuer UI, API und Replay, ohne jetzt schon die konkrete Runtime-Implementierung festzuziehen.

### Pflichtbloecke pro Tick

- `tick_context`: Wer handelt, was ist akut, welche Minute des Verdichtungsfensters laeuft gerade.
- `perception`: Was die Spielfigur in diesem Tick konkret wahrnimmt.
- `decision_window`: Welche atomaren Reaktionen jetzt plausibel zur Wahl stehen.
- `resolution`: Was aus der gewaelten Aktion unmittelbar folgt.
- `carry_tick_state`: Welche Spannung, Drohung, Bewegung oder offene Reaktion in den naechsten Tick weitergetragen wird.

### Referenzschema

```json
{
   "tick_context": {
      "dense_mode": true,
      "tick_index": 7,
      "tick_length_seconds": 60,
      "remaining_turn_minutes": 23,
      "actors": ["spieler", "npc_01"]
   },
   "perception": {
      "scene_pressure": "hoch",
      "visible_changes": ["npc_01 hebt die Stimme", "zwei Schritte Abstand bleiben"],
      "immediate_risk": "sozialer_konflikt"
   },
   "decision_window": {
      "allowed_actions": ["antworten", "beschwichtigen", "drohen", "zurueckweichen"],
      "free_text_allowed": true,
      "response_deadline": "immediate"
   },
   "resolution": {
      "player_action": "beschwichtigen",
      "npc_response": "zwoegert, bleibt aber angespannt",
      "state_patch_notes": ["konflikt_nicht_eskaliert", "anspannung_bleibt_hoch"]
   },
   "carry_tick_state": {
      "continue_dense_mode": true,
      "open_pressure": ["angespannte_stimmung", "unklare_absicht_des_npc"],
      "elapsed_dense_minutes": 7
   }
}
```

### Semantische Regeln fuer das Tick-Schema

- Jeder Tick repraesentiert genau `1 Minute` und darf nicht in kleinere Basiseinheiten zerlegt werden.
- `continue_dense_mode` bleibt nur dann `true`, wenn unmittelbar weitere Gegenreaktionen erwartet werden.
- `remaining_turn_minutes` muss nach jedem Tick sinken und nach dem Ende des Verdichtungsfensters in `time_state` des Turn-Schemas aufgehen.
- Das Tick-Schema ersetzt die normale Budgetpruefung nicht dauerhaft, sondern unterbricht sie nur fuer die verdichtete Lage.

### Prioritaetskette zwischen Turn und Tick

- Solange Handlungen als planbarer Ablauf vorliegen, bleibt der normale Turn das fuehrende Modell.
- Sobald Gegenreaktionen wichtiger werden als Vorausplanung, uebernimmt das Tick-Schema die Fuehrung.
- Nach Ende der unmittelbaren Reaktionslage kehrt die Auswertung immer in das Turn-Schema zurueck; Verdichtung ist nie der dauerhafte Basismodus.

### Ende der Verdichtung

- Die Verdichtung endet, wenn keine unmittelbare Gegenreaktion mehr noetig ist.
- Die Verdichtung endet auch, wenn die Situation wieder stabil und fuer grobere Planung geeignet ist.
- Nach dem Ende fuehrt die KI die verstrichenen Ticks in einen neuen Turn-Kontext zurueck und weist die verbleibende Restzeit sichtbar aus.
- Beispiel: `12 Minuten Verdichtung` fuehren bei einem frischen Turn zu `18 Minuten Restzeit` im normalen 30-Minuten-Modus.

Spieler-Ausgaberegeln fuer die Turn-Mechanik v0.1
-------------------------------------------------

### Ziel der Ausgaberegeln

- Die mechanische Bewertung soll fuer den Spieler klar, knapp und nachvollziehbar erscheinen.
- Das System darf intern detailliert rechnen, nach aussen aber nicht in technischem Rauschen versinken.
- Jede Systemmeldung soll einen klaren Zweck haben: informieren, begrenzen, bestaetigen oder den naechsten Schritt anbieten.

### Pflichtsignale fuer Budgetbewertung

- `innerhalb des Rahmens`: Die KI bestaetigt knapp, dass der Plan in den aktuellen Turn passt, und spielt ohne Warnsprache aus.
- `knapp drueber`: Die KI benennt, dass der Plan den Rahmen leicht ueberzieht, und macht sichtbar, dass Restteile begonnen oder offen bleiben koennen.
- `deutlich drueber`: Die KI sagt klar, dass der Plan nicht sauber in den Turn passt, und verlangt eine bewusste Entscheidung zwischen Kürzung und fragmentierter Ausfuehrung.
- `unspielbar`: Die KI blockiert den Plan klar und benennt den realen Grund statt nur die abstrakte Kategorie.

### Sprachregeln fuer Budgethinweise

- Hinweise muessen konkret bleiben und sollen Minutenlogik oder Plausibilitaet benennen, nicht bloss `zu viel` oder `geht nicht` sagen.
- Hinweise duerfen kurz sein, muessen aber immer den naechsten Schritt eroeffnen: anpassen, bestaetigen oder vorbereitende Teilhandlung waehlen.
- Bei `knapp drueber` und `deutlich drueber` soll erkennbar sein, welche Teile voraussichtlich zuerst wegfallen oder offen bleiben.

### Sprachregeln fuer harte Blockaden

- Harte Blockaden muessen den blockierenden Faktor explizit benennen: Koerper, Werkzeug, Zugang, Wissen oder soziale Position.
- Wenn eine Blockade aufloesbar ist, soll die KI unmittelbar eine oder mehrere vorbereitende Teilhandlungen anbieten.
- Harte Blockaden duerfen nicht wie Spielverbote klingen, sondern wie konkrete Weltgrenzen der aktuellen Lage.

### Sprachregeln fuer Fragmentierung und Carry-Over

- Wenn ein Plan nur teilweise ausspielbar ist, muss die KI zwischen `erledigt`, `begonnen`, `unterbrochen` und `offen` lesbar trennen.
- Carry-Over soll fuer den Spieler als greifbarer Zustand erscheinen, nicht als abstraktes Systemflag.
- Wiederaufnahmevorteile sollen sichtbar werden, etwa durch Formulierungen wie `Werkzeug liegt bereits bereit` oder `der Zugang ist noch offen`.

### Sprachregeln fuer Verdichtungswechsel

- Der Einstieg in Verdichtung muss klar markiert werden: Die Situation wird unmittelbarer, Entscheidungen werden kleiner und reagieren jetzt im Minutentakt.
- Die Rueckkehr aus Verdichtung muss ebenfalls klar markiert werden: Die akute Lage ist vorbei, die Restzeit im aktuellen Turn wird sichtbar ausgewiesen.
- Verdichtungswechsel duerfen nicht still passieren; der Spieler muss merken, wann das System von Plan- auf Reaktionslogik umschaltet.

### Verbotene Ausgabemuster

- Keine nackten Kategorien ohne Begruendung, etwa nur `unspielbar` oder `zu lang`.
- Keine technischen Rohdaten ohne spielerische Einordnung.
- Keine versteckte Fragmentierung, bei der Schritte wegfallen, ohne dass der Spieler es vorher oder spaetestens im Resultat sieht.
- Kein stiller Wechsel in oder aus Verdichtung.

### Referenzformulierungen v0.1

- `innerhalb des Rahmens`: `Das passt in den aktuellen Turn. Ich spiele die Schritte in dieser Reihenfolge aus.`
- `knapp drueber`: `Das ist etwas mehr, als in diesen Turn sauber hineinpasst. Ich kann den Plan anspielen, aber die letzten Schritte bleiben wahrscheinlich begonnen oder offen.`
- `deutlich drueber`: `Das passt nicht mehr sauber in den aktuellen Turn. Du kannst den Plan kuerzen oder bestaetigen, dass ich ihn fragmentiert ausspiele.`
- `harte Blockade`: `So kannst du das im Moment nicht tun: Dir fehlt hier das passende Werkzeug. Du koenntest stattdessen zuerst nach geeignetem Material suchen.`
- `Verdichtungsstart`: `Die Lage kippt in unmittelbare Reaktion. Ab jetzt zaehlt jede Minute einzeln.`
- `Verdichtungsende`: `Die akute Lage beruhigt sich. Fuer diesen Turn bleiben noch 18 Minuten planbare Zeit.`

UI-Verankerung des Turn-Feedbacks v0.1
--------------------------------------

### Pflichtflaechen pro abgeschlossenem Turn

- Die Stage-Flaeche zeigt immer das eigentliche Lagebild, die Ausspielung und den Turn-Abschluss in spielbarer Form.
- Eine kompakte Turn-Zusammenfassung zeigt immer sichtbar `erledigt`, `begonnen` oder `unterbrochen`, `offen` und den naechsten Anschluss; sie darf nicht nur im Tiefenlog versteckt sein.
- Budgethinweise, harte Blockaden und Verdichtungswechsel muessen im unmittelbaren Interaktionsbereich erscheinen, also dort, wo der Spieler auch entscheidet oder bestaetigt.
- Carry-Over, Restzeit und Resume-relevante Hinweise muessen zusaetzlich in der Ops-/Statusflaeche lesbar bleiben, damit sie nicht nach dem naechsten Textblock aus dem Blick fallen.

### Zuordnung der Rueckmeldesignale

- Sofortige Weltreaktionen gehoeren primaer in die Stage-Flaeche und sekundär in `world_log`.
- Wahrnehmung, Entscheidungsdruck und persoenliche Folgen der Figur gehoeren primaer in die Stage-Flaeche und sekundär in `pc_log`.
- Offene, begonnene oder unterbrochene Arbeiten muessen sowohl in der Turn-Zusammenfassung als auch in einer stabilen Carry-Over-/Resume-Ansicht erscheinen.
- Verdichtungsstart und Verdichtungsende muessen als gut sichtbare Modusmarker erscheinen; dieselben Marker muessen spaeter auch im Replay wiedererkennbar sein.

### Verbote fuer die Anzeigeebene

- Kein Mindestsignal des Turn-Feedbacks darf ausschliesslich in `world_log`, `pc_log` oder Replay versteckt bleiben.
- Die UI darf `carry_over` nicht nur als abstrakte ID-Liste zeigen; mindestens Zustand und konkreter Wiederaufnahmehinweis muessen sichtbar sein.
- Die Stage-Flaeche darf die eigentliche Konsequenz eines Turns nicht durch reine Techniktexte ersetzen; technische Daten bleiben unterstuetzend, nicht fuehrend.

Referenzdurchlaeufe v0.1
------------------------

Die folgenden Beispiele simulieren die definierte Mechanik als vollstaendige Referenzfaelle. Sie sind kein Lore-Kanon, sondern mechanische Belegfaelle fuer Ablauf, Bewertung, Ausspielung und Rueckmeldung.

### Referenzfall A - Normaler 30-Minuten-Turn ohne Verdichtung

#### Ausgangslage

- Die Figur befindet sich in einem vertrauten Wartungsbereich.
- Ein Ventil in Abschnitt C6 zeigt Druckverlust, aber keine akute Gefahr.
- Werkzeug ist in der Naehe verfuegbar, die Umgebung ist eng und leicht unaufgeraeumt.

#### KI-Lagebild

`Im Wartungsgang C6 hoerst du weiter das unruhige Zischen aus dem linken Leitungsstrang. Das Ventil verliert Druck, aber noch haelt das System. Dein Werkzeugschrank steht am Ende des Gangs, der Zugang zur Leitung ist frei.`

#### Spielerplan

`Ich hole das passende Werkzeug, oeffne die Wartungsklappe, pruefe das Ventil, ziehe die lockere Verbindung nach und teste danach kurz, ob der Druck stabil bleibt.`

#### Zerlegte Handlungsschritte

1. Werkzeug holen
2. Wartungsklappe oeffnen
3. Ventil sichten und Schaden pruefen
4. Verbindung nachziehen
5. kurze Druckprobe

#### Abgeleitete Bewertung

- `Werkzeug holen`: `8 Minuten`
   Modifikator: Umgebung leicht unaufgeraeumt `+2`
   Ergebnis: `10 Minuten`
- `Wartungsklappe oeffnen`: `3 Minuten`
   Ergebnis: `3 Minuten`
- `Ventil pruefen`: `8 Minuten`
   Modifikator: vertrautes Umfeld `-2`
   Ergebnis: `6 Minuten`
- `Verbindung nachziehen`: `10 Minuten`
   Modifikator: passendes Werkzeug verfuegbar `0`
   Ergebnis: `10 Minuten`
- `Druckprobe`: `4 Minuten`
   Ergebnis: `4 Minuten`
- `Uebergangsaufschlag`: `3 Minuten`

Gesamtwert: `36 Minuten`

#### Budgetentscheidung

- Klasse: `knapp drueber`
- Systemausgabe:
   `Das ist etwas mehr, als in diesen Turn sauber hineinpasst. Ich kann den Plan anspielen, aber die letzten Schritte bleiben wahrscheinlich begonnen oder offen.`

#### Spielerentscheidung

- Der Spieler bestaetigt die fragmentierte Ausspielung.

#### Ausspielung

- Werkzeug wird geholt.
- Wartungsklappe wird geoeffnet.
- Das Ventil wird geprueft und die lockere Verbindung identifiziert.
- Die Verbindung wird nachgezogen.
- Fuer die vollstaendige Druckprobe reicht die Restzeit nicht mehr; sie wird begonnen, aber nicht sauber abgeschlossen.

#### Turn-Ergebnis Referenzfall A

- `erledigt`: Werkzeug holen, Wartungsklappe oeffnen, Ventil pruefen, Verbindung nachziehen
- `begonnen`: Druckprobe
- `offen`: keine weiteren Schritte

#### Carry-Over Referenzfall A

- `Druckprobe C6`: begonnen, Leitung offen, Werkzeug liegt bereit, Wiederaufnahme verkuerzt

#### Systemausgabe zum Abschluss

`Du stabilisierst die lockere Verbindung am Ventil, bevor der Turn endet. Fuer die vollstaendige Druckprobe reicht die Zeit nicht mehr ganz; der Zugang ist noch offen und dein Werkzeug liegt bereit.`

#### Mindestfeedback des Turns Referenzfall A

- sichtbar geschafft: Verbindung stabilisiert
- sichtbar offen: Druckprobe nicht abgeschlossen
- unmittelbare Weltreaktion: Zischen nimmt ab, aber die Stabilitaet ist noch nicht bestaetigt
- naechster Anschluss: Druckprobe im Folgeturn sauber zu Ende bringen

### Referenzfall B - Turn mit Verdichtungswechsel

#### Ausgangslage Referenzfall B

- Die Figur spricht in einem engen Gang mit einem angespannten NPC ueber knappe Vorratsausgabe.
- Die Lage ist sozial aufgeladen, aber zunaechst noch planbar.

#### KI-Lagebild Referenzfall B

`Der Versorgungshelfer vor dir wirkt uebernaechtigt und gereizt. Hinter ihm warten zwei weitere Personen, und du merkst, dass jede falsche Formulierung die Stimmung kippen lassen kann.`

#### Spielerplan Referenzfall B

`Ich spreche ihn ruhig an, erklaere die Lage, versuche ihn zu beruhigen und will danach mit ihm die Ausgabe kurz neu ordnen.`

#### Erste Budgetbewertung

- Der Plan ist zunaechst als sozialer Mehrschrittplan lesbar.
- Bevor die volle Minutenrechnung abgeschlossen wird, kippt die Lage durch unmittelbare Gegenreaktion in Verdichtung.

#### Verdichtungsstart

Systemausgabe:
`Die Lage kippt in unmittelbare Reaktion. Ab jetzt zaehlt jede Minute einzeln.`

#### Tick-Folge

Tick 1:
- Wahrnehmung: Der NPC hebt die Stimme und tritt einen halben Schritt naeher.
- Spieleraktion: beschwichtigen
- Reaktion: Er zoegert, bleibt aber angespannt.

Tick 2:
- Wahrnehmung: Eine wartende Person mischt sich ein.
- Spieleraktion: klare Prioritaet setzen
- Reaktion: Die zweite Person weicht verbal zurueck, der NPC bleibt fokusiert.

Tick 3:
- Wahrnehmung: Der unmittelbare Druck sinkt leicht.
- Spieleraktion: konkrete Neuordnung der Ausgabe vorschlagen
- Reaktion: Der NPC nickt knapp und laesst dich ausreden.

Tick 4:
- Wahrnehmung: Keine direkte Eskalation mehr, Lage stabilisiert sich.
- Reaktion: Verdichtungsende wird moeglich.

#### Verdichtungsende

Systemausgabe:
`Die akute Lage beruhigt sich. Fuer diesen Turn bleiben noch 26 Minuten planbare Zeit.`

#### Rueckkehr in den normalen Turn

- Die direkte Reaktionslage ist beendet.
- Der Rest des Turns kann wieder als planbare kurze Organisationshandlung ausgespielt werden.

#### Restliche Ausspielung

- Die Figur ordnet die Ausgabe fuer die naechsten Minuten neu.
- Die wartende Gruppe beruhigt sich vorlaeufig.

#### Turn-Ergebnis Referenzfall B

- `erledigt`: erste Deeskalation, Ausgabe kurz neu geordnet
- `unterbrochen`: keine technische Unterbrechung, aber soziale Spannung bleibt als Folgezustand bestehen
- `offen`: laengerfristige Versorgungsklaerung

#### Carry-Over Referenzfall B

- `Versorgungskonflikt Gang Nord`: offen, soziale Spannung reduziert, Vertrauen des Helfers fragil, weitere Klaerung noetig

#### Mindestfeedback des Turns Referenzfall B

- sichtbar geschafft: akute Eskalation verhindert
- sichtbar offen: Versorgungslage bleibt instabil
- unmittelbare Weltreaktion: Gruppe beruhigt sich, NPC bleibt angespannt
- naechster Anschluss: Konflikt kann im naechsten Turn wieder als normaler Plan oder erneut verdichtet weiterlaufen

### Referenzfall C - Harte Blockade mit vorbereitender Teilhandlung

#### Ausgangslage Referenzfall C

- Die Figur will ein verriegeltes Technikdepot hinter einer Sicherheitstuer oeffnen, um dort einen Spannungsregler auszutauschen.
- Der Zugang ist nicht frei; die Figur hat weder Autorisierung noch das passende Override-Werkzeug.
- In unmittelbarer Naehe befindet sich jedoch ein Aufsichtsposten, an dem ein temporaerer Wartungsschluessel ausgegeben werden koennte.

#### KI-Lagebild Referenzfall C

`Vor dir sitzt die verriegelte Sicherheitstuer zum Technikdepot. Ohne Freigabe oder passenden Override kommst du an den Regler dahinter nicht heran. Zwei Gaenge weiter ist noch der Aufsichtsposten besetzt.`

#### Spielerplan Referenzfall C

`Ich gehe direkt an die Tuer, oeffne das Depot und tausche sofort den Spannungsregler aus.`

#### Blockadebewertung

- Kernschritt `Depot oeffnen` scheitert an `zugangsseitig unmoeglich`.
- Der Folgeeingriff `Spannungsregler austauschen` ist ohne diesen Zugang ebenfalls nicht spielbar.
- `budget_decision`: `unspielbar`
- `hard_block`: `true`

#### Systemausgabe bei Blockade

`So kommst du hier im Moment nicht hinein: Die Sicherheitstuer blockiert den Zugang zum Depot, und dir fehlt die noetige Freigabe oder ein passendes Override-Werkzeug. Du koenntest stattdessen zuerst am Aufsichtsposten einen Wartungsschluessel besorgen oder eine Freigabe erbitten.`

#### Alternativpfad des Spielers

`Dann gehe ich zuerst zum Aufsichtsposten und versuche, fuer die Reparatur einen temporaeren Wartungsschluessel zu bekommen.`

#### Neubewertung des Alternativpfads

- `zum Aufsichtsposten gehen`: `6 Minuten`
- `Lage erklaeren und Freigabe erbitten`: `5 Minuten`
- `Wartungsschluessel uebernehmen und Rueckweg antreten`: `7 Minuten`
- `Uebergangsaufschlag`: `2 Minuten`

Gesamtwert: `20 Minuten`

#### Budgetentscheidung Referenzfall C

- Klasse: `innerhalb_des_rahmens`
- Systemausgabe:
   `Das passt in den aktuellen Turn. Ich spiele zuerst die vorbereitende Freigabe aus; der eigentliche Reglertausch kann danach sauber geplant werden.`

#### Ausspielung Referenzfall C

- Die Figur erreicht den Aufsichtsposten.
- Nach kurzer Begruendung erhaelt sie einen temporaeren Wartungsschluessel.
- Der Schluessel wird fuer den naechsten Zugriff bereitgehalten; der Reglertausch selbst beginnt in diesem Turn noch nicht.

#### Turn-Ergebnis Referenzfall C

- `erledigt`: Aufsichtsposten erreicht, Freigabe erbeten, Wartungsschluessel erhalten
- `begonnen`: keine
- `offen`: Spannungsregler im Technikdepot austauschen

#### Carry-Over Referenzfall C

- `Depotzugang Techniksektor`: offen, Wartungsschluessel fuer den Folgeturn vorhanden, Zugang jetzt prinzipiell vorbereitet
- `Spannungsregler austauschen`: offen, Blockade aufgeloest, eigentliche Reparatur noch nicht begonnen

#### Mindestfeedback des Turns Referenzfall C

- sichtbar geschafft: Die urspruengliche Zugangsblockade ist praktisch aufgeloest.
- sichtbar offen: Der eigentliche Reglertausch steht noch aus.
- unmittelbare Weltreaktion: Der Aufsichtsposten erkennt die Wartung als plausibel an und gibt begrenzte Freigabe.
- naechster Anschluss: Der Folgeturn kann mit vorbereitetem Zugang direkt in die Reparaturplanung gehen.

Konsolidierter Zwischenstand
----------------------------

- Der Spielstart ist jetzt als gefuehrter Uebergang Hub -> Spielhauptmenue -> Erzaehler-KI -> Charaktererstellung oder bestehende Figur festgezogen.
- Der Nutzer ist im Hub Operator, im Spiel aber ausschliesslich Spieler seiner Figur ohne Adminrechte.
- Der Standard-Turn ist jetzt als 30-Minuten-Turn mit Lagebild, Planung, Budgetpruefung, Ausspielung und Aufloesung definiert.
- Die KI soll Zeit aus atomaren Schritten, Grundwerten, Modifikatoren und Sequenzverlust ableiten, statt frei dramatisch zu setzen.
- Die Modifikator-Matrix besitzt jetzt eine feste Prioritaetslogik: erst Blockade, dann Verdichtungsbedarf, dann Minutenrechnung.
- Die Budgetpruefung arbeitet jetzt mit klaren Schwellen fuer innerhalb des Rahmens, knapp drueber, deutlich drueber und unspielbar.
- Offene Arbeiten werden nicht mehr nur narrativ, sondern ueber die Zustaende begonnen, unterbrochen und offen plus konkrete Persistenzfelder getragen.
- Folgen werden in Sofortfolgen und verzoegerte Folgen getrennt.
- Dichte direkte Interaktionen mit NPC koennen ueber definierte Trigger in einen minutennahen Tick-Modus uebergehen und danach in den 30-Minuten-Kontext zurueckgefuehrt werden.
- Harte Blockaden muessen konkret begruendet werden und sollen, wenn moeglich, in vorbereitende Teilhandlungen statt in blosses Scheitern uebersetzt werden.
- Die Spielerausgabe ist jetzt als eigene Regelschicht definiert: Budgethinweise, Fragmentierung, Blockaden und Verdichtungswechsel muessen fuer den Spieler sichtbar, knapp und handlungsleitend formuliert werden.
- Mechanik-Gates sind jetzt als gegebene Prueffaelle formulierbar, Replay und Checkpoint-Grenzen fuer Verdichtung explizit gezogen, und das Turn-Feedback ist auf feste UI-Flaechen statt nur auf Textprinzipien abgebildet.

Moderationsfragen fuer die gemeinsame Festlegung
-----------------------------------------------

Diese Fragen sollen den Spielaufbau gemeinsam festzurren, ohne zu frueh in Einzelimplementierung oder RP-Content abzurutschen. Wir koennen sie nacheinander beantworten und die Ergebnisse anschliessend als feste Zielstruktur in dieser SSOT nachziehen.

### A. Produktkern und Spielversprechen

1. Was soll der Spieler in den ersten 5 bis 10 Minuten konkret erleben: eher Einstieg in einen laufenden Betrieb, eher klares Missionsbriefing oder eher freies Erkunden eines Systems?
2. Soll sich der Sim vor RP-Integration schon wie ein echtes Spiel anfuehlen oder eher wie ein spielnaher Operations-Client mit fruehem Gameplay-Kern?
3. Was ist die kleinste spielbare Einheit: ein einzelner Turn, eine kurze Szene, ein Auftrag, ein Slot oder eine Session?
4. Was ist der eigentliche Kernreiz: Entscheidungen, Textantworten, Systemkontrolle, Ressourcenmanagement, Spannung, Atmosphaere oder Fortschritt?
5. Woran merkt der Spieler nach kurzer Zeit, dass er Fortschritt macht?

### B. Spielerrolle und Perspektive

1. Wer ist der Spieler vor RP-Integration funktional: Operator, Teilnehmer, Spielfigur, Supervisor oder Hybrid?
2. Handelt der Spieler direkt in der Welt oder zunaechst nur ueber Hub, Chat und Systembefehle?
3. Soll es vor RP bereits eine klare Figur/Perspektive geben oder erst spaeter mit RP-Modul?
4. Wie stark soll die Perspektive vermittelt werden: neutral-technisch, halb diegetisch oder bereits stark immersiv?
5. Muss der Spieler zwischen Systemebene und Spielfigur-Ebene sichtbar umschalten?

### C. Start des Spiels

1. Was ist der erste Bildschirm nach App-Start: Hub, Hauptmenue, Fortsetzen, Slot-Auswahl oder Intro?
2. Soll der erste Start direkt in eine aktive Session fuehren oder ueber ein bewusstes Setup?
3. Welche Informationen braucht der Spieler zu Beginn zwingend, und was soll erst spaeter sichtbar werden?
4. Braucht es einen kurzen Guided Start oder darf der Spieler sofort frei bedienen?
5. Soll es vor dem eigentlichen Loop schon einen kleinen Startentscheid geben?

### D. Kernloop und Rhythmus

1. Wie sieht ein kompletter Spielzyklus aus Sicht des Spielers aus?
2. Ist der Loop eher promptbasiert, optionsbasiert oder hybrid?
3. Wie viele sichtbare Schritte soll ein einzelner Turn haben?
4. Soll der Spieler immer zuerst lesen und dann handeln oder parallel Informationen und Aktion sehen?
5. Was beendet einen Turn: Bestaetigung, Antwort des Systems, Zustandsupdate oder expliziter Weiter-Button?

### E. Entscheidungen und Konsequenzen

1. Welche Arten von Entscheidungen soll es vor RP bereits geben?
2. Sollen Konsequenzen sofort sichtbar sein oder erst ueber Logs, Zustandswerte und spaetere Folgen?
3. Wie hart dürfen Fehlentscheidungen sein: Korrekturfrei, weich rueckholbar oder bewusst teuer?
4. Braucht das System schon vor RP ein Gefuehl von Risiko und Unsicherheit?
5. Gibt es vor RP bereits Zustandsverschlechterungen, Blockaden oder Fail-Forward?

### F. Progression und Spielziel

1. Gibt es schon vor RP ein klares Kurzzeitziel pro Session?
2. Gibt es mittelfristige Meta-Fortschritte wie Freischaltungen, neue Ansichten, bessere Datenlage oder mehr Bedienoptionen?
3. Wie sichtbar soll Progression sein: Zahlen, Marker, neue Knoten, neue Menues oder rein gefuehlt?
4. Soll der Spieler auf ein Ende pro Session hinarbeiten oder auf offene Fortsetzung?
5. Wann fuehlt sich eine Session als erfolgreich an?

### G. Informationen, UI und Lesefluss

1. Was ist die primaere Informationsflaeche: Chat, Stage, Statuspanel, Log oder Karte?
2. Was muss immer sichtbar bleiben, auch unter enger Flaeche?
3. Welche Informationen duerfen hinter Panels, Tabs oder Aufklappern verschwinden?
4. Was ist im UI wichtiger: lesbare Atmosphaere, schnelle Bedienung oder klare Systemtransparenz?
5. Soll sich der Spieler eher durch ein Cockpit oder eher durch eine fokussierte Szene bewegen?

### H. Session, Save, Resume, Replay

1. Was soll Fortsetzen genau bedeuten: selben Turn, selben Slot, denselben Checkpoint oder letzte stabile Session?
2. Soll Replay rein technisch sein oder bereits spielerisch nutzbar wirken?
3. Wie sichtbar soll der Unterschied zwischen Live-Zustand, Resume-Anker und Replay-Zustand sein?
4. Duerfen Spieler bewusst in alte Checkpoints zurueckspringen oder nur technisch fortsetzen?
5. Was ist der kleinste stabile Save-Punkt?

### I. Schwierigkeitsgrad, Druck und Fehlerkultur

1. Soll das Spiel vor RP eher stressarm, moderat angespannt oder schon spuerbar druckvoll sein?
2. Gibt es Zeitdruck, Ressourcenknappheit oder nur Entscheidungsdruck?
3. Wie soll das Spiel auf ungueltige oder unklare Eingaben reagieren?
4. Muss der Spieler Fehler verstehen koennen, ohne in technische Sprache zu fallen?
5. Wie oft darf das Spiel den Spieler abbremsen, bevor es frustrierend wird?

### J. RP-Integrationsnaht

1. Was soll sich fuer den Spieler aendern, sobald das RP-Modul spaeter hinzukommt?
2. Welche Teile des jetzigen Spielaufbaus muessen dann stabil bleiben?
3. Was darf mit RP ersetzt oder erweitert werden, ohne den Kernloop zu zerstoeren?
4. Soll RP als neuer Modus, als tieferer Layer oder als inhaltliche Aufladung desselben Loops erscheinen?
5. Welcher Punkt markiert inhaltlich und technisch den saubersten Uebergang?

Umfangreiche Checkliste wichtiger Spielelemente
----------------------------------------------

Die folgende Checkliste ist als Arbeitsraster gedacht. Sie trennt bewusst zwischen Pflichtfragen fuer den Kern und spaeteren Komfort- oder Ausbaupunkten.

### 1. Spielidentitaet

- [ ] Kernfantasie des Spiels in einem Satz festhalten.
- [ ] Primaeres Spielversprechen an den Spieler definieren.
- [ ] Klare Aussage treffen, ob der Pre-RP-Sim bereits Spiel oder vorbereiteter Spielclient ist.
- [ ] Zielgefuehl der ersten Session benennen.
- [ ] Abgrenzung zwischen Sim-Hub, eigentlichem Spiel und spaeterem RP-Inhalt festziehen.

### 2. Spielerrolle

- [ ] Rolle des Spielers eindeutig benennen.
- [ ] Perspektive festlegen: ich bin Figur, ich steuere Figur, ich steuere System oder Hybrid.
- [ ] Sichtbare Inworld-Ebene und sichtbare Systemeebene trennen.
- [ ] Definieren, ob vor RP bereits eine feste Figur oder nur ein funktionaler Blickwinkel existiert.
- [ ] Regeln fuer Perspektivwechsel festlegen.

### 3. Startfluss

- [ ] Ersten Screen nach App-Start definieren.
- [ ] Flow fuer Erststart festlegen.
- [ ] Flow fuer Wiederkehrer festlegen.
- [ ] Klaeren, ob Fortsetzen prominenter ist als Neues Spiel.
- [ ] Session-Auswahl, Slot-Auswahl oder direkter Einstieg priorisieren.
- [ ] Klaren Einstieg ohne Ueberforderung planen.
- [ ] Mindestinformationen zum Spielstart definieren.
- [ ] Optionalen Guided Start oder Tutorial-Impuls festlegen.

### 4. Hauptmenue und Navigation

- [ ] Hauptmenue-Bloecke definieren.
- [ ] Klare Navigation zwischen Hub, Live-Spiel, Replay und Optionen festlegen.
- [ ] Rueckwege aus jedem Bereich bestimmen.
- [ ] Unterbrechen/Fortsetzen/Pause-Verhalten definieren.
- [ ] Sichtbare und versteckte Navigationsebenen trennen.
- [ ] Sicherstellen, dass Navigation nicht mit Spielzustand kollidiert.

### 5. Kernloop

- [ ] Vollstaendigen Spielerzyklus dokumentieren.
- [ ] Trigger eines neuen Turns definieren.
- [ ] Ende eines Turns definieren.
- [ ] UI-Feedback waehrend eines laufenden Turns festlegen.
- [ ] Systemreaktion nach Spielerinput beschreiben.
- [ ] Zustandstransition nach jeder Aktion bestimmen.
- [ ] Minimale Loopdauer und gefuehlten Rhythmus festlegen.
- [ ] Wartezustand und In-Flight-Zustand sichtbar machen.

### 6. Eingabeformen

- [ ] Festlegen, ob Freitext, Buttons, Quick Actions oder Hybrid genutzt werden.
- [ ] Gueltige und ungueltige Eingaben definieren.
- [ ] Verhalten bei leerer, unklarer oder widerspruechlicher Eingabe festlegen.
- [ ] Bestaetigungsmechaniken fuer folgenreiche Aktionen definieren.
- [ ] Mobile/enge Layout-Situation fuer Eingabe mitdenken.

### 7. Informationsarchitektur

- [ ] Primaere Hauptflaeche definieren.
- [ ] Sekundaere Informationsflaechen definieren.
- [ ] Immer sichtbare Informationen benennen.
- [ ] Kontextinformationen benennen, die nur situativ auftauchen.
- [ ] Technische Diagnostik von Spielerinformation sauber trennen.
- [ ] Prioritaetsregeln fuer enge Bildschirmhoehen festlegen.

### 8. Sichtbarer Spielzustand

- [ ] Sichtbare Kernzustandswerte definieren.
- [ ] Unsichtbare interne Zustandswerte definieren.
- [ ] Klaeren, was der Spieler direkt lesen darf.
- [ ] Klaeren, was nur indirekt ueber Folgen sichtbar wird.
- [ ] Definieren, wann Zustandsaenderungen im UI erscheinen.
- [ ] Regellogik fuer Statusindikatoren festlegen.

### 9. Entscheidungen

- [ ] Entscheidungstypen katalogisieren.
- [ ] Entscheidungsdichte pro Turn festlegen.
- [ ] Kurzfristige und mittelfristige Konsequenzen unterscheiden.
- [ ] Risiko und Sicherheit pro Entscheidungsklasse definieren.
- [ ] Fail-Forward-Regeln festlegen.
- [ ] Harte Sackgassen vermeiden oder bewusst markieren.

### 10. Fortschritt und Motivation

- [ ] Kurzfristige Ziele pro Session definieren.
- [ ] Mittelfristige Ziele definieren.
- [ ] Sichtbare Fortschrittsmarker festlegen.
- [ ] Motivationsschleife benennen: Entdecken, Optimieren, Ueberleben, Erzielen, Freischalten.
- [ ] Bedingung definieren, wann sich eine Session gelungen anfuehlt.

### 11. Ressourcen und Drucksysteme

- [ ] Relevante Ressourcen bestimmen.
- [ ] Klaeren, ob Zeit eine echte Ressource ist.
- [ ] Klaeren, ob Aufmerksamkeit, Zugriff oder Optionen begrenzte Ressourcen sind.
- [ ] Regeneration oder Wiederherstellung festlegen.
- [ ] Knappheitssignale im UI definieren.
- [ ] Schwellwerte fuer Warnungen festlegen.

### 12. Risiko, Scheitern und Recovery

- [ ] Arten von Fehlschlaegen definieren.
- [ ] Recovery-Pfade fuer Fehlentscheidungen festlegen.
- [ ] Klaeren, ob ein Turn scheitern kann, ohne die Session zu zerstoeren.
- [ ] Feedbackstil bei Fehlern bestimmen.
- [ ] Technische Fehler von spielinternen Fehlern trennen.
- [ ] Saubere Rueckkehr nach Fehlern planen.

### 13. Sessionstruktur

- [ ] Was eine Session ist, eindeutig definieren.
- [ ] Was ein Slot ist, eindeutig definieren.
- [ ] Was ein Turn ist, eindeutig definieren.
- [ ] Was ein Checkpoint ist, eindeutig definieren.
- [ ] Grenzen zwischen diesen Ebenen im UI klar markieren.
- [ ] Sessionstart, Sessionpause und Sessionende planen.

### 14. Save, Resume und Replay

- [ ] Speicherzeitpunkte definieren.
- [ ] Minimalen stabilen Resume-Anker festlegen.
- [ ] Replay-Zweck definieren: Debug, Nachvollzug, Spielhilfe oder Feature.
- [ ] Unterschiede zwischen Live, Resume und Replay im UI sichtbar machen.
- [ ] Checkpoint-Auswahl regeln.
- [ ] Ruecksprungregeln definieren.
- [ ] Artefaktvertrag sichtbar an Produktlogik anbinden.

### 15. Weltfeedback und Logs

- [ ] Rolle von `world_log` festlegen.
- [ ] Rolle von `pc_log` festlegen.
- [ ] Klaeren, wie viel davon der Spieler direkt sieht.
- [ ] Event-Historie strukturieren.
- [ ] Letzte wichtige Aenderungen hervorheben.
- [ ] Informationsrauschen begrenzen.

### 16. Atmosphaere und Praesentation

- [ ] Gewuenschten Ton des Spiels festlegen.
- [ ] Verhaeltnis zwischen funktionaler UI und Immersion bestimmen.
- [ ] Leselast pro Screen einschaetzen.
- [ ] Dichte von Flavor-Text versus Systemtext festlegen.
- [ ] Audio, Animation oder Statuswechsel als Stimmungstraeger priorisieren.

### 17. UI-Komposition

- [ ] Layout-Hierarchie definieren.
- [ ] Wichtigste Paneele priorisieren.
- [ ] Mindestgroessen kritischer Bereiche festlegen.
- [ ] Verhalten auf kleinen Hoehen und Breiten festlegen.
- [ ] Scrollen, Aufklappen oder Tabben pro Bereich definieren.
- [ ] Overlay-Regeln, Modalfenster und Blocking-Zustaende festlegen.

### 18. Tutorial und Onboarding

- [ ] Entscheiden, ob es ein echtes Tutorial braucht.
- [ ] Fruehe Erklaerungen dosieren.
- [ ] Ersten Pflichtlernmoment definieren.
- [ ] Begriffe wie Session, Slot, Replay, Resume spielerfreundlich erklaeren.
- [ ] Hilfe- und Erklaertexte von Systemdiagnostik trennen.

### 19. Optionen und Komfort

- [ ] Wichtige Settings fuer den Spielstart definieren.
- [ ] Komfortfunktionen wie Texttempo, Fokusmodus oder reduzierte Diagnostik pruefen.
- [ ] Wiederkehrende Nutzerpraeferenzen persistent machen.
- [ ] Klaeren, was im Hub-Prefs-Bereich bleibt und was ins Spielmenue gehoert.

### 20. Technische Robustheit aus Spielsicht

- [ ] Verhalten bei fehlender Runtime definieren.
- [ ] Verhalten bei langsamer Antwort definieren.
- [ ] Verhalten bei partiell fehlenden Daten definieren.
- [ ] Sichtbare Degradationspfade planen.
- [ ] Nutzerfuehrung fuer Retry, Warten und Abbruch festlegen.

### 21. Integrationsgrenze zum RP-Modul

- [ ] Klar definieren, was vor RP stabil stehen muss.
- [ ] Klar definieren, was RP spaeter erstmal liefern darf.
- [ ] Erste RP-Integrationsstelle im Flow bestimmen.
- [ ] Ersetzen versus Erweitern pro Systembereich klaeren.
- [ ] Sicherstellen, dass RP den Sim-Kernloop nicht bricht.

### 22. Gate vor RP-Integration

- [ ] Produktkriterien fuer den Pre-RP-Sim festlegen.
- [ ] Qualitaetskriterien fuer UI und Loop festlegen.
- [ ] Kriterien fuer lesbaren Spielzustand festlegen.
- [ ] Kriterien fuer Save/Resume/Replaysicherheit festlegen.
- [ ] Kriterien fuer Nutzerverstaendnis und Onboarding festlegen.

### 23. Priorisierung fuer den naechsten Planungsschritt

- [ ] Drei absolut unverzichtbare Kernelemente bestimmen.
- [ ] Drei Elemente benennen, die spaeter kommen duerfen.
- [ ] Einen ersten vertikalen Slice des Spielaufbaus definieren.
- [ ] Offene Punkte markieren, die vor Implementierung entschieden werden muessen.
- [ ] Punkte markieren, die bewusst erst mit RP entschieden werden sollen.

Definition of Done (Planung)
----------------------------

- Spielaufbau ist in Phasen mit klarer Integrationsgrenze dokumentiert.
- Sim- und RP-Verantwortungen sind getrennt und explizit benannt.
- Akzeptanzkriterien fuer den Start der RP-Integration sind belegbar festgelegt.
- Ein strukturierter Fragenkatalog liegt vor, mit dem der Spielaufbau gemeinsam beantwortet und konkretisiert werden kann.
- Eine umfangreiche Checkliste deckt die wichtigsten Spielelemente fuer Pre-RP-Sim, Kernloop und RP-Naht ab.
