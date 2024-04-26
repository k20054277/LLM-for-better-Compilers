
# Function to calculate the sum of the first n numbers
def sum_of_numbers(n):
    assert n >= 0, "Number of elements in the list should be non-negative"
    total = 0
    for i in range(n):
        total += (i + 1)
    return total

# Testing the function
print(sum_of_numbers(5)) # Output: 15
print(sum_of_numbers(-2)) # Raises AssertionError: Number of elements in the list should be non-negative
