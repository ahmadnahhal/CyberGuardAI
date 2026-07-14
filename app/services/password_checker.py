"""
Password analysis service for CyberGuard AI.

This module contains the business logic used to evaluate
password strength. It does not contain any Streamlit code.
"""

import math
import re
from pathlib import Path
SEQUENCES = [
    "1234567890",
    "abcdefghijklmnopqrstuvwxyz",
    "qwertyuiop",
]

def load_common_passwords() -> set[str]:
    """
    Load the list of common passwords.
    """

    file_path = Path("data/common_passwords.txt")

    if not file_path.exists():
        return set()

    with file_path.open("r", encoding="utf-8") as file:
        return {
            line.strip().lower()
            for line in file
            if line.strip()
        }
        
def has_repeated_characters(password: str) -> bool:
    """
    Return True if the password consists of only one repeated character.
    """

    if not password:
        return False

    return len(set(password)) == 1

def contains_sequence(password: str) -> bool:
    """
    Return True if the password contains a predictable sequence.
    """

    password = password.lower()

    for sequence in SEQUENCES:

        for i in range(len(sequence) - 2):

            chunk = sequence[i:i + 3]

            if chunk in password:
                return True

    return False
        
def analyze_password(password: str) -> dict:
    """
    Analyze a password and return security metrics.
    """

    score = 0
    recommendations = []
    common_passwords = load_common_passwords()

    length = len(password)

    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_symbol = bool(re.search(r"[^A-Za-z0-9]", password))

    # Length
    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        recommendations.append(
            "Use at least 12 characters."
        )

    # Uppercase
    if has_upper:
        score += 2
    else:
        recommendations.append(
            "Add uppercase letters."
        )

    # Lowercase
    if has_lower:
        score += 2
    else:
        recommendations.append(
            "Add lowercase letters."
        )

    # Numbers
    if has_digit:
        score += 2
    else:
        recommendations.append(
            "Add numbers."
        )

    # Symbols
    if has_symbol:
        score += 2
    else:
        recommendations.append(
            "Add special characters."
        )
        
    # Repeated characters
    if has_repeated_characters(password):
     score = max(score - 3, 0)
     recommendations.append("Avoid repeating the same character throughout the password.")
     
    if contains_sequence(password):
     score = max(score - 2, 0)
     recommendations.append("Avoid predictable sequences such as '123', 'abc', or 'qwerty'.")
    
    if password.lower() in common_passwords:
     return {
        "score": 0,
        "strength": "Very Weak",
        "entropy": 0,
        "crack_time": "Instantly",
        "recommendations": [
            "This password is extremely common.",
            "Choose a unique password that is not found in common password lists.",
        ],
    }

    entropy = calculate_entropy(
        password,
        has_upper,
        has_lower,
        has_digit,
        has_symbol,
    )

    strength = determine_strength(score)

    crack_time = estimate_crack_time(entropy)

    return {
        "score": score,
        "strength": strength,
        "entropy": round(entropy, 1),
        "crack_time": crack_time,
        "recommendations": recommendations,
    }
    
def calculate_entropy(
    password,
    upper,
    lower,
    digit,
    symbol,
):
    """
    Estimate password entropy in bits.
    """

    charset = 0

    if lower:
        charset += 26

    if upper:
        charset += 26

    if digit:
        charset += 10

    if symbol:
        charset += 32

    if charset == 0:
        return 0

    return len(password) * math.log2(charset)

def determine_strength(score):
    """
    Convert the numeric score into a label.
    """

    if score <= 3:
        return "Weak"

    if score <= 6:
        return "Medium"

    if score <= 8:
        return "Strong"

    return "Very Strong"

def estimate_crack_time(entropy: float) -> str:
    """
    Estimate how long it would take to brute-force a password.

    This is an educational estimate based on entropy alone.
    Real-world attacks may be much faster if the password
    is common or follows predictable patterns.
    """

    if entropy < 20:
        return "Instantly"

    elif entropy < 35:
        return "Minutes"

    elif entropy < 50:
        return "Days"

    elif entropy < 65:
        return "Months"

    elif entropy < 80:
        return "Years"

    elif entropy < 100:
        return "Centuries"

    return "Practically impossible"