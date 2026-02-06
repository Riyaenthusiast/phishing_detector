# phishing_detector
A full-stack phishing email detection system that analyzes email content using both rule-based heuristics and machine learning models. The system provides real-time verdicts with confidence scores through a secure API backend and an interactive Streamlit dashboard.
The system consists of three layers:

Frontend (Streamlit): User interface for real-time email testing and visualization

Backend (FastAPI): REST API endpoint /analyze for email processing

Detection Engine: Combines rule-based phishing keyword scoring with a trained ML classifier

The backend returns structured JSON responses including:

Phishing verdict

Rule-based risk score

Machine learning confidence level

This modular architecture supports scalability, real-time analysis, and SOC-style deployment models.

🛠️ Tech Stack

Backend: FastAPI (Python)

Frontend: Streamlit

ML: Scikit-learn, NLP

Security: Input validation, API-based architecture

Tools: Git, Postman

▶️ How to Run
git clone https://github.com/yourusername/phishing-detection-engine.git
cd phishing-detection-engine
pip install -r requirements.txt
uvicorn app:app --reload
streamlit run dashboard.py

📊 Features

✔ Phishing email classification
✔ Rule-based + ML hybrid detection
✔ Confidence score generation
✔ Real-time dashboard testing
✔ RESTful API architecture

📌 Example API Response
{
  "verdict": "Phishing",
  "confidence": 0.93,
  "rule_score": 8.5
}

👤 Author

Riya Singh — Cybersecurity & ML Enthusiast

If you want, I can:
✅ Add screenshots section
✅ Add dataset/model training section
✅ Convert this into SIH / college submission format
✅ Add badges + GitHub styling

Just tell me 💙
