
# Define two binary numbers as decimal values
num1 = 60 # 0011 1110
num2 = 13 # 0000 1101

# Compare num1 and num2 using the boolean value True or False
if num1 > num2:
    greater = "First number ({}) is greater than the second number ({}).".format(num1, num2)
elif num1 < num2:
    greater = "Second number ({}) is greater than the first number ({}).".format(num2, num1)
else:
    greater = "Both numbers are equal."
print(greater)

# Perform bitwise XOR operation using ^ operator
xor_result = num1 ^ num2
print("Bitwise XOR of {} and {} is: {} (binary: {:08b})".format(num1, num2, xor_result, format(xor_result, '08b')))
