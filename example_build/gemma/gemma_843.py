
# This Python program demonstrates the use of and and in operators

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Check if 3 is in the list
if 3 in numbers:
    print("3 is in the list")

# Check if all numbers in the list are greater than 2
for num in numbers:
    if num > 2:
        print(num + " is greater than 2")

# Print the elements of the list that are divisible by 2
for num in numbers:
    if num % 2 == 0:
        print(num + " is divisible by 2")
