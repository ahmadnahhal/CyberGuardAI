def analyze_email(email_text: str):

    text = email_text.lower()

    score = 0
    findings = []

    suspicious_keywords = [
        "urgent",
        "verify",
        "password",
        "login",
        "bank",
        "click",
        "account",
        "gift",
        "free",
        "winner",
    ]

    for keyword in suspicious_keywords:

        if keyword in text:
            score += 1
            findings.append(f"Contains '{keyword}'")

    if "http://" in text:
        score += 2
        findings.append("Uses insecure HTTP link")

    if "https://" in text:
        findings.append("Contains HTTPS link")

    if score >= 6:
        risk = "High"

    elif score >= 3:
        risk = "Medium"

    else:
        risk = "Low"

    return {
        "risk": risk,
        "score": score,
        "findings": findings,
    }