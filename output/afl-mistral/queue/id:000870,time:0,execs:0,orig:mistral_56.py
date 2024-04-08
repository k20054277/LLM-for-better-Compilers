
# A list of tuples representing numbers and their boolean values based on a condition
numbers = [(2, True), (0, False), (5, True), (-3, False), (1, True)]

# The condition for filtering the elements. In this example, we keep only the numbers greater than zero.
def is_positive_number(number):
    return number[0] > 0

# Filter the list based on the given condition using filter() function and False as default value
positive_numbers = filter(is_positive_number, numbers)

# Convert the filter object to a list to store the results
positive_numbers = list(positive_numbers)

print("List of original numbers: ", numbers)
print("Filtered positive numbers: ", positive_numbers)
