from app.services.information_service import answer_question


def execute(
    question: str,
    conversation_history: list | None = None,
):

    result = answer_question(
        question,
        conversation_history,
    )

    return {
        "status": "success",
        "tool": "information",
        "data": result,
        "error": None,
    }