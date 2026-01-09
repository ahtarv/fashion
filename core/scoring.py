import time

NEUTRAL_COLORS = {
    "black", "white", "grey", "beige", "brown", "navy", "cream"
}

WARM_COLORS = {
    "beige", "brown", "tan", "olive", "rust"
}

COOL_COLORS = {
    "blue", "grey", "navy", "black", "white"
}


def score_outfit(outfit, preferences, memory):
    score = 0
    reasons = []
    now = time.time()

    colors = outfit.get("colors", [])

    if colors:
        neutral_count = sum(c in NEUTRAL_COLORS for c in colors)
        warm_count = sum(c in WARM_COLORS for c in colors)
        cool_count = sum(c in COOL_COLORS for c in colors)

        if neutral_count >= 2:
            score+= 2
            reasons.append("Clean neutral color palette")
        
        if warm_count >= 2:
            score+= 1
            reasons.append("Warm color palette")
        
        if cool_count >= 2:
            score+= 1
            reasons.append("Cool color palette")
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

        if outfit["id"] in memory.get("recent_outfits", []):
            score -= 3
            reasons.append("shown recently, reducing repetition")

    return score, reasons

def compute_confidence(score, reasons, exploration = False):
    base = min(score/10, 1.0)
    if exploration:
        base *= 0.6
    return round(base, 2)
