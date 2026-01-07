import json
import matplotlib.pyplot as plt

MEMORY_FILE = "memory/user_memory.json"
OUTPUT_FILE = "preferences.png"

with open(MEMORY_FILE, "r") as f:
    memory = json.load(f)

tags = list(memory["preferred_tags"].keys())
scores = [memory["preferred_tags"][t]["score"] for t in tags]

print("Tags:", tags)
print("Scores:", scores)

plt.figure(figsize=(8, 4))
plt.bar(tags, scores)
plt.xlabel("Style Tags")
plt.ylabel("Preference Score")
plt.title("Learned Style Preferences")

plt.tight_layout()
plt.savefig(OUTPUT_FILE)

print(f"Saved plot to {OUTPUT_FILE}")
