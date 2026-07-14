def detect_intent(user_input: str) -> str:
    """
    Determine which capability the user is requesting.
    """

    text = user_input.lower()

    password_keywords = [
        "password",
        "passphrase",
        "credential",
    ]

    phishing_keywords = [
        "phishing",
        "email",
        "link",
        "url",
    ]

    report_keywords = [
        "report",
        "pdf",
        "summary",
    ]

    for keyword in password_keywords:
        if keyword in text:
            return "password"

    for keyword in phishing_keywords:
        if keyword in text:
            return "phishing"

    for keyword in report_keywords:
        if keyword in text:
            return "report"

    return "information"