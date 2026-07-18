import streamlit as st

from app.services.history_service import (
    get_chat_history,
    clear_chat_history,
)


def show():

    st.title("🕘 Chat History")

    st.write(
        "View previously saved conversations with CyberGuard AI."
    )

    st.divider()

    history = get_chat_history()

    col1, col2 = st.columns([4, 1])

    with col1:
        st.subheader(
            f"💬 Conversations ({len(history)})"
        )

    with col2:

        if history:

            if st.button(
                "🗑 Clear History",
                use_container_width=True,
            ):

                clear_chat_history()

                st.success(
                    "Chat history cleared."
                )

                st.rerun()

    if not history:

        st.info(
            "No conversations have been saved yet."
        )

        return

    for chat in history:

        (
            chat_id,
            user_message,
            assistant_response,
            created_at,
        ) = chat

        with st.expander(
            f"💬 Conversation #{chat_id}"
        ):

            st.caption(
                f"Created: {created_at}"
            )

            st.markdown("---")

            st.markdown("### 👤 User")

            st.write(user_message)

            st.markdown("### 🤖 CyberGuard AI")

            st.code(
                assistant_response,
                language="text",
            )