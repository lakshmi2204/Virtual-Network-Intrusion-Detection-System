# Virtual Network Intrusion Detection System (VNIDS)

## Overview

Virtual Network Intrusion Detection System (VNIDS) is a real-time cybersecurity monitoring system developed using Python and Flask. It captures live network packets, detects common network attacks, classifies their severity, logs security events, and provides a web-based dashboard with real-time monitoring and desktop alerts.

---

## Features

- Real-time packet capture
- Port Scan Detection
- SYN Flood Detection
- Brute Force Detection
- Severity Classification
- SQLite-based Attack Logging
- Interactive Flask Dashboard
- Desktop Popup Alerts
- Alert Sound Notifications
- Automatic IP Blocking
- Live Threat Monitoring

---

## Technologies Used

- Python
- Flask
- Scapy
- SQLite
- HTML
- CSS
- JavaScript
- Chart.js
- Linux (Ubuntu)
- VMware

---

## Project Structure

```
Virtual-Network-Intrusion-Detection-System/
│
├── app.py
├── packet_capture.py
├── port_scan_detection.py
├── syn_flood_detection.py
├── brute_force_detection.py
├── severity.py
├── logger.py
├── log_insert.py
├── event_trigger.py
├── attack_state.py
├── block_ip2.py
├── unblock.py
│
├── desktop/
│   ├── alert_receiver.py
│   ├── alert_trigger.py
│   ├── popup_alert.py
│   └── sound_alert.py
│
├── templates/
│
├── sounds/
│
├── requirements.txt
└── README.md
```

---

## Detection Workflow

1. Capture live packets.
2. Detect malicious network activity.
3. Classify attack severity.
4. Store logs in SQLite database.
5. Display alerts on dashboard.
6. Trigger desktop popup and sound alerts.
7. Automatically block malicious IP addresses.

---

## Dashboard

The dashboard provides:

- Threat Overview
- Live Alerts
- Attack Logs
- Severity-wise Statistics
- Charts and Analytics
- Blocked IP List

---

## Future Enhancements

- Machine Learning-based Intrusion Detection
- Email Notifications
- Multi-user Authentication
- Cloud Deployment
- Threat Intelligence Integration

---

## Author

**Pendyala Lakshmi**

B.Tech – Computer Science & Engineering (Cyber security)

Cybersecurity Enthusiast
