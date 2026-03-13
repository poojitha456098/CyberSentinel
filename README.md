# CyberSentinel – AI-Based Security Monitoring System

CyberSentinel is a cybersecurity monitoring dashboard that detects anomalous user behavior using machine learning techniques.
The system simulates enterprise login activity, analyzes behavioral patterns using an ensemble anomaly detection model, and classifies activity into **Normal, Suspicious, or High Risk**.

It provides a real-time security dashboard, threat intelligence view, and attack analytics to visualize potential threats.

---

## Features

* Real-time security monitoring dashboard
* Behavioral anomaly detection using multiple AI models
* Risk classification (Normal / Suspicious / High Risk)
* Live security event feed
* Threat intelligence panel for detected attack patterns
* Attack analytics visualization using charts
* Multi-page cybersecurity dashboard interface

---

## System Architecture

User Activity Logs
→ Feature Extraction
→ AI Anomaly Detection Models
→ Risk Score Calculation
→ Threat Classification
→ Security Dashboard Visualization

---

## Technologies Used

* Python
* Flask
* Scikit-learn
* NumPy
* HTML
* CSS
* JavaScript
* Chart.js

---

## Project Structure

cybersentinel/

│
├── app.py
├── model.py
├── simulator.py
├── requirements.txt
├── README.md

├── static/
│   └── style.css

├── templates/
│   ├── dashboard.html
│   ├── threats.html
│   └── analytics.html

---

## Installation

Clone the repository

git clone https://github.com/YOUR_USERNAME/cybersentinel.git

Navigate to the project folder

cd cybersentinel

Install dependencies

pip install -r requirements.txt

Run the application

python app.py

Open the browser and go to

http://127.0.0.1:5000

---

## Dashboard Modules

### Security Dashboard

Displays real-time system logs, anomaly detection results, and risk classifications.

### Threat Intelligence

Shows detected threat patterns such as brute-force attempts, suspicious logins, and abnormal activity.

### Attack Analytics

Provides visualization of attack trends and regional activity distribution using charts.

---

## Use Case

CyberSentinel demonstrates how AI-based anomaly detection can be used to monitor user behavior and identify potential cybersecurity threats in enterprise systems.

This project can serve as a prototype for security monitoring platforms and behavioral threat detection systems.

---

## Author

Polemoni Poojitha

Computer Science and Engineering Student
