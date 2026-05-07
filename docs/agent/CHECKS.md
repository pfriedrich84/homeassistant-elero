# Agent Checks

Validation commands for agents. Run the smallest relevant set before finishing changes, and report what passed or failed.

## Documentation-only changes

From the repository root:

```bash
python3 scripts/check_markdown_links.py
```

Use when changing Markdown files, docs indexes, or agent/tool instruction shims.

## Python syntax safety

From the repository root:

```bash
python3 -m compileall custom_components tests scripts
```

Use when changing Python files or validation scripts. This checks syntax without requiring Home Assistant to be installed.

## Python tests

From the repository root, when test dependencies are installed:

```bash
python3 -m pytest
```

Use when changing integration behavior, config flows, entities, services, or tests. The repository currently has a placeholder test plan; add/adjust tests as implementation grows.

## Linting

From the repository root, when Ruff is installed:

```bash
ruff check .
```

Use when changing Python code or build configuration. Ruff settings live in [`../../pyproject.toml`](../../pyproject.toml).

## HACS/Home Assistant packaging review

For integration packaging changes, inspect:

```text
custom_components/elero/manifest.json
hacs.json
README.md
docs/user/HACS.md
```

Use when changing metadata, domain names, integration layout, HACS requirements, or installation docs.
