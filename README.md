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
 Tech Stack:
Backend: FastAPI (Python)
Frontend: Streamlit
ML: Scikit-learn, NLP
Security: Input validation, API-based architecture
Tools: Git, Postman

