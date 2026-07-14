import streamlit as st

from app.services.password_checker import analyze_password


def show():

    st.title("🔑 Password Strength Checker")

    st.write(
        "Evaluate the security of your password."
    )

    password = st.text_input(
        "Enter your password",
        type="password",
    )

    if st.button(
        "Analyze Password",
        use_container_width=True,
    ):

        if not password:
            st.warning(
                "Please enter a password."
            )
            return

        result = analyze_password(password)

        st.success(
            f"Strength: {result['strength']}"
        )

        st.metric(
            "Score",
            f"{result['score']}/10"
        )

        st.metric(
            "Entropy",
            f"{result['entropy']} bits"
        )

        st.metric(
            "Estimated Crack Time",
            result["crack_time"],
        )

        st.subheader("Recommendations")

        if result["recommendations"]:

            for recommendation in result["recommendations"]:
                st.write(f"• {recommendation}")

        else:
            st.success(
                "Excellent password!"
            )