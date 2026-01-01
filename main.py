import json
from core.scoring import score_outfit
from memory.memory_store import load_memory, update_memory

with open("data/sample_outfits.json") as f:
    outfits = json.load(f)

memory = load_memory()

user_preferences = {
    "styles": ["minimal", "neutral"],
    "season": "fall"
}

ranked = sorted(
    outfits,
    key=lambda o: score_outfit(o, user_preferences, memory)[0],
    reverse=True
)

best = ranked[0]
score, reasons = score_outfit(best, user_preferences, memory)

print("\nRecommended Outfit:")
print(f"Top: {best['top']}")
print(f"Bottom: {best['bottom']}")
print(f"Shoes: {best['shoes']}")

print("\nWhy this outfit:")
for r in reasons:
    print("-", r)

feedback = input("\nDid you like this outfit? (yes/no): ").strip().lower()
if feedback in ["yes", "no"]:
    update_memory(best, feedback)

print("Memory updated.")
