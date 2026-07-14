import streamlit as st

from app.agent.graph import process_request


def show():

    st.title("📚 Cybersecurity Learning")

    question = st.text_input(
        "Ask a cybersecurity question"
    )

    if st.button(
        "Ask",
        use_container_width=True,
    ):

        if not question:
            st.warning("Please enter a question.")
            return

        response = process_request(
            question,
            intent="information",
        )

        result = response["result"]

        st.subheader(result["topic"].title())

        st.write(result["answer"])