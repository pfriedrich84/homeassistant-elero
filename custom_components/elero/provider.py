"""RF provider capability models for Elero.

This module intentionally contains no hardware-specific logic.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True, frozen=True)
class RFProviderCapabilities:
    """Capabilities exposed by a compatible RF provider."""

    supports_tx: bool = True
    supports_rx: bool = False
    supports_sniffing: bool = False
    supports_rssi: bool = False
    supports_frequency_offset: bool = False
    supported_frequencies_hz: set[int] = field(default_factory=set)
    supported_modulations: set[str] = field(default_factory=set)

    def supports_elero_basic_tx(self) -> bool:
        """Return whether this provider appears suitable for basic Elero TX."""
        return (
            self.supports_tx
            and 868_300_000 in self.supported_frequencies_hz
            and bool({"OOK", "ASK"} & self.supported_modulations)
        )
