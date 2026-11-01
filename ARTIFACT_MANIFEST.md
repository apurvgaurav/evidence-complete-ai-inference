# Artifact manifest and reviewer map

## Exact public evidence object

The manuscript-bound evidence object is:

`HCC_M54_MAC_PUBLIC_RETURN_ea84833e-cb15-4099-8f99-26415c4861ca.zip`

- Bytes: `32,734,870`
- SHA-256: `a91f2d714ba9421566635bcabe7953799c0706586975b1eac84d2e9ea5f439a2`
- Unique ZIP members: `65`
- Manifest-declared payloads: `64/64` verified

The exact ZIP should be attached unchanged to the GitHub Release tagged `v1.0-hcc-submission`. Do not unzip/re-zip or alter it for the manuscript-bound release.

## Evidence-to-claim map

| Reviewer question | Canonical evidence member(s) |
|---|---|
| Was the protocol frozen before scientific execution? | `protocol_FREEZE_DECLARATION.json`, `protocol_FREEZE_SEAL.json` |
| What was selected and scheduled? | `protocol_FROZEN_SELECTION.json`, `protocol_FROZEN_SCHEDULE.json` |
| What are the normalized 3,000 outcomes? | `analysis_NORMALIZED_EPISODES.ndjson` |
| Do the headline counts reproduce? | `analysis_R1_*`, `analysis_R2_*`, `analysis_R3_*`, plus `verification/recompute_primary_results.py` |
| Is timing/evidence coverage complete? | `analysis_R4_TIMING_RESOURCE_AND_EVIDENCE_COVERAGE.json` |
| What happened after ordinal 1? | `amendment_M53_*`, `amendment_M54_*`, `PRIOR_M52_*`, `PRIOR_M53_*` |
| Did ordinals 2–3000 execute exactly once in continuation? | `CONTINUATION_DISPATCH_JOURNAL.ndjson` and manifest |
| Were repository guards preserved? | `MAC_GUARD_BEFORE.json`, `MAC_GUARD_AFTER.json` |
| What runtime was used? | `HOST_RUNTIME.json`, `MODEL_SERVICE_LIFECYCLE.json`, runtime pin files |
| Can every public payload be byte-verified? | `PUBLIC_MANIFEST_SHA256.json` |

## What is intentionally not claimed

This artifact does not establish production prevalence, cloud-scale throughput, adversarial/Byzantine source authority, multi-organization independence, or frontier-model representativeness. Those are outside the frozen study contract.
