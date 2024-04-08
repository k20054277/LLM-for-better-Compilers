
# Define some variables
num = 10
is_positive = True

# Use if statement with a single condition
if num > 0:
    print("The number is positive")

# Use if-else statement with a single condition
if is_positive:
    print("The variable is set to True")
else:
    print("The variable is set to False or another falsy value")

# Use if-elif-else statement with multiple conditions
if num > 0:
    print("The number is positive")
elif num == 0:
    print("The number is zero")
else:
    print("The number is negative")
