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
    Use the LLM to determine which tool should handle the user's request.
    Falls back safely if the model returns extra text.
    """

    try:

        response = ask_groq(
            ROUTER_SYSTEM_PROMPT,
            user_input,
        )

        print("\n===== ROUTER =====")
        print("USER:", user_input)
        print("RAW RESPONSE:", response)
        print("==================\n")

        response = response.lower().strip()

        for intent in VALID_INTENTS:
            if intent in response:
                return intent

    except Exception as error:

        print(f"Router Error: {error}")

    return "information"