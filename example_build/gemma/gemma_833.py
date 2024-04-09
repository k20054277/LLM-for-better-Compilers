
# Demonstrate the use of and and del

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use and to check if all numbers are greater than 2
if all(number > 2 for number in numbers):
    print("All numbers are greater than 2")

# Delete elements from the list using del
del numbers[2]

# Print the updated list
print(numbers)
