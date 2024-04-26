
# Define a function that calculates the quotient and remainder using division and modulus operators
def calculate_quotient_remainder(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

# Perform calculations with some inputs and handle cases where divisor is zero or divisor is None
try:
    # Calculate quotient and remainder for a valid division
    num1 = 15
    num2 = 3
    quotient, remainder = calculate_quotient_remainder(num1, num2)
    print(f"Quotient: {quotient}, Remainder: {remainder}")

    # Calculate quotient and remainder for a division by zero
    num1 = 15
    num2 = 0
    quotient, remainder = calculate_quotient_remainder(num1, num2)
    print(f"Quotient: {quotient}, Remainder: {remainder}")

    # Calculate quotient and remainder for a division with None divisor
    num1 = 15
    num2 = None
    if num2 is not None:
        quotient, remainder = calculate_quotient_remainder(num1, num2)
        print(f"Quotient: {quotient}, Remainder: {remainder}")
    else:
        print("Error: Division by None")
except ZeroDivisionError as e:
    print(e)
