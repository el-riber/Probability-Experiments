
# 🎲 Simulate Probability Experiments

This Python program simulates four probability experiments and visualizes the results using bar charts. It helps users understand basic probability concepts through interactive simulations.

---

## ✅ Features

- **Task 1:** Simulate 100 coin tosses → count and plot heads vs. tails.
- **Task 2:** Simulate 60 die rolls → show frequency of each face (1–6).
- **Task 3:** Draw 20 cards from a shuffled deck → count red vs. black cards.
- **Task 4:** Flip 2 coins 50 times → count occurrences of both heads and at least one head.

All simulations include graphical output using `matplotlib`.

---

## 🧪 Test Cases

### ✅ Normal Cases

1. Toss 100 coins → expect ~50 heads and ~50 tails.
2. Roll a die 60 times → expect roughly equal distribution.
3. Draw 20 cards → about 10 red and 10 black.
4. Flip two coins 50 times → ~12-15 both heads, ~38-45 at least one head.

### ⚠️ Edge Cases

1. Toss 0 coins → empty results.
2. Roll 1 die → minimal output.
3. Draw 60 cards from a 52-card deck → should still work due to replacement logic.

---

## 🚀 How to Run

### Requirements

- Python 3.7+
- `matplotlib` installed

```bash
pip install matplotlib
````

### Run the Application

```bash
python probability_experiments.py
```

Each task runs sequentially and displays a plot for each experiment.

---

## 📹 Demonstration Video

🎥 [Watch the video demonstration](https://www.youtube.com/your-demo-link)

Includes:

* Code walkthrough
* All 4 experiment runs
* 3 normal and 3 edge case demonstrations

---

## 📄 License

This project was created as part of the Application Development BAS program at North Seattle College.

