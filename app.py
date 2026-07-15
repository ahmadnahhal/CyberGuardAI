import streamlit as st

from app.components.sidebar import render_sidebar
from app.ui.home import show as show_home
from app.ui.assistant import show as show_assistant
from app.ui.phishing import show as show_phishing
from app.ui.password import show as show_password
from app.ui.reports import show as show_reports
from app.ui.history import show as show_history
from app.ui.about import show as show_about
from app.database.database import initialize_database
from app.state.app_state import initialize

st.set_page_config(
    page_title="CyberGuard AI",
    page_icon="🛡️",
    layout="wide",
)

initialize_database()

initialize()

if "page" not in st.session_state:
    st.session_state["page"] = "Dashboard"
    
page = render_sidebar()

if page == "Dashboard":
    show_home()

elif page == "Assistant":
    show_assistant()

elif page == "Phishing":
    show_phishing()

elif page == "Passwords":
    show_password()

elif page == "Reports":
    show_reports()

elif page == "History":
    show_history()

elif page == "About":
    show_about()