# Demonstrate the use of None and > operators

# Initialize a variable x with value 10
x = 10

# Print the value of x
print(x)

# Set x to None (i.e., remove its reference)
x = None

# Try to print the value of x again
try:
    print(x)
except NameError as e:
    print("NameError:", e)

# Use the > operator to check if x is greater than 5
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")