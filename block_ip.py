import subprocess

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

    print(f"[BLOCKED] {ip}")