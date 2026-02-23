---
stand: 2026-02-23 03:01
update: Frische-Review durchgeführt; globale Mechanik-Regeln und Verweise geprüft (kein Kanon-Delta).
slug: reference-campaign-state
category: Admin
canvas: campaign-state
schemaVersion: 1
language: de
owners: [admin-novapolis]
tags: [rp, campaign, state, mechanics]
status: active
relatedSlugs: [current-state, memory-bundle, canvas-t0-timeline]
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/00-admin/Reference-Campaign-State.md' 'novapolis-rp/database-rp/00-admin/Canvas-T0-Timeline.md' 'novapolis-rp/database-rp/00-admin/Migrationsplan-Admin-Novapolis.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-23 03:02); .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py 'novapolis-rp/database-rp/00-admin/Reference-Campaign-State.md' 'novapolis-rp/database-rp/00-admin/Canvas-T0-Timeline.md' 'novapolis-rp/database-rp/00-admin/Migrationsplan-Admin-Novapolis.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-23 03:02); npm --prefix novapolis-rp/coding/tools/validators run validate:rp PASS (2026-02-23 03:02)
validators:
  - id: rp
    cmd: 'npm --prefix novapolis-rp\coding\tools\validators run validate:rp'
  - id: crossrefs
    cmd: 'npm --prefix novapolis-rp\coding\tools\validators run validate:crossrefs'
decisions: [DEC-2026-02-09-01, DEC-2026-02-09-02]
terms:
  REFLEX-CONTROL: { aliases: ['Reflex-Control', 'Reflex-CONTROL'], kind: rule }
  REFLEX-SPEECH: { aliases: ['Reflex-Speech'], kind: rule }
  PROXIMITY: { aliases: ['Nähe-Kopplung'], kind: rule }
  JEALOUSY-GLOVES: { aliases: ['Kontakt-Guard', 'Eifersuchts-Guard'], kind: rule }
  DETACH: { aliases: ['Reflex-Detach', 'Detachment', 'REFLEX-DETACH'], kind: rule }
  SE-POOLS: { aliases: ['SE', 'Symbiose-Energie Pools'], kind: resource }
fsm:
  states:
    - id: CALM
      description: Normalbetrieb, geringe Bedrohung
    - id: ALERT
      description: Erhöhtes Risiko/Unbekanntes
    - id: CRISIS
      description: Akute Gefahr; Notfallprotokolle erlaubt
    - id: AFTERMATH
      description: Gefahr gebrochen; Deeskalation/Review
    - id: MAINTENANCE
      description: Geplante Ruhe-/Service-Fenster
  overlays:
    - id: SCHONMODUS
      enter:
        - se_lte: 0
        - se_pct_lt: 25
        - hard_proximity_violation: true
      exit:
        - se_pct_gte: 25
        - proximity_restored: true
      effect: 'Bonus/Feinsteuerung deaktiviert; Minimalfunktionen aktiv'
  transitions:
    - from: CALM
      to: ALERT
      triggers: [sensor_alarm, unknown_contact, proximity_breach, unsafe_env]
      entry: [tighten_proximity, raise_guard, prep_comm_short]
    - from: ALERT
      to: CALM
      guards: [debrief_ok, env_stable, caregiver_regulated]
      exit: [log_essentials, restore_normal_window]
    - from: ALERT
      to: CRISIS
      triggers: [acute_threat, medical_escalation, stop_ignored_by_third_party]
      entry: [activate_emergency, allow_reflex_control, prioritize_warning_pings]
    - from: CRISIS
      to: ALERT
      guards: [immediate_threat_broken, not_yet_secure]
      exit: [reduce_block, vitals_check, stabilize_env]
    - from: CRISIS
      to: AFTERMATH
      guards: [secure_confirmed, caregiver_capable]
      entry: [deescalate, care_med_psych, brief_review, write_protocol]
    - from: AFTERMATH
      to: CALM
      guards: [regen_reset_done, todos_assigned, lessons_logged]
    - from: CALM
      to: MAINTENANCE
      triggers: [sleep, service_window, long_transfer]
    - from: MAINTENANCE
      to: CALM
      exit: [self_test_short]
---

<!-- id: doc-reference-campaign-state -->
Reference: Campaign State (global mechanics)
============================================

Diese Datei ist die globale Mechanik-SSOT für RP-Regeln.

Fraktionsspezifische State-Snapshots wurden ausgelagert:

- Novapolis: [novapolis-campaign-state](../01-factions/novapolis/00-doctrine/novapolis-campaign-state.md)

<!-- id: fsm-campaign -->
FSM-Hinweis (global)
--------------------

- Die detaillierte Kampagnen-FSM pro Fraktion liegt in den jeweiligen Fraktions-Doctrines.
- Diese Datei hält die global gültigen Mechanik-Regeln (`SE-POOLS`, `INSTANCES`, `PROXIMITY`, `REFLEX-*`, `DETACH`, `JEALOUSY-GLOVES`).

<!-- id: rule-se-pools -->
Mechanik (Reference): Symbiose-Energie (SE) - Pools (Reflex-System)
---------------------------------------------------------------

Ziel: Support-/Exo-Verbrauch als **temporäre Kapazität** modellieren, ohne Menschen mit Zahlen-Tracking zu belasten.

Grundsätze
----------

- SE ist eine **Reflex-interne Ressource** (Reflex + Instanzen). Menschen haben keinen eigenen SE-Pool.
- Pools sind **strikt getrennt**: keine direkte Übertragung/„Umladung“ zwischen Reflex, Lumen, Echo oder zukünftigen Instanzen.
- „Kompatibilität mit Entwicklung“: Wachstum/Training ist pro Entität getrennt (physisch: Pool/Regeneration; mental: Kontrolle/Trigger).

Poolgrößen (Startwerte, größenbasiert)
--------------------------------------

Diese Werte sind bewusst klein skaliert (spielbar, wenig Buchhaltung):

- Reflex (Primär, groß): `SE_max = 12`
- Echo (Instanz, mittel): `SE_max = 8`
- Lumen (Instanz, klein): `SE_max = 6`

Regel für zukünftige Instanzen:

- Bei Aktivierung wird ein `SE_max` vergeben, abhängig von physischer Größe/Trägervolumen:
  - klein: 5-7
  - mittel: 8-10
  - groß: 11-13
- Der Wert wird im jeweiligen Charakter-Canvas dokumentiert.

Verbrauch (Heuristik)
---------------------

SE-Kosten pro „Einsatz“ (ein klar abgegrenzter Schutz-/Support-Impuls) sind kategorisiert:

- leicht: 1 SE (Feinmotorik, kurzer Scan, leichte Dämpfung)
- mittel: 2 SE (stabiler Schutzschirm, merkliche Kraft-/Dämpfungsverstärkung)
- stark: 3 SE (Notfall-Kokon, starke Abschirmung, längere Hochleistung)

Überlastung & Bonus-Regeln
--------------------------

- Wenn `SE_aktuell` unter 25% von `SE_max` fällt: **Bonus/Verstärkungen entfallen**, es bleibt nur Grundschutz/Grundfunktion.
- Wenn `SE_aktuell` 0 erreicht: Entität geht in Schonmodus (Rückzug auf Grundschicht), bis Regeneration greift.

Regeneration (einfach)
----------------------

- Ruhig/ohne Einsatz: +1 SE pro 30 Minuten.
- „Reset“: nach einem echten Ruheblock (z. B. Schlaf-/Regenerationsfenster, SL-Entscheid) wieder auf `SE_max`.

<!-- id: rule-instances -->
Instanzen (Reference): Wissensstand & Persönlichkeit
---------------------------------------------------

Entscheidung (INSTANCES)
------------------------

- Bei der Entstehung einer Instanz wird ein **Wissensstand als Snapshot** übernommen: die Instanz startet mit dem Wissen des erzeugenden Trägers zum Zeitpunkt $t_0$ (Reflex, Lumen, Echo oder spätere Instanz).
- **Persönlichkeit wird nicht kopiert**: Die Instanz ist eine eigenständige Person/Entität. Sie teilt Grunddispositionen (z. B. "chaotisch gut", Verlustangst/Nähebedürfnis), aber die Entwicklung beginnt erst ab $t_0$.
- Danach gilt: Wissen/Erfahrung **divergieren**. Es gibt **keinen automatischen Wissensabgleich** zwischen Trägern.

Wissensabgleich (optional, bewusst)
----------------------------------

- Spätere Wissensübertragung ist nur als **bewusster Austausch** möglich (Kommunikation/Training/Protokolle), nicht als Hintergrund-Sync.
- Wenn ein formaler Abgleich benötigt wird, wird er als eigener Schritt dokumentiert (z. B. im Trainingsstand/Log), inklusive "was wurde geteilt".

Training/Achsen (langfristig kompatibel)
----------------------------------------

- Physisch: SE-Pool/Regeneration bleibt strikt getrennt pro Entität.
- Mental/Verhalten: Kontrolle/Trigger/Consent werden pro Instanz trainiert (Einfluss der Bezugsperson ist zentral).
- Spezialisierung: Jede Instanz hat eine Hauptfähigkeit/Scope, der nicht automatisch auf andere Träger übergeht.

<!-- id: rule-proximity -->
Mechanik (Reference): Nähe-Kopplung (PROXIMITY)
----------------------------------------------

Ziel: Eine spielbare `PROXIMITY`-Regel für die Bezugspaare **Reflex↔Ronja**, **Lumen↔Jonas**, **Echo↔Kora**.

Grundannahmen (PROXIMITY)
-----------------------------

- Proximity ist **tatsächliche Nähe** (Distanz, optional Kontakt). Sie wirkt als Stabilitätsanker.
- Proximity hat zwei Treiber: **Zuneigung/Bindung** (Affektion) und **Schutz/Bedrohung** (Guard).
- Proximity ist **situativ** (Zustand wechselt je nach Lage); Intensität und Verhalten unterscheiden sich zwischen Reflex und Instanzen.

Zustände (Heuristik)
--------------------

- `CALM`: Affektionsnähe dominiert. Nähe wird aktiv gesucht, um Bindung/Regulation zu stabilisieren.
- `ALERT`: Unbekanntes/Risiko. Distanzfenster wird enger; Schutzpositionierung nimmt zu.
- `CRISIS`: Akute Selbst-/Fremdgefährdung. Schutzhandlungen dürfen kurzfristig übergriffig werden, bis die unmittelbare Gefahr gebrochen ist; danach Deeskalation.

<!-- id: dec-2026-02-09-02 -->
Distanzfenster (Startwerte)
---------------------------

Diese Werte sind Startwerte, nicht „hart“; Anpassung über Training.

- Lumen↔Jonas: bevorzugt <= 20 m (Werkstatt-/Arbeitsfenster). > 20 m: Unruhe/Schonmodus-Trigger.
- Echo↔Kora: bevorzugt <= 10 m (C6/Alarmfenster). > 20 m: Schonmodus-Trigger.
- Reflex↔Ronja: bevorzugt sehr eng (Körperkontakt/unter ~3 m), insbesondere in `ALERT/CRISIS`.

Distanzfolgen (spielbar)
------------------------

- Wenn das bevorzugte Fenster länger überschritten wird: steigende Unruhe, Fokusverlust, Rückzug/Schonmodus.
- Schonmodus bedeutet: Minimalfunktionen (Grundschutz, Beobachten), weniger Initiative und weniger „Feinsteuerung“.

Training (Ziele)
----------------

- Instanzen: Stabilität bei Distanz verbessern (z. B. auf 30-50 m mit Sicht/Funkkontakt), ohne Arbeitsfähigkeit zu verlieren.
- Reflex: Deeskalation/Stop-Reaktion verbessern und Eskalationen kürzer halten.

Scope-Unterschiede
------------------

- Reflex (Primär): stärkster Affektions- und Schutztreiber; in `CRISIS` darf er kurzfristig blockieren/abschirmen (z. B. Bewegung unterbinden, Kokon/Abschirmung), um Leben zu sichern.
- Instanzen (Lumen/Echo): Nähe wird gesucht (Affektion), Schutzhandlungen bleiben **lokal und kurz** (z. B. Hand stoppen, Sichtlinie schützen), um Arbeitsfähigkeit und Alltag zu ermöglichen.

<!-- id: rule-reflex-speech -->
Mechanik (Reference): Reflex Sprache/Audio (REFLEX-SPEECH)
--------------------------------------------------------

Ziel: Eine klare, spielbare Sprach-/Audio-Regel für Reflex, ohne Widerspruch zu Symbiose-Stufe I.

Grundannahmen
-------------

- Reflex kann Informationen als "Stimme" übermitteln, ohne akustisch im Raum zu sprechen.
- Es gibt zwei Kanäle: **Privatkanal (Ronja-only)** und **Broadcast (über Technik)**.

Kanal A: Privatkanal (Ronja-only, Tympanon-Kopplung)
----------------------------------------------------

- Reflex koppelt sich an Ronjas Hörsystem ("Tympanon") und erzeugt einen internen Schall-/Signalreiz, den **nur Ronja** als Stimme wahrnimmt.
- Das ist **kein Raumklang**: Außenstehende hören nichts.
- Default-Regel: Aktivierung nur mit Ronjas Freigabe (Signal/Consent). Ronja kann jederzeit abbrechen ("Stop" / "Signal aus").

Kanal B: Broadcast (über Geräte)
-------------------------------

- Reflex kann sich an ein technisches Gerät koppeln (z. B. Ohrhörer/Headset/Funkgerät/Intercom/Telefon) und darüber Audio ausgeben.
- Wer das Gerät nutzt bzw. es hören kann, hört Reflex ("Broadcast").

Dauer & Erschöpfung (Heuristik)
-------------------------------

- "Ping" (Sekunden, Warnung/Signal): jederzeit möglich, sehr geringe Belastung.
- "Satz" (kurz, <= 1 Minute): geringe Belastung.
- "Gespräch" (mehrere Minuten): merkliche Belastung → Pausen einplanen.
- "Dauerkanal" (lange Kopplung): nicht als Default; nutzt sich ab (kognitiv/sensorisch) und erhöht Dysregulationsrisiko.

Kosten/Limitierung (kompatibel mit SE)
--------------------------------------

- Privatkanal und Broadcast zählen als **leichte bis mittlere** Aktivität (je nach Dauer/Intensität).
- Bei niedriger SE (nahe Schonmodus) wird Kommunikation **kurz, selten, priorisiert** (Warnungen/Essentials vor Smalltalk).

Consent & Notfall-Override
--------------------------

- Im Normalfall gilt: Privatkanal nur mit Consent; Abbruchwunsch wird respektiert.
- In `CRISIS` (akute Selbst-/Fremdgefährdung) darf Reflex **kurz** ("Notfall-Ping") auch ohne vorherige Freigabe warnen, wenn dies unmittelbar lebensrettend ist.
- Nach Ende der Akutlage gilt sofort wieder: Consent + Deeskalation + Pause.

<!-- id: rule-reflex-control -->
Mechanik (Reference): Schutz-Übernahme (REFLEX-CONTROL)
------------------------------------------------------

Ziel: Eine klare, spielbare Regel für Schutz-Übernahme und Rückgabe, die Reflex' Überreaktionsrisiko begrenzt.

Grundsatz (Decision, REFLEX-CONTROL)
-----------------------------------

- **Rückgabe/Entkopplung erfolgt erst, wenn die Situation als "Sicher" eingeschätzt wird (nicht früher).**

<!-- id: dec-2026-02-09-01 -->
Definition "Sicher" (Heuristik)
-------------------------------

"Sicher" bedeutet als Mindeststandard:

- keine akute Bedrohung mehr (kein unmittelbarer Angriff/Absturz/Erstickung/Brand),
- Ronja ist wieder handlungs- und entscheidungsfähig (Atmung/Orientierung stabil),
- Umgebung ist stabil genug, dass ein Loslassen nicht sofort wieder in `CRISIS` kippt.

Stop / Deeskalation
-------------------

- Ronjas "Stop" ist ein **Deeskalationssignal**: Reflex reduziert Druck/Blockaden auf das notwendige Minimum.
- **Volle Entkopplung** erfolgt trotzdem erst bei "Sicher".

Scope & Kosten (kompatibel)
---------------------------

- Schutz-Übernahme ist `CRISIS`-verknüpft (akute Selbst-/Fremdgefährdung) und soll zeitlich kurz bleiben.
- Bei niedriger SE (nahe Schonmodus) wird Kontrolle grober und kürzer; Rückgabe-Check bleibt Pflicht.


<!-- id: rule-detach -->
Mechanik (Reference): Detachment & Beweglichkeit (REFLEX-DETACH)
---------------------------------------------------------------

Ziel: Widerspruchsfrei festlegen, was "Trennung" bedeutet (Primärinstanz vs Instanzen) und welche kurzen Sonderfälle spielbar sind.

Grundsatz (Decision)
--------------------

- **Reflex (Primärinstanz) bleibt immer mit Ronjas Körper verbunden.** Keine vollständige Trennung.
- **Instanzen (z. B. Lumen/Echo) sind an ihre Bezugsperson gekoppelt**, dürfen aber in sicheren Kontexten kurzzeitig ohne permanenten Körperkontakt im Nahbereich agieren.

Reflex (Primärinstanz, Ronja)
-----------------------------

- "Strecken/Seestern" ist erlaubt als **Umpositionierung ohne Entkopplung** (Ausbreiten, Umgreifen, Abstützen, Abschirmen), aber Reflex bleibt durchgehend Teil der anliegenden Symbiose.
- Reflex erzeugt dabei **keine frei laufende, eigenständige Teil-Instanz** außerhalb Ronjas.
- Wenn ein Vorgang eine echte Abtrennung erfordern würde, gilt: **nicht möglich** (stattdessen: Werkzeug/Person anfordern, oder Instanzen nutzen, falls vorhanden).

Instanzen (Lumen/Echo): lokales Agieren ohne Dauer-Körperkontakt
--------------------------------------------------------------

- Default: Nähe/Regulation über Kontakt bzw. sehr kurze Distanz (siehe PROXIMITY-Startwerte). "Trennung" im Sinn dieser Regel meint: **kein dauerhafter Körperkontakt**, nicht "weit weg".
- Erlaubt: kurzzeitig im Nahbereich bewegen (z. B. Werkstatt-/Verwaltungsaufgabe, Material reichen, Sensorcheck), solange der Kontext **sicher** ist.

Kosten/Limitierung (SE-kompatibel, Heuristik)
---------------------------------------------

- Ohne externe Energiequelle steigt der Aufwand deutlich: lokales Agieren ohne Kontakt zählt als **zusätzliche Belastung** (SE-Verbrauch steigt schneller; Schonmodus wird wahrscheinlicher).
- Mit externer Energiequelle/Anker (z. B. Werkbank/Station-Power/geladenes Modul) ist lokales Agieren **länger und stabiler**, ohne dass SE-Pools zwischen Entitäten übertragen werden.
- Wenn die Instanz Unruhe/Stress zeigt oder "Stop" kommt: **sofort zurück in Nähe/Kontakt**; bei Überschreiten des eigenen Distanzfensters kippt sie in Schonmodus.


<!-- id: rule-jealousy-gloves -->
Mechanik (Reference): Kontakt-Guard / Eifersuchts-Guard (JEALOUSY-GLOVES)
------------------------------------------------------------------------

Ziel: Eine spielbare, "süße" Jealousy-Detailregel, die **körperlichen Kontakt** konsensbasiert behandelt und unangenehme Dynamiken vermeidet.

Grundsatz (Decision, JEALOUSY-GLOVES)
------------------------------------

- Reflex (und Instanzen bei ihrer Bezugsperson) darf als Reaktion auf unerwünschten Körperkontakt einen **Kontakt-Guard** bilden: Er legt sich **nicht nur als Handschuh über die Haut**, sondern kann die **konkret betroffene Körperstelle** (z. B. Schulter, Arm, Hand, Rücken) mit einer dünnen Schicht **bedecken/abschirmen**, sodass der Kontakt nicht direkt zustande kommt.
- Der Kontakt-Guard ist **Blockade/Barriere**, keine Bestrafung: kein Schmerz, keine Luft-/Sichtblockade, kein "Festhalten" als Default.

Consent, Stop, Freigabe
-----------------------

- **Consent-first:** Kontakt-Guard ist im Normalfall nur aktiv, wenn die Bezugsperson das möchte (oder es als "süßes" Verhalten akzeptiert).
- **"Stop" beendet sofort** den Kontakt-Guard (Deeskalation auf 0), sofern keine akute Gefahr vorliegt.
- **"Freigabe"** (oder eine von der Bezugsperson definierte Freigabe-Phrase) erlaubt den Kontakt: Reflex/Instanz zieht sich an der Stelle zurück.

Eskalation (Heuristik)
----------------------

- Default ist erst Signal/Warnung (Kribbeln/Kälte), dann erst Bedecken der Stelle.
- Wenn wiederholt versucht wird, die Grenze zu übergehen, wird die Barriere dichter und Reflex/Instanz fordert explizit Freigabe oder Abstand.
- Wenn es **keine Jealousy-Situation**, sondern eine **Bedrohung/Übergriff** ist, greifen die Schutzregeln aus `REFLEX-CONTROL` (CRISIS) statt JEALOUSY-GLOVES.


<!-- id: policy-new-entities -->
Admin/Canon-Policy (Reference): Neue Entitäten / "Lebewesen"
------------------------------------------------------------

Grundsatz
---------

- Es gibt ohne Adminfreigabe **kein** weiteres neues/undefiniertes Lebewesen außer **Reflex** (inkl. Instanzen wie Lumen/Echo).
- Hinweise wie "Lebewesen unter dem Boden" (C6) sind bis zur Adminfreigabe als **Artefakt/Noise/Gerücht** zu behandeln und werden nicht als Canon-Entität etabliert.

Praxis
------

- Wenn so ein Hinweis im Spiel auftaucht: maximal als Signalrauschen in Narrative/Logs notieren (ohne neue Spezies/Entität zu definieren).
- Erst nach expliziter Adminfreigabe darf daraus eine neue Entität werden.

Externe Handschuhe / Kleidung
-----------------------------

- Externe Handschuhe sind als **Arbeits-/Witterungsschutz** grundsätzlich ok.
- Wenn Kontakt-Guard aktiv ist, hat die Schutzschicht Priorität: Reflex/Instanz legt sich an der **betroffenen Stelle** so, dass der unerwünschte Kontakt zuverlässig blockiert wird (auch über Stoff/Handschuh möglich).


<!-- id: economy-kugeln -->
Währung (Reference): Kugeln
---------------------------

Fraktionsbezogene Ausprägung/Preisbänder liegen in den Handels-/Diplomatie-Unterlagen der Fraktionen.

- Novapolis: [novapolis-pricebands](../01-factions/novapolis/06-handel-diplomatie/novapolis-pricebands.md)

<!-- id: project-draisine -->
Projekt-Reference: Draisine
---------------------------

Projekt-Details wurden in den Projekt-Canvas verschoben.

- Novapolis-Projekt: [Draisine-Transportmodul](../01-factions/novapolis/05-projects/Draisine-Transportmodul.md)


Inventar / Ressourcen (Arbeitsstand)
------------------------------------

- D5-Inventar gepflegt.
- C6-Funde verbucht (Filter, Energiezellen, Werkzeuge); Versorgungsschwerpunkte mit Marei abgestimmt.
- Fehlend/Offen: Schweißausrüstung, Adapter DN60. Hydrofilter-Behälter als Reserve.

Fortschritt (Reporting-Detail)
------------------------------

- Nordlinie 01 berichtet getrennt: Erkundung / Sicherung / Betrieb (0-100%).

Timeline-Skizze (aus ehem. Core-Block)
--------------------------------------

Hinweis: Diese Sequenz ist eine **Skizze** und muss an das finale T+0-Fenster in [Canvas-T0-Timeline](./Canvas-T0-Timeline.md) angepasst werden.

1. Erwachen D5 → Selbstcheck → Wartungsauftrag.
2. Erstkontakt Reflex, Dämpfungs-Test, Regeln.
3. C6: Funk/Scan, Reaktorstabilisierung, Suche/Leichenfund; Evakuierungsaufnahme (20 Personen) gemeinsam mit Marei.
4. D5: Wiederaufbau; Jonas eingebunden; Pahl in Pflege.
5. Projektstart „Nordlinie 01“; Vorratsläufe; Überwachung an C6.

Offene Fäden (Detail)
---------------------

- Nordlinie 01: Schweißgerät, DN60-Adapter, Statikprüfung.
- C6: Überwachungssplitter auswerten; eventuelle Überlebende.
- E3: Anomalie „E3-Gefahr“ untersuchen; Reaktivierungsplan abstimmen.
- Reflex-Forschung: Sensorik, Trägerarchitektur („Wirbelsäule“), Exo-Prototyp.
- Fraktionen: Signale/Beobachtungen sammeln.
- Jonas: Vertrauen festigen; Werkstatt einrichten.
- Hydrofilter: Aufbereitung/Tests.

Links
-----
- Canon-Core → [memory-bundle.md](./memory-bundle.md)
- Timeline (T+0) → [Canvas-T0-Timeline.md](./Canvas-T0-Timeline.md)
- Szene (T+0 Status-Ping) → [scene-2025-10-27-a.md](../06-scenes/scene-2025-10-27-a.md)
- Nordlinie 01 → [Nordlinie-01.md](../01-factions/novapolis/05-projects/Nordlinie-01.md)
- Inventar (Fraktion) → [Novapolis-inventar.md](../01-factions/novapolis/04-inventory/Novapolis-inventar.md)

<!-- id: validation -->

Validierung (How to)
--------------------

Führe die Validatoren aus, um RP-Dokumente und Crossrefs zu prüfen:

```bash
npm --prefix novapolis-rp\coding\tools\validators run validate:rp
npm --prefix novapolis-rp\coding\tools\validators run validate:crossrefs
```
