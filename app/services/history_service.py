from app.database.database import get_connection


def save_chat(user_message: str, assistant_response: str):
    """
    Save one interaction to the chat_history table.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO chat_history (
            user_message,
            assistant_response
        )
        VALUES (?, ?)
        """,
        (
            user_message,
            assistant_response,
        ),
    )

    connection.commit()
    connection.close()