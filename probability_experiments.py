import random
import matplotlib.pyplot as plt
from collections import Counter


def simulate_coin_tosses(n=100):
    results = [random.choice(["Heads", "Tails"]) for _ in range(n)]
    counts = Counter(results)

    plt.bar(counts.keys(), counts.values())
    plt.title(f"{n} Coin Tosses")
    plt.xlabel("Outcome")
    plt.ylabel("Count")
    plt.show()
    return counts


def simulate_die_rolls(n=60):
    results = [random.randint(1, 6) for _ in range(n)]
    counts = Counter(results)

    plt.bar(range(1, 7), [counts.get(i, 0) for i in range(1, 7)])
    plt.title(f"{n} Die Rolls")
    plt.xlabel("Die Face")
    plt.ylabel("Frequency")
    plt.show()
    return counts


def simulate_card_draws(n=20):
    deck = ["Red"] * 26 + ["Black"] * 26
    results = [random.choice(deck) for _ in range(n)]
    counts = Counter(results)

    plt.bar(counts.keys(), counts.values(), color=["red", "black"])
    plt.title(f"{n} Card Draws")
    plt.xlabel("Card Color")
    plt.ylabel("Count")
    plt.show()
    return counts


def simulate_compound_coin_flips(n=50):
    both_heads = 0
    at_least_one_head = 0

    for _ in range(n):
        flip1 = random.choice(["Heads", "Tails"])
        flip2 = random.choice(["Heads", "Tails"])
        if flip1 == "Heads" and flip2 == "Heads":
            both_heads += 1
        if flip1 == "Heads" or flip2 == "Heads":
            at_least_one_head += 1

    labels = ["Both Heads", "At Least One Head"]
    values = [both_heads, at_least_one_head]

    plt.bar(labels, values, color=["blue", "green"])
    plt.title(f"{n} Double Coin Flips")
    plt.ylabel("Occurrences")
    plt.show()

    return {"both_heads": both_heads, "at_least_one_head": at_least_one_head}


def main():
    print("📊 Probability Experiments Simulator")

    simulate_coin_tosses()
    simulate_die_rolls()
    simulate_card_draws()
    simulate_compound_coin_flips()


if __name__ == "__main__":
    main()
