from flask import Flask, render_template, jsonify
from simulator import generate_log
from model import predict_risk

app = Flask(__name__)

log_history = []

def create_log():

    log = generate_log()

    login_hour = int(log["login_time"].split(":")[0])
    ip_flag = 1 if log["ip_region"] == "Unknown Region" else 0
    request_rate = log["files_accessed"] / max(1, log["session_duration"])

    features = [
        login_hour,
        log["failed_attempts"],
        ip_flag,
        log["files_accessed"],
        log["session_duration"],
        request_rate
    ]

    risk_score = predict_risk(features)

    if risk_score > 70:
        status = "High Risk"
    elif risk_score > 40:
        status = "Suspicious"
    else:
        status = "Normal"

    log["risk_score"] = risk_score
    log["status"] = status

    log_history.insert(0, log)

    if len(log_history) > 30:
        log_history.pop()


@app.route("/")
def dashboard():

    normal = sum(1 for l in log_history if l["status"] == "Normal")
    suspicious = sum(1 for l in log_history if l["status"] == "Suspicious")
    risk = sum(1 for l in log_history if l["status"] == "High Risk")

    return render_template(
        "dashboard.html",
        logs=log_history,
        normal_count=normal,
        suspicious_count=suspicious,
        high_risk_count=risk
    )


@app.route("/api/logs")
def api_logs():

    create_log()

    normal = sum(1 for l in log_history if l["status"] == "Normal")
    suspicious = sum(1 for l in log_history if l["status"] == "Suspicious")
    risk = sum(1 for l in log_history if l["status"] == "High Risk")

    return jsonify({
        "logs": log_history,
        "normal": normal,
        "suspicious": suspicious,
        "risk": risk
    })


@app.route("/threats")
def threats():

    return render_template(
        "threats.html",
        logs=log_history
    )


@app.route("/analytics")
def analytics():

    return render_template(
        "analytics.html",
        logs=log_history
    )

if __name__ == "__main__":
    app.run(debug=True)