
# Define some variables with false values
condition1 = False
condition2 = 0
condition3 = None

# Use of the 'or' operator with multiple conditions
result = condition1 or condition2 or condition3

print("Result: ", result)

# Now let's check each condition individually
print("Condition 1 is false: ", condition1)
print("Condition 2 is false (when considered as a boolean): ", bool(condition2))
print("Condition 3 is None: ", condition3 is None)

# Using 'or' with conditions having at least one true value
condition4 = "some string"
result = condition1 or condition4
print("Result with at least one true condition: ", result)
