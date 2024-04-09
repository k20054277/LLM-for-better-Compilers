
# Demonstrate the use of and and iteration

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use and to check if all numbers are greater than 2
are_greater_than_2 = and(number > 2 for number in numbers)

# Iterate over the list of numbers and print each one
for number in numbers:
    print(number)

# Print the result of the and operation
print(are_greater_than_2)
