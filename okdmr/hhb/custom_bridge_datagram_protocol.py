#!/usr/bin/env python3
from asyncio import protocols

from okdmr.hhb.settings import BridgeSettings
from okdmr.hhb.snmp import SNMP


class CustomBridgeDatagramProtocol(protocols.DatagramProtocol, LoggingTrait):
    def __init__(self, settings: BridgeSettings) -> None:
        super().__init__()
        self.settings = settings

    async def hytera_repeater_obtain_snmp(
        self, address: tuple, force: bool = False
    ) -> None:
        self.settings.hytera_repeater_ip = address[0]
        if self.settings.snmp_enabled:
            if force or not self.settings.hytera_snmp_data.get(address[0]):
                await SNMP().walk_ip(address, self.settings)
        else:
            self.log_warning("SNMP is disabled")
