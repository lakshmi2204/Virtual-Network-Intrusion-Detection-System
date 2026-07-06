import subprocess
import threading
import time

BLOCK_TIME = 900   # 15 minutes = 900 seconds


def unblock_ip(ip):

    unblock_cmd = f"sudo iptables -D INPUT -s {ip} -j DROP"

    subprocess.run(unblock_cmd, shell=True)

    print(f"[UNBLOCKED] {ip}")


def block_ip(ip):

    check_cmd = f"sudo iptables -C INPUT -s {ip} -j DROP"

    result = subprocess.run(
        check_cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    if result.returncode == 0:
        print(f"[INFO] {ip} already blocked")
        return

    block_cmd = f"sudo iptables -A INPUT -s {ip} -j DROP"

    subprocess.run(block_cmd, shell=True)

    print(f"[BLOCKED] {ip} for 15 minutes")

    timer = threading.Timer(BLOCK_TIME, unblock_ip, args=[ip])

    timer.start()