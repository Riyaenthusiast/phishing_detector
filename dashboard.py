import streamlit as st
import requests

st.set_page_config(page_title="Phishing Detection Engine", layout="centered")

st.title("🚨 Phishing Detection Engine")

sender = st.text_input("Sender Email")
subject = st.text_input("Email Subject")
body = st.text_area("Email Body")

if st.button("Analyze Email"):
    payload = {
        "sender": sender,
        "subject": subject,
        "body": body
    }

    res = requests.post("http://127.0.0.1:8000/analyze", json=payload)

    if res.status_code == 200:
        data = res.json()

        st.subheader("🔍 Detection Result")
        st.write("**Verdict:**", data["verdict"])
        st.write("**Rule Score:**", data["rule_score"])
        st.write("**Confidence:**", f'{int(data["confidence"] * 100)}%')

        st.progress(data["confidence"])

    else:
        st.error("Backend not reachable")
