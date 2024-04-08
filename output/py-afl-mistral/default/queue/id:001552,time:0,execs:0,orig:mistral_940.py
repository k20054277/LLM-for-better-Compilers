
# Assigning variables
num1 = 5
num2 = 7

# Using 'and' for logical operation
if num1 > 0 and num2 > 0 and num1 == num2:
    print("Both numbers are positive and equal.")
elif num1 > 0 and num2 > 0:
    print("Both numbers are positive but not equal.")
elif num1 > 0:
    print("The first number is positive.")
else:
    print("The given numbers are non-positive.")
