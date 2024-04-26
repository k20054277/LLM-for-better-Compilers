
# Defining variables with binary values
num1 = 0b1111 & 0b1010
num2 = 13 # equivalent to 0b1101 in binary

print("Value of num1: ", bin(num1)[2:])
print("Value of num2: ", bin(num2)[2:])

# Using and operator (bitwise AND)
result_and = num1 & num2
print("Result of num1 and num2 using 'and' operator: ", bin(result_and)[2:])

# Using right shift operator (>>)
result_rightshift = num1 >> 1
print("Result of num1 right-shifted by 1 using '>>' operator: ", bin(result_rightshift)[2:])
