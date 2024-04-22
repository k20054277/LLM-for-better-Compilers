
# Define a tuple
numbers = (1, 2, 3, 4, 5)

# Use 'and' to check if multiple conditions are true
# In this case, we'll check if an number is in the tuple and if it's even
def is_even_in_tuple(number, given_numbers):
    return number in given_numbers and number % 2 == 0

# Test some numbers
print(is_even_in_tuple(2, numbers))  # True
print(is_even_in_tuple(1, numbers))  # False
print(is_even_in_tuple(3, numbers))  # False
print(is_even_in_tuple(4, numbers))  # True
