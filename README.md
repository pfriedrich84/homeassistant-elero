# homeassistant-elero

Experimental Home Assistant custom integration for Elero RF devices.

This repository is intended as the Home Assistant integration layer for Elero devices. It should be hardware-agnostic and use Home Assistant `radio_frequency` providers where possible.

## Project Status

Early architecture skeleton. Not functional yet.

This repository is designed to follow after the RF provider/gateway work in:

- `pfriedrich84/esphome-elero` issue #176
- `pfriedrich84/esphome-elero` issue #177

## Core Idea

The Home Assistant integration should not depend on one specific LilyGO/CC1101 gateway.

Instead:

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

## RF Provider First

The LilyGO/CC1101 gateway is only one possible backend.

Potential RF providers:

- ESPHome LilyGO/CC1101 RF provider
- other ESPHome RF transmitter nodes
- MQTT RF bridges
- USB RF transmitters
- future Home Assistant RF providers

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

## HACS Installation

When this integration becomes functional:

1. Add this repository as a custom repository in HACS.
2. Select category: Integration.
3. Install.
4. Restart Home Assistant.
5. Add the integration from Settings → Devices & services.

## Manual Installation

Copy:

```text
custom_components/elero/
```

to:

```text
/config/custom_components/elero/
```

Then restart Home Assistant.

## Development

See:

- `docs/ARCHITECTURE.md`
- `docs/DEVELOPMENT.md`
- `docs/RF_PROVIDER_STRATEGY.md`
- `docs/HACS.md`
- `docs/CORE_UPSTREAMING.md`
