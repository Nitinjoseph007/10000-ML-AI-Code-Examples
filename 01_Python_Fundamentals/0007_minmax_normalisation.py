# Example 7: Min-max normalisation

numbers = [10, 20, 30, 40, 50]

minimum = min(numbers)
maximum = max(numbers)

if maximum == minimum:
    normalised = [0.0] * len(numbers)
else:
    normalised = [
        (x - minimum) / (maximum - minimum)
        for x in numbers
    ]

print("Original data:", numbers)
print("Normalised data:", normalised)
