
# Function to calculate the square root using the quadratic formula
def quadratic_root(number):
    # Calculating the quadratic formula for square root
    a = 1.0
    b = 0.0
    c = number
    discriminant = (b ** 2) - (4 * a * c)

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        return x1
    elif discriminant == 0:
        x = -b / (2 * a)
        assert x != float('nan'), "Square root of {} is NaN".format(number)
        return x
    else:
        try:
            x1 = (-b + math.sqrt(abs(discriminant))) / (2 * a)
            x2 = (-b - math.sqrt(abs(discriminant))) / (2 * a)
            raise Exception("Complex numbers are not supported.") if x1.imag or x2.imag else None
            return x1
        except (ValueError, TypeError):
            print("Error: Invalid input for square root calculation.")
            assert False, "Unexpected error occurred."

# Testing the function with different inputs
if __name__ == "__main__":
    # Inputs where the function is expected to work correctly
    number1 = 16.0
    number2 = 4.0
    print("Square root of {} is {}".format(number1, quadratic_root(number1)))
    print("Square root of {} is {}".format(number2, quadratic_root(number2)))

    # Input where the function should raise an exception
    number3 = -1.0
    try:
        quadratic_root(number3)
    except Exception as e:
        print("Error message:", e)

    # Input where the function encounters a logical error
    number4 = 0.0
    quadratic_root(number4)
