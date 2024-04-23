
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return f"{self.real} + {self.imaginary}j"

    def custom_repr(self):
        return f"ComplexNumber({self.real}, {self.imaginary})"

# Create an instance of ComplexNumber class
complex_number = ComplexNumber(3, 4)

# Assign alias using 'as'
alias = complex_number as C

print("Default String Representation:")
print(complex_number)
print("Aliased Object Representation:")
print(C)
print("Custom Representation with repr():")
print(repr(ComplexNumber(3, 4))) # This will print ComplexNumber(3, 4)
print(repr(complex_number))     # This will print 'ComplexNumber(3, 4)' by default
complex_number.custom_repr()   # This will print: ComplexNumber(3, 4)
