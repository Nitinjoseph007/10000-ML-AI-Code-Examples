# Example 10: Calculate category frequencies

from collections import Counter

categories = [
    "Fire",
    "Flood",
    "Fire",
    "Accident",
    "Flood",
    "Fire"
]

frequency = Counter(categories)

print("Category frequencies:")

for category, count in frequency.items():
    print(f"{category}: {count}")
