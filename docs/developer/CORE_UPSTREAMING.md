# Home Assistant Core Upstreaming Strategy

## Goal

Eventually evaluate whether Elero support should be proposed for Home Assistant Core.

## What Could Belong In Core

- Elero integration domain
- config flow
- cover entities
- device registry integration
- repair flows
- RF provider selection
- protocol integration through reusable libraries

## What Should Not Belong In Core

- CC1101 SPI drivers
- ESP32 firmware logic
- timing-critical RF loops
- RF sniffing internals
- replay/debug tooling
- calibration tooling

## Readiness Criteria

Before considering Core:

- HACS integration is stable.
- Provider-agnostic architecture is proven.
- RF provider APIs are stable enough.
- Protocol handling is testable.
- The integration has tests and diagnostics.
- Maintenance burden is reasonable.
