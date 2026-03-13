import numpy as np
from sklearn.ensemble import IsolationForest, RandomForestClassifier
from sklearn.linear_model import LogisticRegression

# -----------------------------
# Reproducibility
# -----------------------------
np.random.seed(42)

# -----------------------------
# Dataset Size
# -----------------------------
normal_samples = 500
abnormal_samples = 120

# -----------------------------
# Generate NORMAL Behavior
# -----------------------------
normal_data = np.column_stack([
    np.random.randint(8, 18, normal_samples),        # login hour (working hours)
    np.random.randint(0, 3, normal_samples),         # failed attempts
    np.zeros(normal_samples),                        # ip change
    np.random.randint(5, 40, normal_samples),        # files accessed
    np.random.randint(120, 300, normal_samples),     # session duration
    np.random.uniform(0.02, 0.2, normal_samples)     # request rate
])

# -----------------------------
# Generate ABNORMAL Behavior
# -----------------------------
# Early night + late night logins
abnormal_login = np.concatenate([
    np.random.randint(0, 6, abnormal_samples // 2),
    np.random.randint(18, 24, abnormal_samples - abnormal_samples // 2)
])

abnormal_data = np.column_stack([
    abnormal_login,
    np.random.randint(3, 8, abnormal_samples),              # more failed attempts
    np.random.choice([0, 1], abnormal_samples, p=[0.3, 0.7]),
    np.random.randint(50, 300, abnormal_samples),           # moderate to high file access
    np.random.randint(10, 150, abnormal_samples),           # shorter sessions
    np.random.uniform(0.3, 1.2, abnormal_samples)           # higher request rate
])

# -----------------------------
# Combine Dataset
# -----------------------------
X = np.vstack((normal_data, abnormal_data))
y = np.array([0]*normal_samples + [1]*abnormal_samples)

# -----------------------------
# Train Models
# -----------------------------
iso_model = IsolationForest(contamination=0.15, random_state=42)
iso_model.fit(normal_data)  # Unsupervised (normal only)

rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X, y)

lr_model = LogisticRegression(max_iter=1000)
lr_model.fit(X, y)

# -----------------------------
# Risk Prediction
# -----------------------------
def predict_risk(features):
    features_array = np.array([features])

    # --- Isolation Forest ---
    iso_raw = iso_model.decision_function(features_array)[0]
    
    # Convert roughly (-0.4 to 0.2 range) into 0–1
    iso_score = min(max((-iso_raw + 0.2) / 0.6, 0), 1)

    # --- Supervised Models ---
    rf_prob = rf_model.predict_proba(features_array)[0][1]
    lr_prob = lr_model.predict_proba(features_array)[0][1]

    # --- Ensemble (more balanced) ---
    final_score = (
        0.4 * iso_score +
        0.35 * rf_prob +
        0.25 * lr_prob
    )

    risk_score = int(final_score * 100)

    return risk_score