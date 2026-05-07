# AGENTS.md — homeassistant-elero Agent Instructions

Tool-neutral entry point for coding agents working in this repository. Keep this file short; put durable guidance in `docs/agent/`.

## Read first

1. [`docs/agent/RULES.md`](docs/agent/RULES.md) — non-negotiable project rules and domain invariants.
2. [`docs/agent/PROJECT.md`](docs/agent/PROJECT.md) — project context, architecture notes, and important paths.
3. [`docs/agent/CHECKS.md`](docs/agent/CHECKS.md) — validation commands to run before finishing changes.
4. [`docs/agent/WORKFLOWS.md`](docs/agent/WORKFLOWS.md) — reusable maintenance workflows.
5. [`docs/agent/SAFETY.md`](docs/agent/SAFETY.md) — safe/unsafe operations for agents.
6. [`docs/agent/AUTORESEARCH.md`](docs/agent/AUTORESEARCH.md) — optional metric-driven experiment workflow.

## Project docs

- [`docs/README.md`](docs/README.md) — documentation index.
- [`docs/developer/ARCHITECTURE.md`](docs/developer/ARCHITECTURE.md) — architecture and data flow.
- [`docs/developer/RF_PROVIDER_STRATEGY.md`](docs/developer/RF_PROVIDER_STRATEGY.md) — RF provider strategy and capability model.
- [`docs/developer/DEVELOPMENT.md`](docs/developer/DEVELOPMENT.md) — local development notes.
- [`docs/user/HACS.md`](docs/user/HACS.md) — HACS installation and packaging notes.

## Quick summary

`homeassistant-elero` is an experimental Home Assistant custom integration for Elero RF devices. It should remain hardware-agnostic: Home Assistant entities and workflows live here, while CC1101/ESPHome firmware, RF sniffing, timing loops, and low-level radio drivers belong in RF provider/gateway projects.

Before finishing code changes, run the relevant checks from [`docs/agent/CHECKS.md`](docs/agent/CHECKS.md).
