
# Define some variables
num1 = 5
num2 = 10
flag1 = True
flag2 = False

# Using and operator (Both conditions must be true)
if (num1 > 4 and num2 < 15):
    print("Condition 1 is true")

# Using or operator (At least one condition must be true)
if (flag1 and flag2 or not flag1):
    print("Condition 2a is true")

# Demonstrating the use of parentheses for complex conditions
if ((num1 > 4) or (num2 < 5)) and flag1:
    print("Condition 3 is true")
