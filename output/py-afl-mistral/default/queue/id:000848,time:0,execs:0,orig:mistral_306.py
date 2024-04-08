
# Assigning None to a variable
none_var = None
print("Variable 'none_var' is:", none_var)
print("Type of variable 'none_var':", type(none_var))

# Assigning a float value to a variable
float_var = 3.14
print("Variable 'float_var' is:", float_var)
print("Type of variable 'float_var':", type(float_var))

# Using None as default value in a function
def greet(name = None):
    if name is not None:
        print("Hello, ", name)
    else:
        print("Hello!")

greet()  # prints "Hello!"
greet("John")  # prints "Hello, John"

# Using float in arithmetic operations
num1 = 5
num2 = 3.5
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2
remainder = num1 % num2

print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)
print("Remainder:", remainder)
