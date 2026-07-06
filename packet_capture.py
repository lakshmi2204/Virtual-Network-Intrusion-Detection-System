from scapy.all import sniff, IP, TCP
from syn_flood_detection import detect_syn_flood
from port_scan_detection import detect_port_scan
from brute_force_detection import detect_brute_force

DEBUG = False

def process_packet(packet):
    try:
        if packet.haslayer(IP) and packet.haslayer(TCP):

            src_ip = packet[IP].src
            dst_port = packet[TCP].dport
        
            if DEBUG:
                print(f"[TCP] Source IP: {src_ip} -> Destination Port: {dst_port}")

        #call all detection functions
            if detect_brute_force(packet):
                return
            if detect_syn_flood(packet):
                return
            detect_port_scan(packet)
                

    except Exception as e:
        import traceback
        print("\n ERROR DETECTED ")
        traceback.print_exc()

print("Starting IDS Packet Capture...")

try:
    sniff(filter="tcp", iface="ens33", prn=process_packet, store=False)
except KeyboardInterrupt:
    print("\n IDS Stopped Gracefully ")
