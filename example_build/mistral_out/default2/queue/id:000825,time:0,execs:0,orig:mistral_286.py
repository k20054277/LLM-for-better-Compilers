
# Define a list with some elements and assign None to one of its elements
numbers = [1, 2, None, 4, 5, 6]

print("Original List: ", numbers)

# Using all() function to check if all elements in the list are not equal to None
if all(numbers):
    print("All elements in the list are not None.")
else:
    print("One or more elements in the list are None.")

# Now let's test a list where some elements are None
boolean_list = [True, False, None, True, None]

print("\nBoolean List: ", boolean_list)

if all(boolean_list):
    print("All elements in the list are True.")
else:
    print("One or more elements in the list are False or None.")

# In this case, since we have some None values in the list, the if condition will evaluate to False
