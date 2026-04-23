---
stand: 2026-04-23 16:00
update: Der RP-Laufzeitbereich fuehrt jetzt zusaetzlich einen append-only Rohpfad fuer Chattranskripte pro Session.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp/results/reports/checks_report_20260423_155606.md; snapshot-lock PASS (2026-04-23 16:00)
---

RP Runtime Staging
==================

Zweck
-----

Dieser Pfad ist die kontrollierte Laufzeit- und Arbeitsflaeche fuer RP im Chat.

- Hier landen neue oder veraenderte Fakten zuerst als Arbeitsstand.
- Nichts unter `rp-runtime/` ist automatisch RP-SSOT.
- Promotion in `novapolis-rp/database-rp/**` erfolgt erst nach Review oder expliziter User-Freigabe.

Geeignete Inhalte
-----------------

- laufende Szenen- und Sitzungsprotokolle
- rohe Chattranskripte pro Session als append-only JSONL
- neue Figuren in Arbeitsform
- Beziehungs- und Fraktionsaenderungen auf Probe
- Inventar- und Ressourcenverschiebungen waehrend eines RP-Laufs
- Welt- oder Standortstatus zwischen zwei Promotionsschritten

Empfohlene Struktur
-------------------

- `sessions/<session-id>/scene-log.md`
- `sessions/<session-id>/transcript.jsonl`
- `characters/<slug>.md`
- `relationships/<slug>.md`
- `inventories/<slug>.md`
- `state/<slug>.md`

Vorhandene Startstruktur
------------------------

- `sessions/README.md` und `sessions/session-template.md`
- `sessions/transcript-template.jsonl`
- `characters/README.md` und `characters/character-template.md`
- `relationships/README.md` und `relationships/relationship-template.md`
- `inventories/README.md` und `inventories/inventory-template.md`
- `state/README.md` und `state/state-template.md`

Automatische Routing-Matrix
---------------------------

- Szenenzuege, verdichtete Turn-Protokolle und Kurzauswertung: `sessions/<session-id>/scene-log.md`
- ungekuerzter RP-/Admin-Chatverlauf: `sessions/<session-id>/transcript.jsonl`
- Figurenanlage oder Figurenupdate: `characters/<slug>.md`
- Beziehungs- oder Loyalitaetsverschiebung: `relationships/<slug>.md`
- Inventar-, Transfer- oder Ressourcenupdate: `inventories/<slug>.md`
- Welt-, Orts-, Fraktions- oder Projektstatus: `state/<slug>.md`

Regel fuer Mischfaelle
----------------------

- Ein RP-Zug mit mehreren Folgen landet nicht nur in einer Datei.
- Der Ablauf geht immer nach `sessions/<session-id>/scene-log.md`.
- Jede zusaetzliche belastbare Folge wird parallel in die passende Typdatei geschrieben.
- Sekundaerdateien bleiben knapp, referenzieren aber nach Moeglichkeit Session und Turn.

Vertragsregeln
--------------

- RP-SSOT bleibt `novapolis-rp/database-rp/**`.
- `rp-runtime/` ist absichtlich fluechtiger, aber nachvollziehbarer als freie Chat-Improvisation.
- `transcript.jsonl` bleibt append-only Rohspur und ist weder RP-SSOT noch direkt trainierbar.
- Jeder Eintrag soll kenntlich machen, ob er `Probe`, `Arbeitsstand`, `review_required` oder `promotion_ready` ist.
- Wenn Faktenlage unsicher ist, bleibt der Eintrag hier und wandert nicht direkt in den Kanon.

Promotion-Pfad
--------------

1. Szene oder Verwaltungsakt im Chat erzeugt ein Arbeitsartefakt unter `rp-runtime/`
2. Rohchat kann parallel append-only in `sessions/<session-id>/transcript.jsonl` mitlaufen
3. Review auf Kanontreue, Belastbarkeit und Stil
4. Erst danach gezielte Uebernahme nach `database-rp/**` oder in andere kuratierte Artefakte

Schneller Testwechsel
---------------------

1. Im Agentenwaehler `Novapolis RP Szenenlabor und Ton-Fit` aktivieren.
2. Fuer den ersten Wechseltest den folgenden Prompt verwenden.

```text
Modus: Labor.
Session-ID: c6-h47-handelsfenster-01
Perspektive: C6, Logistik- und Empfangsebene
Ort: C6 Aussenposten
Ton: angespannt, knapp, pragmatisch
Stimmung: kontrollierte Unsicherheit unter Versorgungsdruck
Ziel: Setze die bestehende Szene ab Turn 2 fort. Trenne Inworld-Szene und Kurzauswertung sauber. Wenn belastbare Folgen entstehen, route sie in den bestehenden Runtime-Baum unter sessions/, inventories/, relationships/ oder state/.
```

Erwartete Testspur
------------------

- Pflichtpfad: `sessions/c6-h47-handelsfenster-01/scene-log.md`
- Nur bei belastbarer Folge: `inventories/c6.md`, `relationships/mara-quell-zu-c6.md` oder `state/c6.md`
- Kein direkter Schreibzugriff nach `novapolis-rp/database-rp/**` ohne explizite Promotion-Freigabe
