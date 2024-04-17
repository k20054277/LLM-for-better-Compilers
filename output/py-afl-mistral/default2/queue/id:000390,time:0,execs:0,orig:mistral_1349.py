
# List of numbers
numbers = [1, 2, 3, 4, 5]

# Function to check if each number is greater than zero
def is_positive(number):
    assert number > 0, f"Number {number} should be positive."
    return number

# Using map to apply the function to all elements in the list
positive_numbers = list(map(is_positive, numbers))

print("Original Numbers: ", numbers)
print("Positive Numbers: ", positive_numbers)
