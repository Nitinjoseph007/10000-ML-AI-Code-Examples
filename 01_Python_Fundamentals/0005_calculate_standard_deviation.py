# Example 5: Calculate population standard deviation

import math

numbers = [10, 20, 30, 40, 50]

mean = sum(numbers) / len(numbers)

variance = sum(
    (x - mean) ** 2 for x in numbers
) / len(numbers)

standard_deviation = math.sqrt(variance)

print("Dataset:", numbers)
print("Standard deviation:", standard_deviation)
