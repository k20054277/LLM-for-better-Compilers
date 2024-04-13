
# This Python program demonstrates the use of and and reversed

# Define a function to reverse a list
def reverse_list(lst):
    return lst[::-1]

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Reverse the list
reversed_numbers = reverse_list(numbers)

# Print the original list and the reversed list
print("Original list:", numbers)
print("Reversed list:", reversed_numbers)

# Check if the lists are equal
if numbers == reversed_numbers:
    print("The lists are equal")
else:
    print("The lists are not equal")
