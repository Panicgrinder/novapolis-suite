---
stand: 2026-04-18 00:55
update: Das Produktmodell fuehrt jetzt auch die knappe Handover-Formel hinter slot 30 und den gemeinsamen Release-Evidence-Pfad fuer den ersten Vertikalslice.
checks: snapshot-lock PASS (2026-04-18 00:55); markdownlint=PASS; frontmatter=PASS
---

Text-RPG Pre-RP Product Model v1
================================

Zweck
-----

Diese SSOT fuehrt den verbliebenen strategischen Produktkern fuer den Sim-vor-RP-Pfad. Sie sammelt die noch offenen Produktannahmen, einen kompakten Entscheidungsraster und das Arbeitsraster fuer den ersten belastbaren Pre-RP-Spielzustand, ohne erneut Turn-, Start-, Gate- oder UI-Details als Parallelquelle zu duplizieren.

Scope
-----

- Produktkern und Spielversprechen des Pre-RP-Sim-Pfads
- Fortschrittsbild, Konsequenzstil und Fehlertoleranz
- player-facing Lesart von Session, Save, Resume und Replay
- allgemeine Produktlesart der RP-Integrationsnaht ohne UI- oder Adapter-Detailvertrag
- Arbeitsraster fuer noch nicht kanonisierte Produktentscheidungen

Nicht-Ziele
-----------

- kein Ersatz fuer Sessionvertrag, Product Gate, Slice-Handover, Start-Chooser oder Sim-UI-IA
- keine Detailmatrix fuer Zeit, Budget, Verdichtung oder harte Blockaden
- keine neue RP-Lore-, Slot- oder Welt-SSOT
- keine Runtime-Implementierung oder UI-Spezifikation auf Node-Ebene

Wahrheitsrahmen
---------------

- `novapolis-dev/docs/specs/text-rpg-session-contract-v1.md` bleibt Zielquelle fuer Feld-, Zustands-, Save-, Resume- und Replay-Anker.
- `novapolis-dev/docs/process/text-rpg-product-gate-v1.ssot.md` bleibt Zielquelle fuer Gate-, KPI- und Artefaktpflichten.
- `novapolis-dev/docs/process/text-rpg-slice-2-handover-v1.ssot.md` bleibt Zielquelle fuer den gemeinsamen Folgepfad hinter `slot 30`.
- `novapolis-dev/docs/process/rp-start-chooser.ssot.md` und `novapolis-dev/docs/process/rp-text-rpg-startpaket-slot-00-05-2026-04-05.md` bleiben Zielquellen fuer produktiven Neueinstieg und Startanker bei `slot_00`.
- `novapolis-dev/docs/process/sim-ui-menue-ia.ssot.md` bleibt Zielquelle fuer Screen-, Menue- und Rueckwegaufbau.
- `novapolis-dev/docs/process/text-rpg-turn-budget-model-v1.ssot.md` bleibt Zielquelle fuer die ausdifferenzierte Turn-Budget-Mechanik.

Quellenbasis
------------

- `novapolis-dev/docs/specs/text-rpg-session-contract-v1.md`
- `novapolis-dev/docs/process/text-rpg-product-gate-v1.ssot.md`
- `novapolis-dev/docs/process/text-rpg-slice-2-handover-v1.ssot.md`
- `novapolis-dev/docs/process/rp-start-chooser.ssot.md`
- `novapolis-dev/docs/process/rp-text-rpg-startpaket-slot-00-05-2026-04-05.md`
- `novapolis-dev/docs/process/sim-ui-menue-ia.ssot.md`
- `novapolis-dev/docs/process/text-rpg-turn-budget-model-v1.ssot.md`
- `novapolis_agent/docs/runbook.md`

Strategische Leitannahmen
-------------------------

### Fortschrittsbild und Realismusanspruch

- Das Spiel soll als realitaetsnahes RP angelegt sein und Fortschritt primaer ueber Weltreaktion statt ueber gamifizierte Marker vermitteln.
- Der Spieler soll Fortschritt vor allem daran erkennen, wie Welt, Fraktionen, Gruppen und Einzelpersonen auf seine Aktionen reagieren.
- Ein zweiter zentraler Fortschrittsanzeiger liegt in Tages- und Wochenabrechnungen fuer Gueter, Waren und wirtschaftliche Lage im Fraktions- bzw. Gruppenkontext.

### Objektive Einordnung des aktuellen Planungsstands

- Der bisherige Rahmen ist konsistent: Hub und Spiel sind nicht nur andere Screens, sondern unterschiedliche Rollen- und Rechteebenen.
- Die Erzaehler-KI ist als Eintrittsschwelle stark gesetzt; sie braucht spaeter jedoch klare Grenzen, damit sie den Spieler fuehrt, aber nicht System- oder Regelarbeit ueberlagert.
- Die flexible Eingabestruktur ist produktseitig stark, muss spaeter aber auf gleiche Entscheidungsqualitaet und Balancing geprueft werden, damit nicht verschiedene Modi zu unterschiedlichen Spielniveaus fuehren.
- Der realitaetsnahe Fortschrittsanspruch ist fachlich plausibel, erzeugt aber das Risiko, dass Fortschritt kurzfristig zu indirekt wirkt. Fuer den eigentlichen Turn-Ablauf werden daher zusaetzlich lokale, unmittelbar lesbare Rueckmeldesignale noetig sein.

Erster suiteweiter Vertikalslice
--------------------------------

- Kernfantasie des Spiels in einem Satz: Du fuehrst als neu eingesetzte Figur in Novapolis einen kleinen, folgenreichen Einsatzstart und siehst sofort, wie Welt, Gruppen und Lage auf deinen ersten Zug reagieren.
- Primaeres Spielversprechen: In den ersten `5-10` Minuten bekommst du einen klaren Einstieg, mindestens eine bedeutende Entscheidung, sichtbare Konsequenzen und einen stabilen Wiedereinstiegspunkt fuer dieselbe Session.
- Zielgefuehl der ersten Session: Du sollst nach dem ersten Abschnitt das Gefuehl haben, die Lage verstanden, eine erste Position bezogen und einen belastbaren Anker fuer die Fortsetzung erreicht zu haben.
- Der erste suiteweite Vertikalslice fuehrt verbindlich ueber `Hub -> Spielhauptmenue -> Charakterstart -> erster Vollturn -> turn_resume_ready`.
- Sichtbare Fortschrittssignale im ersten Slice sind ein lesbarer Szenenwechsel, eine sichtbare Welt- oder Gruppenreaktion und ein klar benannter naechster Anschluss im selben Lauf.
- Der kleinste stabile Save-Punkt ist das erste `turn_resume_ready` nach einem voll ausgespielten ersten Turn; davor gibt es keinen versprochenen Resume-Anker.
- Replay-Zweck bleibt Nachvollzug und Wiedereinstiegshilfe fuer denselben Lauf und nicht ein paralleler Fortschrittspfad, kein Ersatz fuer Live-Spiel und kein eigenes Feature-Ziel.

Priorisierung fuer diesen Schnitt
---------------------------------

- Drei unverzichtbare Kernelemente: KI-gestuetzter Charakterstart im Spielhauptmenue, sichtbarer erster Vollturn mit `Szene/Konsequenz/Optionen/State_Patches`, Save-/Resume-/Replay-Bruecke ab dem ersten `turn_resume_ready`.
- Drei bewusst spaetere Elemente: breitere Startauswahl und mehr Hintergruende, aktive RP-Integration hinter `slot 30`, Komfort-/Atmosphaereausbau wie TTS-Polish, Audio-Breite und zusaetzliche Sim-Atmosphaere.

Gezielt offene Restfragen
-------------------------

| Restfrage | Aktueller Zuschnitt | Zielquelle fuer Entscheidung |
| --- | --- | --- |
| Wie hart darf Fail-Forward bei blockierten oder deutlich ueberzogenen Plaenen formuliert werden? | Geklaert: `teilmoeglich` fuer anspielbare Fragmentierung, `verschoben` fuer deutlich ueberzogene Zielplaene mit Vorarbeit oder Aufteilung und `blockiert` fuer reale Kernblockaden mit vorbereitender Alternative. | `novapolis-dev/docs/process/text-rpg-turn-budget-model-v1.ssot.md` |
| Welche Knappheits- und Warnsignale muessen im Hub sichtbar werden, bevor voller Komfortausbau beginnt? | Geklaert: `stille Hintergrundlage`, `Knappheit`, `Warnung` und `Ueberzug` bilden die kanonische Viererlesart fuer den ersten Vertikalslice. | `novapolis-dev/docs/process/sim-ui-menue-ia.ssot.md` |
| Welche kurze Produktformel beschreibt den ersten aktiven Wechsel vom Pre-RP-Pfad in den RP-Folgeblock hinter `slot 30`? | Geklaert: `Weiter im selben Lauf: offener Druck, offene Aufgaben, klarer naechster Zug.` bleibt die knappe player-facing Formel fuer denselben Handover und denselben Resume-Anker. | `novapolis-dev/docs/process/text-rpg-slice-2-handover-v1.ssot.md` und `novapolis-dev/docs/process/rp-folgekorridor-slot-31-35.ssot.md` |

Entscheidungsraster fuer den verbleibenden Produktrest
-----------------------------------------------------

Der verbleibende Produktrest wird hier nicht mehr als lange Fragenliste gefuehrt, sondern als kompakter Raster. Jede offene Formulierungsarbeit soll von hier aus in die passende Zielquelle nachgezogen werden und nicht als neue Sammelbeschreibung stehen bleiben.

| Raster | Bereits fest | Verbleibende Formulierungsarbeit | Zielquelle fuer Nachzug |
| --- | --- | --- | --- |
| Produktkern und Spielversprechen | Der Pre-RP-Pfad bleibt spielnaher Operations-Client mit fruehem Gameplay-Kern; Fortschritt soll primaer ueber Weltreaktion und second-level ueber wirtschaftliche Lage lesbar sein. | Die Endform fuer Kernfantasie, Spielversprechen und Sessionziel ist unten festgezogen; spaeter folgt bei Bedarf nur noch die Gate-kurze Verdichtung. | Diese Datei, spaeter Produkt Gate bei Gate-Relevanz |
| Entscheidungen und Konsequenzen | Turn-Antworten, Konsequenzen, Patch-Hinweise und sichtbare Rueckmeldesignale sind als Produktmuster gesetzt; harte Dead Ends sollen vermieden werden. | Die Recovery-Sprache ist jetzt festgezogen; offen bleibt hier spaeter nur noch eine knappe Gate-Verdichtung derselben Begriffe. | Diese Datei, spaeter Turn-Budget-Modell oder Product Gate je nach Vertragsnaehe |
| Ressourcen und Drucksysteme | Wirtschaftliche Lage, Risiko und Turn-Rueckmeldung sollen nicht nur im SSOT-Hintergrund stehen, sondern im ersten Slice direkt sichtbar bleiben. | Die Viererlesart fuer `stille Hintergrundlage`, `Knappheit`, `Warnung` und `Ueberzug` ist jetzt festgezogen; spaeter folgt bei Bedarf nur noch eine UI-nahe Verdichtung fuer konkrete Styles oder Widgets. | Diese Datei, Sim-UI-IA, spaeter Sim-Pfad |
| Session, Save, Resume, Replay | Live-, Resume- und Replay-Unterschiede sind als UI-Lesart gebunden; Resume-Anker und Handover laufen ueber denselben Sessionvertrag. | Der kleinste stabile Save-Punkt ist jetzt das erste `turn_resume_ready` nach dem ersten Vollturn; Replay bleibt Nachvollzug und Wiedereinstiegshilfe fuer denselben Lauf. | Session Contract, UI-IA, Product Gate |
| RP-Integrationsnaht | Der erste Anschluss liegt hinter `slot 30`; minimaler RP-Adapter-Scope und UI-Hinweise ohne aktive RP-Integration sind bereits ausgelagert. | Die knappe player-facing Produktformel ist jetzt festgezogen; spaeter folgt nur noch eine Oberflaechenverdichtung derselben Sprache in Gate- oder UI-Texten. | Slice-2-Handover, spaeter RP-Produktpfad |

Kanonische Handover-Formel hinter `slot 30`
-------------------------------------------

- Die knappe player-facing Formel fuer den ersten aktiven Anschluss hinter `slot 30` lautet verbindlich: `Weiter im selben Lauf: offener Druck, offene Aufgaben, klarer naechster Zug.`
- `Weiter im selben Lauf` bindet den Anschluss an denselben Session-, Save-, Resume- und Replay-Rahmen statt an einen neuen Produktpfad.
- `offener Druck` markiert den fortgesetzten Lage-, Risiko- oder Reichweitendruck aus dem Pre-RP-Slice, ohne einen zweiten Warnbegriff neben der bereits gesetzten Warnsignal-Matrix zu eroeffnen.
- `offene Aufgaben` macht den Carry-Over aus begonnenen, unterbrochenen oder offenen Arbeiten lesbar.
- `klarer naechster Zug` verpflichtet den Handover auf einen konkreten Anschluss statt auf ein loses Episodenversprechen.
- Dieselbe Kurzformel bleibt absichtlich knapp genug fuer Produktmodell, Handover-SSOT, RP-Folgekorridor, Product Gate, Runbook und Workspace-Status.

Release-Evidence-Pfad fuer den ersten Vertikalslice
--------------------------------------------------

- Der suiteweite Freigabepfad fuer den ersten Vertikalslice haengt jetzt an `novapolis-dev/docs/process/text-rpg-release-evidence-bundle-v1.ssot.md`.
- Die Produktlesart bleibt: `Checks: full` deckt die repoweite Baseline ab, `Checks: text-rpg product gate` deckt den eigentlichen Slice-Vertrag ab, die deterministischen Referenzfaelle belegen denselben Artefaktpfad, und der Sim-Export-Smoke belegt den produktiven Windows-Start ausserhalb des Editors.
- Release-reif ist derselbe Slice erst dann, wenn auch lokale Modellruntime fuer den `gm_session`-Gate-Teil und der exportierte Sim-Smoke fuer `novapolis-sim/exports/windows/NovapolisSim.exe` belastbar vorliegen.

Kanonische Recovery-Lesart
--------------------------

- `teilmoeglich` ist die verbindliche Produktlesart fuer einen Turn, der denselben Plan sichtbar anspielt, aber nicht vollstaendig abschliesst. Der Spieler sieht, was geschafft ist, was offen bleibt und worauf der naechste Schritt aufsetzt.
- `verschoben` ist die verbindliche Produktlesart fuer einen deutlich ueberzogenen Plan. Die Rueckmeldung verlegt den Zielplan nicht still nach hinten, sondern macht sichtbar, dass jetzt nur Vorarbeit, ein engerer Teilschritt oder eine bewusst bestaetigte Aufteilung in Frage kommt.
- `blockiert` ist die verbindliche Produktlesart fuer reale Kernblockaden. Die Rueckmeldung benennt die Blockade klar und fuehrt direkt in einen vorbereitenden Alternativschritt statt in einen toten Endpunkt.
- Der Pre-RP-Pfad vermeidet damit harte Dead Ends als Standardform: Scheitern darf Tempo, Reichweite, Sicherheit oder Spielraum kosten, soll aber moeglichst in einen lesbaren Anschluss uebergehen.

Kanonische Warnsignal-Matrix
---------------------------

- `stille Hintergrundlage` ist die ruhige, fortlaufende Lesart fuer Welt-, Wirtschafts- und Betriebszustand ohne unmittelbaren Eingriffsdruck. Sie haelt den Spieler ueber Richtung und Grundton informiert, ohne den laufenden Turn zu unterbrechen.
- `Knappheit` signalisiert eine begrenzte Ressource oder einen enger werdenden Spielraum, der noch beherrschbar ist, aber nicht mehr ignoriert werden sollte. Die Rueckmeldung nennt knapp, was knapp wird und welcher naechste Schritt die Lage stabilisieren kann.
- `Warnung` signalisiert nahen negativen Druck auf Sicherheit, Lage oder Anschlussfaehigkeit. Die Rueckmeldung macht sichtbar, welche unmittelbare Folge droht, wenn der Spieler den Punkt weiter laufen laesst.
- `Ueberzug` signalisiert, dass der aktuelle Plan nicht mehr sauber in den Turn-Rahmen passt. Die Rueckmeldung bleibt an die Recovery-Lesart gebunden und fuehrt in `teilmoeglich` oder `verschoben`, statt ein paralleles Warnsystem zu eroeffnen.
- Die Viererlesart ist absichtlich knapp: `stille Hintergrundlage` fuer Grundton, `Knappheit` fuer enger werdende Mittel, `Warnung` fuer akuten Handlungsdruck, `Ueberzug` fuer turnbezogene Planueberdehnung.
- Fuer den ersten Vertikalslice muessen diese Signale mindestens wirtschaftliche Lage, Sicherheitsdruck, Anschlussrisiko und Turn-Passung lesbar machen; Komfort- oder Atmosphaerehinweise gehoeren nicht in diese Pflichtmatrix.

Arbeitsraster
-------------

Die folgende Checkliste bleibt als Arbeitsraster fuer den noch nicht uebernommenen Rest bestehen. Bereits abgehakte Punkte sind in dieser Datei oder in den benannten Zielquellen kanonisiert.

### 1. Spielidentitaet

- [x] Kernfantasie des Spiels in einem Satz festhalten.
- [x] Primaeres Spielversprechen an den Spieler definieren.
- [x] Zielgefuehl der ersten Session benennen.

### 2. Entscheidungen und Konsequenzen

- [ ] Entscheidungstypen katalogisieren.
- [ ] Kurzfristige und mittelfristige Konsequenzen unterscheiden.
- [x] Fail-Forward-Regeln festlegen.
- [x] Harte Sackgassen vermeiden oder bewusst markieren.

### 3. Fortschritt und Motivation

- [x] Kurzfristige Ziele pro Session definieren.
- [ ] Mittelfristige Ziele definieren.
- [x] Sichtbare Fortschrittsmarker festlegen.
- [x] Bedingung definieren, wann sich eine Session gelungen anfuehlt.

### 4. Ressourcen und Drucksysteme

- [ ] Relevante Ressourcen bestimmen.
- [ ] Klaeren, ob Zeit eine echte Ressource ist.
- [x] Knappheitssignale im UI definieren.
- [x] Schwellwerte fuer Warnungen festlegen.

### 5. Risiko, Scheitern und Recovery

- [x] Arten von Fehlschlaegen definieren.
- [x] Recovery-Pfade fuer Fehlentscheidungen festlegen.
- [x] Feedbackstil bei Fehlern bestimmen.
- [ ] Saubere Rueckkehr nach Fehlern planen.

### 6. Sessionstruktur

- [ ] Was eine Session ist, eindeutig definieren.
- [ ] Was ein Slot ist, eindeutig definieren.
- [ ] Was ein Turn ist, eindeutig definieren.
- [ ] Was ein Checkpoint ist, eindeutig definieren.

### 7. Save, Resume und Replay

- [x] Speicherzeitpunkte definieren.
- [x] Minimalen stabilen Resume-Anker festlegen.
- [x] Replay-Zweck definieren: Debug, Nachvollzug, Spielhilfe oder Feature.
- [x] Unterschiede zwischen Live, Resume und Replay im UI sichtbar machen.

### 8. Integrationsgrenze zum RP-Modul

- [x] Klar definieren, was vor RP stabil stehen muss.
- [x] Klar definieren, was RP spaeter erstmal liefern darf.
- [x] Erste RP-Integrationsstelle im Flow bestimmen.
- [ ] Sicherstellen, dass RP den Sim-Kernloop nicht bricht.

### 9. Gate vor RP-Integration

- [x] Produktkriterien fuer den Pre-RP-Sim festlegen.
- [ ] Qualitaetskriterien fuer UI und Loop festlegen.
- [x] Kriterien fuer lesbaren Spielzustand festlegen.
- [x] Kriterien fuer Save/Resume/Replaysicherheit festlegen.

### 10. Priorisierung fuer den naechsten Planungsschritt

- [x] Drei absolut unverzichtbare Kernelemente bestimmen.
- [x] Drei Elemente benennen, die spaeter kommen duerfen.
- [x] Einen ersten vertikalen Slice des verbleibenden Spielaufbaus definieren.
- [x] Offene Punkte markieren, die vor Implementierung entschieden werden muessen.

Definition of Done
------------------

- Der strategische Produktrest des Sim-vor-RP-Pfads liegt nicht mehr nur in der alten Sim-Planungs-SSOT, sondern in einer eigenen aktiven Prozessquelle.
- Produktannahmen, Entscheidungsraster und Arbeitsraster sind klar von Sessionvertrag, Product Gate, Startpfad, Handover, UI-IA und Turn-Budget-Modell getrennt.
- UI-Hinweise fuer den Zustand ohne aktives RP liegen jetzt in `sim-ui-menue-ia.ssot.md`; der minimale RP-Adapter-Scope liegt jetzt in `text-rpg-slice-2-handover-v1.ssot.md`.
- Kuenftige Entscheidungen aus diesem Rest lassen sich direkt in ihre Zielquellen nachziehen, ohne die alte Sammel-SSOT erneut anwachsen zu lassen.