# Define a variable called "my_variable" with the value True
my_variable = True

# Use the global keyword to access the global namespace
print(globals().get('my_variable'))  # Output: True

# Assign False to the variable in the global namespace
globals()['my_variable'] = False

# Print the value of the variable in the global namespace
print(globals().get('my_variable'))  # Output: False