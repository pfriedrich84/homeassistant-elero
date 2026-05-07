# AGENTS.md

Guidance for coding agents working on `homeassistant-elero`.

## Mission

Build a Home Assistant custom integration for Elero RF devices that is hardware-agnostic and can use Home Assistant RF providers where possible.

This project should not become a CC1101 driver or ESPHome firmware repository.

## Architecture Rules

Keep these layers separate:

```text
Home Assistant integration
    ↓
Elero protocol abstraction / rf-protocols
    ↓
Home Assistant radio_frequency provider
    ↓
External RF backend
```

## Do

- Keep the integration provider-agnostic.
- Prefer Home Assistant config entries over YAML.
- Use Home Assistant entity patterns.
- Keep Elero cover/device logic testable.
- Document assumptions clearly.
- Add TODO comments where HA RF APIs are not yet stable.
- Keep `custom_components/elero/` HACS-compatible.

## Do Not

- Add ESP32 firmware code here.
- Add CC1101 SPI drivers here.
- Hard-code LilyGO/CC1101 as the only supported backend.
- Depend on undocumented Home Assistant internals.
- Implement sniffing or timing-critical RF loops in Python.

## Important Related Work

- `pfriedrich84/esphome-elero` issue #176: ESPHome RF gateway/provider architecture.
- `pfriedrich84/esphome-elero` issue #177: HA/HACS/Core integration strategy.

## Suggested First Tasks

1. Keep the repository skeleton HACS-valid.
2. Implement a basic config flow placeholder.
3. Add provider selection model.
4. Add stub Elero cover entities.
5. Add architecture docs before real RF send logic.
