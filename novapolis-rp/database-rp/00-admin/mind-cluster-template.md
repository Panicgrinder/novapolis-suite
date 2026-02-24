---
stand: 2026-02-24 15:35
update: Template auf mind-cluster umgestellt; Einfluss/Bedrohung und Entitaetsdatei-Prinzip explizit ergaenzt.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '.github/instructions/mind-cluster.instructions.md' 'novapolis-rp/database-rp/00-admin/mind-cluster-template.md' 'novapolis-rp/database-rp/01-factions/novapolis/07-mind-clusters/ronja-kerschner-mind-cluster.md' 'novapolis-rp/database-rp/01-factions/novapolis/02-characters/Ronja-Kerschner.md' '.github/copilot-instructions-headings.md' 'novapolis-dev/docs/brainstorming.rp.md' 'novapolis-dev/docs/donelog.md' 'DONELOG.md' PASS (2026-02-24 15:10); .\.venv\Scripts\python.exe scripts\check_frontmatter.py 'novapolis-rp/database-rp/00-admin/mind-cluster-template.md' 'novapolis-rp/database-rp/01-factions/novapolis/07-mind-clusters/ronja-kerschner-mind-cluster.md' 'novapolis-rp/database-rp/01-factions/novapolis/02-characters/Ronja-Kerschner.md' '.github/copilot-instructions-headings.md' 'novapolis-dev/docs/brainstorming.rp.md' 'novapolis-dev/docs/donelog.md' 'DONELOG.md' PASS (2026-02-24 15:10); npm --prefix novapolis-rp/coding/tools/validators run validate:rp PASS (2026-02-24 15:10)
slug: mind-cluster-template
category: admin
status: active
version: "0.1"
---

Mind Cluster Template (Sphaerenmodell)
======================================

Zweck
-----
- Einheitliche Vorlage fuer beziehungsbezogene Zustandsmodelle in Novapolis.
- Trennung zwischen verbindlicher Governance und fachlichem Modulverhalten.

Governance-Referenz (verbindlich)
---------------------------------

- Verbindliche Regeln liegen zentral in `.github/instructions/mind-cluster.instructions.md`.
- Dieses Template dupliziert keine Governance, sondern bildet den fachlichen Modul-Part ab.
- Bei Konflikt gilt immer die Scoped Instruction als Regelquelle.

Entitaetsdatei-Prinzip (fachlich)
---------------------------------

- Pro Entitaet genau eine Datei: `<slug>-mind-cluster.md`.
- Diese Datei ist SSOT fuer beziehungsnahe Zustandsdaten der Entitaet.
- Charakterdateien halten dazu nur Referenz/Pointer, keine Duplikate von:
- Beziehungen
- Verhaltenssignatur
- geistnahem Status/Kondition

Modul-Part (dynamisches Sphaerenverhalten)
------------------------------------------

Sphaerenachsen
--------------
- `x`: links/rechts (`-100 .. +100`)
- `y`: hinten/vorne (`-100 .. +100`)
- `z`: prosozial (`+`) vs. egoistisch (`-`) (`-100 .. +100`)
- `normtreue`: normative Bewertung (`-100 .. +100`)

Driftprinzip (erwuenscht)
-------------------------
- Drift ist Teil des Modells und darf unvorhersehbare Verlaeufe erzeugen.
- Extremzustand ist moeglich, aber nicht permanent ohne Ereignisdruck.

Ruecklauf zur Null ohne externen Impuls
---------------------------------------
- Pro Tick wirkt Ruecklauf Richtung `0` je Betrag der aktuellen Lage:
- `|value| >= 90`: `0.40 / tick`
- `80 <= |value| <= 89`: `0.20 / tick`
- `70 <= |value| <= 79`: `0.10 / tick`
- `60 <= |value| <= 69`: `0.05 / tick`
- `50 <= |value| <= 59`: `0.02 / tick`
- `|value| < 50`: `0.00 / tick`
- Vorzeichen bleibt beim Ruecklauf erhalten, bis `0` erreicht ist.

Tick- und Zeitmodell
--------------------
- Referenz: `24` Ticks pro Tag.
- Jede Bewegung protokolliert `day`, `tick`, `event_id`.
- Ist-Stand wird aus letzter Mutation plus Tick-Ruecklauf rekonstruiert.

Bias-Profile (Observer)
-----------------------
- `misstrauen`
- `fraktionsloyalitaet`
- `trauma_sensitivitaet`
- `autoritaetsakzeptanz`
- Bias wirkt nur ueber dokumentierte Faktoren in `applied_rules[]`.

Event-Taxonomie
---------------
- `support`, `betrayal`, `promise_kept`, `promise_broken`, `resource_share`, `resource_denial`, `rescue`, `harm`, `coerce`, `deescalate`, `escalate`, `intel_share`, `intel_hide`

Skalen fuer Event-Scores
------------------------
- `intent_score`: `-100 .. +100`
- `impact_score`: `-100 .. +100`
- `norm_event_score`: `-100 .. +100`
- `certainty`: `0.0 .. 1.0`

Startparameter (Default)
------------------------
- `step_limit_xy = 6`
- `step_limit_z = 5`
- `step_limit_normtreue = 4`
- `deadband_xy = 6`
- `soft_zone = 85`
- `streak_boost_ab = 3`
- `streak_boost_factor = 1.25`
- `w_intent = 0.45`
- `w_impact = 0.55`
- `w_normtreue = 0.30`

Relationsnahe Zusatzdimensionen (Pflicht)
-----------------------------------------

- `einfluss` (`-100 .. +100`): wahrgenommene Wirksamkeit in Entscheidungen/Netzwerken.
- `bedrohung` (`-100 .. +100`): wahrgenommene Gefaehrdung fuer den Observer.

Bezug zu AI-Behavior-Mapping
----------------------------
- Adapterpflicht fuer `O,E,M,N,C,S,L,T` und Modifikatoren.
- Default-Mapping:
- `L/E` staerken `vertrauen` und `kooperationsneigung`.
- `M` staerkt `machtprojektion`, erhoeht kontextabhaengig `konfliktneigung`.
- `C/N` erhoehen `volatility`.
- Modifikatoren (`k`, `p`, `r` usw.) wirken als Multiplikatorfaktoren im Auditpfad.

Testpflicht
-----------
- Pflichtlauf je `policy_version`:
- `20` Events mit festem Seed.
- mindestens ein Szenario je Domain (`sicherheit`, `versorgung`, `diplomatie`, `technik`, `persoenlich`).
- Pflichtszenario: `Buero -> Tunnel` mit `ronja-kerschner` als Observer.

KPI-Zielkorridore
-----------------
- `flip_rate_neutral`: `0.10 .. 0.35`
- `avg_step_size`: `1.5 .. 4.5`
- `extreme_time_ratio`: `< 0.20`
- `misinterpretation_rate`: `0.15 .. 0.45`

Audit- und Runbook-Pflicht
--------------------------
- Jede Mutation schreibt `reason_codes[]` und `applied_rules[]`.
- Incident-Playbook fuer Drift-Ausreisser vorhanden.
- Rollback auf letzte stabile `policy_version` dokumentiert.

Kurzbeispiel (Instanz)
----------------------

```json
{
  "observer_id": "char:ronja-kerschner",
  "target_id": "char:jonas-merek",
  "target_type": "character",
  "policy_version": "v0.1.0",
  "x": 14.0,
  "y": 22.0,
  "z": 11.0,
  "normtreue": 18.0,
  "vertrauen": 42.0,
  "loyalitaet": 36.0,
  "ansehen": 48.0,
  "ruf": 12.0,
  "machtprojektion": 9.0,
  "kooperationsneigung": 44.0,
  "konfliktneigung": -8.0,
  "einfluss": 15.0,
  "bedrohung": -12.0,
  "relation_status": "kooperativ",
  "pos_streak": 2,
  "neg_streak": 0,
  "confidence": 0.68,
  "volatility": 0.33,
  "last_updated": "2026-02-24T12:03:00+01:00",
  "event_id": "evt:tunnel-shift-0007",
  "reason_codes": ["support", "promise_kept"],
  "applied_rules": ["R-PIPE-BASE", "R-CLAMP", "R-STATUS-MAP"],
  "top_contributors": ["resource_share", "safe_return"]
}
```
