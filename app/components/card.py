import streamlit as st

def status_card(icon: str, title: str, value: str):
    """Display a reusable dashboard status card."""

    with st.container(border=True):
        st.markdown(f"### {icon}")
        st.caption(title)
        st.markdown(f"## {value}")