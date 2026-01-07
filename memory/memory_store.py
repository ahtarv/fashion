import json
import os
import time

MEMORY_FILE = "memory/user_memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {
            "preferred_tags": {},
            "recent_outfits": []
        }
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

    if "preferred_tags" not in memory:
        memory["preferred_tags"] = {}
    
    if "recent_outfits" not in memory:
        memory["recent_outfits"] = []

    return memory

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def update_memory(outfit, feedback):
    memory = load_memory()
    now = int(time.time())

    for tag in outfit["tags"]:
        entry = memory["preferred_tags"].get(tag, {
            "score": 0,
            "last_updated": now
        })

        if feedback == "like":
            entry["score"] += 1
        elif feedback == "dislike":
            entry["score"] -= 1

        entry["last_updated"] = now
        memory["preferred_tags"][tag] = entry

    save_memory(memory)
