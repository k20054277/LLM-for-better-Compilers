
# This is a simple Python script for demonstrating the usage of True and //=

# Define some variables
num1 = 25
num2 = 7
quotient = 0
remainder = 0
is_valid_input = True

# Check if the input is valid (both numbers should be integers)
if type(num1) != int or type(num2) != int:
    print("Error: Both num1 and num2 must be integers.")
    is_valid_input = False
else:
    # Perform division and get the quotient
    quotient = num1 // num2
    
    # Display the quotient
    print(f"The quotient of {num1} and {num2} is {quotient}")

    # Perform floor division assignment
    num1 //= num2

    # Display the updated value of num1
    print(f"After performing num1 //= num2, num1 becomes: {num1}")
