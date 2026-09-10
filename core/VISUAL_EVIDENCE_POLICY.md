# Product Governance Visual Engineering Evidence Policy

Version: 0.1.0-alpha
Protocol: DELIVERY-LIFECYCLE-1.0
Authority: `zhouzengrui369-commits/knowme-ecosystem#39`

## Purpose

Product Governance must classify visual-product work before Engineering Delivery begins and must ensure the frozen `engineering_required` evidence contract requires Engineering Delivery to personally inspect human-reviewable visual evidence before `ENGINEERING_READY`.

```text
CODE_PASS
TEST_PASS
GATE_PASS
LOCAL_AGENT_PASS
!= ENGINEERING_ACTUALLY_INSPECTED_PRODUCT_OUTPUT
```

## Visual work classification

`VISUAL_WORK_CLASS=YES` whenever the frozen work materially includes one or more of:

```text
VISUAL_BASELINE
DEMO_RETURN
UI
LAYOUT
PRODUCT_SHELL
VISUAL_INHERITANCE
RESPONSIVE_LAYOUT
2D_3D_VISUAL_BEHAVIOR
INTERACTION_CONTINUITY
ANIMATION_OR_MOTION
```

Equivalent project-specific categories may be added. Product Governance must not classify obviously visual work as non-visual merely to bypass this gate.

## Required frozen evidence fields

For `VISUAL_WORK_CLASS=YES`, the Goal/Milestone Contract or approved exact addendum must classify these as `engineering_required`:

```text
ENGINEERING_VISUAL_EVIDENCE_REQUIRED=YES
HUMAN_REVIEWABLE_VISUAL_EVIDENCE=COMPLETE
ENGINEERING_VISUAL_EVIDENCE_INSPECTED=YES
ENGINEERING_PERSONAL_EVIDENCE_INSPECTION_REQUIRED=YES
ENGINEERING_VISUAL_CONFORMANCE=PASS
TEXT_RECEIPT_ONLY_SUFFICIENT=NO
LOCAL_AGENT_SELF_DECLARED_VISUAL_PASS_SUFFICIENT=NO
```

Product Governance defines which visual requirements, viewports, product states, Demo/reference states and interaction states must be evidenced. Engineering Delivery owns the visual Engineering adjudication.

## Minimum human-reviewable evidence package

The frozen contract must require, as applicable:

1. Demo/reference ↔ candidate paired screenshots;
2. complete screenshots of core product pages/surfaces;
3. key interaction before/after captures;
4. contact sheet and/or video/continuous capture for dynamic interaction;
5. protected responsive viewports;
6. visual difference index;
7. exact candidate identity;
8. SHA256 evidence-integrity manifest;
9. source/test/runtime evidence mapping.

Each item/index entry must identify enough metadata to answer:

```text
WHAT_AM_I_LOOKING_AT
WHICH_CANDIDATE
WHICH_VIEWPORT
WHICH_PRODUCT_STATE
WHICH_REQUIREMENT
WHICH_DEMO_REFERENCE
WHAT_DIFFERENCE_IS_VISIBLE
WHAT_AUTHORITY_MAY_ALLOW_THE_DIFFERENCE
```

Before Engineering Delivery views the evidence, the difference index must use:

```text
ENGINEERING_ADJUDICATION=PENDING
```

## Candidate Admission intake

For visual work, Product Governance must not begin Candidate Admission unless the fresh Engineering Ready package includes:

```text
ENGINEERING_VISUAL_EVIDENCE_REQUIRED=YES
HUMAN_REVIEWABLE_VISUAL_EVIDENCE=COMPLETE
ENGINEERING_VISUAL_EVIDENCE_INSPECTED=YES
ENGINEERING_PERSONAL_EVIDENCE_INSPECTION_REQUIRED=YES
ENGINEERING_VISUAL_CONFORMANCE=PASS
ENGINEERING_VISUAL_EVIDENCE_REFS=<exact durable refs>
ENGINEERING_VISUAL_EVIDENCE_SHA256_MANIFEST_REF=<exact ref>
```

Product Governance verifies presence, exact identity binding and contract coverage. It does **not** re-perform or substitute for the Engineering visual adjudication.

Missing required visual fields means:

```text
CANDIDATE_ADMISSION_BLOCKED=YES
```

not a partial PASS.

## Mid-line evidence requirement changes

If the Human Owner/Product Governance adds or changes a visual Engineering evidence requirement after an Engineering Ready terminal, and that change affects `engineering_required` evidence or the Engineering Ready close condition:

```text
APPROVED_CHANGE_REQUEST
→ FREEZE_EXACT_ADDENDUM_OR_SUCCESSOR_CONTRACT
→ HOLD_OR_INVALIDATE_CURRENT_FORWARD_PROGRESSION_STATE
→ FRESH_INDEPENDENT_ENGINEERING_DELIVERY_REENTRY
```

The earlier Engineering terminal remains immutable and historically valid under the rule in force when it was issued unless an independent contemporaneous defect already made it invalid.

Product Governance must not rewrite the historical terminal to claim it was invalid at issuance merely because a stricter successor rule now exists.

## Exact-SHA evidence reuse

An evidence-only fresh Engineering re-entry may reuse existing exact-SHA technical evidence only by fresh Engineering adjudication when:

```text
CANDIDATE_SHA_UNCHANGED
AND EVIDENCE_IDENTITY_MATCHES
AND NO_RUNTIME_OR_SOURCE_DRIFT
```

Product Governance may authorize this bounded reuse in the addendum/handoff but may not declare reused technical evidence sufficient on Engineering's behalf.

## Local Agent boundary

Local Agent may capture, record, package, hash, sanitize and return visual evidence under the exact request. It may not declare Demo return, visual parity, Product Experience or Human Owner acceptance.

The visual-evidence rule grants no Local Agent source/test/commit/push/PR/governance mutation or repair authority.

Human-reviewable evidence must be attached to the authoritative Issue/PR or stored independently with exact references and integrity hashes. Do not commit visual evidence into the product candidate if doing so changes the candidate SHA being evidenced.

## Non-equivalence

```text
LOCAL_AGENT_OBSERVATION
!= ENGINEERING_ADJUDICATION
ENGINEERING_VISUAL_CONFORMANCE_PASS
!= CANDIDATE_ADMITTED
!= PRODUCT_REVIEW_ELIGIBLE
!= PRODUCT_EXPERIENCE_PASS
!= DEMO_RETURN_ACCEPTED
!= HUMAN_OWNER_ACCEPTED
!= RELEASE_AUTHORIZED
!= GOAL_MILESTONE_CLOSED
```
