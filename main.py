import json
from core.scoring import score_outfit
from memory.memory_store import load_memory, update_memory

with open("data/sample_outfits.json", "r") as f:
    outfits = json.load(f)

memory = load_memory()

user_preferences = {
    "styles": ["minimal",  "neutral"],
    "season": "fall"
}

ranked_outfits = sorted(
    outfits,
    key = lambda o: score_outfit(o, user_preferences),
    reverse=True
)

best = ranked_outfits[0]
print(f"Recommened Outfit:")
print(f"Top: {best['top']}")
print(f"Bottom: {best['bottom']}")
print(f"Shoes: {best['shoes']}")

print("\nWhy this outfit:")
for r in reasons:
    print("-", r)

print("memory updated")