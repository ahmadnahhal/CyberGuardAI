from app.services.phishing_service import analyze_email


def execute(email_text: str):

   result = analyze_email(email_text)

   return {
    "status": "success",
    "tool": "phishing",
    "data": result,
    "error": None,
    }