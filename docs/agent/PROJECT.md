# Agent Project Brief — homeassistant-elero

Concise project context for coding agents. Prefer canonical docs linked below instead of duplicating full manuals here.

## Purpose

`homeassistant-elero` is an experimental Home Assistant custom integration for Elero RF devices. The repository owns Home Assistant config flows, entities, provider selection, HACS packaging, and user-facing Elero workflows. It does not own RF hardware firmware or low-level radio transport implementations.

## Core architecture

- **Home Assistant integration** (`custom_components/elero/`) owns config entries, cover entities, services, translations, and Home Assistant setup/unload behavior.
- **Elero protocol abstraction / rf-protocols** should eventually own command encoding details or expose reusable protocol support.
- **Home Assistant `radio_frequency` provider** is the intended abstraction for selecting a compatible transmitter.
- **External RF backends** such as ESPHome LilyGO/CC1101 nodes, MQTT RF bridges, USB RF transmitters, or future HA RF providers own hardware-specific behavior.

## Important paths

```text
custom_components/elero/    Home Assistant integration runtime files
custom_components/elero/manifest.json  HACS/Home Assistant integration metadata
docs/agent/                 Tool-neutral agent instructions
docs/developer/             Architecture, roadmap, setup, and maintainer docs
docs/user/                  Installation and user-facing docs
scripts/                    Lightweight repository validation utilities
tests/                      Planned Home Assistant integration tests
```

## Canonical docs

- [`../developer/ARCHITECTURE.md`](../developer/ARCHITECTURE.md) — architecture and repository split.
- [`../developer/RF_PROVIDER_STRATEGY.md`](../developer/RF_PROVIDER_STRATEGY.md) — provider strategy and capability model.
- [`../developer/DEVELOPMENT.md`](../developer/DEVELOPMENT.md) — local development notes and first implementation tasks.
- [`../developer/INITIAL_ROADMAP.md`](../developer/INITIAL_ROADMAP.md) — phased project roadmap.
- [`../developer/CORE_UPSTREAMING.md`](../developer/CORE_UPSTREAMING.md) — possible Home Assistant Core path.
- [`../developer/GITHUB_SETUP.md`](../developer/GITHUB_SETUP.md) — repository/release setup notes.
- [`../user/HACS.md`](../user/HACS.md) — HACS installation and packaging notes.

## Agent docs

- [`RULES.md`](RULES.md) — non-negotiable project rules.
- [`CHECKS.md`](CHECKS.md) — validation commands.
- [`WORKFLOWS.md`](WORKFLOWS.md) — reusable maintenance workflows.
- [`SAFETY.md`](SAFETY.md) — safe/unsafe operations.
- [`AUTORESEARCH.md`](AUTORESEARCH.md) — optional metric-driven experiment workflow.
