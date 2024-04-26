
# Define some variables
x = 10
y = "ten"
z = 10

# Using 'and' operator
if x > 5 and x < 20:
    print("x is between 5 and 20")

# Using 'is' operator for comparing two variables for identity
if x is z:
    print("x and z are identical") # This will be printed

# Using 'is' operator for comparing two expressions
if (x > 5) is (y < 20):
    print("x is greater than 5 and y is less than 20") # This will not be printed as the conditions are different types
