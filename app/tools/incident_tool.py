import json

from app.llm.groq_client import ask_groq
from app.prompts.incident_prompt import INCIDENT_SYSTEM_PROMPT
from app.services.language_service import get_user_language
from app.services.incident_service import (
    create_incident,
    get_all_incidents,
    get_incident,
    update_incident_status,
    delete_incident,
)


def execute(
    user_input: str,
    conversation_history: list | None = None,
) -> dict:

    language = get_user_language()
    
    history_text = ""

    if conversation_history:

     history_text = "Recent conversation:\n\n"

     for turn in conversation_history:

        history_text += (
            f"User: {turn['user']}\n"
            f"Assistant: {turn['assistant']}\n\n"
        )

    response = ask_groq(
    INCIDENT_SYSTEM_PROMPT,
    f"""
Respond ONLY in {language}.

{history_text}

User request:

{user_input}

Use the recent conversation if the request refers to previous topics
using words like "it", "that", "this", or similar.

Return ONLY valid JSON.
""",
)

    incident = json.loads(response)

    result = create_incident(
        title=incident["title"],
        description=incident["description"],
        severity=incident["severity"],
    )

    return {
        "status": "success",
        "tool": "incident",
        "data": result,
        "error": None,
    }


def list_incidents() -> dict:
    """
    Return all incidents.
    """

    result = get_all_incidents()

    return {
        "status": "success",
        "tool": "incident",
        "data": result,
        "error": None,
    }


def retrieve_incident(incident_id: int) -> dict:
    """
    Return a single incident.
    """

    result = get_incident(incident_id)

    if result is None:
        return {
            "status": "error",
            "tool": "incident",
            "data": None,
            "error": "Incident not found.",
        }

    return {
        "status": "success",
        "tool": "incident",
        "data": result,
        "error": None,
    }


def change_status(
    incident_id: int,
    status: str,
) -> dict:
    """
    Update an incident status.
    """

    update_incident_status(
        incident_id,
        status,
    )

    return {
        "status": "success",
        "tool": "incident",
        "data": {
            "incident_id": incident_id,
            "status": status,
        },
        "error": None,
    }


def remove_incident(
    incident_id: int,
) -> dict:
    """
    Delete an incident.
    """

    delete_incident(incident_id)

    return {
        "status": "success",
        "tool": "incident",
        "data": {
            "incident_id": incident_id,
        },
        "error": None,
    }