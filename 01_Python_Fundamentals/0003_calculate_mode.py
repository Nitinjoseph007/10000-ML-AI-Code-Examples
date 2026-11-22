# Example 3: Calculate the mode of a dataset

from collections import Counter


def calculate_mode(numbers):
    if not numbers:
        raise ValueError("The dataset cannot be empty.")

    frequencies = Counter(numbers)

    highest_frequency = max(frequencies.values())

    modes = [
        number
        for number, frequency in frequencies.items()
        if frequency == highest_frequency
    ]

    return modes


# Example dataset
numbers = [10, 20, 20, 30, 40, 20, 50]

mode = calculate_mode(numbers)

print("Dataset:", numbers)
print("Mode:", mode)
