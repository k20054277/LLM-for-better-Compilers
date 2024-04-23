
# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Set a variable to a number not in the list
search_number = 6

# Check if search_number is in the numbers list using the 'in' keyword
if search_number in numbers:
    print("{} is present in the list".format(search_number))
else:
    print("{} is not present in the list".format(search_number))

# Demonstrate False value
if not (search_number in numbers):
    print("{} is not present in the list (using 'not' and 'in')".format(search_number))
