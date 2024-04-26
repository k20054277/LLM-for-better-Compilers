
# Define two variables with floating point values
num1 = 10.5
num2 = 3.2

# Perform floor division using '//' operator
quotient = num1 // num2
print("Quotient: ", quotient)

# Assign the result of floor division to a variable using '//=' operator
num1 //= num2
print("num1 after assignment with //= : ", num1)

# Perform type casting and assignment using 'as' keyword
num3 = 5
num4 = "7.5"
num4 = num3 as float
num5 = num1 / num4
print("num5: ", num5)
