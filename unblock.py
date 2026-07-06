import subprocess

def unblock_ip(ip):

    unblock_cmd = f"sudo iptables -D INPUT -s {ip} -j DROP"

    subprocess.run(unblock_cmd, shell=True)

    print(f"[UNBLOCKED] {ip}")