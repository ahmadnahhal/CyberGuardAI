from app.services.phishing_service import analyze_email


def execute(email_text: str):

    return analyze_email(email_text)