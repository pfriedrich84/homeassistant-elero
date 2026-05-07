# homeassistant-elero

Experimental Home Assistant custom integration for Elero RF devices.

This repository is intended as the Home Assistant integration layer for Elero devices. It should be hardware-agnostic and use Home Assistant `radio_frequency` providers where possible.

## Project status

Early architecture skeleton. Not functional yet.

This repository is designed to follow after the RF provider/gateway work in:

- `pfriedrich84/esphome-elero` issue #176
- `pfriedrich84/esphome-elero` issue #177

## Core idea

The Home Assistant integration should not depend on one specific LilyGO/CC1101 gateway.

```text
Elero Cover in Home Assistant
    ↓
homeassistant-elero
    ↓
rf-protocols / Elero encoder
    ↓
Home Assistant radio_frequency provider
    ↓
any compatible RF transmitter
```

## What belongs here

- Home Assistant config flow
- Elero cover entities
- RF provider selection
- provider capability validation
- pairing/import workflows
- device/entity registry integration
- HACS packaging
- possible future Home Assistant Core path

## What does not belong here

- CC1101 SPI handling
- ESP32 firmware
- low-level RF timings
- interrupt-driven RF sniffing
- RSSI/frequency calibration internals
- advanced RF debugging firmware

Those belong in RF provider/gateway firmware or integrations.

## Installation

### HACS custom repository

When this integration becomes functional:

1. Add this repository as a custom repository in HACS.
2. Select category: Integration.
3. Install.
4. Restart Home Assistant.
5. Add the integration from Settings → Devices & services.

See [`docs/user/HACS.md`](docs/user/HACS.md) for HACS notes.

### Manual installation

Copy:

```text
custom_components/elero/
```

to:

```text
/config/custom_components/elero/
```

Then restart Home Assistant.

## Documentation

Start with the documentation index: [`docs/README.md`](docs/README.md).

Developer docs:

- [`docs/developer/ARCHITECTURE.md`](docs/developer/ARCHITECTURE.md)
- [`docs/developer/RF_PROVIDER_STRATEGY.md`](docs/developer/RF_PROVIDER_STRATEGY.md)
- [`docs/developer/DEVELOPMENT.md`](docs/developer/DEVELOPMENT.md)
- [`docs/developer/INITIAL_ROADMAP.md`](docs/developer/INITIAL_ROADMAP.md)
- [`docs/developer/CORE_UPSTREAMING.md`](docs/developer/CORE_UPSTREAMING.md)

Agent instructions:

- [`AGENTS.md`](AGENTS.md)
