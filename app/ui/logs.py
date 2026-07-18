import streamlit as st

from app.services.log_service import (
    get_execution_logs,
    clear_execution_logs,
)


def show():

    st.title("📋 Execution Logs")

    st.write(
        "History of every AI decision and tool execution."
    )

    st.divider()

    col1, col2 = st.columns([3, 1])

    with col2:

        if st.button(
            "🗑 Clear Logs",
            use_container_width=True,
        ):

            clear_execution_logs()

            st.rerun()

    logs = get_execution_logs()

    if not logs:

        st.info("No execution logs yet.")

        return

    for timestamp, intent, tool, status, message in logs:

        with st.expander(
            f"{timestamp} • {intent.upper()}"
        ):

            st.write(f"**Intent:** {intent}")

            st.write(f"**Tool:** {tool}")

            st.write(f"**Status:** {status}")

            st.write("**Message:**")

            st.write(message)