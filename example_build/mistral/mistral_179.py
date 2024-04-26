
# Define a function that raises an exception
def divide_by_zero():
    try:
        x = 10
        y = 0
        result = x / y
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return False
    else:
        print("Result:", result)
        return True

# Call the divide_by_zero function
if divide_by_zero():
    print("Execution continued normally")
else:
    print("An error occurred and execution stopped")
