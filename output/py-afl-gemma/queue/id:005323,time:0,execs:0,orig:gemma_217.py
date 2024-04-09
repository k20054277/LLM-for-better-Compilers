
# This Python program demonstrates the use of and and min

# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use and to check if all numbers are greater than 5
and_greater_than_5 = all(number > 5 for number in numbers)

# Use min to find the minimum value in the list
minimum_value = min(numbers)

# Print the results
print("The numbers are greater than 5:", and_greater_than_5)
print("The minimum value in the list is:", minimum_value)
