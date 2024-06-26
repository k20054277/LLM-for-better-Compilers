
# Demonstrating False
print("Demonstrating False:")
boolean_value = False
if boolean_value:
    print("This should not be printed because Boolean value is False.")
else:
    print("This will be printed as the Boolean value is False.")

# Demonstrating complex numbers
print("\nDemonstrating complex numbers:")
real_part = 5.0
imaginary_part = 3.0j
complex_number = complex(real_part, imaginary_part)
print("Complex number: ", complex_number)
print("Real part: ", complex_number.real)
print("Imaginary part: ", complex_number.imag)
print("Conjugate: ", complex_number.conjugate())
print("Abs value: ", abs(complex_number))
print("Arg value: ", arg(complex_number))
