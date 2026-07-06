from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def get_logs():
    conn = sqlite3.connect("logs.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT timestamp, ip, attack_type, severity
        FROM attack_log
        ORDER BY id DESC
        LIMIT 20
    """)
    rows = cursor.fetchall()
    conn.close()
    logs = []
    for row in rows:
        logs.append({
            "time": row[0],
            "source": row[1],
            "message": row[2],
            "severity": row[3]
        })
    return logs

@app.route('/')
@app.route('/dashboard')
def dashboard():
    level = request.args.get('level')
    logs = get_logs()
    if level:
        logs = [l for l in logs if l["severity"] == level]
    counts = {
        s: sum(1 for l in logs if l["severity"] == s)
        for s in ["LOW", "MEDIUM", "HIGH", "CRITICAL"]
    }
    return render_template(
        "dashboard.html",
        logs=logs,
        counts=counts,
        alerts=[
            "Port scan detected",
            "SYN flood detected",
            "Brute force detected"
        ],
        blocked_ips=[
            "192.168.27.129"
        ],
        timeline_labels=[
            "Port Scan",
            "SYN Flood",
            "Brute Force"
        ],
        timeline_data=[
            counts["MEDIUM"],
            counts["HIGH"],
            counts["CRITICAL"]
        ]
    )

@app.route('/api/logs')
def api_logs():
    logs=get_logs()
    if logs:
        return jsonify(logs[0])
    return jsonify({})



@app.route('/about')
def about(): return render_template("about.html")

@app.route('/contact')
def contact(): return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
