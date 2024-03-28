
# Using True
number = 10
if number > 5:
    print("Number is greater than 5")
else:
    print("Number is less than or equal to 5")

# Using bitwise right shift operator (>>)
binary_number = 0b1111_0101 # binary representation of decimal number 9 (decimal 0b means it's in binary form)
shifted_number = binary_number >> 2
print(bin(shifted_number)) # prints "0b0011_1100" which is the binary representation of decimal number 3
print(decimal(shifted_number)) # prints 3, the decimal equivalent of the shifted binary number
