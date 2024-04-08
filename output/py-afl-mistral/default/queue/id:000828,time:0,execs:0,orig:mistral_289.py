
# This function takes an integer as an argument and returns its binary representation
def to_binary(number):
    return bin(number)[2:]

# Demonstrating the use of None
num = 10
if num is None:
    print("Number is None")
else:
    print(f"The number {num} in binary is: {to_binary(num)}")

# Assigning None to a variable
num = None
if num is not None:
    print(f"The number is: {num}")
else:
    print("Number is None")

# Demonstrating the use of bin() function with negative numbers and floats
print(bin(-10))  # prints '-0b1010110110111111111111111111011'
print(bin(3.14))  # prints '0b11.100110011111010101101101101111'
