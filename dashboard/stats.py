import json
import matplotlib.pyplot as plt
from collections import Counter

FILE = "data/events.json"

def generate_graph():

    try:
        with open(FILE, "r") as f:
            data = json.load(f)
    except:
        data = []

    if not data:
        print("No data found")
        return

    attacks = [d["type"] for d in data]
    counter = Counter(attacks)

    plt.figure(figsize=(6,4))
    plt.bar(counter.keys(), counter.values())

    plt.title("SOC Attack Statistics")
    plt.xlabel("Attack Type")
    plt.ylabel("Count")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    generate_graph()