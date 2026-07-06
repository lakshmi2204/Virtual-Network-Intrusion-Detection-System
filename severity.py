def get_severity(attack_type):

    severity_map = {
        "Port Scan": "MEDIUM",
        "SYN Flood": "HIGH",
        "Brute Force": "CRITICAL"
    }
    return severity_map.get(
        attack_type,
        "LOW"
    )
