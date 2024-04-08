
# This function takes an iterable (like a list or tuple) as an argument,
# and returns the sum of all elements in that iterable.
def sum_of_numbers(numbers):
    return sum(numbers)

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Use False as an argument to check if the list is empty
sum_of_positives = sum_of_numbers(numbers) if numbers else 0

print("Sum of all numbers: ", sum_of_positives)
