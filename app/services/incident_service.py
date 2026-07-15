from datetime import datetime

from app.database.database import get_connection


def create_incident(
    title: str,
    description: str,
    severity: str,
) -> dict:
    """
    Create a new cybersecurity incident.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO incidents (
                title,
                description,
                severity,
                status,
                created_at
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                title,
                description,
                severity,
                "Open",
                datetime.now().isoformat(),
            ),
        )

        connection.commit()

        incident_id = cursor.lastrowid

        return {
            "incident_id": incident_id,
            "title": title,
            "description": description,
            "severity": severity,
            "status": "Open",
        }

    finally:
        connection.close()


def get_all_incidents() -> list[tuple]:
    """
    Return all incidents.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                id,
                title,
                description,
                severity,
                status,
                created_at
            FROM incidents
            ORDER BY created_at DESC
            """
        )

        return cursor.fetchall()

    finally:
        connection.close()


def get_incident(incident_id: int):
    """
    Return one incident by ID.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                id,
                title,
                description,
                severity,
                status,
                created_at
            FROM incidents
            WHERE id = ?
            """,
            (incident_id,),
        )

        return cursor.fetchone()

    finally:
        connection.close()


def update_incident_status(
    incident_id: int,
    status: str,
) -> None:
    """
    Update an incident status.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE incidents
            SET status = ?
            WHERE id = ?
            """,
            (
                status,
                incident_id,
            ),
        )

        connection.commit()

    finally:
        connection.close()


def delete_incident(
    incident_id: int,
) -> None:
    """
    Delete an incident.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM incidents
            WHERE id = ?
            """,
            (incident_id,),
        )

        connection.commit()

    finally:
        connection.close()