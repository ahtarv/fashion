import streamlit as st
import json
import random

from core.scoring import score_outfit, compute_confidence
from memory.memory_store import load_memory, update_memory, save_memory

# ----------------------------
# Config
# ----------------------------
EXPLORATION_RATE = 0.2

st.set_page_config(page_title="AI Personal Stylist", layout="centered")

# ----------------------------
# Load data
# ----------------------------
with open("data/sample_outfits.json") as f:
    outfits = json.load(f)

memory = load_memory()

user_preferences = {
    "styles": ["minimal", "neutral"],
    "season": "fall"
}

# ----------------------------
# Session state
# ----------------------------
if "current_outfit" not in st.session_state:
    st.session_state.current_outfit = None
    st.session_state.exploring = False
    st.session_state.score = 0
    st.session_state.reasons = []
    st.session_state.confidence = 0

# ----------------------------
# Recommendation logic
# ----------------------------
def recommend():
    exploring = random.random() < EXPLORATION_RATE

    if exploring:
        outfit = random.choice(outfits)
    else:
        ranked = sorted(
            outfits,
            key=lambda o: score_outfit(o, user_preferences, memory)[0],
            reverse=True
        )
        outfit = ranked[0]

    score, reasons = score_outfit(outfit, user_preferences, memory)
    confidence = compute_confidence(score, reasons, exploring)

    # repetition tracking
    memory.setdefault("recent_outfits", [])
    memory["recent_outfits"].append(outfit["id"])
    memory["recent_outfits"] = memory["recent_outfits"][-5:]
    save_memory(memory)

    st.session_state.current_outfit = outfit
    st.session_state.exploring = exploring
    st.session_state.score = score
    st.session_state.reasons = reasons
    st.session_state.confidence = confidence

# ----------------------------
# UI
# ----------------------------
st.title("🧠 AI Personal Stylist")

if st.button("👕 Recommend Outfit"):
    recommend()

outfit = st.session_state.current_outfit

if outfit:
    if st.session_state.exploring:
        st.info("Exploring a new style")

    st.subheader("Recommended Outfit")
    st.write(f"**Top:** {outfit['top']}")
    st.write(f"**Bottom:** {outfit['bottom']}")
    st.write(f"**Shoes:** {outfit['shoes']}")

    st.subheader("Why this outfit")
    for r in st.session_state.reasons:
        st.write(f"- {r}")

    st.subheader(f"Confidence: {int(st.session_state.confidence * 100)}%")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("👍 Like"):
            update_memory(outfit, "like")
            st.success("Feedback saved")

    with col2:
        if st.button("👎 Dislike"):
            update_memory(outfit, "dislike")
            st.warning("Feedback saved")

# ----------------------------
# Sidebar: Memory inspection
# ----------------------------
st.sidebar.title("🧠 Learned Preferences")

memory = load_memory()
for tag, data in memory.get("preferred_tags", {}).items():
    st.sidebar.write(f"{tag}: {data['score']}")
