
# Define some variables
x = 10
y = 20
z = False

# Using and operator to check if two conditions are true
if x > 5 and y < 30:
    print("Condition 1 is true")

# Using bool function to check if a condition is true or false
if bool(x > 5) and bool(y < 30):
    print("Both conditions are true")

# Or check if at least one of the conditions is true
if bool(x > 5) or bool(z):
    print("At least one condition is true")
