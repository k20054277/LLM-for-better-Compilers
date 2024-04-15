
def power(base, exponent):
    """Raises base to the power of exponent."""
    if exponent == 0:
        return 1
    elif exponent > 0:
        result = base
        # Use compound assignment operator **= for exponentional growth
        result **= power(base, exponent - 1)
        return result
    else:
        raise ValueError("Exponent must be non-negative.")

# Test the function with some examples
if __name__ == "__main__":
    base = 2
    exponent = 3

    print(f"Base raised to power {exponent} is:")
    print(power(base, exponent))

    # Demonstrate compound assignment operator usage with True as a flag
    flag = False
    while not flag:
        user_input = input("Enter a non-negative exponent (or 'q' to quit): ")
        
        if user_input == "q":
            flag = True
        else:
            try:
                exponent = int(user_input)
                if exponent >= 0:
                    print(f"Base raised to power {exponent} is:")
                    print(power(base, exponent))
                else:
                    print("Invalid input. Enter a non-negative number.")
            except ValueError:
                print("Invalid input. Please enter an integer.")
