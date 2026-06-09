from scoring import calculate_score
from entropy import calculate_entropy


def get_entropy_rating(entropy):
    if entropy < 40:
        return "Poor"

    if entropy < 60:
        return "Fair"

    if entropy < 80:
        return "Good"

    return "Excellent"

def analyze_password(password):
    score = calculate_score(password)
    entropy = calculate_entropy(password)
    entropy_rating = get_entropy_rating(entropy)

    issues = []
    suggestions = []

    if len(password) < 12:
        issues.append("Password is too short")
        suggestions.append("Use at least 12 characters")

    if not any(char.isupper() for char in password):
        issues.append("No uppercase letters")
        suggestions.append("Add uppercase letters")

    if not any(char.islower() for char in password):
        issues.append("No lowercase letters")
        suggestions.append("Add lowercase letters")

    if not any(char.isdigit() for char in password):
        issues.append("No numbers")
        suggestions.append("Add numbers")

    if not any(not char.isalnum() for char in password):
        issues.append("No special characters")
        suggestions.append("Add special characters")

    if score < 40:
        strength = "Weak"
    elif score < 70:
        strength = "Moderate"
    else:
        strength = "Strong"

    return {
        "score": score,
        "entropy": entropy,
        "entropy_rating": entropy_rating,
        "strength": strength,
        "issues": issues,
        "suggestions": suggestions
    }