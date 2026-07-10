import streamlit as st

DEFAULT_PAGE = "Dashboard"

def initialize():
    if "page" not in st.session_state:
        st.session_state.page = DEFAULT_PAGE

    if "ai_status" not in st.session_state:
        st.session_state.ai_status = "Connected"

    if "theme" not in st.session_state:
        st.session_state.theme = "Dark"

    if "language" not in st.session_state:
        st.session_state.language = "English"