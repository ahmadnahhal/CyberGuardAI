from app.database.database import get_connection


def save_log(
    intent: str,
    selected_tool: str,
    status: str,
    message: str,
) -> int:
    """
    Save one execution log.

    Returns:
        int: ID of the saved log.
    """

    connection = get_connection()

    try:

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO execution_logs (
                intent,
                selected_tool,
                status,
                message
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                intent,
                selected_tool,
                status,
                message,
            ),
        )

        connection.commit()

        return cursor.lastrowid

    finally:

        connection.close()
        
def get_logs() -> list[tuple]:
    """
    Return every execution log.
    """

    connection = get_connection()

    try:

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                id,
                timestamp,
                intent,
                selected_tool,
                status,
                message
            FROM execution_logs
            ORDER BY timestamp DESC
            """
        )

        return cursor.fetchall()

    finally:

        connection.close()
        
def clear_logs() -> None:
    """
    Delete every execution log.
    """

    connection = get_connection()

    try:

        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM execution_logs
            """
        )

        connection.commit()

    finally:

        connection.close()