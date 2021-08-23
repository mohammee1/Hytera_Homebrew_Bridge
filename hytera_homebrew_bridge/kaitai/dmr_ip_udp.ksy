meta:
  id: dmr_ip_udp
  endian: le
doc: |
  ETSI TS 102 361-3 V1.3.1, section 7, PDUs
enums:
  source_ip_address_ids:
    0b0000: radio_network
    0b0001: usb_ethernet_interface_network
  destination_ip_address_ids:
    0b0000: radio_network
    0b0001: usb_ethernet_interface_network
    0b0010: group_network
  udp_port_ids:
    0b0000000: present_in_extended_header
    0b0000001: utf16be_text_message_port_5016
    0b0000010: location_interface_protocol
types:
  udp_ipv4_compressed_header:
    doc: |
      7.2.3 UDP/IPv4 Compressed Header, Table 7.14
    seq:
      - id: ipv4_identification
        size: 2
      - id: source_ip_address_id
        type: b4
        doc: SAID
      - id: destination_ip_address_id
        type: b4
        doc: DAID
      - id: header_compression_opcode_msb
        type: b1
      - id: udp_source_port_id
        type: b7
        doc: SPID
      - id: header_compression_opcode_lsb
        type: b1
      - id: udp_destination_port_id
        type: b7
        doc: DPID
      - id: extended_header_1
        size: 2
        doc: |
          in this order: source port (if SPID==0) or destination port (if SPID!=0) or data (if SPID!=0 and DPID!=0)
      - id: extended_header_2
        size: 2
        doc: |
          in this order: destination port (if SPID==0 and DPID==0) or data (if SPID!=0 and DPID!=0)