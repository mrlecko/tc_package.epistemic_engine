# Epistemic Engine – Truth Capsules Package

This package contains a multi-lens "epistemic engine" for multi-perspective reasoning, structured as a Truth Capsules add-on.

## Contents

- `capsules/epistemic/` – Foundation + individual lens capsules (skeletons)
- `bundles/` – Core and full Epistemic Engine bundles
- `profiles/` – Usage wrappers (multi-lens vs single-lens demos)
- `manifests/` – Ready-to-run scenarios for the SPA / CLI
- `artifacts/examples/epistemic_engine/` – Example prompts/outputs (placeholders)

## How to merge into `truth_capsules`

From the root of your `truth_capsules` repo:

```bash
cp -R /path/to/tc_package.epistemic_engine/{capsules,bundles,profiles,manifests,artifacts} .
```

Then run the usual checks:

```bash
python scripts/capsule_linter.py capsules
python scripts/bundle_linter.py bundles
pytest
```

You can then open the SPA (or use the CLI) and select the Epistemic Engine profile / bundle to run multi-lens analyses.

v0.0.0 - use for inspiration only

