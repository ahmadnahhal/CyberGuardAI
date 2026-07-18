from app.services.report_service import generate_report


def execute(
    user_input: str,
    conversation_history: list | None = None,
 ) -> dict:
    
    history_text = ""

    if conversation_history:

     history_text = "Recent conversation:\n\n"

     for turn in conversation_history:

        history_text += (
            f"User: {turn['user']}\n"
            f"Assistant: {turn['assistant']}\n\n"
        )
        
    """
    Generate a cybersecurity report.
    """

    report = generate_report(
     f"""
     {history_text}

     User request:

     {user_input}

     If the user refers to previous topics using words like
     'it', 'that', 'this', or similar,
     use the recent conversation as context.
     """
    )

    return {
        "status": "success",
        "tool": "report",
        "data": report,
        "error": None,
    }