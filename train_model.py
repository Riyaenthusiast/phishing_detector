import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

data = {
    "text": [
        "Verify your bank account now",
        "Urgent password reset required",
        "Click here to win prize",
        "Meeting scheduled tomorrow",
        "Invoice attached",
        "Lunch at 2pm"
    ],
    "label": [1, 1, 1, 0, 0, 0]  # 1 = phishing, 0 = safe
}

df = pd.DataFrame(data)

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression())
])

model.fit(df["text"], df["label"])
joblib.dump(model, "phishing_model.pkl")

print("Model trained & saved")
