
# This Python program demonstrates the use of and and reversed

# Define a function to reverse a list
def reverse_list(lst):
    return lst[::-1]

# Create a list of numbers
lst = [1, 2, 3, 4, 5]

# Reverse the list
reversed_lst = reverse_list(lst)

# Print the original list
print(lst)

# Print the reversed list
print(reversed_lst)

# Check if the lists are equal
print(lst == reversed_lst)
