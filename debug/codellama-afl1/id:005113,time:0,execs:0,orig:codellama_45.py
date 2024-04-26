# Using True and {} in Python

# Creating a list of numbers using the range() function
numbers = list(range(1, 6))

# Creating a dictionary with the numbers as keys and their square roots as values
squares = {number: number ** 0.5 for number in numbers}

print(squares)