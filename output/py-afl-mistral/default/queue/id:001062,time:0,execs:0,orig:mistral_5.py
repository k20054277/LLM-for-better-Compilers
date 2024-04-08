
# Demonstrating False
if not 5 > 10:
    print("Five is less than ten, which is false.")
else:
    print("Five is greater than or equal to ten, which is true.")
    
# Demonstrating as keyword
import math

result = math.sqrt(-1)
complex_number = complex(0, result)  # Creating a complex number from the real and imaginary parts

# The following line is equivalent to: complex_number = complex('-i')
complex_number as imaginary_unit = complex('-i')

print("Complex number: ", complex_number)
print("Imaginary unit: ", imaginary_unit)
