
# Define a set of numbers
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Print the elements of the set
print(numbers)

# Use the as keyword to assign a variable to the set
as fruits = numbers

# Print the elements of the variable
print(fruits)

# Check if a number is in the set
if 5 in fruits:
    print("5 is in the set")

# Iterate over the set
for fruit in fruits:
    print(fruit)

# Print the cardinality of the set
print("The cardinality of the set is:", len(fruits))
