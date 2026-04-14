---
stand: 2026-04-14 16:27
update: Die SSOT fuehrt jetzt einen strukturierten Fragenkatalog und eine umfangreiche Checkliste zur gemeinsamen Festlegung des Spielaufbaus vor RP-Integration.
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

Quellenbasis
------------

- `novapolis-dev/docs/process/text-rpg-product-gate-v1.ssot.md`
- `novapolis-dev/docs/process/text-rpg-slice-2-handover-v1.ssot.md`
- `novapolis-dev/docs/specs/text-rpg-session-contract-v1.md`
- `novapolis_agent/docs/runbook.md`
- `novapolis-sim/scripts/Main.gd`

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

Offene Planungsfragen
---------------------

- Welcher minimale RP-Adapter-Scope wird im ersten Integrationsschnitt akzeptiert?
- Welche Sim-seitigen KPIs gelten als Gate fuer den Wechsel in den RP-Integrationslauf?
- Welche UI-Hinweise sind fuer User-Fuehrung noetig, wenn RP noch nicht aktiv ist?

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
