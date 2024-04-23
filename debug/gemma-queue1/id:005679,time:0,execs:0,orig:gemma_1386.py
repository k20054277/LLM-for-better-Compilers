
def square(x):
    return x**2

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use map to square each number in the list
squared_numbers = map(square, numbers)

# Assert that the squared numbers are correct
assert squared_numbers == [1, 4, 9, 16, 25]

# Print the squared numbers
print(squared_numbers)
