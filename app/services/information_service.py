from app.knowledge.cybersecurity import KNOWLEDGE_BASE
from app.llm.groq_client import ask_groq
from app.prompts.information_prompt import INFORMATION_SYSTEM_PROMPT


def answer_question(question: str) -> dict:
    """
    Answer a cybersecurity question.

    1. Use the local knowledge base if possible.
    2. Otherwise ask the Groq LLM.
    """

    text = question.lower()

    for keyword, answer in KNOWLEDGE_BASE.items():

        if keyword in text:

            return {
                "topic": keyword,
                "answer": answer,
            }

    try:

        answer = ask_groq(
            INFORMATION_SYSTEM_PROMPT,
            question,
        )

        return {
            "topic": "llm",
            "answer": answer,
        }

    except Exception as error:

        return {
            "topic": "error",
            "answer": (
                f"Unable to contact the AI model.\n\n"
                f"Error: {error}"
            ),
        }