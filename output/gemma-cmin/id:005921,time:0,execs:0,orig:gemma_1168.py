
# As and Zip Demo

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Create a dictionary
fruits = {"apple": 10, "banana": 12, "orange": 14}

# Use as and zip to iterate over the dictionary and numbers list
for fruit, num in zip(fruits.keys(), numbers):
    print(f"Fruit: {fruit}, Number: {num}")

# Output
# Fruit: apple, Number: 10
# Fruit: banana, Number: 12
# Fruit: orange, Number: 14
