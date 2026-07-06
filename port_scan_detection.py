from attack_state import syn_flooding_ips
from scapy.all import sniff, IP, TCP
from collections import defaultdict
from event_trigger import trigger_event
from syn_flood_detection import syn_tracker, SYN_THRESHOLD
import time

port_scan_tracker = defaultdict(set)

# Detection settings
PORT_THRESHOLD = 20
TIME_WINDOW = 5

# Cooldown system
last_alert_time = {}
ALERT_COOLDOWN = 20   # seconds


def detect_port_scan(packet):

    if packet.haslayer(IP) and packet.haslayer(TCP):

        src_ip = packet[IP].src
        dst_port = packet[TCP].dport
        if src_ip in syn_flooding_ips:
            return False

        current_time = time.time()

        port_scan_tracker[src_ip].add((dst_port, current_time))

        # Remove old entries
        port_scan_tracker[src_ip] = {

            (port, t)

            for port, t in port_scan_tracker[src_ip]

            if current_time - t <= TIME_WINDOW
        }

        unique_ports = set(

            port

            for port, t in port_scan_tracker[src_ip]

        )


        if src_ip in last_alert_time and \
           current_time - last_alert_time[src_ip] < ALERT_COOLDOWN:
            return

        if len(unique_ports) >= PORT_THRESHOLD:

            # Check cooldown
            if src_ip not in last_alert_time or \
               current_time - last_alert_time[src_ip] > ALERT_COOLDOWN:

                trigger_event(src_ip, "Port Scan")
                last_alert_time[src_ip] = current_time
                port_scan_tracker[src_ip].clear()
                return True
        return False


