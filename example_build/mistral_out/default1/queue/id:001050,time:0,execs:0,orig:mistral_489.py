
# Definition of a function that checks if a number is positive, zero or None
def check_number(num):
    if num is None:
        print("Number is None")
    elif num > 0:
        print("Number is positive")
    else:
        print("Number is non-positive")

# Definition of some variables with None value
num1 = None
num2 = -5
num3 = 0

# Using or operator to check if num1 is None or num2 is negative
if num1 is None or num2 < 0:
    print("Either the number is None or it's non-positive")

# Calling the function with different arguments
check_number(num1)
check_number(num2)
check_number(num3)

# Using or operator to check if a variable is None or a condition is True
if not num1 and (num2 < 0 or num3 > 5):
    print("Both conditions are true")
