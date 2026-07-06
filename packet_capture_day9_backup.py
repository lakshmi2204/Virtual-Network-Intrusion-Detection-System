from scapy.all import sniff, IP, TCP

def process_packet(packet):

    if packet.haslayer(IP) and packet.haslayer(TCP):

        src_ip = packet[IP].src
        dst_port = packet[TCP].dport

        print(f"[TCP] Source IP: {src_ip} -> Destination Port: {dst_port}")

print("Starting TCP Packet Capture...")

sniff(filter="tcp", iface="ens33", prn=process_packet, store=False)
