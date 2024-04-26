
# This Python program demonstrates the use of True and ^ operators

# Define a boolean variable
is_active = True

# Use True to check if a condition is true
if is_active:
    print("The condition is true")

# Use True to negate a boolean variable
not_active = not is_active

# Use the XOR operator (^), which returns True if the two operands are different
print(True ^ False)

# Use the XOR operator to toggle the value of a boolean variable
is_active ^= True

# Print the updated value of is_active
print(is_active)
