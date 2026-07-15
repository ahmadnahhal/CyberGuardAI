from app.llm.groq_client import ask_groq
from app.prompts.router_prompt import ROUTER_SYSTEM_PROMPT


VALID_INTENTS = {
    "password",
    "phishing",
    "incident",
    "report",
    "information",
}


def detect_intent(user_input: str) -> str:
    """
    Use the LLM to determine which tool should handle the request.
    """

    try:

        intent = ask_groq(
            ROUTER_SYSTEM_PROMPT,
            user_input,
        ).strip().lower()

        if intent in VALID_INTENTS:
            return intent

    except Exception as error:

        print(f"Router Error: {error}")

    return "information"