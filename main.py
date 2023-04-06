import scapy.all as scapy

# scapy.conf.iface - default interface
HostIP = scapy.get_if_addr(scapy.conf.iface)
TargetIP = f"{HostIP}/24"

# Prepare arp packet with TargetIP as destination
ArpPacket = scapy.ARP(pdst=TargetIP)

# ff:ff:ff:ff:ff:ff - Broadcast MAC Address
EtherBroadcastPacket = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
Packet = EtherBroadcastPacket/ArpPacket

# Send Packet and store response
Result = scapy.srp(Packet, timeout=3)[0]

Devices = []

for sent, received in Result:
    # for each response, append ip and mac address to `clients` list
    Devices.append({'ip': received.psrc, 'mac': received.hwsrc})

print(f"\nHost device IP Address: [{HostIP}],  MAC Address: [{scapy.Ether().src}]\n")
print(f"Found {len(Devices)} available devices in the network:")

for i, device in enumerate(Devices):
    print(f"Device [{i+1}] IP Address: [{device['ip']}], MAC Address: [{device['mac']}]")
