
# This Python program demonstrates the use of and and is operators

# Define a function
def check_condition(x, y):
    return x > 5 and y < 10

# Check if the condition is true
if check_condition(8, 6):
    print("The condition is true")

# Check if the condition is false
if not check_condition(2, 12):
    print("The condition is false")

# Use the and operator to combine two conditions
if x > 5 and y < 10:
    print("Both conditions are true")

# Use the is operator to compare two objects
if a is b:
    print("a and b are the same object")

# Use the is operator to compare two objects for equality
if a is not b:
    print("a and b are not the same object")
