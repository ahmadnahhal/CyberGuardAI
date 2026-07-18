from app.database.database import get_connection


def save_preference(key: str, value: str):

    connection = get_connection()

    try:

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO user_preferences(
                preference_key,
                preference_value
            )
            VALUES(?, ?)
            ON CONFLICT(preference_key)
            DO UPDATE SET
            preference_value=excluded.preference_value
            """,
            (
                key,
                value,
            ),
        )

        connection.commit()

    finally:

        connection.close()


def get_preference(key: str):

    connection = get_connection()

    try:

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT preference_value
            FROM user_preferences
            WHERE preference_key=?
            """,
            (key,),
        )

        row = cursor.fetchone()

        if row:

            return row[0]

        return None

    finally:

        connection.close()


def get_all_preferences():

    connection = get_connection()

    try:

        cursor = connection.cursor()

        cursor.execute(
           """
            SELECT
            preference_key,
            preference_value
            FROM user_preferences
            ORDER BY preference_key
            """
            )

        return cursor.fetchall()

    finally:

        connection.close()
        
def delete_preference(key: str):

    connection = get_connection()

    try:

        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM user_preferences
            WHERE preference_key = ?
            """,
            (key,),
        )

        connection.commit()

    finally:

        connection.close()


def clear_preferences():

    connection = get_connection()

    try:

        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM user_preferences
            """
        )

        connection.commit()

    finally:

        connection.close()