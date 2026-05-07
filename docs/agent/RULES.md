# Agent Rules

Core rules for coding agents working on `homeassistant-elero`.

## Product / domain safety

- Keep this repository focused on the Home Assistant custom integration for Elero devices.
- Keep the integration hardware-agnostic and provider-agnostic.
- Do not turn this repository into an ESPHome firmware, CC1101 driver, RF sniffer, or low-level radio debugging project.
- Preserve HACS compatibility for `custom_components/elero/`.

## Architecture invariants

- Keep these layers separate:

  ```text
  Home Assistant integration
      ↓
  Elero protocol abstraction / rf-protocols
      ↓
  Home Assistant radio_frequency provider
      ↓
  External RF backend
  ```

- Prefer Home Assistant config entries and entity patterns over YAML-only workflows.
- Keep provider capability detection explicit and gracefully handle missing or incompatible providers.
- Treat advanced RF diagnostics as optional provider capabilities, not requirements for basic cover control.
- Leave TODOs where Home Assistant RF provider APIs are not stable yet.

## Change discipline

- Prefer small, reviewable changes.
- Update docs when behavior, architecture, validation, installation, or HACS expectations change.
- Keep Elero cover/device logic testable and isolated from Home Assistant glue where practical.
- Run relevant checks before finishing; see [`CHECKS.md`](CHECKS.md).
- Do not expose or modify secrets from Home Assistant config directories, `.env` files, tokens, or runtime data.
