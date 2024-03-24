
# app.py
def divide(x, y):
    """Divides x by y."""
    if y is None:
        return None
    else:
        result = x / y
        return result

if __name__ == "__main__":
    num1 = 10
    num2 = 5
    print(f"Result of {num1} divided by {num2}: {divide(num1, num2)}")

    # Demonstrate None as a return value
    print("Function called with y=None: ", divide(num1, None))
