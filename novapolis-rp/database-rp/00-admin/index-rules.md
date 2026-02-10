---
stand: 2026-02-10 22:45
update: Frontmatter normalisiert.
checks: "not run (not requested)"
slug: index-rules
category: Admin
schemaVersion: 1
language: de
status: active
owners: [admin-novapolis]
tags: [rp, rules, index]
relatedSlugs: [reference-campaign-state]
---

Index: Regeln, Policies und FSM
===============================

Zweck: Zentrale Übersicht aller Regel-/Policy-Sektionen und Entscheidungsanker (IDs), um menschliche und KI-basierte Verwaltung zu erleichtern.

Quelldatei (Aggregator)
-----------------------
- reference: `reference-campaign-state` → ./Reference-Campaign-State.md

Abschnitts-IDs (interne Anker für KI)
-------------------------------------
- fsm-campaign → Kampagnen-Zustandsmaschine
- rule-se-pools → Symbiose-Energie (SE) – Pools
- rule-instances → Instanzen: Wissensstand & Persönlichkeit
- rule-proximity → Nähe-Kopplung (PROXIMITY)
- rule-reflex-speech → Reflex Sprache/Audio (REFLEX-SPEECH)
- rule-reflex-control → Schutz-Übernahme (REFLEX-CONTROL)
- rule-detach → Detachment & Beweglichkeit (REFLEX-DETACH)
- rule-jealousy-gloves → Kontakt-Guard / Eifersuchts-Guard (JEALOUSY-GLOVES)
- policy-new-entities → Admin/Canon-Policy: Neue Entitäten
- economy-kugeln → Währung: „Kugeln“ (neu vs gebraucht)
- project-draisine → Projekt: Draisine-/Transportmodul (D5)

Decision-IDs (kanonische Festlegungen)
--------------------------------------
- DEC-2026-02-09-01 → `REFLEX-CONTROL`: Rückgabe/Entkopplung erst bei "Sicher"
- DEC-2026-02-09-02 → `PROXIMITY`: Distanzfenster (Startwerte) als Default

Hinweis
-------
- Die obigen IDs sind als HTML-Kommentare in der Quelldatei markiert (z. B. `<!-- id: rule-proximity -->`).
- Für klickbare Navigation nutze die Abschnittsüberschriften in `Reference-Campaign-State.md`.
