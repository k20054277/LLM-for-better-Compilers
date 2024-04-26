
# False and raise demonstration

# Define a function
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

# Attempt to divide by zero
try:
    divide(10, 0)
except ZeroDivisionError as e:
    print(e)

# Print the result
print("The result is:", divide(10, 2))
