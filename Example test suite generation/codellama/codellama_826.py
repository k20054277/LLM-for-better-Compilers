# This program demonstrates the use of and and except in Python

# Using and
print("Hello")
print("World")
print("and")
print("Python")

# Output:
# Hello
# World
# and
# Python

# Using except
try:
    print(1/0)
except ZeroDivisionError as e:
    print("Division by zero!", e)

# Output:
# Division by zero! division by zero