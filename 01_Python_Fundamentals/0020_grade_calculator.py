score = float(input("Enter your score (0–100): "))

if not 0 <= score <= 100:
    print("Score must be between 0 and 100.")
elif score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")