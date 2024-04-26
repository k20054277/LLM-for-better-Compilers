# Define a variable with a value of None
x = None

# Print the value of x
print(x)

# If x is None, print "x is None"
if x is None:
    print("x is None")

# If x is not None, print "x is not None"
else:
    print("x is not None")

# Use or to combine two conditions
if x is None or x == 0:
    print("x is either None or equal to 0")