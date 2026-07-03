def analyze_prompt(prompt):

    score = 100
    issues = []

    if len(prompt.split()) < 8:
        score -= 20
        issues.append("Prompt is too short.")

    if "for" not in prompt.lower():
        score -= 15
        issues.append("Target audience is not specified.")

    if "format" not in prompt.lower():
        score -= 15
        issues.append("Output format is missing.")

    if "explain" not in prompt.lower() and "create" not in prompt.lower() and "write" not in prompt.lower():
        score -= 15
        issues.append("Action is not clearly defined.")

    if score < 0:
        score = 0

    return score, issues