# Example 9: Detect outliers using the IQR method

numbers = [10, 12, 13, 14, 15, 16, 18, 100]

sorted_numbers = sorted(numbers)


def calculate_median(values):
    n = len(values)
    middle = n // 2

    if n % 2 == 1:
        return values[middle]

    return (
        values[middle - 1] + values[middle]
    ) / 2


middle = len(sorted_numbers) // 2

q1 = calculate_median(sorted_numbers[:middle])
q3 = calculate_median(sorted_numbers[middle:])

iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = [
    x for x in numbers
    if x < lower_bound or x > upper_bound
]

print("Dataset:", numbers)
print("Lower bound:", lower_bound)
print("Upper bound:", upper_bound)
print("Outliers:", outliers)
