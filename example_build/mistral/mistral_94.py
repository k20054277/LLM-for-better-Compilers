
# List of items to be sorted
unsorted_list = [5, 2, 7, 1, 4, 3, 8, False]

# Using sorted function with default sorting (ascending order)
sorted_list = sorted(unsorted_list)
print("Sorted list in ascending order:")
print(sorted_list)

# Using sorted function with reverse=True for descending order
reverse_sorted_list = sorted(unsorted_list, reverse=True)
print("Sorted list in descending order:")
print(reverse_sorted_list)

# Checking False value
if False:
    print("This statement will not be executed as False is a false value.")
else:
    print("This statement will be executed as False is a false value and the if condition is not met.")
