# Epistemic Engine Tasks – Integration Notes

This directory defines **Tasks** for the Epistemic Engine, which act as
reusable execution recipes binding:

- Inputs (e.g. `question`)
- Truth Capsules profile + bundle
- A concrete runner (`scripts/run_epistemic_engine_llm.py`)
- Output format + schema

## Tasks

- `task.epistemic.multi_lens_analysis_v1`
  - Multi-lens mode: one call per lens + synthesis
  - Best for deep reasoning and downstream tooling

- `task.epistemic.single_shot_epistemic_v1`
  - Single-shot mode: one LLM call returning a full synthesis
  - Best for quick feedback and interactive use

Both tasks assume:

- Epistemic Engine capsules, bundles, and profiles are installed
- `scripts/run_epistemic_engine_llm.py` is available
- The `llm` CLI is installed and configured
- `LLM_MODEL` environment variable is optionally set

---

## CLI Affordance – Run Task

A minimal CLI wrapper can load a task YAML and execute it by filling the
`args_template` with an `input.question` value.

Example usage (conceptual):

```bash
python scripts/run_tc_task_epistemic.py       --task-id task.epistemic.multi_lens_analysis_v1       --question "Should we open source our internal tooling?"
```

The script resolves:

- `bindings.default_profile`
- `bindings.default_bundle`
- `engine.entrypoint`
- `engine.args_template`

and then runs the appropriate shell command.

---

## SPA Affordance – “Run Task…” Button

In the SPA, you can add:

- A dropdown of available `task.*` ids (loaded from `tasks/`)
- A text area for `question`
- A “Run Task” button that, when clicked, either:
  - Shows the fully composed shell command for the user to run locally, or
  - Calls a backend endpoint that invokes `run_tc_task_epistemic.py`.

Minimal frontend shape (pseudo-code):

```js
// given: TASKS is a map of taskId -> task metadata
runTaskBtn.addEventListener('click', () => {
  const taskId = taskSelect.value;
  const question = questionInput.value.trim();
  if (!taskId || !question) return;

  // Option A: just show the shell command for copy-paste
  const cmd = [
    'python scripts/run_tc_task_epistemic.py',
    '--task-id', JSON.stringify(taskId),
    '--question', JSON.stringify(question)
  ].join(' ');

  outputArea.textContent = cmd;
});
```

This keeps the SPA thin: it delegates all execution semantics to the
Truth Capsules + Tasks + Runner stack.
