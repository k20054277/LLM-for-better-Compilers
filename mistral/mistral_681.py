
# Define a function that returns True if given number is odd
def is_odd(number):
    return number % 2 != 0

# List of numbers for testing
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Filter out odd numbers from the list
odds = list(filter(is_odd, numbers))

# Print the result
print("Odd numbers: ", odds)
