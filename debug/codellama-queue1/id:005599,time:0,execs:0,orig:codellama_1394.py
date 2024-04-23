# Define a function that takes a list as input and returns the sum of all elements in the list
def sum_list(my_list):
    # Use assert to check that the input is a list
    assert type(my_list) == list, "Input must be a list"

    # Initialize the sum variable
    total = 0

    # Iterate over the elements in the list and add them to the sum
    for element in my_list:
        total += element

    return total

# Test the function with different inputs
print(sum_list([1, 2, 3]))       # Should output 6
print(sum_list([1, 2, 3, 4]))   # Should output 10
print(sum_list([1, 2, 3, 4, 5])) # Should output