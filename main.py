import json
from core.scoring import score_outfit, compute_confidence
from memory.memory_store import load_memory, update_memory
import random

with open("data/sample_outfits.json") as f:
    outfits = json.load(f)

memory = load_memory()

budget = float(input("Enter your budget: "))
print(type(outfits[0]["price"]), outfits[0]["price"])


user_preferences = {
    "styles": ["minimal", "neutral"],
    "season": "fall",
    "budget": budget
}

ranked = sorted(
    outfits,
    key=lambda o: score_outfit(o, user_preferences, memory)[0],
    reverse=True
)

best = ranked[0]
score, reasons = score_outfit(best, user_preferences, memory)

affordable_outfits = [
    o for o in outfits if o["price"] <= user_preferences["budget"]
]

if not affordable_outfits:
    print("No outfits available under your budget")
    exit()


exploration_rate = 0.2
exploring = random.random() < exploration_rate

if exploring:
    print("Exploring a new option....")
    best = random.choice(affordable_outfits)
else:
    ranked = sorted(
        affordable_outfits,
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
print(f"Price: ${best['price']}")

print("\nWhy this outfit:")
for r in reasons:
    print("-", r)

print(f"\nConfidence: {confidence * 100:.0f}%")

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


