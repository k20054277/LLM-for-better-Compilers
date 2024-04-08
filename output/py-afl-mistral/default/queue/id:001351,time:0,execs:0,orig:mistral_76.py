
# Define some values
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
false_value = False

# Use max with a list of numbers and a sentinel value less than any number in the list
largest_number = max(numbers)
print("The largest number from the given list is:", largest_number)

# Use max with two numbers and `False` as a sentinel value, which will return the first number as it's false for all comparison purposes
comparison = max(10, False)
print("The maximum of 10 and False is:", comparison)

# Comparing False to numbers and using max to find the largest number among given numbers
largest_among_false_and_numbers = max([False, *numbers])
print("The largest number among False and given numbers is:", largest_among_false_and_numbers)
