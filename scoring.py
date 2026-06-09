def calculate_score(password):
    score = 0

    length = len(password)

    score += min(length * 4, 40)

    if any(c.isupper() for c in password):
        score += 15

    if any(c.islower() for c in password):
        score += 15

    if any(c.isdigit() for c in password):
        score += 15

    if any(not c.isalnum() for c in password):
        score += 15

    return min(score, 100)