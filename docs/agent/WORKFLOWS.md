# Agent Workflows

Reusable, tool-neutral workflows for common repository tasks.

## Standard change workflow

1. Read [`RULES.md`](RULES.md) and the relevant docs in [`PROJECT.md`](PROJECT.md).
2. Inspect current state with `git status --short` before editing.
3. Keep the change small and reviewable.
4. Update docs when behavior, architecture, installation, HACS metadata, or validation expectations change.
5. Run relevant checks from [`CHECKS.md`](CHECKS.md).
6. Summarize changed files, validation results, and follow-up work.

## Local CI simulation

Use this when a change touches multiple subsystems or CI configuration.

1. Run the Markdown link check:

   ```bash
   python3 scripts/check_markdown_links.py
   ```

2. Run Python syntax validation:

   ```bash
   python3 -m compileall custom_components tests scripts
   ```

3. If dependencies are installed, run tests and linting:

   ```bash
   python3 -m pytest
   ruff check .
   ```

If one check fails, continue with independent checks where practical so the final report is complete.

## Integration behavior workflow

Use this when changing `custom_components/elero/` behavior.

1. Confirm the change preserves the `elero` domain and HACS layout.
2. Keep Home Assistant setup/config-flow logic separate from Elero protocol/provider logic.
3. Add or update tests for config flow, entity setup, provider validation, or command dispatch where practical.
4. Update user/developer docs if setup, configuration, or architecture changes.
5. Run Python syntax validation and any available tests/lints from [`CHECKS.md`](CHECKS.md).

## Documentation workflow

Use this when reorganizing or adding Markdown.

1. Put agent-only guidance in `docs/agent/`.
2. Put maintainer/contributor details in `docs/developer/`.
3. Put installation, configuration, and user workflows in `docs/user/`.
4. Keep root `README.md` as the human entry point and root `AGENTS.md` as the agent entry point.
5. Run `python3 scripts/check_markdown_links.py`.

## Release/HACS workflow

Use this when preparing releases or HACS changes.

1. Review [`../user/HACS.md`](../user/HACS.md).
2. Check `custom_components/elero/manifest.json`, `hacs.json`, and root `README.md`.
3. Confirm the repository still contains exactly one integration under `custom_components/elero/`.
4. Do not tag, publish, or push releases unless the user explicitly asks.
