# Example 8: Standardise data using z-scores

import math

numbers = [10, 20, 30, 40, 50]

mean = sum(numbers) / len(numbers)

variance = sum(
    (x - mean) ** 2 for x in numbers
) / len(numbers)

std_dev = math.sqrt(variance)

if std_dev == 0:
    standardised = [0.0] * len(numbers)
else:
    standardised = [
        (x - mean) / std_dev
        for x in numbers
    ]

print("Original data:", numbers)
print("Standardised data:", standardised)


