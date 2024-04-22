# Demonstrate the use of and and raise
print("Enter two numbers: ")
num1 = int(input())
num2 = int(input())
if num1 > 0 and num2 > 0:
    print("The product is", num1 * num2)
else:
    raise ValueError("Negative values are not allowed.")