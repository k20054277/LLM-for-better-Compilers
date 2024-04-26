
# Logical AND operation with integers
a = 5
b = 10
c = 15

if a > 4 and b < 15:
    print("Both conditions are true")
else:
    print("At least one condition is false")

# Logical AND operation with booleans
x = True
y = False
z = True

print(x and y)  # prints False
print(x and z)  # prints True

# Bitwise XOR operation between numbers
num1 = 5
num2 = 3
result = num1 ^ num2
print("Result of bitwise XOR: ", result)  # prints: Result of bitwise XOR: 6
