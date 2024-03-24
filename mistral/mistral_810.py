
# Define some variables
x = 5
y = 10
z = x

# Use the 'and' operator
if x > 0 and y < 20:
    print("x is positive and y is less than 20")

# Use the 'is' operator to compare objects (not values!) for identity
if z is x:
    print("x and z refer to the same object")
else:
    print("x and z do not refer to the same object")
