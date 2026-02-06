from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os

app = FastAPI()

class EmailRequest(BaseModel):
    sender: str
    subject: str
    body: str

# -------- Safe ML Model Load --------
MODEL_PATH = "phishing_model.pkl"

if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    model = None

# -------- Rule-based detection --------
def rule_based_detection(text):
    keywords = ["urgent", "verify", "password", "bank", "click", "login"]
    return sum(1 for word in keywords if word in text.lower())

@app.post("/analyze")
def analyze_email(data: EmailRequest):
    rule_score = rule_based_detection(data.body)

    # ML prediction (safe fallback)
    if model:
        ml_prob = model.predict_proba([data.body])[0][1]
    else:
        ml_prob = rule_score / 5  # fallback estimate

    verdict = "Phishing" if (rule_score >= 3 or ml_prob >= 0.6) else "Safe"
    confidence = round(max(rule_score / 5, ml_prob), 2)

    return {
        "verdict": verdict,
        "rule_score": rule_score,
        "ml_probability": round(ml_prob, 2),
        "confidence": confidence
    }
