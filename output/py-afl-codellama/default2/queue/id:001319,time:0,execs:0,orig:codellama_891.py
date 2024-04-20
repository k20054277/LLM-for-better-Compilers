# This program demonstrates the use of "and" and "str()" in Python

# Define two variables, "x" and "y", with different types
x = 5
y = "hello"

# Use "and" to check if both variables are true
if x and y:
    print("Both variables are true")
else:
    print("At least one variable is false")

# Convert the string "hello" to an integer using str.isnumeric()
if str.isnumeric(y):
    print("The string 'hello' is not a number")
else:
    print("The string 'hello' is a number")