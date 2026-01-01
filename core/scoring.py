def score_outfit(outfit, preferences):
    score = 0

    for tag in outfit["tags"]:
        if tag in preferences["styles"]:
            score+= 2
            resons.append(f"matches your prefferred styles ({tag})")

    if tag in memory["preferred_tags"]:
        score += memory["preferred_tags"][tag]
        resons.append(f"you like {tag} before")
    
    if tag in memory["disliked_tags"]:
        score -= memory["disliked_tags"][tag]
        resons.append(f"you dislike {tag} before")
    
    if outfit["season"] == preferences["season"]:
        score += 1
        resons.append(f"matches your season ({outfit['season']})")
    
    return score, resons