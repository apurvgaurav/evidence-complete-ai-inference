#!/usr/bin/env python3
"""Recompute the paper's principal finite counts from the normalized M54 record.

Uses only Python's standard library and reads directly from the audited ZIP.
It does not rerun inference or modify evidence.
"""
from __future__ import annotations
import collections, json, sys, zipfile
from pathlib import Path

NORMALIZED = "analysis_NORMALIZED_EPISODES.ndjson"
JOURNAL = "CONTINUATION_DISPATCH_JOURNAL.ndjson"
ARMS = ["C0_PREFIX", "C1_QUIESCENCE", "C2_RECB", "B3_PREFIX", "B3_COMPLETE"]
DISPLAY = {
    "C0_PREFIX": "C0 prefix",
    "C1_QUIESCENCE": "C1 quiescence",
    "C2_RECB": "C2 complete",
    "B3_PREFIX": "B3 prefix",
    "B3_COMPLETE": "B3 complete",
}

def load_ndjson(z, name):
    return [json.loads(x) for x in z.read(name).decode("utf-8").splitlines() if x.strip()]

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 verification/recompute_primary_results.py evidence/HCC_M54_...zip")
        raise SystemExit(2)
    path = Path(sys.argv[1])
    with zipfile.ZipFile(path) as z:
        rows = load_ndjson(z, NORMALIZED)
        journal = load_ndjson(z, JOURNAL)

    assert len(rows) == 3000, len(rows)
    assert len({r["episode_id"] for r in rows}) == 3000
    assert {r["execution_ordinal"] for r in rows} == set(range(1, 3001))
    assert sum(bool(r["evidence_coverage"]) for r in rows) == 3000
    assert sum(bool(r["unknown"]) for r in rows) == 0
    assert sum(bool(r["contradictory_evidence"]) for r in rows) == 0
    assert sum(bool(r["outside_domain"]) for r in rows) == 0
    assert sum(bool(r["fault_reached"]) for r in rows) == 960
    assert sum(bool(r["fault_not_reached"]) for r in rows) == 240
    assert sum(bool(r["closed_no_effect"]) for r in rows) == 1141

    print("Core accounting")
    print("---------------")
    print("episodes:            3000/3000")
    print("unique episode IDs:  3000")
    print("evidence coverage:   3000/3000")
    print("unknown:             0")
    print("contradictory:       0")
    print("outside-domain:      0")
    print("fault reached:       960")
    print("fault not reached:   240")
    print("closed no effect:    1141")

    print("\nPrimary outcomes (Table 3)")
    print("--------------------------")
    expected_invalid = {"C0_PREFIX":179, "C1_QUIESCENCE":120, "C2_RECB":0, "B3_PREFIX":240, "B3_COMPLETE":0}
    expected_valid = {"C0_PREFIX":240, "C1_QUIESCENCE":240, "C2_RECB":240, "B3_PREFIX":300, "B3_COMPLETE":300}
    for arm in ARMS:
        inv = [r for r in rows if r["arm"] == arm and r["source_state"] == "PREEXISTING_INVALID"]
        val = [r for r in rows if r["arm"] == arm and r["source_state"] == "VALID"]
        inv_n = sum(int(r["source_invalid_acceptance"] or 0) for r in inv)
        val_n = sum(int(r["valid_source_delivery"] or 0) for r in val)
        assert len(inv) == 300 and len(val) == 300
        assert inv_n == expected_invalid[arm], (arm, inv_n)
        assert val_n == expected_valid[arm], (arm, val_n)
        print(f"{DISPLAY[arm]:14s} invalid {inv_n:3d}/300   valid {val_n:3d}/300")

    print("\nInvalid-source acceptance by cell (Table 4)")
    print("-------------------------------------------")
    for cell in ["I0", "Ishort", "Ilong", "Ilong-R0", "Ilong-R2"]:
        vals = []
        for arm in ARMS:
            ss = [r for r in rows if r["cell_id"] == cell and r["arm"] == arm]
            assert len(ss) == 60
            vals.append(sum(int(r["source_invalid_acceptance"] or 0) for r in ss))
        print(f"{cell:10s}: " + "  ".join(f"{DISPLAY[a]}={v}/60" for a, v in zip(ARMS, vals)))

    print("\nValid-source delivery by cell (Table 5)")
    print("---------------------------------------")
    for cell in ["V0", "Vshort", "Vlong", "Vlong-R0", "Vlong-R2"]:
        vals = []
        for arm in ARMS:
            ss = [r for r in rows if r["cell_id"] == cell and r["arm"] == arm]
            assert len(ss) == 60
            vals.append(sum(int(r["valid_source_delivery"] or 0) for r in ss))
        print(f"{cell:10s}: " + "  ".join(f"{DISPLAY[a]}={v}/60" for a, v in zip(ARMS, vals)))

    r367 = [r for r in rows if r["execution_ordinal"] == 367]
    assert len(r367) == 1
    r = r367[0]
    assert r["arm"] == "C0_PREFIX" and r["cell_id"] == "Ishort" and r["modality"] == "vision"
    assert r["source_reference_status"] == "REJECT_SEMANTIC" and r["source_invalid_acceptance"] == 0
    assert r["recipient_attempt_count"] == 0 and r["evidence_coverage"] is True
    print("\nOrdinal 367 boundary case")
    print("-------------------------")
    print(f"arm={r['arm']} cell={r['cell_id']} modality={r['modality']}")
    print(f"source={r['source_reference_status']} invalid_acceptance={r['source_invalid_acceptance']}")
    print(f"recipient_attempt_count={r['recipient_attempt_count']} evidence_coverage={r['evidence_coverage']}")

    kinds = collections.Counter(e["kind"] for e in journal)
    assert kinds["SLOT_RESERVED"] == 2999
    assert kinds["EXECUTOR_DISPATCH_INTENT"] == 2999
    assert kinds["EXECUTOR_RETURNED"] == 2999
    assert kinds.get("EXECUTOR_FAILED", 0) == 0
    print("\nContinuation journal")
    print("--------------------")
    print(f"SLOT_RESERVED={kinds['SLOT_RESERVED']}")
    print(f"EXECUTOR_DISPATCH_INTENT={kinds['EXECUTOR_DISPATCH_INTENT']}")
    print(f"EXECUTOR_RETURNED={kinds['EXECUTOR_RETURNED']}")
    print(f"EXECUTOR_FAILED={kinds.get('EXECUTOR_FAILED', 0)}")
    print("\nPASS: primary manuscript counts reproduced directly from normalized evidence.")

if __name__ == "__main__":
    main()
