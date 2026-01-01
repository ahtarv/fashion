import time

def score_outfit(outfit, preferences, memory):
    score = 0
    reasons = []
    now = time.time()

    for tag in outfit["tags"]:
        # Preference match
        if tag in preferences["styles"]:
            score += 2
            reasons.append(f"matches your preferred style ({tag})")

        # Learned memory
        if tag in memory["preferred_tags"]:
            entry = memory["preferred_tags"][tag]
            age = now - entry["last_updated"]
            decay = max(0.2, 1 - (age / (60 * 60 * 24 * 7)))  # 1 week decay
            weighted = entry["score"] * decay

            score += weighted
            reasons.append(f"you liked {tag} before")

    return score, reasons
