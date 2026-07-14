import sqlite3
from pathlib import Path

DATABASE_PATH = Path("data/cyberguard.db")


def get_connection():
    """
    Create and return a connection to the SQLite database.
    """
    DATABASE_PATH.parent.mkdir(exist_ok=True)

    return sqlite3.connect(DATABASE_PATH)

def initialize_database():
    """
    Create all database tables if they do not exist.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS password_checks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        password_strength TEXT,
        score INTEGER,
        entropy REAL,
        crack_time TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS phishing_reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        risk_level TEXT,
        findings TEXT,
        recommendations TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        report_type TEXT,
        content TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chat_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_message TEXT,
        assistant_response TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    connection.commit()
    connection.close()