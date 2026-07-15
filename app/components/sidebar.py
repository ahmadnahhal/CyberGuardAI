import streamlit as st

# Navigation items (icon, page name)
NAV_ITEMS = [
    ("🏠", "Dashboard"),
    ("🤖", "Assistant"),
    ("📧", "Phishing"),
    ("🔑", "Passwords"),
    ("📄", "Reports"),
    ("🕘", "History"),
    ("ℹ️", "About"),
]


def render_sidebar():
    """Render the application sidebar and return the selected page."""

    if "page" not in st.session_state:
        st.session_state.page = "Dashboard"

    with st.sidebar:

        # ===== Header =====
        st.markdown(
            """
            <div style="text-align:center;">
                <h2 style="margin-bottom:0;">🛡 CyberGuard AI</h2>
                <p style="color:#94A3B8; margin-top:0;">
                    Personal Cybersecurity Assistant
                </p>
                <p style="font-size:12px; color:gray;">
                    Version 1.0.0
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.divider()

        # ===== Navigation =====
        for icon, name in NAV_ITEMS:

            # Highlight current page
            if st.session_state.page == name:
                st.markdown(
                    f"""
                    <div style="
                        background:#1E3A8A;
                        color:white;
                        padding:8px;
                        border-radius:8px;
                        margin-bottom:6px;
                        text-align:center;
                        font-weight:bold;
                    ">
                        {icon} {name}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            else:
                if st.button(
                    f"{icon} {name}",
                    use_container_width=True,
                    key=f"nav_{name}"
                ):
                    st.session_state.page = name
                    st.rerun()

        st.divider()

        # ===== AI Status =====
        st.markdown("### 🤖 AI Status")
        st.success("Connected")
        
        st.divider()

        st.caption("Language")
        st.write("🇬🇧 English")

        st.caption("AI Model")
        st.write("Groq (coming soon)")
        
        st.divider()

        st.caption("© 2026 CyberGuard AI")

    return st.session_state.page