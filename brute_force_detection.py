from scapy.all import sniff, TCP, IP
import time
from event_trigger import trigger_event
from block_ip2 import block_ip
from logger import log_attack

# Store attempts
ssh_attempts = {}
last_alert_time = {}
COOLDOWN = 20
# Settings
BRUTE_THRESHOLD = 5
TIME_WINDOW = 15  # seconds

def detect_brute_force(packet):
    if packet.haslayer(TCP) and packet.haslayer(IP):

        if packet[TCP].dport == 22 and packet[TCP].flags & 0x02:  # SSH port

            src_ip = packet[IP].src
            current_time = time.time()

            if src_ip not in ssh_attempts:
                ssh_attempts[src_ip] = []

            ssh_attempts[src_ip].append(current_time)

            # Keep only recent attempts
            ssh_attempts[src_ip] = [
                t for t in ssh_attempts[src_ip]
                if current_time - t <= TIME_WINDOW
            ]

            if len(ssh_attempts[src_ip]) >= BRUTE_THRESHOLD:

               current_time = time.time()

               #cooldown check
               if src_ip in last_alert_time and current_time - last_alert_time[src_ip] < COOLDOWN:return

               last_alert_time[src_ip] = current_time

               severity = "CRITICAL"
               print(f"[CRITICAL] Brute Force Detected from {src_ip}")

               trigger_event(src_ip, "Brute Force")
               log_attack(src_ip, "BRUTE FORCE", severity)
               if severity in ["HIGH", "CRITICAL"]:
                   block_ip(src_ip)
               ssh_attempts[src_ip].clear()
               return True
            return False

