import sqlite3
from datetime import datetime

def insert_log(ip, attack_type, severity):

    # Connect to database
    conn = sqlite3.connect("logs.db")

    cursor = conn.cursor()

    # Current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Insert log
    cursor.execute("""
        INSERT INTO attack_log 
        (timestamp, ip, attack_type, severity)
        VALUES (?, ?, ?, ?)
    """, (timestamp, ip, attack_type, severity))

    # Save changes
    conn.commit()

    # Close database
    conn.close()

    print(f"[LOGGED] {attack_type} from {ip} ({severity})")