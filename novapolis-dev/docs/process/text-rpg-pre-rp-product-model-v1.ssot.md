---
stand: 2026-04-17 01:04
update: Das Produktmodell nennt den frueheren Redirect nicht mehr explizit und verweist nur noch direkt auf aktive Zielquellen.
checks: snapshot-lock PASS (2026-04-17 01:04); markdownlint=PASS; frontmatter=PASS
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

Entscheidungsraster fuer den verbleibenden Produktrest
-----------------------------------------------------

Der verbleibende Produktrest wird hier nicht mehr als lange Fragenliste gefuehrt, sondern als kompakter Raster. Jede offene Formulierungsarbeit soll von hier aus in die passende Zielquelle nachgezogen werden und nicht als neue Sammelbeschreibung stehen bleiben.

| Raster | Bereits fest | Verbleibende Formulierungsarbeit | Zielquelle fuer Nachzug |
| --- | --- | --- | --- |
| Produktkern und Spielversprechen | Der Pre-RP-Pfad bleibt spielnaher Operations-Client mit fruehem Gameplay-Kern; Fortschritt soll primaer ueber Weltreaktion und second-level ueber wirtschaftliche Lage lesbar sein. | Die erste 5-bis-10-Minuten-Spielerfahrung und das primaere Spielversprechen noch in eine knappe Endform bringen. | Diese Datei, spaeter Produkt Gate bei Gate-Relevanz |
| Entscheidungen und Konsequenzen | Turn-Antworten, Konsequenzen, Patch-Hinweise und sichtbare Rueckmeldesignale sind als Produktmuster gesetzt; harte Dead Ends sollen vermieden werden. | Entscheidungstypen, Fail-Forward-Haerte und Recovery-Sprache noch enger benennen. | Diese Datei, spaeter Turn-Budget-Modell oder Product Gate je nach Vertragsnaehe |
| Session, Save, Resume, Replay | Live-, Resume- und Replay-Unterschiede sind als UI-Lesart gebunden; Resume-Anker und Handover laufen ueber denselben Sessionvertrag. | Kleinsten stabilen Save-Punkt und player-facing Replay-Zweck noch knapp ausformulieren. | Session Contract, UI-IA, Slice-2-Handover |
| RP-Integrationsnaht | Der erste Anschluss liegt hinter `slot 30`; minimaler RP-Adapter-Scope und UI-Hinweise ohne aktive RP-Integration sind bereits ausgelagert. | Die spielerseitige Lesart des Wechsels von Pre-RP zu aktivem RP noch in eine kurze Produktformel verdichten. | Slice-2-Handover, spaeter RP-Produktpfad |

Arbeitsraster
-------------

Die folgende Checkliste bleibt als Arbeitsraster fuer den noch nicht uebernommenen Rest bestehen.

### 1. Spielidentitaet

- [ ] Kernfantasie des Spiels in einem Satz festhalten.
- [ ] Primaeres Spielversprechen an den Spieler definieren.
- [ ] Zielgefuehl der ersten Session benennen.

### 2. Entscheidungen und Konsequenzen

- [ ] Entscheidungstypen katalogisieren.
- [ ] Kurzfristige und mittelfristige Konsequenzen unterscheiden.
- [ ] Fail-Forward-Regeln festlegen.
- [ ] Harte Sackgassen vermeiden oder bewusst markieren.

### 3. Fortschritt und Motivation

- [ ] Kurzfristige Ziele pro Session definieren.
- [ ] Mittelfristige Ziele definieren.
- [ ] Sichtbare Fortschrittsmarker festlegen.
- [ ] Bedingung definieren, wann sich eine Session gelungen anfuehlt.

### 4. Ressourcen und Drucksysteme

- [ ] Relevante Ressourcen bestimmen.
- [ ] Klaeren, ob Zeit eine echte Ressource ist.
- [ ] Knappheitssignale im UI definieren.
- [ ] Schwellwerte fuer Warnungen festlegen.

### 5. Risiko, Scheitern und Recovery

- [ ] Arten von Fehlschlaegen definieren.
- [ ] Recovery-Pfade fuer Fehlentscheidungen festlegen.
- [ ] Feedbackstil bei Fehlern bestimmen.
- [ ] Saubere Rueckkehr nach Fehlern planen.

### 6. Sessionstruktur

- [ ] Was eine Session ist, eindeutig definieren.
- [ ] Was ein Slot ist, eindeutig definieren.
- [ ] Was ein Turn ist, eindeutig definieren.
- [ ] Was ein Checkpoint ist, eindeutig definieren.

### 7. Save, Resume und Replay

- [ ] Speicherzeitpunkte definieren.
- [ ] Minimalen stabilen Resume-Anker festlegen.
- [ ] Replay-Zweck definieren: Debug, Nachvollzug, Spielhilfe oder Feature.
- [x] Unterschiede zwischen Live, Resume und Replay im UI sichtbar machen.

### 8. Integrationsgrenze zum RP-Modul

- [ ] Klar definieren, was vor RP stabil stehen muss.
- [x] Klar definieren, was RP spaeter erstmal liefern darf.
- [x] Erste RP-Integrationsstelle im Flow bestimmen.
- [ ] Sicherstellen, dass RP den Sim-Kernloop nicht bricht.

### 9. Gate vor RP-Integration

- [ ] Produktkriterien fuer den Pre-RP-Sim festlegen.
- [ ] Qualitaetskriterien fuer UI und Loop festlegen.
- [ ] Kriterien fuer lesbaren Spielzustand festlegen.
- [ ] Kriterien fuer Save/Resume/Replaysicherheit festlegen.

### 10. Priorisierung fuer den naechsten Planungsschritt

- [ ] Drei absolut unverzichtbare Kernelemente bestimmen.
- [ ] Drei Elemente benennen, die spaeter kommen duerfen.
- [ ] Einen ersten vertikalen Slice des verbleibenden Spielaufbaus definieren.
- [ ] Offene Punkte markieren, die vor Implementierung entschieden werden muessen.

Definition of Done
------------------

- Der strategische Produktrest des Sim-vor-RP-Pfads liegt nicht mehr nur in der alten Sim-Planungs-SSOT, sondern in einer eigenen aktiven Prozessquelle.
- Produktannahmen, Entscheidungsraster und Arbeitsraster sind klar von Sessionvertrag, Product Gate, Startpfad, Handover, UI-IA und Turn-Budget-Modell getrennt.
- UI-Hinweise fuer den Zustand ohne aktives RP liegen jetzt in `sim-ui-menue-ia.ssot.md`; der minimale RP-Adapter-Scope liegt jetzt in `text-rpg-slice-2-handover-v1.ssot.md`.
- Kuenftige Entscheidungen aus diesem Rest lassen sich direkt in ihre Zielquellen nachziehen, ohne die alte Sammel-SSOT erneut anwachsen zu lassen.