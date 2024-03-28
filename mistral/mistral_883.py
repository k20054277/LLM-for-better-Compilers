
# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use logical 'and' operation to check if a number is even and greater than 3
evens_greater_than_three = list(filter(lambda x: x % 2 == 0 and x > 3, numbers))
print("Even numbers greater than 3: ", evens_greater_than_three)

# Use mathematical 'sum' function to find the sum of all elements in a list
total = sum(numbers)
print("Sum of all numbers: ", total)
