import streamlit as st

st.set_page_config(
    page_title="CyberGuard AI",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ CyberGuard AI")

st.subheader("Personal Cybersecurity Triage Assistant")

st.write(
    """
Welcome to CyberGuard AI!

This application will help users:

- Analyze cybersecurity incidents
- Detect phishing attempts
- Check password strength
- Learn cybersecurity best practices
- Generate incident reports
"""
)