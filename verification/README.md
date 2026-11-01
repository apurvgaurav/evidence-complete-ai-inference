# Verification

These scripts inspect the frozen M54 public evidence package. They do **not** rerun the scientific experiment and use only the Python standard library.

After downloading the release asset into `evidence/`, from the repository root run:

```bash
python3 verification/verify_artifact.py evidence/HCC_M54_MAC_PUBLIC_RETURN_ea84833e-cb15-4099-8f99-26415c4861ca.2.zip
python3 verification/recompute_primary_results.py evidence/HCC_M54_MAC_PUBLIC_RETURN_ea84833e-cb15-4099-8f99-26415c4861ca.2.zip
```

The first command verifies the exact outer ZIP hash/byte length and every payload declared in `PUBLIC_MANIFEST_SHA256.json`.

The second recomputes the main finite counts, Tables 3–5, the ordinal-367 boundary disposition, and continuation-journal event counts.
