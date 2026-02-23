---
stand: 2026-02-23 03:24
update: Frische-Review durchgeführt; Spannungs-/PsyLink-Referenzen gegen SSOT geprüft (kein Kanon-Delta).
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/00-admin/Ereignislog-Weltgeschehen.md' 'novapolis-rp/database-rp/00-admin/Cluster-Index.md' 'novapolis-rp/database-rp/00-admin/Missionslog.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-23 03:25); .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py 'novapolis-rp/database-rp/00-admin/Ereignislog-Weltgeschehen.md' 'novapolis-rp/database-rp/00-admin/Cluster-Index.md' 'novapolis-rp/database-rp/00-admin/Missionslog.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-23 03:25); npm --prefix novapolis-rp/coding/tools/validators run validate:rp PASS (2026-02-23 03:25)
slug: cluster_index_v1
category: admin
status: review
version: "0.2"
---

Cluster-Index (v1)
==================

Zweck
-----
- Referenz für Fraktions- und Cluster-Signaturen (Eisenkonklave, Arkologie, Händlerbund, Schienenbund).
- Liefert die Diplomatie-/Prioritätswerte aus `database-raw/99-exports/RAW-canvas-2025-10-16T16-55-00-000Z.txt`.
- Ergänzt `AI-Behavior-Mapping.md` um Cluster-spezifische Kontextdaten (z. B. Konfliktpotenziale, Führungen, aktive Systeme).

Verifizierungsrahmen (Kanon)
----------------------------
- SSOT-Priorität: kuratierte RP-Dateien in `database-rp/**` schlagen unklare RAW-Reste in der operativen Lesart.
- PsyLink-/Dissonanz-Schwellen kommen aus [AI-Behavior-Mapping](./AI-Behavior-Mapping.md#psymatrix-abgleich-routine).
- Relationen/Handelslagen werden nur mit belegten Fraktions-Relationslogs bewertet:
  - [Relationslog-Novapolis](../01-factions/novapolis/06-handel-diplomatie/Relationslog-Novapolis.md)
  - [Relationslog-Eisenkonklave](../01-factions/eisenkonklave/06-handel-diplomatie/Relationslog-Eisenkonklave.md)
  - [Handel-Diplomatie-Haendlergilde](../01-factions/haendlerbund/06-handel-diplomatie/Handel-Diplomatie-Haendlergilde.md)

Aktueller Stand
---------------
- Cluster `eisenkonklave_operativ`: Priorität mittel, Systeme `relationslog_eisenkonklave_v1`, `handelslog_eisenkonklave_v1`.
- Cluster `arkologie_a1`: Priorität mittel, Systeme `relationslog_arkologie_v1`.
- Cluster `schattenbund_feld` (Schienenbund): Priorität mittel, Systeme `relationslog_schattenbund_v1`.
- Cluster `haendlergilde_extern` (Händlerbund): Priorität niedrig, Systeme `relationslog_haendlergilde_v1`, `handelslog_haendlergilde_v1`.

Spannungen (evidenzgebunden)
----------------------------

| Paarung | Kanonische Evidenz | Lageeinschätzung | Stand |
| --- | --- | --- | --- |
| Novapolis ↔ Händlerbund | [Relationslog-Novapolis](../01-factions/novapolis/06-handel-diplomatie/Relationslog-Novapolis.md), [Handel-Diplomatie-Haendlergilde](../01-factions/haendlerbund/06-handel-diplomatie/Handel-Diplomatie-Haendlergilde.md) | kooperativ im Aufbau bei kontrollierter Informationspolitik (`[SECRECY]`) | teilverifiziert |
| Novapolis ↔ Eisenkonklave | [Relationslog-Novapolis](../01-factions/novapolis/06-handel-diplomatie/Relationslog-Novapolis.md), [Relationslog-Eisenkonklave](../01-factions/eisenkonklave/06-handel-diplomatie/Relationslog-Eisenkonklave.md) | neutral bis wachsam; Konfliktpotenzial benannt, kein akuter Bruch belegt | teilverifiziert |
| Eisenkonklave ↔ Schienenbund | [Relationslog-Eisenkonklave](../01-factions/eisenkonklave/06-handel-diplomatie/Relationslog-Eisenkonklave.md) | feindselige Tendenz im Eisenkonklave-SSOT vermerkt | teilverifiziert |
| Arkologie-Bezüge | [Relationslog-Eisenkonklave](../01-factions/eisenkonklave/06-handel-diplomatie/Relationslog-Eisenkonklave.md), [Relationslog-Novapolis](../01-factions/novapolis/06-handel-diplomatie/Relationslog-Novapolis.md) | keine belastbare direkte Interaktion im Novapolis-SSOT; regionaler Einflussfaktor bleibt offen | offen |

PsyLinks & Dissonanz-Gate
-------------------------

| Prüffeld | Regel | Status |
| --- | --- | --- |
| PsyLink-Zuordnung | Meta-Cluster nutzt Anchor-/PsyLink-Referenzen aus `meta_cluster_index_v1` als Rohbasis; operative Auslegung erfolgt über kuratierte SSOT-Artefakte | aktiv |
| `PsySignatur_Dissonanz` | > 0.25 triggert Moderation/Deeskalation vor Eskalationspfaden | aktiv |
| Kohäsion | < 0.60 erhöht Konfliktgewichtung in Dialog-/Lageableitungen | aktiv |
| Priorisierung | Cluster mit Priorität `hoch` werden vor nachgelagerten Szenarioableitungen geprüft | aktiv |

Abgleich zu AI-Behavior-Mapping
-------------------------------
- Schwellen und Drift-Logik sind in [AI-Behavior-Mapping](./AI-Behavior-Mapping.md#psymatrix-abgleich-routine) als verbindliche Routine dokumentiert.
- Dieser Index führt keine eigenen numerischen Driftwerte ein, sondern verweist auf die dortigen Guardrails.

Offene Verifikation
-------------------
- Fehlende fraktionsübergreifende Normalform (einheitliche Diplomatie-Skala über alle Relationslogs).
- Arkologie-/Schienenbund-Beziehungen benötigen zusätzliche belegte Missions-/Ereignisanker, bevor eine harte Spannungswertung gesetzt wird.
- Bei neuen Belegen zuerst Fraktions-SSOT aktualisieren, danach Cluster-Index nachziehen (kein inverser Kanonfluss).

ToDo
----
- Nächste Ausbaustufe: einheitliche Diplomatie-Skala je Paarung (numerisch + textlich) auf Basis verifizierter Fraktionslogs.
- Missionslog-/Ereignislog-Anker für Arkologie und Schienenbund ergänzen, sobald belastbare Evidenz vorliegt.
- Validierungsintervall (7 InGame-Tage) mit konkretem Prüfrun im Workflow verankern.
