from app.services.password_checker import analyze_password


def execute(password: str):

    result = analyze_password(password)

    return {
        "status": "success",
        "tool": "password",
        "data": result,
        "error": None,
    }