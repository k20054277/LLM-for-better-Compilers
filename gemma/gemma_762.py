
# True and tryexcept demonstration
try:
    # Attempt to divide by zero
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    # Handle the exception
    print("Cannot divide by zero")
    result = None

# Output
# Cannot divide by zero
# result = None
