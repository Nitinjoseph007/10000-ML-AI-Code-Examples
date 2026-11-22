# Example 4: Calculate population variance

numbers = [10, 20, 30, 40, 50]

mean = sum(numbers) / len(numbers)

variance = sum(
    (x - mean) ** 2 for x in numbers
) / len(numbers)

print("Dataset:", numbers)
print("Mean:", mean)
print("Variance:", variance)









