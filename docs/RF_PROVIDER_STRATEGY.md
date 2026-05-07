# RF Provider Strategy

## Objective

`homeassistant-elero` should work with any compatible Home Assistant RF provider, not just one LilyGO/CC1101 implementation.

The LilyGO/CC1101 gateway is an important first backend, but not a hard dependency of this integration.

## Target Flow

```text
homeassistant-elero
    ↓
Elero protocol encoder
    ↓
Home Assistant radio_frequency provider
    ↓
compatible RF backend
```

## Candidate Providers

- ESPHome LilyGO/CC1101 RF provider
- other ESPHome RF transmitter nodes
- MQTT RF bridges
- USB RF transmitters
- future Home Assistant RF providers

## Provider Capability Model

The integration should eventually validate whether a provider supports:

- transmit support
- required frequency, e.g. 868.3 MHz
- required modulation
- required timing precision
- repeat count
- optional diagnostics
- optional receive/sniff support
- optional RSSI
- optional frequency offset reporting

Illustrative model:

```python
class RFProviderCapabilities:
    supports_tx: bool
    supports_rx: bool
    supports_sniffing: bool
    supports_rssi: bool
    supports_frequency_offset: bool
    supported_frequencies_hz: set[int]
    supported_modulations: set[str]
```

## Graceful Degradation

If a provider only supports transmit:

- cover commands should work
- sniffing should be unavailable
- diagnostics should show limited capability

If a provider supports diagnostics:

- expose additional repair/diagnostics info
- potentially support remote import workflows

If no compatible provider exists:

- config flow should explain what is missing
- no entities should be created in a broken state

## Open Questions

- Final HA RF provider API shape
- How `rf-protocols` exposes Elero support
- Whether Elero encoding should live in HA, rf-protocols, or a separate library
- How capabilities are discovered or declared
