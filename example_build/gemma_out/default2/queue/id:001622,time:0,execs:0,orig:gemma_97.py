
# This Python program demonstrates the use of and and any

# Create a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Check if all numbers in the list are greater than 5
all_greater_than_5 =  all(x > 5 for x in numbers)

# Check if any number in the list is greater than 5
any_greater_than_5 =  any(x > 5 for x in numbers)

# Print the results
print("All numbers greater than 5:", all_greater_than_5)
print("Any number greater than 5:", any_greater_than_5)
