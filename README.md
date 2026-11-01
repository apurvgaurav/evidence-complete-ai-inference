# Evidence-Complete Admission and Durable Recovery in AI Inference Services

Reproducibility artifact for the manuscript **Evidence-Complete Admission and Durable Recovery in AI Inference Services**, prepared for submission to *High-Confidence Computing*.

## Core claim

This study separates two system properties that are easy to conflate:

- **Admission correctness:** does the evidence available at authorization justify the effect?
- **Durable recovery:** will an already-authorized effect survive a source-side failure?

A recovery mechanism can faithfully recover the wrong decision. In the frozen study, evidence-complete admission blocked all scheduled preexisting-invalid releases, while durable-origin state recovered valid effects after source-response loss and also recovered invalid effects that had already been authorized under prefix admission.

## Study snapshot

- 3,000 scheduled episodes; 3,000 retained.
- 60 immutable input clusters: 30 text and 30 vision.
- 10 source/disclosure/recovery cells × 5 release arms.
- Exactly one genuine model forward per scheduled episode.
- Evidence coverage: 3,000/3,000.
- Unknown, contradictory, outside-domain outcomes: 0.
- Audited M54 evidence ZIP SHA-256: `a91f2d714ba9421566635bcabe7953799c0706586975b1eac84d2e9ea5f439a2`.

## Verify the paper in five minutes

The exact audited evidence ZIP will be attached to the GitHub Release tagged `v1.0-hcc-submission`.

Expected asset name:

`HCC_M54_MAC_PUBLIC_RETURN_ea84833e-cb15-4099-8f99-26415c4861ca.zip`

After downloading it into `evidence/`, run:

```bash
python3 verification/verify_artifact.py evidence/HCC_M54_MAC_PUBLIC_RETURN_ea84833e-cb15-4099-8f99-26415c4861ca.zip
python3 verification/recompute_primary_results.py evidence/HCC_M54_MAC_PUBLIC_RETURN_ea84833e-cb15-4099-8f99-26415c4861ca.zip
```

The scripts require Python 3.10+ and use only the standard library. They do **not** rerun the scientific experiment.

Expected headline results:

| Arm | Invalid-source acceptance | Valid-source delivery |
|---|---:|---:|
| C0 prefix | 179/300 | 240/300 |
| C1 quiescence | 120/300 | 240/300 |
| C2 complete | 0/300 | 240/300 |
| B3 prefix | 240/300 | 300/300 |
| B3 complete | 0/300 | 300/300 |

## Repository map

- `verification/` — standard-library verification and result-recomputation scripts.
- `evidence/` — exact evidence-package identity and download instructions.
- `protocol/` — map to frozen protocol artifacts inside the evidence ZIP.
- `environment/` — execution-environment and offline-control summary.
- `ARTIFACT_MANIFEST.md` — reviewer-oriented evidence-to-claim map.
- `CITATION.cff` — citation metadata.

## Scientific boundary

This is a finite descriptive mechanism study, not a claim about deployment prevalence or production-scale performance. The contract assumes a finite declared producer roster, truthful captured records, one genuine forward per request/epoch, and a valid or wrong-parent terminal selection. Unknown/unregistered producers, Byzantine finality, multiple genuine executions, arbitrary delegation trees, and production latency/cost are outside the current experimental contract.

## Post-start implementation correction

Ordinal 1 exposed a normalizer defect. It was preserved and never rerun. The M53 continuation failed before READY and consumed zero new scientific cases. M54 changed only the continuation child-service target and executed untouched ordinals 2–3000. The evidence package contains the correction chronology, code manifests, failure audits, run journal, and before/after repository guards. No cohort member, arm, cell, seed, threshold, endpoint, or observed outcome was changed.

## Data redistribution

Raw corpus objects whose redistribution basis was not established are intentionally not included. The artifact retains source identifiers, hashes, acquisition references, runtime/model pins, preprocessing information, and transformations needed for audit/reconstruction subject to the original data providers' terms.

## License

No repository-wide license has been granted yet. Third-party models, datasets, software, documentation, and referenced works retain their original terms.
