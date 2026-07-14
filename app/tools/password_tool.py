from app.services.password_checker import analyze_password


def execute(password: str):
    """
    Execute the password analysis tool.
    """

    return analyze_password(password)