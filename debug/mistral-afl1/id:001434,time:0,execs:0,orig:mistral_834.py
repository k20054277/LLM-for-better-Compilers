
# Demonstrating the usage of 'and' operator
def is_positive(num):
    return num > 0

def is_even(num):
    return num % 2 == 0

number = int(input("Enter a number: "))
if is_positive(number) and is_even(number):
    print(f"The number {number} is positive and even.")
else:
    print(f"The number {number} is not positive and/or not even.")

# Demonstrating the usage of 'complex' data type
import cmath

real_part = 3.0
imaginary_part = 2.0
complex_num = complex(real_part, imaginary_part)

print("Real part:", real_part)
print("Imaginary part:", imaginary_part)
print("Complex number:", complex_num)
print("Conjugate of the complex number:", complex_num.conjugate())
print("Modulus (magnitude) of the complex number:", abs(complex_num))
print("Phase angle of the complex number:", cmath.phase(complex_num))
