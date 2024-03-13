
# Define a calculator function that returns quotient, remainder and checks for division by zero
def calc_division(dividend, divisor):
    if divisor != 0:
        quotient = dividend // divisor
        remainder = dividend % divisor
        return quotient, remainder
    else:
        print("Error: Division by zero")
        return None, None

# Main function to test the calculator function with different inputs
if __name__ == "__main__":
    num1 = 15
    num2 = 3

    # Call the calculator function and store the result in a variable
    result = calc_division(num1, num2)

    if result is not None:
        print("Quotient:", result[0])
        print("Remainder:", result[1])

    num1 = 7
    num2 = 0

    # Call the calculator function with divisor as zero and check for None return
    result = calc_division(num1, num2)

    if result is None:
        print("No quotient or remainder obtained due to division by zero")
    else:
        print("Error in input. Quotient and Remainder not calculated.")
