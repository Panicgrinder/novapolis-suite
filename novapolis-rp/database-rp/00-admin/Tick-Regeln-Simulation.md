---
stand: 2026-02-22 00:17
update: Dual-Log-Standard (world_log/pc_log), Sichtbarkeitsfelder und Übergaberegeln für 24x1h global ergänzt.
checks: "npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-02-22 00:09); .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py 'novapolis-dev/docs/todo.rp.md' 'novapolis-dev/docs/donelog.md' 'novapolis-rp/database-rp/00-admin' 'novapolis-rp/database-rp/01-factions/novapolis/05-projects' 'novapolis-rp/database-rp/01-factions/haendlerbund/05-projects' 'novapolis-rp/database-rp/01-factions/eisenkonklave/05-projects' 'novapolis-rp/database-rp/01-factions/arkologie-a1/05-projects' 'novapolis-rp/database-rp/01-factions/schienenbund/05-projects' 'novapolis-rp/database-rp/01-factions/schattenbund/05-projects' 'novapolis-rp/database-rp/01-factions/fluesterkollektiv/05-projects' PASS (EXITCODE=0, 2026-02-22 00:09)"
slug: tick-regeln-simulation
category: Admin
schemaVersion: 1
language: de
status: active
owners: [admin-novapolis]
tags: [rp, rules, simulation, tick]
relatedSlugs: [index-rules, process-workflow, sim-state-schema]
---

Tick-Regeln & Simulation
========================

Grundtakt
---------
- Das RP läuft strikt rundenbasiert in Ticks von exakt 1 Stunde.
- Ein Tag umfasst genau 24 Ticks.
- `tick_of_day` ist die Tick-Nummer innerhalb des Tages und wird immer von 1 bis 24 gezählt.
- `tick_global` ist die fortlaufende Tick-Nummer ab Kampagnenstart und wird ohne Reset hochgezählt.
- Jeder Tick wird in fester Phasenreihenfolge verarbeitet; Abweichungen sind unzulässig.

Phasen pro Tick (verbindlich)
-----------------------------

### 1) Planungsphase (Spieler, außerhalb der Weltzeit)
Der Spieler beschreibt ausschließlich die beabsichtigte Handlung des eigenen Charakters für die kommende Stunde. Mindestangaben sind verpflichtend:
- Ziel/Absicht
- Ort
- Vorgehen/Mittel
- Priorität
- erwartete Dauer (1 Tick oder mehrere)
- Risiko-/Gewaltfreigabe (`vermeiden` | `notfalls` | `aggressiv`)
- Ressourcenfreigabe (erlaubte Ressourcen oder `keine`)
- Stop-Condition (bei Dauer > 1 Tick verpflichtend)
- Kommunikationsabsicht (wen kontaktieren, über welchen Kanal)

Optional:
- Erfolgsdefinition, wenn für die Auflösung sinnvoll.

### 2) Zugphase (Spieler, In-Character)
- Der Spieler beschreibt konkrete Handlung und Kommunikation in der Welt.
- NPCs dürfen nicht direkt gesteuert werden.
- Aufgaben an NPCs sind nur über IC-Kommunikation zulässig.
- Eine NPC-Aufgabe gilt erst als gültig, wenn alle vier Bedingungen erfüllt sind:
  1. Kontakt ist plausibel hergestellt.
  2. Botschaft ist verständlich übermittelt.
  3. NPC ist zuständig.
  4. NPC entscheidet: angenommen / abgelehnt / vertagt.
- Entscheidung und Kurzbegründung müssen im Tick-Report erscheinen.

### 3) Simulation (KI, kausal, pending bis Commit)
**Start-of-Tick-Maintenance**
- Fortführung laufender Tasks/Progress
- Prüfung von Timern/Countdowns
- Ggf. Zustandsprüfungen ohne Statusänderung
- In der Start-of-Tick-Maintenance dürfen keine Statuswerte verändert werden.

**Decay-Regel (eindeutig)**
- Status-Decay (z. B. Hunger, Erschöpfung) wird exakt einmal pro Tick angewendet.
- Decay wird ausschließlich in Phase (d) Ressourcenbilanz berechnet, nicht in der Start-of-Tick-Maintenance.

**Verarbeitungsreihenfolge (hart)**
a) Direkte Konsequenzen/Proben/Konflikte aus der SC-Handlung  
b) NPC-Handlungen nach Zielen/Wissen sowie Beobachtungen/Kommunikation  
c) Fraktionszüge (inkl. Spielerfraktion nur über Strukturen/NPCs)  
d) Ressourcenbilanz (Verbrauch, Produktion, Statusänderungen inkl. einmaligem Decay)  
e) Warenfluss/Logistik/Handel  
f) Beziehungen/Reputation  
g) World-State-Update

**End-of-Tick-Commit**
- Alle Änderungen sind bis einschließlich Phase (f) nur `pending`.
- Der Zustand wird erst nach Abschluss von (g) verbindlich (`committed`).

Langdauernde Handlungen & Fast-Forward
--------------------------------------
- Langdauernde Handlungen dürfen mehrere Ticks umfassen und werden tickweise fortgeschrieben.
- Plausible Unterbrechungen sind jederzeit möglich.
- Fast-Forward ist bei monotonen Langläufern erlaubt:
  - intern muss weiterhin tickweise simuliert werden,
  - nach außen darf gebündelt berichtet werden.
- Jeder Abbruch/Abschluss muss auf exakten `tick_of_day`, exakten `tick_global` und Uhrzeit referenzieren.
- Bei Abbruch wird der Rest des aktuellen Ticks normal ausgespielt (nicht weiter gebündelt).
- Optionale Default-Fallback-Handlung kann vom Spieler vorab festgelegt werden.
- Ohne Fallback wählt die KI eine konservative, charakterkonforme Minimalreaktion.

Unterbrechungs-Trigger (Priorität, verbindlich)
-----------------------------------------------
1. Lebensgefahr / akuter Konflikt  
2. Spielerdefinierte Stop-Conditions  
3. Kommunikationsereignisse (nur bei plausiblen Kommunikationsmitteln/Kanalverfügbarkeit)  
4. Ziel erreicht / Ziel gescheitert / Material fehlt / Weg blockiert  
5. Relevante Zustandsänderungen

- Alle Trigger werden pro internem Tick geprüft.
- Spielerdefinierte Stop-Conditions werden immer zusätzlich geprüft und beenden Fast-Forward sofort bei Eintritt.

Parallelität & Wissensweitergabe
--------------------------------
- „Gleichzeitigkeit“ innerhalb einer Stunde wird durch die feste Phasenreihenfolge modelliert.
- Spätere Phasen dürfen nur auf Informationen reagieren, die bis dahin plausibel wahrgenommen oder kommuniziert wurden.
- Keine implizite Allwissenheit, keine sofortige globale Informationsverteilung.

Informationsgrenzen (Anti-Spoiler)
----------------------------------
- Ausgabe wird strikt getrennt in:
  - IC-Wissen sicher
  - Beobachtung/Hinweise (unsicher)
  - Unbekannt bleibt unbekannt
- Interne Simulation darf allwissend rechnen, die Ausgabe darf dieses Wissen nicht unzulässig offenlegen.
- Bei Fast-Forward werden nur Ereignisse berichtet, die den SC erreichen/auffallen oder später als Spuren plausibel sichtbar sind.

Dual-Log-Standard (24x1h, global)
---------------------------------
- Pro Tick werden zwei Log-Ebenen geführt:
  - `world_log`: vollständige Weltwahrheit (intern, vollständig).
  - `pc_log`: nur für den Spielercharakter sichtbare/zugängliche Informationen.
- Pflichtfelder je Log-Eintrag: `scope`, `channel`, `source`, `confidence`, `freshness`.
- Zulässige `scope`-Werte: `private`, `allies_only`, `pc`, `public`, optional `redacted`.
- Sichtbarkeitsregel: Eintrag erscheint nur im `pc_log`, wenn Scope/Empfänger/Kanal plausibel sind.
- Rückblenden sind erlaubt als Sichtbarkeitsänderung (`allies_only`/`hidden` -> `pc`), nicht als Retcon der Weltwahrheit.
- Der globale Standard bleibt fraktionsneutral; konkrete Inhalte liegen in den Fraktions-Templates unter `01-factions/*/05-projects/`.

Optionales Modul Wetter/Anomalien
---------------------------------
- Wetter/Anomalien werden nur genutzt, wenn das Setting dieses Modul aktiv führt.
- Wenn nicht aktiv, wird das Modul explizit ausgelassen.

Reporting-Template pro Tick (verbindlich, knapp)
-------------------------------------------------
- Zeit (Datum + Uhrzeit), `tick_of_day`, `tick_global`
- Ort/Lage in 1 Satz
- SC-Handlung → Outcome (Probe/Konflikt nur wenn nötig)
- Relevante NPC-/Fraktions-/Logistik-Änderungen (nur Wichtiges)
- Snapshot: Ressourcen/Status + offene Entscheidungen (2–5 Punkte)
- NPC-Aufgabenstatus: angenommen / abgelehnt / vertagt (mit Kurzbegründung)

Completeness-Checkliste
-----------------------
- [x] Grundtakt
- [x] Phasen 1–3
- [x] Start-of-Tick-Maintenance
- [x] Decay-Regel (einmal pro Tick, nur in (d))
- [x] Pending/Commit
- [x] Langdauernd & Fast-Forward
- [x] Trigger-Priorität
- [x] Parallelität/Wissensweitergabe
- [x] Informationsgrenzen
- [x] Optionalmodul Wetter/Anomalien (nur wenn aktiv)
- [x] Reporting-Template inkl. `tick_of_day` und `tick_global`