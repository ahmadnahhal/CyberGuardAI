from app.services.incident_service import (
    create_incident,
    get_all_incidents,
    get_incident,
    update_incident_status,
    delete_incident,
)


def execute(user_input: str) -> dict:
    """
    Execute the incident management tool.
    """

    result = create_incident(
        title="Cybersecurity Incident",
        description=user_input,
        severity="Medium",
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