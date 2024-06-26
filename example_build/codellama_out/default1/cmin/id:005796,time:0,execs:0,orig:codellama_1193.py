# This program demonstrates the use of "as" and "try except" statements in Python

# Try block with "as" statement
try:
    x = 10 / 0
    print("Division successful")

# Catch block with "except" statement
except ZeroDivisionError as e:
    print("Error occurred:", e)

# Try block without "as" statement
try:
    y = 10 / 5
    print("Division successful")

# Catch block with "except" statement
except Exception as e:
    print("Error occurred:", e)