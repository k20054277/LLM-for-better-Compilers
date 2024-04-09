
# Demonstrating use of and and enumerate

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use and to check if each number is greater than 2
for num in numbers:
    if num > 2:
        print(num)

# Use enumerate to get the index and value of each item in the list
for index, num in enumerate(numbers):
    print(index, num)
