---
description: Regeln fuer Mind-Cluster-Governance, Sphaerenbegriff, Entitaetsdatei-Prinzip, Datenpflichten und Validierung.
name: Mind Cluster Instructions
applyTo: novapolis-rp/database-rp/00-admin/mind-cluster-template.md,novapolis-rp/database-rp/01-factions/**/*.md
---

Mind Cluster Governance
=======================

Ziel
----
- Einheitliche Regeln fuer Mind-Cluster-Daten in Novapolis sichern.
- Interpretation minimieren und Reproduzierbarkeit erhoehen.

Begriffsregeln
--------------
- Ab sofort wird nur `Sphaere` verwendet; `Kugel` ist im Scope unzulaessig.
- Dateibezeichnung `relations-` ist im Scope unzulaessig; es gilt `mind-`.
- Datenebenen muessen strikt getrennt bleiben:
- Governance-Teil: verbindliche Regeln und Gates.
- Modul-Part: fachliche Modellierung und Mechanik.

Brainstorming-Modus
-------------------
- Aktive RP-Brainstorming-Dokumente sind Ideenspeicher.
- Inhalte aus dem Brainstorming gelten nicht als Baseline/Spec ohne explizite User-Freigabe im aktuellen Prompt.
- Bei Uebernahme in SSOT muss die Uebernahme als neue verbindliche Regel markiert werden.

Entitaetsdatei-Prinzip (SSOT)
-----------------------------
- Pro Entitaet genau eine Mind-Cluster-Datei (`<slug>-mind-cluster.md`).
- Diese Datei ist die einzige SSOT fuer beziehungsnahe Zustandsdaten dieser Entitaet.
- Charakterdateien duerfen darauf nur referenzieren, nicht duplizieren:
- Beziehungen
- Verhaltenssignatur
- geistnaher Status/Kondition

Sphaerenmodell-Regeln
---------------------
- Wertebereich ist fuer alle relevanten Scores auf `-100 .. +100` begrenzt.
- Drift ist erlaubt und gewuenscht; nur Grenzwerte und Governance begrenzen.
- Ohne externen Impuls driftet jeder Zustand regelgebunden Richtung `0`.
- Bewusstsein hat keinen Direktschreibzugriff auf den inneren Zustand; nur Event-Impulse sind erlaubt.

Pflichtdaten
------------
- Gerichtete Beziehung speichern (`observer -> target`), niemals als ungerichtete Wahrheit.
- Pflichtfelder pro Beziehung:
- `observer_id`, `target_id`, `target_type`, `policy_version`
- `x`, `y`, `z`, `normtreue`
- `vertrauen`, `loyalitaet`, `ansehen`, `ruf`, `machtprojektion`, `kooperationsneigung`, `konfliktneigung`, `einfluss`, `bedrohung`
- `relation_status` mit Enum `neutral|kooperativ|angespannt|feindlich`
- `confidence` und `volatility` als `float` im Bereich `0.0 .. 1.0` (inklusive)
- `pos_streak`, `neg_streak`, `last_updated`, `event_id`
- `reason_codes[]`, `applied_rules[]`, `top_contributors[]`
- `event_id` folgt dem Format `evt:<domain>-<seq>` (Beispiel: `evt:tunnel-shift-0007`)
- `applied_rules[]` darf nur registrierte Rule-IDs enthalten:
- Governance-IDs `R-MCL-*` (aus Regelmatrix)
- Engine-IDs `E-MCL-*` (registriertes Engine-Set)
- Freitext in `applied_rules[]` ist unzulaessig.
- `reason_codes[]` ist taxonomiebasiert:
- Baseline-Form `RC-<event_type>` (z. B. `RC-support`)
- Erweiterungen nur als registrierte Taxonomieeintraege.

Update-Disziplin
----------------
- Deterministische Reihenfolge ist Pflicht:
- Event normalisieren -> Basisdelta -> Streak/Bias -> Confidence -> Limits -> Hard-Rules -> Clamp/Status -> Persist.
- Harte Regeln (Consent/Safety/Authority) duerfen nicht weich ueberstimmt werden.
- Jede Aenderung muss auditierbar sein (Reason Codes + angewandte Regel-IDs).
- Individuelle Entitaetsaktionen im RP sind Mind- und Relationship-relevant zu behandeln, sobald sie eine andere Entitaet, Gruppe oder Fraktion beruehren: Vor der Aktion muessen das handelnde Entitaetsdossier, zugehoeriger Mind-Cluster oder Runtime-Mind-Arbeitsstand und relevante Ziel-Dossiers geladen sein; nach der Aktion werden betroffene Dossierflaechen gemeinsam konsolidiert.
- Wenn die Aktion keine belegbare geistnahe oder relationale Verschiebung erzeugt, wird das als `keine neue Mind-Delta`, `keine neue Relationship-Delta` oder `carry_forward_confirmed` dokumentiert, statt Mind- oder Relationship-Schicht still veralten zu lassen.
- Aggregate Roster wie Bewohnergruppen duerfen als Roster-Traeger laufen, solange keine einzelne Person daraus individuell handelt; sobald eine Person individuell handelt, braucht sie vor dem Zug einen eigenen Entitaets- und Mind-/Runtime-Schnitt.
- Event-Taxonomie ist geschlossen, aber erweiterbar nur mit Registrierungspflicht in dieser Datei; neue Event-Typen sind ohne gleichzeitige Validator-Abdeckung unzulaessig.
- Registrierte Event-Taxonomie (Baseline):
- `support`, `betrayal`, `promise_kept`, `promise_broken`, `resource_share`, `resource_denial`, `rescue`, `harm`, `coerce`, `deescalate`, `escalate`, `intel_share`, `intel_hide`
- Registrierte Reason-Code-Baseline:
- `RC-<event_type>` fuer alle registrierten Event-Typen
- zusaetzlich registrierte Legacy-Migrationscodes: `RC-bootstrap`, `RC-migration_from_character_canvas`
- Bias-/Profilfaktoren sind als externes Profil erlaubt, aber nicht als impliziter Rechenkern dieser Governance zu interpretieren.
- Registriertes Engine-ID-Set (Baseline):
- `E-MCL-PIPE`
- `E-MCL-DRIFT`
- `E-MCL-CONFIDENCE-WEIGHT`
- `E-MCL-LIMITS`
- `E-MCL-CLAMP`
- `E-MCL-STATUS-MAP`
- `E-MCL-HARD-GATE`
- Migrations-/Kompatibilitaetsregel (deterministisch):
- Legacy-Werte ausserhalb von Enum/Range/Taxonomie werden nicht still korrigiert.
- Validator meldet harte Fehler mit Feldpfad und erwartetem Register/Range.
- Migration erfolgt als explizite Datenaenderung mit dokumentierter Rule-/Reason-Trace.

Validierung
-----------
- Pflicht-Gates bei Markdown-Aenderungen im Scope:
- `npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md'`
- `scripts/check_frontmatter.py` (scoped auf geaenderte Dateien)
- Fachvalidierung fuer RP-Dokumente:
- `npm --prefix novapolis-rp/coding/tools/validators run validate:rp`

Aenderungspflichten
-------------------
- Bei mutationalen Aenderungen im Scope ist ein passender DONELOG-Eintrag im selben Lauf Pflicht.
- Bei strukturellen Instruction-Aenderungen ist der Headings-Index im selben Lauf zu aktualisieren.
- Policy-Aenderungen erhoehen `policy_version` semantisch (`vMAJOR.MINOR.PATCH`).

Regelmatrix
-----------
- `id: R-MCL-NAME, priority: 1, scope: mind_cluster, trigger: file_create_or_rename, action: enforce_mind_prefix_naming, validation: no_relations_prefix_remaining_in_scope, exceptions: historical_logs, notes: avoid_misinterpretation`
- `id: R-MCL-TERM, priority: 1, scope: mind_cluster, trigger: content_update, action: enforce_term_sphaere_only, validation: no_kugel_terms_in_scope, exceptions: historical_quotes, notes: terminology_guard`
- `id: R-MCL-MODE, priority: 1, scope: brainstorming, trigger: brainstorming_update, action: keep_ideas_non_binding, validation: no_baseline_without_explicit_user_decision, exceptions: none, notes: prompt_authority`
- `id: R-MCL-SSOT, priority: 1, scope: entity_state, trigger: character_or_cluster_update, action: keep_mind_cluster_as_single_source, validation: no_duplicate_relations_signature_condition_blocks_in_character_file, exceptions: brief_pointer_links, notes: one_entity_one_mind_cluster`
- `id: R-MCL-ACTION-SYNC, priority: 1, scope: entity_action_runtime, trigger: individual_entity_action, action: load_entity_dossier_mind_and_relevant_target_dossiers_before_action_and_persist_joint_post_action_delta_or_no_delta_note, validation: no_individual_action_with_stale_or_missing_mind_or_relationship_runtime_in_entity_dossier, exceptions: pure_self_action_without_external_target_or_aggregate_roster_without_individual_action, notes: entity_mind_and_relationship_entries_are_one_operational_pair_when_other_entities_are_affected`
- `id: R-MCL-REL-SYNC, priority: 1, scope: relationship_runtime, trigger: action_affects_other_entity_group_or_faction, action: update_directed_relationship_entry_in_observer_dossier_or_record_no_relationship_delta, validation: relationship_runtime_matches_mind_delta_or_explicit_carry_forward, exceptions: no_external_target, notes: relationship_entries_remain_runtime_working_state_until_promoted`
- `id: R-MCL-DATA, priority: 1, scope: mind_state, trigger: schema_change_or_write, action: enforce_required_fields_and_directionality, validation: observer_target_fields_present_including_einfluss_bedrohung, exceptions: none, notes: no_global_truth`
- `id: R-MCL-PIPE, priority: 1, scope: update_engine, trigger: event_apply, action: enforce_deterministic_pipeline, validation: ordered_steps_logged, exceptions: none, notes: reproducibility_first`
- `id: R-MCL-HARD, priority: 1, scope: safety_authority, trigger: consent_or_authority_event, action: apply_hard_rules_before_soft_weights, validation: applied_rules_contains_hard_rule, exceptions: none, notes: non_overridable`
- `id: R-MCL-AUDIT, priority: 1, scope: traceability, trigger: state_mutation, action: persist_reason_and_rule_trace, validation: reason_codes_and_applied_rules_present, exceptions: none, notes: explainability`
- `id: R-MCL-VAL, priority: 1, scope: docs_and_rp, trigger: markdown_change, action: run_lint_frontmatter_and_rp_validator, validation: all_required_gates_pass, exceptions: none, notes: gate_discipline`
- `id: R-MCL-IDSET, priority: 1, scope: traceability, trigger: state_mutation, action: enforce_registered_rule_id_sets, validation: applied_rules_only_contains_registered_R_MCL_or_E_MCL_ids, exceptions: none, notes: no_freetext_rule_ids`
- `id: R-MCL-REASON, priority: 1, scope: traceability, trigger: state_mutation, action: enforce_reason_code_taxonomy, validation: reason_codes_follow_registered_taxonomy_with_rc_event_baseline, exceptions: none, notes: no_freetext_reason_codes`
- `id: R-MCL-EVENTREG, priority: 1, scope: event_taxonomy, trigger: event_type_usage_or_extension, action: enforce_closed_but_registerable_taxonomy, validation: event_type_in_registered_set_and_validator_updated_same_change_set, exceptions: none, notes: controlled_extensibility`
- `id: R-MCL-MIG, priority: 1, scope: migration, trigger: legacy_value_detected, action: fail_with_explicit_migration_required, validation: no_silent_autofix_and_auditable_remediation, exceptions: none, notes: deterministic_compatibility`
