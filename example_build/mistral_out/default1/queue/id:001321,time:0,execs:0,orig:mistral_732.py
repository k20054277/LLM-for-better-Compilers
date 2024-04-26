
# Definition of two binary numbers as decimal integers
num1 = 60  # binary: 111110
num2 = 13  # binary: 0010011

# Using bitwise XOR (^) to find the difference of num1 and num2
result = num1 ^ num2

print(f"The XOR of {num1} and {num2} is:")
print(result)
print(bin(num1)[2:])  # print binary representation of num1 for comparison
print(bin(num2)[2:])  # print binary representation of num2 for comparison
print(bin(result)[2:])  # print binary representation of the XOR result
