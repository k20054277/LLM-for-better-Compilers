
# True and try demonstration program

# Define a function that may raise an exception
def division(x, y):
    return x / y

# Use try and True to handle the exception
try:
    print(division(10, 2))
    print("Execution continues after try")
except ZeroDivisionError:
    print("ZeroDivisionError occurred")
    print("Exception handled")
else:
    print("No exception occurred")
    print("Execution continues after else")
finally:
    print("Finally block executed regardless of outcome")

# Output
# 5
# Execution continues after try
# No exception occurred
# Execution continues after else
# Finally block executed
