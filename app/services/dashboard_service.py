from app.database.database import get_connection


def get_dashboard_statistics() -> dict:
    """
    Return dashboard statistics.
    """

    connection = get_connection()

    try:

        cursor = connection.cursor()

        cursor.execute(
            "SELECT COUNT(*) FROM reports"
        )
        reports = cursor.fetchone()[0]

        cursor.execute(
            "SELECT COUNT(*) FROM incidents"
        )
        incidents = cursor.fetchone()[0]

        threat_level = "Low"

        if incidents >= 10:
            threat_level = "Critical"

        elif incidents >= 5:
            threat_level = "High"

        elif incidents >= 2:
            threat_level = "Medium"

        return {
            "reports": reports,
            "incidents": incidents,
            "threat_level": threat_level,
            "ai_status": "Ready",
        }

    finally:

        connection.close()