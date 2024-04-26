
# This Python program demonstrates the use of assert and reversed

# Define a function to reverse a list
def reverse_list(lst):
    return lst[::-1]

# Create a list of numbers
lst = [1, 2, 3, 4, 5]

# Assert that the reverse of the list is the original list in reverse order
assert reverse_list(lst) == lst.reverse()

# Print the reversed list
print(reverse_list(lst))

# Output:
# [5, 4, 3, 2, 1]
