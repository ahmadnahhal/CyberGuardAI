from app.services.report_service import generate_report


def execute(user_input: str) -> dict:
    """
    Generate a cybersecurity report.
    """

    report = generate_report(user_input)

    return {
        "status": "success",
        "tool": "report",
        "data": report,
        "error": None,
    }