# Epistemic Engine – Truth Capsules Package

This package adds a multi-lens **epistemic engine** on top of
`truth_capsules`. It turns your assistant into a configurable
multi-perspective reasoner using composable **lenses**, **bundles**, and **profiles** rather than one giant system prompt.

> **Status:** Early / experimental (v0.0.x).  
> Use for exploration and inspiration; expect breaking changes.

---

## What this package gives you

- A **foundation capsule** that explains the Epistemic Engine methodology.
- A set of **epistemic lenses** (Stoic, Pragmatic, Systems, Phenomenological,
  Adversarial, Dialectical, Execution, Meta, Synthesis).
- A couple of **bundles** that wire those lenses together into an engine.
- Example **profiles** that show how to run:
  - a full multi-lens analysis, or
  - a single lens in isolation.
- Example **manifests** you can load in the SPA / CLI to see it in action.

The goal is to make “multi-perspective reasoning with a proper synthesis step”
a reusable, inspectable part of your Truth Capsules stack.

---

## Contents

- `capsules/epistemic/`  
  Foundation + individual lens capsules (each lens is an informational capsule
  with statement, pedagogy, and assumptions).

- `bundles/`  
  Epistemic Engine bundles (e.g. “core” vs “full” packs of lenses).

- `profiles/`  
  Usage wrappers that define how the engine is projected:
  - multi-lens orchestration;
  - single-lens demo profiles for each perspective.

- `manifests/`  
  Ready-to-run scenarios for the SPA / CLI (engine + bundle + profile +
  example inputs).

- `artifacts/examples/epistemic_engine/`  
  Example prompts/outputs and fixtures (currently placeholders / WIP).

---

## How to merge into `truth_capsules`

From the root of your `truth_capsules` repo:

```bash
cp -R /path/to/tc_package.epistemic_engine/{capsules,bundles,profiles,manifests,artifacts} .
````

Then run the usual checks:

```bash
python scripts/capsule_linter.py capsules
python scripts/bundle_linter.py bundles
pytest
```

If everything passes, you can open the SPA (or use the CLI) and select:

- the **Epistemic Engine profile**, and
    
- one of the **Epistemic Engine bundles**
    

to run multi-lens analyses on your own questions.

---

## Notes & Next Steps

- This is a **minimal basis**, not a finished product.
    
- Expect to:
    
    - tweak lens wording to match your use case,
        
    - adjust bundles (which lenses are included),
        
    - customise profiles for your organisation’s tone and constraints.