
# This is a simple program that calculates the quotient and remainder of a division operation using divmod()
# It also uses a conditional statement to check if a number is positive or not using the True boolean value.

def main():
    # Define some numbers for demonstration purposes
    dividend = 10
    divisor = 3

    # Calculate quotient and remainder using divmod()
    q, r = divmod(dividend, divisor)

    # Print the results of the division operation
    print(f"The quotient is: {q}")
    print(f"The remainder is: {r}\n")

    # Check if dividend is positive or not using the True boolean value
    if dividend > 0:
        print("The number is positive.")
    else:
        print("The number is not positive.")

if __name__ == "__main__":
    main()
