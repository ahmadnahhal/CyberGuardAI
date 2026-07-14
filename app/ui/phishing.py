import streamlit as st

from app.agent.graph import process_request


def show():

    st.title("📧 Phishing Detection")

    email = st.text_area(
        "Paste an email or message"
    )

    if st.button(
        "Analyze Email",
        use_container_width=True,
    ):

        if not email:

            st.warning("Please paste an email.")

            return

        response = process_request(
            email,
            intent="phishing",
        )

        result = response["result"]

        if result["risk"] == "High":
            st.error(f"Risk: {result['risk']}")

        elif result["risk"] == "Medium":
            st.warning(f"Risk: {result['risk']}")

        else:
            st.success(f"Risk: {result['risk']}")

        st.metric(
            "Risk Score",
            result["score"],
        )

        st.subheader("Indicators")

        if result["findings"]:

            for finding in result["findings"]:
                st.write(f"• {finding}")

        else:
            st.success("No suspicious indicators found.")