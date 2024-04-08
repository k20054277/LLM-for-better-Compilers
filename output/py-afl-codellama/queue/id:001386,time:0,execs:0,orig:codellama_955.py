# Using and to check if both conditions are true
if 5 > 3 and 2 > 1:
    print("Both conditions are true")

# Refactoring using an inline if statement
if (5 > 3) and (2 > 1):
    print("Both conditions are true")

# Refactoring using a variable to store the result of the first condition
result = 5 > 3
if result and 2 > 1:
    print("Both conditions are true")

# Refactoring using an inline if statement with short-circuit evaluation
if (5 > 3) and (2 > 1):
    print("Both conditions are true")