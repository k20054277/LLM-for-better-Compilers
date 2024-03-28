
# This Python program demonstrates the use of True and divmod

# Define two numbers
num1 = 10
num2 = 3

# Check if num1 is divisible by num2 using True and divmod
if num1 % num2 == 0:
    print(num1 + " is divisible by " + num2)

# Use divmod to find the quotient and remainder when num1 is divided by num2
 quotient, remainder = divmod(num1, num2)

# Print the quotient and remainder
print("The quotient is:", quotient)
print("The remainder is:", remainder)
