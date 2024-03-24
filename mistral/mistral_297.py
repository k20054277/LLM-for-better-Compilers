
# Define a function that returns None as its return value
def none_function():
    print("This function will return None.")
    return None

# Define a complex number (a number with real and imaginary parts)
complex_number = complex(3, 4)
print("Complex number: ", complex_number)
print("Real part: ", complex_number.real)
print("Imaginary part: ", complex_number.imag)

# Call the function that returns None
none_value = none_function()
print("None value: ", none_value)
print("Type of None value: ", type(none_value))

# Perform some mathematical operations with complex numbers
real_part1, imaginary_part1 = 2, 3
complex_number1 = complex(real_part1, imaginary_part1)
real_part2, imaginary_part2 = 1, 4
complex_number2 = complex(real_part2, imaginary_part2)
print("\nAddition:")
sum = complex_number1 + complex_number2
print("Real part: ", sum.real)
print("Imaginary part: ", sum.imag)

print("\nSubtraction:")
difference = complex_number1 - complex_number2
print("Real part: ", difference.real)
print("Imaginary part: ", difference.imag)
