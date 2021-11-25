#!/usr/bin/env python3
import os
import sys

from okdmr.kaitai.hytera.hytera_dmr_application_protocol import (
    HyteraDmrApplicationProtocol,
)

try:
    import hytera_homebrew_bridge
except ImportError:
    sys.path.append(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    )

from hytera_homebrew_bridge.tests.prettyprint import prettyprint

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("use as %s <hexstring>" % sys.argv[0])
        exit(0)

    packet = HyteraDmrApplicationProtocol.from_bytes(bytes.fromhex(sys.argv[1]))
    prettyprint(packet)
    # print(packet)
    # print(packet.message_type)
