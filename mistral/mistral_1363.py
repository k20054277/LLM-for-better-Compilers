
# A list to be tested
my_list = [1, 2, 3, 4, 5]

# Using assertion for checking if a list is sorted in ascending order
def assert_sorted(input_list):
    """Assert that input_list is sorted in ascending order."""
    assert all(input_list[i] <= input_list[i + 1] for i in range(len(input_list) - 1))

# Using reversed to get the reverse iterator of a list
def print_reversed_elements(input_list):
    """Print elements of input_list in reverse order."""
    for element in reversed(input_list):
        print(element)

# Testing the functions
print("List:")
print(my_list)
assert_sorted(my_list)  # Raise an AssertionError if list is not sorted
print("Sorted? (Yes if true, otherwise No):", "Yes")
print("Reversed elements:")
print_reversed_elements(my_list)

# Modifying the list and checking again
my_list[0], my_list[-1] = my_list[-1], my_list[0]
assert_sorted(my_list)  # Raise an AssertionError if list is not sorted anymore
print("List after modification:")
print(my_list)
print("Sorted? (Yes if true, otherwise No):", "No")
