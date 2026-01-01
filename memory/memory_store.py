import json
import os

MEMORY_FILE = "memory/user_memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {
            "preferred_tags": {},
            "disliked_tags": {}
        }
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def update_memory(outfit, feedback):
    memory = load_memory()

    for tag in outfit["tags"]:
        if feedback == "like":
            memory["preferred_tags"][tag] = memory["preferred_tags"].get(tag, 0) + 1
        elif feedback == "dislike":
            memory["disliked_tags"][tag] = memory["disliked_tags"].get(tag, 0) + 1

    save_memory(memory)
