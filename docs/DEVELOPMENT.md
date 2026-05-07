# Development Guide

## Local Development Install

Clone this repository into your Home Assistant config directory:

```bash
cd /config
mkdir -p custom_components
git clone https://github.com/pfriedrich84/homeassistant-elero.git /tmp/homeassistant-elero
cp -r /tmp/homeassistant-elero/custom_components/elero custom_components/
```

Restart Home Assistant.

Then add the integration via:

```text
Settings → Devices & services → Add integration → Elero
```

## Expected Repository Structure

HACS custom integrations should place runtime files under:

```text
custom_components/elero/
```

The domain is `elero`, and the integration folder name must match the manifest domain.

## First Implementation Tasks

1. Keep placeholder config flow working.
2. Replace RF provider entity selector with the final HA RF selector/API once stable.
3. Add data model for Elero devices.
4. Implement manual device import.
5. Implement cover send path.
6. Add tests.
7. Add diagnostics bridge if the selected provider supports it.

## Testing Ideas

Planned test areas:

- config flow
- options flow
- device import validation
- cover entity creation
- provider selection
- graceful error handling when provider is missing
- command encoding handoff
