import subprocess

def show_popup(ip, port, attack_type):

    message = f"{attack_type} detected from {ip} on port {port}"

    subprocess.run([
        "notify-send",
        "🚨 VNIDS ALERT",
        message,
        "-u", "critical",
        "-t", "10000"
    ])

# Test run
if __name__ == "__main__":

    show_popup(
        "192.168.1.5",
        "22",
        "SSH Brute Force Attack"
    )
