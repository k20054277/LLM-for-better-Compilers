
def divide(num1, num2):
    """This function divides num1 by num2."""
    try:
        result = num1 / num2
    except ZeroDivisionError as e:
        print("Error:", e)
        return None

    # Check if the result is even
    if num1 % 2 != 0 and num2 % 2 != 0:
        print("Both numbers must be even.")
        raise Exception("Exception: Both numbers must be even.")

    return result

if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    try:
        result = divide(num1, num2)
    except Exception as e:
        print(e)
    else:
        if result is not None:
            print(f"Result: {result}")
