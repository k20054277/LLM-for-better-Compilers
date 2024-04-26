
# Define some variables
num1 = 5
num2 = 10
is_positive = True

# Conditional statements using 'and' operator
if (num1 > 0) and (num2 > 0):
    print("Both numbers are positive.")
elif (num1 < 0) and (num2 < 0):
    print("Both numbers are negative.")
else:
    print("One number is positive and one is negative.")

# Applying 'and' operator with logical variables
if is_positive and (num1 > num2):
    print("Variable 'is_positive' is True and num1 is greater than num2.")
elif not is_positive and num1 > num2:
    print("Variable 'is_positive' is False and num1 is still greater than num2.")
else:
    print("Variable 'is_positive' and the condition for number comparison is not met.")
