from app.services.information_service import answer_question


def execute(question: str):

    result = answer_question(question)

    return {
    "status": "success",
    "tool": "information",
    "data": result,
    "error": None,
    }