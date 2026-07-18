from app.services.password_checker import analyze_password
from app.services.password_generator import generate_password


def execute(user_input: str):

    text = user_input.lower().strip()

    generate_request = (
        "password" in text
        and any(
            word in text
            for word in (
                "generate",
                "create",
                "make",
                "new",
                "strong",
                "secure",
                "random",
                "passphrase",
            )
        )
    )

    if generate_request:

        password = generate_password()

        result = analyze_password(password)

        result["generated_password"] = password

    else:

        result = analyze_password(user_input)

    return {
        "status": "success",
        "tool": "password",
        "data": result,
        "error": None,
    }