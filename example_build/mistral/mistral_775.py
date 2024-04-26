
# Define a binary number as an integer
binary_number = 60  # equates to 0011 1110 in binary

print("Original Binary Number: ", bin(binary_number)[2:])

# Using True boolean value
boolean_value = True
result = binary_number if boolean_value else 0
print("\nResult with True boolean value: ", result, bin(result)[2:])

# Using bitwise NOT (~) operator
result = ~binary_number
print("\nResult with bitwise NOT operator: ", result, bin(result)[2:])
