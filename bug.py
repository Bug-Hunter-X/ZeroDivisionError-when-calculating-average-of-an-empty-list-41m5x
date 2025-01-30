def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# Example usage (will cause ZeroDivisionError):
my_numbers = []
average = calculate_average(my_numbers)
print(f"The average is: {average}")

# Example usage (will work correctly):
my_numbers = [10, 20, 30]
average = calculate_average(my_numbers)
print(f"The average is: {average}")