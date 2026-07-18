import json
from app.llm.groq_client import ask_groq
from app.prompts.memory_prompt import MEMORY_SYSTEM_PROMPT
from app.services.memory_service import save_preference
from app.services.language_service import set_user_language


def execute(user_input: str):

    try:

        response = ask_groq(
            MEMORY_SYSTEM_PROMPT,
            user_input,
        )

        memory = json.loads(response)
        # Handle language preference
        key = memory.get("key", "").strip().lower()
        value = memory.get("value", "").strip().lower()

        if key == "preferred_language":

           if value in ("english", "french"):

             set_user_language(value)

             return {
              "status": "success",
              "tool": "memory",
              "data": {
                "message": (
                    "Language preference saved."
                    if value == "english"
                    else "Préférence de langue enregistrée."
                )
               },
               "error": None,
              }

    except Exception:

        return {
            "status": "error",
            "tool": "memory",
            "data": None,
            "error": "Unable to extract memory.",
        }

    if not memory.get("save"):

        return {
            "status": "success",
            "tool": "memory",
            "data": {
                "message": "Nothing to remember."
            },
            "error": None,
        }

    key = memory["key"].strip().lower()

    value = memory["value"].strip()

    if key == "preferred_language":

     set_user_language(value)

     return {
        "status": "success",
        "tool": "memory",
        "data": {
            "message": (
                "Language preference saved. I will respond in English from now on."
                if value == "english"
                else "Préférence de langue enregistrée. Je répondrai désormais en français."
            )
        },
        "error": None,
    }

    save_preference(
     key,
     value,
     )

    return {
     "status": "success",
     "tool": "memory",
     "data": {
        "message": f"I'll remember your {key}: {value}"
     },
     "error": None,
    }