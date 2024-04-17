
# This is a simple program that calculates the quotient and remainder of a division operation using divmod() function
def main():
    # Set up some input values
    dividend = 15
    divisor = 4

    # Perform the division using divmod() function
    (quotient, remainder) = divmod(dividend, divisor)

    # Print the result with a message
    print(f'The quotient of {dividend} divided by {divisor} is: {quotient}')
    print(f'The remainder of {dividend} divided by {divisor} is: {remainder}')

    # Demonstrate False value
    boolean_value = False
    if boolean_value:
        print('This should not be printed because the boolean value is False')
    else:
        print('This will be printed because the boolean value is False')
        print('However, the condition in the if statement is never executed since the value is already known to be False')
        print('So, it is more common to use an if statement with a conditional expression that can evaluate to True or False')

if __name__ == '__main__':
    main()
