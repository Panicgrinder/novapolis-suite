---
stand: 2026-02-09 02:46
update: Offene Konflikte aus uncertainties.md ergänzt.
checks: "npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-02-09 02:46)"
category: admin
canvas: curated-konfliktliste
slug: curated-konfliktliste
source: ../../database-curated/staging/*.review.md
---

Curated Konfliktliste (Staging → SSOT)
=====================================

Zweck
-----

Diese Seite bündelt die wichtigsten **Konflikte** und **FACT?**-Punkte aus den Curated-Staging-Reviews, damit Canon-Änderungen nachvollziehbar über Decisions/SSOT laufen.

Quellen (Curated)
-----------------

- [chat-export-complete.review.md](../../database-curated/staging/chat-export-complete.review.md)
- chat-export (1).review.md
- Ergänzende Auszüge: [uncertainties.md](../../../novapolis-dev/docs/process/rp-canvas-rescue/uncertainties.md), [resolved.md](../../database-curated/staging/reports/resolved.md)

Arbeitsregel
------------

- Pro Konflikt: **Problem → Entscheidung → Auswirkungen → SSOT-Patch**.
- Nichts davon gehört in den Canon-Core (`00-admin/memory-bundle.md`) außer stabilen, harten Fakten.

Offen (Quelle: uncertainties.md)
-------------------------------

Diese Punkte sind in `../../../novapolis-dev/docs/process/rp-canvas-rescue/uncertainties.md` noch **unchecked** und damit aktiv zu klären:

- [OPEN] Währung "Kugeln": konkrete Bestandszahlen/Umrechnung in Inventaren noch tbd; SSOT-Patch in Inventaren nachziehen.
- [OPEN] Draisine/Transportmodul: Status + Scope in SSOT (Projekt/Inventar) konsistent und ohne tbd verankern.
- [OPEN] "Lebewesen unter dem Boden" (C6): Einordnung als Gerücht/Signalrauschen vs Anomalie in SSOT eindeutig verankern.

Top-10 Konflikte / FACT?-Punkte (Priorität)
------------------------------------------

1) [OPEN] Währung "Kugeln": Bestandszahlen/Umrechnung in Inventaren tbd (Inventare/Reference).
2) [OPEN] Draisine/Transportmodul: Status + Scope in SSOT (Projekt/Inventar) konsistent verankern.
3) [OPEN] "Lebewesen unter dem Boden" (C6): Gerücht/Signalrauschen vs Anomalie in SSOT fixieren.

Archiv: Gelöste Top-10 (2026-01-11)
----------------------------------

1) Reflex Support-/Exo-Modus: Überlastung/Verbrauch (Review 2025-11-01)
  - Quelle: `uncertainties.md` → `[REFLEX]` (unchecked)
  - Decision (2026-01-10): Support-/Exo-Verbrauch läuft über SE-Kosten (leicht/mittel/stark). Unter 25% von `SE_max` entfallen Bonus/Verstärkungen; bei 0 geht Reflex in Schonmodus (Details: `Reference-Campaign-State.md`).
   - Problem: Mechanik ist als FACT? markiert; konkrete Schwellen/Verbrauch/„Bonus entfällt“ unklar.
   - Layer: Reference (Mechanik-Policy) + Narrative (Belege über Szenen/Tests)
   - Betroffene SSOT-Dateien (vermutet):
    - [Reflex](../01-factions/novapolis/02-characters/Reflex.md)
    - [Reference-Campaign-State](Reference-Campaign-State.md)
   - Priorität: P1

2) Reflex-Instanzen: Kapazitätslogik + Differenzierung (Review 2025-11-01)
  - Quelle: `uncertainties.md` → `[INSTANCES]` (unchecked)
  - Decision (2026-01-10): Wissensstand wird bei Entstehung als Snapshot übernommen; Persönlichkeit ist eigenständig; danach kein automatischer Wissensabgleich.
   - Problem: Instanzen teilen Basislogik, aber Hauptfähigkeiten/Trennung/Training müssen sauber definiert werden.
   - Layer: Reference
   - Betroffene SSOT-Dateien (vermutet):
    - [Reflex](../01-factions/novapolis/02-characters/Reflex.md)
    - [Lumen](../01-factions/novapolis/02-characters/Lumen.md)
    - [Echo](../01-factions/novapolis/02-characters/Echo.md)
   - Priorität: P1

3) Nähe-Kopplung (Proximity): Lumen↔Jonas, Echo↔Kora, Reflex↔Ronja (Review 2025-11-01)
  - Quelle: `uncertainties.md` → `[PROXIMITY]` (unchecked)
  - Decision (2026-01-10): Proximity ist reale Nähe (Distanz/Kontakt) aus Zuneigung+Schutz, situativ (`CALM/ALERT/CRISIS`); Distanzfenster/Schonmodus als Startwerte; Training möglich; Reflex darf bei akuter Selbst-/Fremdgefährdung kurzfristig übergriffig schützen (Reference: `Reference-Campaign-State.md`).
   - Problem: Schwellen/Distanzfolgen/Training offen; darf nicht als „Zwang“ wirken.
   - Layer: Reference
   - Betroffene SSOT-Dateien (vermutet):
    - [Reflex](../01-factions/novapolis/02-characters/Reflex.md)
    - [Jonas-Merek](../01-factions/novapolis/02-characters/Jonas-Merek.md)
    - [Lumen](../01-factions/novapolis/02-characters/Lumen.md)
    - [Echo](../01-factions/novapolis/02-characters/Echo.md)
    - [Kora-Malenkov](../01-factions/haendlerbund/02-characters/Kora-Malenkov.md)
   - Priorität: P1

4) Reflex Sprech-Mechanik (Tympanon): Einwilligung/Dauer/Erschöpfung (Review 2025-11-01)
  - Quelle: `uncertainties.md` → `[REFLEX-SPEECH]` (unchecked)
  - Decision (2026-01-10): Zwei Kanäle: Privatkanal (Ronja-only, Tympanon-Kopplung) vs Broadcast (über Geräte). Default ist Consent + Abbruch jederzeit; Dauerkanal nur begrenzt (Erschöpfung/Schonmodus), Notfall-Ping in `CRISIS` als kurzer Override möglich (Reference: `Reference-Campaign-State.md`).
   - Problem: Consent/Limitierungen müssen eindeutig und spielbar sein.
   - Layer: Reference
   - Betroffene SSOT-Dateien (vermutet):
    - [Reflex](../01-factions/novapolis/02-characters/Reflex.md)
    - [Ronja-Kerschner](../01-factions/novapolis/02-characters/Ronja-Kerschner.md)
   - Priorität: P1

5) Reflex Schutz-Übernahme: Trigger/Sinne/Rückgabeprozess (Review 2025-11-01)
  - Quelle: `uncertainties.md` → `[REFLEX-CONTROL]` (unchecked)
  - Decision (2026-01-10): Rückgabe/Entkopplung erfolgt erst, wenn die Situation als "Sicher" eingeschätzt wird (nicht früher). "Stop" ist Deeskalation (Druck runter), aber volle Entkopplung erst bei "Sicher" (Reference: `Reference-Campaign-State.md`).
   - Problem: Wann darf Reflex dämpfen/übernehmen; wie wird zurückgegeben; welche Kosten.
   - Layer: Reference
   - Betroffene SSOT-Dateien (vermutet):
    - [Reflex](../01-factions/novapolis/02-characters/Reflex.md)
   - Priorität: P1

6) Detachment-Regel: keine vollständige Trennung; Sonderfälle (Review 2025-11-01)
  - Quelle: `uncertainties.md` → `[REFLEX-DETACH]` (unchecked)
  - Decision (2026-01-11): Primärinstanz Reflex bleibt immer mit Ronjas Körper verbunden (keine vollständige Trennung; "Strecken/Seestern" nur als Umpositionierung ohne Entkopplung). Instanzen (Lumen/Echo) dürfen in sicheren Kontexten kurz lokal ohne Dauer-Körperkontakt agieren, mit deutlich erhöhtem SE-Verbrauch ohne externe Energiequelle; externer Anker macht es stabiler, aber ohne Pool-Transfer (Reference: `Reference-Campaign-State.md`).
   - Problem: „Strecken/Seestern“ vs. „nicht trennen“ braucht klare Grenzen (Reichweite/Zeit/Notfall).
   - Layer: Reference
   - Betroffene SSOT-Dateien (vermutet):
    - [Reflex](../01-factions/novapolis/02-characters/Reflex.md)
   - Priorität: P1

7) Handschuh-/Eifersuchts-Policy: Reflex-Handschutz vs externe Handschuhe
  - Quelle: `uncertainties.md` → `[JEALOUSY-GLOVES]` (unchecked)
  - Decision (2026-01-11): Kontakt-Guard ist erlaubt: Reflex/Instanzen bedecken die konkret betroffene Körperstelle der Bezugsperson (nicht nur "als Handschuh") und blockieren so unerwünschten Kontakt; consent-first, "Stop" beendet sofort, "Freigabe" erlaubt Kontakt. Externe Handschuhe als Arbeits-/Witterungsschutz ok (Details: `Reference-Campaign-State.md`).
   - Problem: Policy ist sensibel; muss ohne unangenehme Dynamiken auskommen und als Sicherheitsregel funktionieren.
   - Layer: Reference
   - Betroffene SSOT-Dateien (vermutet):
    - [Reflex](../01-factions/novapolis/02-characters/Reflex.md)
    - [Ronja-Kerschner](../01-factions/novapolis/02-characters/Ronja-Kerschner.md)
   - Priorität: P1

8) Währung „Kugeln“: Definition + Verteilung (Inventare haben tbd)
  - Decision (2026-01-11): "Kugeln" als Währung wird in zwei Stufen geführt: Kugeln (neu) vs Kugeln (gebraucht). Faustregel: 1 neu ≈ 10 gebraucht; gebraucht ist Alltagswährung und Hauptmunition, Qualität streut (Details: `Reference-Campaign-State.md`).
   - Problem: „Neu/alt“ ist als tbd in mehreren Inventaren; Regeln/Mengen/Umrechnung fehlen.
   - Layer: Reference
   - Betroffene SSOT-Dateien (vermutet):
    - [Novapolis-inventar](../01-factions/novapolis/04-inventory/Novapolis-inventar.md)
    - `01-factions/<faction>/04-inventory/`
   - Priorität: P2

9) Draisine/Transportmodul: Status + Scope
   - Problem: In Curated als aktiv/prototypisch erwähnt; in SSOT v. a. als TODO bei Jonas.
   - Decision (2026-01-11): Das Draisine-/Transportmodul ist ein D5-Werkstatt-Prototyp von Jonas mit Sicherheits-/Abnahme-Support durch Pahl. Scope: konservativer Material-/Transport-Usecase für Nordlinie; kein "schneller Zug" und kein Dauerdienst ohne Tunnel-Freigaben. Erster Meilenstein ist ein sicherer Testlauf mit klaren Gates/Logpflicht (Details: `Reference-Campaign-State.md`, Projekt-Canvas `Draisine-Transportmodul.md`).
   - Layer: Reference (Projekt/Inventar) + Narrative (Testlauf)
   - Betroffene SSOT-Dateien (vermutet):
   - [Jonas-Merek](../01-factions/novapolis/02-characters/Jonas-Merek.md)
   - [Draisine-Transportmodul](../01-factions/novapolis/05-projects/Draisine-Transportmodul.md)
    - [caravan-moves](../01-factions/haendlerbund/05-projects/caravan-moves.md) (Koordination/Läufe)
   - Priorität: P2

10) „Lebewesen unter dem Boden“ (C6): Einordnung als Lore/Anomalie vs Gerücht
   - Problem: Curated markiert es als offenen Faktor; muss als Gerücht/Beobachtung oder als Anomalie sauber einsortiert werden.
   - Decision (2026-01-11): Das ist ein Artefakt/Noise (keine neue Spezies/kein neues Lebewesen). Es gibt ohne Adminfreigabe **kein** weiteres neues/undefiniertes Lebewesen außer Reflex (inkl. Instanzen). Reports dieser Art werden bis zur Adminfreigabe als Gerücht/Signalrauschen geführt (wenn überhaupt), nicht als Canon.
   - Layer: Admin/Reference (Policy) → Narrative nur bei expliziter Adminfreigabe
   - Betroffene SSOT-Dateien (Reference):
   - [Reference-Campaign-State](Reference-Campaign-State.md) (Policy: keine neuen Entitäten)
   - Priorität: P2

Offene Punkte (nicht Top-10, aber zu tracken)
---------------------------------------------

- Tagging/Validator-Pipeline für Curated: Staging-Review nennt offene Prozessschritte (Dry-Run/Write-Run/Receipt). Das ist Workflow, kein Canon.
- Weitere [OPEN] in Curated betreffen vor allem Prozess-/Index-/Backup-Policies und sind bereits in Admin-Dokumenten abgedeckt.

Nächste Schritte
----------------

- Punkte 1–10 sind entschieden; nächste Arbeit ist die Ableitung/Verlinkung in den betroffenen SSOT-Dateien (Charaktere/Inventar/Projekt-Canvas) und ggf. Narrative-Belege über Szenen/Tests.

Validierung
-----------

- `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/**/*.md'`
- `python scripts/check_frontmatter.py novapolis-rp/database-rp`
- `python scripts/checks_rp_consistency.py --strict`
