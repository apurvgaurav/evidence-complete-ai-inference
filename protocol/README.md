# Frozen protocol map

The canonical protocol files are preserved inside the exact evidence ZIP rather than duplicated here.

Key members include:

- `protocol_FREEZE_DECLARATION.json` — freeze declaration.
- `protocol_FREEZE_SEAL.json` — frozen research-state seal.
- `protocol_PROTOCOL_CORE.json` — source/effect contract and mechanism definitions.
- `protocol_ANALYSIS_PLAN.json` — finite descriptive analysis plan; `p_values=null`, `equivalence_test=null`.
- `protocol_FROZEN_FRAME.json` — eligible frame.
- `protocol_FROZEN_SELECTION.json` — selected 60 clusters.
- `protocol_FROZEN_SCHEDULE.json` — 3,000 scheduled episode identities and arm/cell schedule.
- `protocol_SCIENTIFIC_RUNTIME_PINS.json` — pinned runtime/model details.
- `protocol_SCIENTIFIC_RUNTIME_INTEGRATION_CONTRACT.json` — scientific runtime integration contract.

Use `verification/verify_artifact.py` before interpreting any extracted member.
