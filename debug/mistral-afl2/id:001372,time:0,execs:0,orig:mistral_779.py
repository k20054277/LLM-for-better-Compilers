
# Define some variables
variable1 = True
variable2 = False

# Use or (logical OR) to check if variable1 is True or variable2 is True
result = variable1 or variable2

print("Variable 1 is:", variable1)
print("Variable 2 is:", variable2)
print("Result of or operation: ", result)

# Let's see the behavior when both variables are False
variable1 = False
variable2 = False
result = variable1 or variable2
print("Result of or operation with both variables as False: ", result)

# And let's see when one variable is True and another is False
variable1 = True
variable2 = False
result = variable1 or variable2
print("Result of or operation with one True and another False: ", result)
