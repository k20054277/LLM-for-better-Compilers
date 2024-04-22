
def divide(dividend, divisor):
    """
    This function divides given dividend by divisor and returns the quotient
    :param dividend: The numerator in division operation
    :param divisor: The denominator in division operation
    :return: The result of the division operation
    """
    try:
        result = dividend / divisor
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    except ValueError:
        print("Error: Denominator must be a number.")
        return None

    return result

print("Enter the dividend and denominator (space-separated):")
input_str = input()
dividend, divisor = map(float, input_str.split())

result = divide(dividend, divisor)

if result is not None:
    print(f"The quotient of {dividend} and {divisor} is: {result}")
else:
    assert False, "An error occurred during division."

# Using a while loop for infinite calculation demonstration (optional)
i = 0
while True:
    print(f"The result of i^2 is {i*i}")
    i += 1
