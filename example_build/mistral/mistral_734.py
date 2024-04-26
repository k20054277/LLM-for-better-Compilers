
# Setting some binary values as integers
binary_value1 = 1
binary_value2 = 1 << 3

print("Binary Value 1 (Decimal): ", binary_value1)
print("Binary Value 2 (Decimal): ", binary_value2)

# Displaying the binary representations
print(f"Binary representation of Binary Value 1: {bin(binary_value1)}")
print(f"Binary representation of Binary Value 2: {bin(binary_value2)}")

# Using True and bitwise left shift together
some_boolean = True
number = binary_value1
number <<= some_boolean

print("Number before assignment with boolean:", number)
print("Boolean value:", some_boolean)

if some_boolean:
    number <<= 1
else:
    number >>= 1

print("Number after assignment with conditional statement:", number)

# Displaying the binary representations of the final numbers
print(f"Binary representation of final Number: {bin(number)}")
