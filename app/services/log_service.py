from app.database.database import get_connection


def log_execution(
    intent: str,
    selected_tool: str,
    status: str,
    message: str,
) -> None:

    connection = get_connection()

    try:

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO execution_logs(
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

    finally:

        connection.close()


def get_execution_logs():

    connection = get_connection()

    try:

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
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


def clear_execution_logs():

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