
# Define a power function using exponentiation operator **
def power(base, exponent):
    # Base case: if exponent is 0, return 1
    if exponent == 0:
        return 1
    else:
        # Recursive call: base * base raised to the power of (exponent - 1)
        return base ** (exponent - 1) * base

# Test cases
print(power(2, 3))                     # Expected output: 8
print(power(5, 2))                     # Expected output: 25
print(power(0, 0))                     # Expected output: 1
print(power(1, -1))                    # Expected output: 1 (since 1 raised to any negative power is 1)
print(power(-3, 2))                    # Expected output: 9 (-3 * -3)
print(power(2, 0))                     # Expected output: 1
print(power(True, 2))                  # Raises a TypeError since you can't raise a Boolean value to a power
