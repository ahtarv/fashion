# 🧠 AI Personal Stylist with Memory, Learning & Exploration

A personalized fashion recommendation system that **learns user preferences over time**, balances **exploration vs exploitation**, avoids repetition, explains its decisions, and reports **confidence levels**.

This project models the **core mechanics of modern recommender systems** (Netflix / Spotify–style logic) applied to fashion, using transparent, interpretable logic rather than black-box models.

---

## 🚀 Features

### ✅ Preference Learning
- Learns from explicit user feedback (`yes` / `no`)
- Updates internal memory after every interaction

### 🧠 Long-Term Memory with Decay
- Preferences weaken over time unless reinforced
- Mimics real human taste evolution

### 🎯 Exploration vs Exploitation (ε-greedy)
- Mostly recommends the best-known option
- Occasionally explores new outfits to avoid stagnation
- **Budget-Aware**: Exploration strictly respects user budget constraints

### 🔁 Repetition / Fatigue Control
- Penalizes recently shown outfits
- Prevents “same outfit every time” failure mode

### 🪞 Explainability
- Every recommendation includes human-readable reasons

### 🎨 Smart Color Analysis
- Automatically detects color palettes (Neutral, Warm, Cool)
- Rewards cohesive color schemes in ranking
- Uses set-based logic to categorize outfit tones

### 📊 Confidence Scoring
- Outputs how confident the system is in each recommendation
- Confidence drops during exploration or weak evidence

### 📈 Offline Visualization
- Saves learned preferences as charts (`preferences.png`)
- No GUI dependency required

---

## 🧩 System Architecture

```

User Feedback (yes / no)
↓
Persistent Memory (JSON)
↓
Scoring Engine
↓
Exploration & Diversity Logic
↓
Recommendation + Explanation + Confidence

```

---

## 🗂 Project Structure

```

fashion/
├── core/
│   └── scoring.py          # scoring + confidence logic
├── memory/
│   └── memory_store.py     # persistent user memory
├── data/
│   └── sample_outfits.json # outfit dataset (18 outfits)
├── main.py                 # main recommendation loop
├── visualize.py            # offline preference visualization
└── README.md

```

---

## 🧠 Memory Format

```json
{
  "preferred_tags": {
    "minimal": {
      "score": 3,
      "last_updated": 1767770150
    }
  },
  "recent_outfits": ["o1", "o9", "o5"]
}
```

### Fields

* `score` → preference strength
* `last_updated` → enables time-based decay
* `recent_outfits` → repetition control

---

## ⚖️ Scoring Logic (Conceptual)

Each outfit is scored using:

* Match with declared preferences
* Learned tag preferences
* **Color Palette Harmony** (Neutral, Warm, Cool analysis)
* Time-decayed memory
* Penalty for recently shown outfits
* Exploration penalty (if applicable)

The system then selects either:

* the highest-scoring outfit (**exploit**), or
* a random outfit (**explore**)

---

## 🎯 Confidence Estimation

Confidence reflects:

* strength of learned signals
* consistency of preferences
* whether exploration was used

Example:

```
Confidence: 40%
```

Lower confidence indicates uncertainty or exploration.

---

## 📊 Visualization

Generate a preference chart:

```bash
python visualize.py
```

Output:

```
preferences.png
```

This image shows how strongly each style tag is preferred over time.

---

## ▶️ How to Run

### Install dependencies

```bash
pip install matplotlib
```

### Run the system

```bash
python main.py
```

### Feedback

* `yes` → reinforces preferences
* `no` → weakens preferences

Run multiple times to observe learning behavior.

---

## 🔍 Example Output

```
Recommended Outfit:
Top: black turtleneck
Bottom: slim trousers
Shoes: chelsea boots

Why this outfit:
- matches your preferred style (minimal)
- you liked minimal before
- shown recently less often

Confidence: 40%
```

---

## 💡 Why This Project Matters

This is **not a rule-based demo**.

It demonstrates:

* stateful AI systems
* reinforcement-style learning loops
* recommender system design
* explainability & uncertainty
* real-world tradeoffs (exploration, fatigue, decay)

These patterns directly apply to:

* recommendation engines
* personalization systems
* LLM memory architectures
* applied ML infrastructure

---

## 🛣 Future Improvements

* Streamlit web dashboard
* Multi-user support
* Embedding-based similarity (semantic tags)
* Adaptive exploration rate
* Confidence-over-time visualization
* Integration with real product catalogs

---

## 👤 Author

Built by **Atharv Kamlesh Patil**
Focused on applied AI systems, personalization, and ML engineering.
