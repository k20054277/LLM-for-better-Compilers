
# This Python program demonstrates the use of True and | operators

# Define a boolean variable
is_active = True

# Use True in an if statement
if is_active:
    print("The user is active.")

# Use True as a condition in a loop
for i in range(10) if is_active else range(5):
    print(i)

# Use True to short-circuit an OR operation
if is_active or False:
    print("The user is active.")

# Use True as a boolean literal
print(True is True)  # Output: True

# Use True to compare with another boolean variable
print(True == is_active)  # Output: True
