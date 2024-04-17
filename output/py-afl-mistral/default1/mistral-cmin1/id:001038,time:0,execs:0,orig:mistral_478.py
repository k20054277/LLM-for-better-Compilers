
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None

    print(f"Result of division: {result}")

    # Using the division assignment operator to update 'num1' with the result of the division.
    num1 /= num2

    print(f"Num1 after division assignment: {num1}")

# Calling the function with some numbers as arguments
divide_numbers(10, 3)
divide_numbers(5, 2)
divide_numbers(4, 0)
