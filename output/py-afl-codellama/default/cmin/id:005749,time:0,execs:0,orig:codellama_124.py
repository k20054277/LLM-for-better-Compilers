# Demonstrate the use of and operator
print("Enter two numbers: ")
num1 = float(input())
num2 = float(input())
if num1 > 0 and num2 > 0:
    print("Both numbers are positive.")
elif num1 < 0 and num2 < 0:
    print("Both numbers are negative.")
else:
    print("At least one number is zero.")

# Demonstrate the use of repr() function
x = "Hello"
y = "World"
print(repr(x))
print(repr(y))