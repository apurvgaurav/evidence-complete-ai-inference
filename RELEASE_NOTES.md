# v1.0-hcc-submission

Reproducibility artifact accompanying **Evidence-Complete Admission and Durable Recovery in AI Inference Services**.

## Release asset

Attach exactly:

`HCC_M54_MAC_PUBLIC_RETURN_ea84833e-cb15-4099-8f99-26415c4861ca.2.zip`

Expected size: **32,734,870 bytes**

SHA-256:

`a91f2d714ba9421566635bcabe7953799c0706586975b1eac84d2e9ea5f439a2`

Do not unzip/re-zip or edit the archive before attaching it.

## Verification

After downloading the release asset:

```bash
python3 verification/verify_artifact.py evidence/HCC_M54_MAC_PUBLIC_RETURN_ea84833e-cb15-4099-8f99-26415c4861ca.2.zip
python3 verification/recompute_primary_results.py evidence/HCC_M54_MAC_PUBLIC_RETURN_ea84833e-cb15-4099-8f99-26415c4861ca.2.zip
```

These scripts inspect the frozen evidence and reproduce the primary finite counts; they do not rerun the experiment.
