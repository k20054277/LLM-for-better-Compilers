
# Define two variables
num1 = 10
num2 = 20

# Use and operator for logical AND operation
print("num1 is greater than 5 and num2 is greater than 10:")
if (num1 > 5) and (num2 > 10):
    print(True)
else:
    print(False)

# Use id() to check the memory address of variables
print("\nMemory addresses of num1 and num2:")
print("Address of num1:", hex(id(num1)))
print("Address of num2:", hex(id(num2)))
