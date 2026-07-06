import socket
from alert_trigger import trigger_alert

HOST = "0.0.0.0"
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print("🚨 Alert Receiver Running... Waiting for alerts...")

while True:
    client, addr = server.accept()

    message = client.recv(1024).decode()

    print("\n🚨 ALERT RECEIVED")
    print("Message:", message)

    # Extract IP from message
    try:
        ip_address = message.split("from ")[1].split(" |")[0]
    except:
        ip_address = "Unknown"

    # Extract Severity
    try:
        severity = message.split("Severity: ")[1]
    except:
        severity = "LOW"

    trigger_alert(message, ip_address, severity)

    client.close()
