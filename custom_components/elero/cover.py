"""Elero cover platform."""

from __future__ import annotations

from dataclasses import dataclass

from homeassistant.components.cover import CoverEntity, CoverEntityFeature
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN


@dataclass(slots=True)
class EleroCoverDescription:
    """Description of an Elero cover."""

    name: str
    device_id: str
    target_id: str


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Elero covers from a config entry."""
    entry_data = hass.data[DOMAIN][entry.entry_id]
    devices = entry_data.get("devices", [])

    entities = [
        EleroCover(
            entry_id=entry.entry_id,
            provider_entity_id=entry_data["provider_entity_id"],
            description=EleroCoverDescription(
                name=device.get("name", "Elero Cover"),
                device_id=device.get("device_id", device.get("target_id", "unknown")),
                target_id=device.get("target_id", "unknown"),
            ),
        )
        for device in devices
    ]

    async_add_entities(entities)


class EleroCover(CoverEntity):
    """Representation of an Elero cover."""

    _attr_supported_features = (
        CoverEntityFeature.OPEN
        | CoverEntityFeature.CLOSE
        | CoverEntityFeature.STOP
    )

    def __init__(
        self,
        entry_id: str,
        provider_entity_id: str,
        description: EleroCoverDescription,
    ) -> None:
        """Initialize the cover."""
        self._entry_id = entry_id
        self._provider_entity_id = provider_entity_id
        self._description = description

        self._attr_name = description.name
        self._attr_unique_id = f"{entry_id}_{description.device_id}"
        self._attr_is_closed = None

    async def async_open_cover(self, **kwargs) -> None:
        """Open the cover."""
        await self._async_send_elero_command("up")

    async def async_close_cover(self, **kwargs) -> None:
        """Close the cover."""
        await self._async_send_elero_command("down")

    async def async_stop_cover(self, **kwargs) -> None:
        """Stop the cover."""
        await self._async_send_elero_command("stop")

    async def _async_send_elero_command(self, command: str) -> None:
        """Send an Elero command through the selected RF provider.

        TODO:
        Replace this placeholder with the final HA radio_frequency service/entity API
        once the provider contract is finalized.
        """
        self.async_write_ha_state()
