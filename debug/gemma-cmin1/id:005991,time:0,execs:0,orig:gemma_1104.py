
# Demonstrate the use of as and any

# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use as to assign a variable to an element in the list
a = numbers[0]

# Use any to check if any element in the list is greater than 5
print(any(x > 5 for x in numbers))

# Use as and any to check if the first element in the list is greater than 5
print(any(x > 5 for x in numbers) and numbers[0] > 5)
