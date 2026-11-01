#!/usr/bin/env python3
"""Verify the exact audited M54 evidence ZIP and its public manifest.

Uses only the Python standard library. It does not rerun the scientific experiment.
"""
from __future__ import annotations
import hashlib, json, sys, zipfile
from pathlib import Path

EXPECTED_BYTES = 32_734_870
EXPECTED_SHA256 = "a91f2d714ba9421566635bcabe7953799c0706586975b1eac84d2e9ea5f439a2"
MANIFEST = "PUBLIC_MANIFEST_SHA256.json"

def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    raise SystemExit(1)

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 verification/verify_artifact.py evidence/HCC_M54_...zip")
        raise SystemExit(2)
    path = Path(sys.argv[1])
    if not path.is_file():
        fail(f"not found: {path}")
    size = path.stat().st_size
    digest = sha256_file(path)
    print(f"Outer ZIP bytes:   {size:,}")
    print(f"Outer ZIP SHA-256: {digest}")
    if size != EXPECTED_BYTES:
        fail(f"outer byte length differs from expected {EXPECTED_BYTES:,}")
    if digest != EXPECTED_SHA256:
        fail("outer SHA-256 differs from the manuscript-bound value")

    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        if len(names) != len(set(names)):
            fail("duplicate ZIP member names detected")
        if MANIFEST not in names:
            fail(f"missing {MANIFEST}")
        manifest = json.loads(z.read(MANIFEST))
        failures = []
        for name, spec in manifest.items():
            if name not in names:
                failures.append(f"missing: {name}")
                continue
            data = z.read(name)
            if len(data) != int(spec["bytes"]):
                failures.append(f"byte mismatch: {name}")
            if sha256_bytes(data) != spec["sha256"]:
                failures.append(f"hash mismatch: {name}")
        undeclared = sorted(set(names) - set(manifest) - {MANIFEST})
        if failures:
            for x in failures:
                print("  ", x)
            fail(f"{len(failures)} manifest verification failure(s)")
        if undeclared:
            fail(f"undeclared ZIP member(s): {undeclared}")
        print(f"Unique ZIP members: {len(names)}")
        print(f"Manifest payloads:  {len(manifest)}/{len(manifest)} verified")
        print("Undeclared scientific payloads: 0")
    print("PASS: artifact bytes and all public-manifest payloads verify.")

if __name__ == "__main__":
    main()
