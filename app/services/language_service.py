from app.services.memory_service import (
    get_preference,
    save_preference,
)


FRENCH_KEYWORDS = {
    "bonjour",
    "merci",
    "oui",
    "non",
    "rapport",
    "incident",
    "mot de passe",
    "sécurité",
    "analyse",
    "phishing",
    "français",
}

ENGLISH_KEYWORDS = {
    "hello",
    "thanks",
    "yes",
    "no",
    "password",
    "report",
    "incident",
    "security",
    "analyze",
    "remember",
    "english",
}


def detect_language(text: str) -> str:

    text = text.lower()

    french = sum(word in text for word in FRENCH_KEYWORDS)
    english = sum(word in text for word in ENGLISH_KEYWORDS)

    if french > english:
        return "french"

    return "english"


def get_user_language() -> str:

    language = get_preference("preferred_language")

    if language:
        return language

    return "english"


def set_user_language(language: str):

    save_preference(
        "preferred_language",
        language.lower(),
    )