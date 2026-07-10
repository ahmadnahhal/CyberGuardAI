import streamlit as st
from app.components.card import status_card
import random
from data.tips import TIPS


def show():
    st.title("🛡️ CyberGuard AI")

    st.subheader("Personal Cybersecurity Triage Assistant")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        status_card("🤖", "AI Status", "Ready")

    with col2:
        status_card("🛡", "Threat Level", "Low")

    with col3:
        status_card("📄", "Reports", "0")

    with col4:
        status_card("📁", "Incidents", "0")

    st.divider()

    st.subheader("🚀 Quick Actions")

    col1, col2 = st.columns(2)

    with col1:
        st.button("🤖 Open Assistant", use_container_width=True)
        st.button("📧 Analyze Email", use_container_width=True)

    with col2:
        st.button("🔑 Check Password", use_container_width=True)
        st.button("📄 Generate Report", use_container_width=True)
    
    st.divider()
    
    st.info(f"💡 Cyber Tip of the Day:\n\n{random.choice(TIPS)}")