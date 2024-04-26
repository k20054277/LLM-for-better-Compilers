
# Set a variable with a false boolean value
is_student = False
print("Is student is:", is_student)
print("Type of is_student is:", type(is_student))

# Convert an integer number to binary using bin() function
number = 5
binary_number = bin(number)[2:]
print("Binary representation of number 5 is:", binary_number)

# Check if boolean value is false and print corresponding binary representation
if not is_student:
    print("You are not a student")
    print("False in binary is:", bin(bool(not is_student))[2:])
else:
    print("You are a student")
