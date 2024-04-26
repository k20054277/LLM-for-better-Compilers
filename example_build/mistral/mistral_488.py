
# Assigning None to a variable
number = None

# Checking if number is not equal to None using and operator
if number is not None and type(number) is not list:
    print("Number is not None and it's not a list")
else:
    print("Number is either None or it's a list")

# Assigning a value to the variable number
number = 5

# Using and operator for logical conditions
if number > 0 and number < 10:
    print("Number is between 0 and 10")
