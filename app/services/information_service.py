from app.knowledge.cybersecurity import KNOWLEDGE_BASE


def answer_question(question: str):

    text = question.lower()

    for keyword, answer in KNOWLEDGE_BASE.items():

        if keyword in text:
            return {
                "topic": keyword,
                "answer": answer,
            }

    return {
        "topic": "unknown",
        "answer": (
            "I don't currently have information about that topic."
        ),
    }