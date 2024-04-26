
# Setting two binary numbers
a = 12 # 1100 in binary (decimal 12)
b = 3  # 0111 in binary (decimal 3)

# Logical AND operation (Perform bitwise AND on each bit and keep result only if both are set)
result_and = a & b
print(f'Result of A & B: {result_and} (Decimal: {bin(result_and)[2:]})')

# Bitwise left shift operation (Shift the bits n places to the left)
result_left_shift = a << 2
print(f'Result of A << 2: {result_left_shift} (Decimal: {decimal(bin(result_left_shift)[2:])})')

# Function for converting binary string to decimal number
def decimal(binary):
    return int(binary, 2)
