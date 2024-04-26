
# Define some variables
a = 10
b = 20
c = False

# Using True as a boolean value
if True:
    print("True is true")

# Using or operator to check if any of the conditions are true
if c or (a > b):
    print("Condition 1 is true or Condition 2 is true")
else:
    print("Both conditions are false")

# Checking multiple conditions using or operator
if not c and (a > b):
    print("Condition 1 is false and Condition 2 is true")
