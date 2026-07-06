from scapy.all import sniff, IP, TCP

def packet_callback(packet):
    print(packet.summary())

print("Starting Packet Sniffer...")
sniff(
    prn=packet_callback,
    store=0
)
