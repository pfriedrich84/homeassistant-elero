# Architecture

## Purpose

`homeassistant-elero` is intended to be the Home Assistant product integration for Elero devices.

It should not own RF hardware drivers.

## Target Architecture

```text
Home Assistant
  └─ Elero integration
       ├─ config flow
       ├─ cover entities
       ├─ pairing/import workflow
       ├─ RF provider selection
       ├─ provider capability validation
       └─ diagnostics bridge where available
            ↓
     Home Assistant radio_frequency abstraction
            ↓
     Any compatible RF provider
            ↓
     ESPHome LilyGO/CC1101 or another backend
```

## Repository Split

### RF provider / gateway repositories

Responsible for:

- ESPHome runtime
- CC1101 or other RF transport
- RF provider capabilities
- optional native diagnostics
- sniffing/capture if supported by hardware
- embedded or backend-specific implementation

### `homeassistant-elero`

Responsible for:

- HA config flow
- Cover entities
- provider selection
- HACS packaging
- possible Core readiness
- user-facing Elero workflows
- protocol/provider orchestration

## Dual Path

### Generic HA RF Path

```text
Elero HA integration
    ↓
rf-protocols / Elero encoder
    ↓
radio_frequency entity
    ↓
compatible RF provider
```

### Optional Advanced Diagnostics Path

```text
RF provider / gateway
    ├─ sniffing
    ├─ RSSI
    ├─ ACK/retransmission
    ├─ frequency diagnostics
    └─ developer tooling
```

Diagnostics are optional provider capabilities, not a requirement for basic Elero control.

## Design Constraints

- Stay hardware-agnostic in Home Assistant.
- Do not assume LilyGO/CC1101 is the only backend.
- Keep provider capability detection explicit.
- Keep advanced RF diagnostics outside HA Core unless there is a clean, generic API.
