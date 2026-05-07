"""Config flow for the Elero integration."""

from __future__ import annotations

from typing import Any

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.data_entry_flow import FlowResult
from homeassistant.helpers.selector import EntitySelector, EntitySelectorConfig

from .const import CONF_PROVIDER_ENTITY_ID, DOMAIN


class EleroConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle an Elero config flow."""

    VERSION = 1

    async def async_step_user(
        self,
        user_input: dict[str, Any] | None = None,
    ) -> FlowResult:
        """Handle the initial step."""
        errors: dict[str, str] = {}

        if user_input is not None:
            await self.async_set_unique_id("elero")
            self._abort_if_unique_id_configured()

            return self.async_create_entry(
                title="Elero",
                data={
                    CONF_PROVIDER_ENTITY_ID: user_input[CONF_PROVIDER_ENTITY_ID],
                    "devices": [],
                },
            )

        schema = vol.Schema(
            {
                vol.Required(CONF_PROVIDER_ENTITY_ID): EntitySelector(
                    EntitySelectorConfig(
                        # TODO: Replace/adjust this once HA RF provider selector APIs
                        # are stable enough for this integration.
                        domain="radio_frequency",
                    )
                )
            }
        )

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
            errors=errors,
        )
