from block_ip2 import block_ip
from logger import log_attack
from attack_state import syn_flooding_ips
from scapy.all import sniff, IP, TCP
from collections import defaultdict
from event_trigger import trigger_event
import time

syn_tracker = defaultdict(list)

# Detection settings
SYN_THRESHOLD = 20
TIME_WINDOW = 5

# Cooldown
last_alert_time = {}
ALERT_COOLDOWN = 20


def detect_syn_flood(packet):

    if packet.haslayer(IP) and packet.haslayer(TCP):

        if packet[TCP].flags & 0x02:

            src_ip = packet[IP].src

            current_time = time.time()

            syn_tracker[src_ip].append((packet[TCP].dport, current_time))

            # Remove old packets
            syn_tracker[src_ip] = [
                (port, t)
                for port, t in syn_tracker[src_ip]
                if current_time - t <= TIME_WINDOW
            ]
            ports = [port for port, t in syn_tracker[src_ip]]
            unique_ports = set(ports)

            if len(unique_ports) > 10:
                return False


            if len(syn_tracker[src_ip]) >= SYN_THRESHOLD:

                if src_ip not in last_alert_time or \
                   current_time - last_alert_time[src_ip] > ALERT_COOLDOWN:

                    syn_flooding_ips.add(src_ip)
                    severity = "HIGH"
                    trigger_event(src_ip, "SYN Flood")
                    log_attack(src_ip, "SYN FLOOD", severity)
                    if severity in ["HIGH", "CRITICAL"]:
                        block_ip(src_ip)
                    last_alert_time[src_ip] = current_time
                    syn_tracker[src_ip].clear()
                    return True
            return False

