from app.knowledge.cybersecurity import KNOWLEDGE_BASE
from app.llm.groq_client import ask_groq
from app.prompts.information_prompt import INFORMATION_SYSTEM_PROMPT
from app.services.memory_service import get_all_preferences
from app.services.language_service import (
    get_user_language,
)


def answer_question(
    question: str,
    conversation_history: list | None = None,
 ) -> dict:
    """
    Answer a cybersecurity question.

    1. Use the local knowledge base if possible.
    2. Otherwise ask the Groq LLM.
    """

    text = question.lower()
    language = get_user_language()

    for keyword, answer in KNOWLEDGE_BASE.items():

     if keyword in text:

        preferences = get_all_preferences()

        memory = ""

        if preferences:

            memory = "Known user preferences:\n"

            for key, value in preferences:

                memory += f"- {key}: {value}\n"

            memory += "\n"

        enhanced = ask_groq(
         INFORMATION_SYSTEM_PROMPT,
          f"""
          Respond ONLY in {language}.

          {memory}

        Knowledge Base:

        {answer}

        User Question:

        {question}

         Expand the answer while remaining consistent with the knowledge base.

         If user preferences are available, naturally adapt the response to them.
         """,

        )

        return {
            "topic": keyword,
            "answer": enhanced,
        }

    try:

        preferences = get_all_preferences()

        memory = ""

        if preferences:

            memory = "Known user preferences:\n"

            for key, value in preferences:

                memory += f"- {key}: {value}\n"

            memory += "\n"

        answer = ask_groq(
         INFORMATION_SYSTEM_PROMPT,
         f"""
         Respond ONLY in {language}.

         {memory}

         User Question:

         {question}
         """,
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