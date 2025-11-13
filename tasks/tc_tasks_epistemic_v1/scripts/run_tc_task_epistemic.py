#!/usr/bin/env python3
"""Run a Truth Capsules Task (epistemic-focused helper).

This minimal helper:
- loads a task YAML definition from tasks/
- fills its args_template with the provided question
- executes the configured engine.entrypoint via subprocess

It is intentionally small; adapt it to your own routing, logging,
and security needs.
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover
    print("ERROR: PyYAML is required: pip install pyyaml", file=sys.stderr)
    sys.exit(1)


ROOT = Path(__file__).resolve().parents[1]
TASKS_DIR = ROOT / "tasks"


def load_task(task_id: str) -> dict:
    fname = TASKS_DIR / f"{task_id}.yaml"
    if not fname.exists():
        # also allow dots -> underscores in filename mapping if desired
        alt = TASKS_DIR / f"{task_id.replace('.', '_')}.yaml"
        if alt.exists():
            fname = alt
        else:
            raise FileNotFoundError(f"Task file not found for id {task_id}: {fname}")
    with fname.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def render_args_template(template: str, task: dict, question: str) -> str:
    # Very small, safe-ish templater for our needs.
    # Supports:
    #   {{input.question}}
    #   {{bindings.default_profile}}
    #   {{bindings.default_bundle}}
    # Environment variables like ${LLM_MODEL:-gpt-4o-mini} are delegated
    # to the shell, not expanded here.
    mapping = {
        "input.question": question,
        "bindings.default_profile": task.get("bindings", {}).get("default_profile", ""),
        "bindings.default_bundle": task.get("bindings", {}).get("default_bundle", ""),
    }

    out = template
    for key, value in mapping.items():
        out = out.replace("{{" + key + "}}", value)
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description="Run a Truth Capsules Task")
    ap.add_argument(
        "--task-id",
        required=True,
        help="Task id (e.g., task.epistemic.multi_lens_analysis_v1).",
    )
    ap.add_argument(
        "--question",
        required=True,
        help="Original question / problem statement.",
    )
    ap.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the command instead of executing it.",
    )
    args = ap.parse_args()

    task = load_task(args.task_id)

    engine = task.get("engine", {})
    entrypoint = engine.get("entrypoint")
    template = engine.get("args_template", "")

    if not entrypoint:
        print("ERROR: task has no engine.entrypoint", file=sys.stderr)
        sys.exit(1)

    arg_str = render_args_template(template, task, args.question).strip()
    # Split on whitespace for now; for more complex needs use shlex.split
    import shlex
    extra_args = shlex.split(arg_str)

    cmd = [entrypoint] + extra_args

    if args.dry_run:
        print(" ".join(cmd))
        return

    proc = subprocess.Popen(cmd)
    proc.wait()
    sys.exit(proc.returncode)


if __name__ == "__main__":
    main()
