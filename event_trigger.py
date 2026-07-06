# event_trigger.py
import socket
from severity import get_severity
from logger import log_attack 

DESKTOP_IP = "192.168.27.130"
PORT = 5050

def trigger_event(src_ip, attack_type):
    severity = get_severity(attack_type)
    message = (
        f"{attack_type} detected "
        f"from {src_ip} "
        f"| Severity: {severity}"
    )

    print("\n ALERT TRIGGERED ")
    print("Message:", message)
    log_attack(src_ip, attack_type, severity)

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((DESKTOP_IP, PORT))

        client.send(message.encode())

        client.close()

    except Exception as e:
        print(" Failed to send alert:", e)
