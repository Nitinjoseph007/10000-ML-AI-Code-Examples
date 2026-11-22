# Example 2: Calculate the median of a dataset

def calculate_median(numbers):
    if not numbers:
        raise ValueError("The dataset cannot be empty.")

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    middle = n // 2

    if n % 2 == 1:
        return sorted_numbers[middle]

    return (
        sorted_numbers[middle - 1] + sorted_numbers[middle]
    ) / 2


# Example dataset
numbers = [10, 20, 30, 40, 50, 60]

median = calculate_median(numbers)

print("Dataset:", numbers)
print("Median:", median)
