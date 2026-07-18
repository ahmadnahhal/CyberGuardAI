from datetime import datetime
from app.llm.groq_client import ask_groq
from app.database.database import get_connection
from app.services.language_service import get_user_language

REPORT_PROMPT = """
You are CyberGuard AI.

You are a professional cybersecurity incident analyst.

You are CyberGuard AI.

You are a professional cybersecurity incident analyst.

IMPORTANT:

Always write the report in the language requested by the user.

If instructed to respond in French, write the entire report in French.

If instructed to respond in English, write the entire report in English.

Never mix languages.

Write a detailed investigation report.

Use this structure exactly:

# CyberGuard Investigation Report

## Executive Summary

## Incident Overview

## Threat Analysis

## Risk Assessment

## Immediate Actions

## Long-Term Recommendations

## Conclusion

Requirements:

- Professional tone.
- Base the report only on the provided incident.
- Never invent impossible facts.
- If information is missing, clearly state assumptions.
- Give practical cybersecurity advice.
"""

def generate_report(
    user_input: str,
    incident_id: int | None = None,
 ) -> dict:
    """
    Generate and save a cybersecurity report.
    """

    language = get_user_language()
    
    title = (
     f"Rapport CyberGuard - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
     if language == "french"
     else f"CyberGuard Report - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
     )

    report = {
     "title": title,
     "report_type": "Cybersecurity Incident",
     "content": ask_groq(
        REPORT_PROMPT,
        f"""
    Respond ONLY in {language}.

    {user_input}
    """,
     ),
    }

    connection = get_connection()

    try:

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO reports(
                title,
                report_type,
                content
            )
            VALUES (?, ?, ?)
            """,
            (
                report["title"],
                report["report_type"],
                report["content"],
            ),
        )

        connection.commit()

        report["report_id"] = cursor.lastrowid

        return report

    finally:

        connection.close()

def get_reports() -> list[tuple]:
    """
    Return all saved reports.
    """

    connection = get_connection()

    try:

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                id,
                title,
                report_type,
                content,
                created_at
            FROM reports
            ORDER BY created_at DESC
            """
        )

        return cursor.fetchall()

    finally:

        connection.close()

def get_report(report_id: int):

    connection = get_connection()

    try:

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                id,
                title,
                report_type,
                content,
                created_at
            FROM reports
            WHERE id = ?
            """,
            (report_id,),
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return {
            "report_id": row[0],
            "title": row[1],
            "report_type": row[2],
            "content": row[3],
            "created_at": row[4],
        }

    finally:

        connection.close()
        
def generate_report_from_incident(
    incident: dict,
) -> dict:

    report = generate_report(
        f"""
Incident Title:
{incident['title']}

Description:
{incident['description']}

Severity:
{incident['severity']}

Status:
{incident['status']}
"""
    )

    return report