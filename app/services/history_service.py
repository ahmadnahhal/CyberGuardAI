from app.database.database import get_connection


def save_chat(
    user_message: str,
    assistant_response: str,
) -> int:
    """
    Save one conversation to the chat_history table.

    Returns:
        int: ID of the saved chat record.
    """

    connection = get_connection()

    try:
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

        return cursor.lastrowid

    finally:
        connection.close()


def get_chat_history() -> list:
    """
    Retrieve all saved conversations.

    Returns:
        list: Chat history ordered from newest to oldest.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                id,
                user_message,
                assistant_response,
                created_at
            FROM chat_history
            ORDER BY created_at DESC
            """
        )

        return cursor.fetchall()

    finally:
        connection.close()


def clear_chat_history() -> None:
    """
    Delete every conversation from the chat history.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM chat_history
            """
        )

        connection.commit()

    finally:
        connection.close()