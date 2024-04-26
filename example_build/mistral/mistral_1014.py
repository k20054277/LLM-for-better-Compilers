
# Set initial values for variables
num1 = 10
num2 = 3

print("Before operation:")
print("num1 =", num1)
print("num2 =", num2)

# Perform logical AND operation and modulus assignment
if num1 > 5 and num2 % 2 == 0:
    # If both conditions are true, then num1 will be decreased by 3, and the result of num1 % 2 will be assigned to num1
    num1 -= 3
    num1 %= 2
    
print("After operation:")
print("num1 =", num1)
print("num2 =", num2)
