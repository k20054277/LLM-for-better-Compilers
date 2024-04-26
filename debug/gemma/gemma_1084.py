
# Demonstrating the use of as and for

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Iterate over the list and print each number squared
for number in numbers:
    print(number ** 2)

# Use as to bind the number variable to each item in the list
for number in numbers:
    as square := number ** 2
    print(square)
