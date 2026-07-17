import random

import streamlit as st

from app.components.card import status_card
from app.services.dashboard_service import get_dashboard_statistics
from data.tips import TIPS


def show():

    stats = get_dashboard_statistics()

    st.title("🛡️ CyberGuard AI")

    st.subheader("Personal Cybersecurity Triage Assistant")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        status_card(
            "🤖",
            "AI Status",
            stats["ai_status"],
        )

    with col2:
        status_card(
            "🛡",
            "Threat Level",
            stats["threat_level"],
        )

    with col3:
        status_card(
            "📄",
            "Reports",
            str(stats["reports"]),
        )

    with col4:
        status_card(
            "📁",
            "Incidents",
            str(stats["incidents"]),
        )

    st.divider()

    st.subheader("🚀 Quick Actions")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🤖 Open Assistant",
            use_container_width=True,
        ):
            st.session_state.page = "Assistant"
            st.rerun()

        if st.button(
            "📧 Analyze Email",
            use_container_width=True,
        ):
            st.session_state.page = "Phishing"
            st.rerun()

    with col2:

        if st.button(
            "🔑 Check Password",
            use_container_width=True,
        ):
            st.session_state.page = "Passwords"
            st.rerun()

        if st.button(
            "📄 Generate Report",
            use_container_width=True,
        ):
            st.session_state.page = "Reports"
            st.rerun()

    st.divider()

    st.info(
        f"💡 Cyber Tip of the Day:\n\n{random.choice(TIPS)}"
    )