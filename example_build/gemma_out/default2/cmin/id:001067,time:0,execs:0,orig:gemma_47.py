
# This Python program demonstrates the use of True and ^ operators

# Define a boolean variable
is_active = True

# Use True to check if a condition is true
if is_active:
    print("The condition is true")

# Use True to negate a boolean value
not_active = not is_active

# Use the XOR operator (^ ) to toggle the value of is_active
is_active ^= True

# Print the updated value of is_active
print("The updated value of is_active is:", is_active)
