import streamlit as st

from app.database.database import get_connection


def show():

    st.title("🕘 History")

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            created_at,
            user_message,
            assistant_response
        FROM chat_history
        ORDER BY id DESC
        """
    )

    rows = cursor.fetchall()

    connection.close()

    if not rows:

        st.info("No history yet.")

        return

    for created_at, user, assistant in rows:

        with st.expander(created_at):

            st.write("### User")

            st.write(user)

            st.write("### Result")

            st.write(assistant)