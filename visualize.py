import matplotlib.pyplot 
matplotlib.use("TkAgg")

import json
import matplotlib.pyplot as plt

MEMORY_FILE = "memory/user_memory.json"

with open(MEMORY_FILE, "r") as f:
    memory = json.load(f)

tags = list(memory["preferred_tags"].keys())
scores = [memory["preferred_tags"][t]["score"] for t in tags]

plt.figure()
plt.bar(tags, scores)
plt.xlabel("Style Tags")
plt.ylabel("Preference Score")
plt.title("Learned Style Preferences")

plt.savefig("preferences.png")
plt.show()
input("Press Enter to close....")