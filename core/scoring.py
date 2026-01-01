def score_outfit(outfit, preferences, memory):
    score = 0
    reasons = []

    for tag in outfit["tags"]:
        if tag in preferences["styles"]:
            score += 2
            reasons.append(f"matches your preferred style ({tag})")

        if tag in memory["preferred_tags"]:
            score += memory["preferred_tags"][tag]
            reasons.append(f"you liked {tag} before")

        if tag in memory["disliked_tags"]:
            score -= memory["disliked_tags"][tag]
            reasons.append(f"you usually dislike {tag}")

    if outfit["season"] == preferences["season"]:
        score += 1
        reasons.append(f"fits the {outfit['season']} season")

    return score, reasons
