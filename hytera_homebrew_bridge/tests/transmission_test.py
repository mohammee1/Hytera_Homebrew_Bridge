#!/usr/bin/env python3
import os
import sys
from argparse import ArgumentParser
from binascii import unhexlify
from typing import Optional

from kaitaistruct import KaitaiStruct

from hytera_homebrew_bridge.dmrlib.packet_utils import try_parse_packet
from hytera_homebrew_bridge.dmrlib.terminal import Terminal
from hytera_homebrew_bridge.dmrlib.transmission_watcher import TransmissionWatcher
from hytera_homebrew_bridge.kaitai.mmdvm import Mmdvm
from hytera_homebrew_bridge.tests.prettyprint import _prettyprint


def arguments() -> ArgumentParser:
    parser = ArgumentParser(description="Read transmission file(s) and debug")
    parser.add_argument(
        "files",
        metavar="file",
        type=str,
        nargs="+",
        help="One or more transmission files in same format",
    )
    parser.add_argument(
        "-t",
        "--type",
        dest="filetype",
        default="pcap",
        choices=["pcap", "pcapng", "hex"],
        help="type of files to read (default: pcap)",
    )
    return parser


if __name__ == "__main__":
    args = arguments().parse_args(sys.argv[1:])
    watcher: TransmissionWatcher = TransmissionWatcher()
    for file in args.files:
        if not os.path.isfile(file):
            print(f"File does not exist {file}")
            continue
        if args.filetype == "hex":
            with open(file, "r") as filehandle:
                for line in filehandle.readlines():
                    packetdata: Optional[KaitaiStruct] = try_parse_packet(
                        unhexlify(line.strip())
                    )
                    print(line.strip())
                    if packetdata:
                        watcher.process_packet(packetdata)
