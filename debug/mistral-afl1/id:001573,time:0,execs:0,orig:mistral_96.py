
# Define a boolean variable 'is_rainning' with an initial value of False
is_raining = False

# Print the value of is_raining in its boolean form
print("Is it raining? ", is_raining)

# Now let's change the value of 'is_raining' and see the impact
is_raining = True

# Print the value of 'is_raining' again, this time with a string representation using str() function
print("Is it raining? ", str(is_raining))

# Another example: an empty list is considered as False in boolean context
my_list = []
print("Is my_list empty? ", str(bool(my_list)))

# Adding an element to the list changes its truth value and string representation
my_list.append(1)
print("Is my_list empty now? ", str(bool(my_list)))
