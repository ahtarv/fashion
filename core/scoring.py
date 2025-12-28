def score_outfit(outfit, preferences):
    score = 0

    for tag in outfit["tags"]:
        if tag in preferences["styles"]:
            score+= 2
        
    if tag in memory["preferred_tags"]:
        score += memory["preferred_tags"][tag]
    
    if tag in memory["disliked_tags"]:
        score -= memory["disliked_tags"][tag]
    
    if outfit["season"] == preferences["season"]:
        score += 1
    
    return score