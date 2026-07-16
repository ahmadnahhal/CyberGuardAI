import streamlit as st

from app.agent.graph import process_request


def show():

    st.title("🤖 CyberGuard AI Assistant")

    st.write(
        "Ask me anything about cybersecurity."
    )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "agent_state" not in st.session_state:
        st.session_state.agent_state = None

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input(
        "Ask CyberGuard AI..."
    )

    if prompt:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.spinner("CyberGuard AI is thinking..."):

            state = process_request(
                prompt,
                st.session_state.agent_state,
            )

            st.session_state.agent_state = state

        assistant_message = state["response"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": assistant_message,
            }
        )

        with st.chat_message("assistant"):
            st.markdown(assistant_message)