# Agent Autoresearch

Optional workflow for autonomous, metric-driven experiment loops. Use it only when the task has a measurable target and repeated iterations are useful.

## Good fits

- Performance or startup-time improvements once the integration has measurable benchmarks.
- Test-suite speed improvements.
- Static-analysis or validation coverage improvements with a stable score.
- Documentation quality experiments when the primary metric is mechanical, such as broken-link count.

## Poor fits

- Documentation-only cleanup without a measurable target.
- Broad subjective refactors without a primary metric.
- Security-sensitive behavior changes without explicit review.
- Hardware/RF behavior changes that require physical devices but lack a safe test harness.

## Required setup

Before starting an experiment loop, define:

1. Primary metric.
2. Benchmark or validation command.
3. Safety checks.
4. Rollback rule.
5. Data and hardware boundary.

## Suggested metrics

- `pytest` duration and pass/fail count once tests exist.
- Ruff violation count.
- Markdown broken-link count.
- Home Assistant/HACS validation pass/fail once CI exists.

## Experiment rules

- Keep each iteration small and reviewable.
- Preserve the provider-agnostic architecture from [`RULES.md`](RULES.md).
- Run relevant checks after each kept result.
- Record failed ideas and why they failed.
- Do not keep a change solely because a secondary metric improved.
