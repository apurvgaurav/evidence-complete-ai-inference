# Execution environment and offline controls

The audited continuation records:

- Host platform: `macOS-27.0.1-arm64-arm-64bit-Mach-O`.
- Scientific model-forward runtime: pinned CPython 3.12.13 macOS-aarch64.
- Controller/transport process: Python 3.13.15 (Clang 21.0.0).
- Both model paths were loaded before the first scientific forward.
- All 60 selected inputs were preloaded.
- Zero warm-up forwards were added to the scientific count.
- Automatic retry was disabled.
- M54 host record reports zero package installs and zero downloads.
- `HF_HUB_OFFLINE=1`, `TRANSFORMERS_OFFLINE=1`, `HF_DATASETS_OFFLINE=1`, `TOKENIZERS_PARALLELISM=false`.

Canonical evidence: `HOST_RUNTIME.json`, `OUTER_CONTROLLER_LAUNCH.json`, `MODEL_SERVICE_LIFECYCLE.json`, `protocol_SCIENTIFIC_RUNTIME_PINS.json`, and `protocol_SCIENTIFIC_RUNTIME_INTEGRATION_CONTRACT.json` inside the evidence ZIP.
