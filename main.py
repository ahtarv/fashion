import json
from core.scoring import score_outfit, compute_confidence
from memory.memory_store import load_memory, update_memory
import random

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

exploration_rate = 0.2
exploring = random.random() < exploration_rate

if exploring:
    print("Exploring a new option....")
    best = random.choice(outfits)
else:
    ranked = sorted(
        outfits,
        key = lambda o: score_outfit(o, user_preferences, memory)[0],
        reverse=True
    )
    best = ranked[0]
    score, reasons = score_outfit(best, user_preferences, memory)

confidence = compute_confidence(score, reasons, exploring)

print("\nRecommended Outfit:")
print(f"Top: {best['top']}")
print(f"Bottom: {best['bottom']}")
print(f"Shoes: {best['shoes']}")

memory["recent_outfits"].append(best["id"])
memory["recent_outfits"] = memory["recent_outfits"][-5:]

from memory.memory_store import save_memory
save_memory(memory)

print("\nWhy this outfit:")
for r in reasons:
    print("-", r)

print(f"\nConfidence: {confidence * 100:.0f}%")

feedback = input("\nDid you like this outfit? (yes/no): ").strip().lower()
if feedback in ["yes", "no"]:
    update_memory(best, feedback)

print("Memory updated.")


