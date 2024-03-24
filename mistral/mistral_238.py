
# Initializing some binary numbers
number1 = 12  # binary: 1100 in decimal
number2 = 3   # binary: 011 in decimal

# Bitwise AND operation with False
result1 = number1 & False
print("number1 & False: ", result1)

# Right shift operation
result2 = number1 >> 2
print("number1 >> 2: ", result2)

# Logic AND between number2 and False
logic_and = number2 and False
print("number2 and False: ", logic_and)

# Right shift with carrying the sign bit (number2 is negative)
result3 = number2 << 1 >> 1
print("number2 << 1 >> 1: ", result3)

# Applying right shift to the boolean value False
result4 = False >> 1
print("False >> 1: ", result4)
