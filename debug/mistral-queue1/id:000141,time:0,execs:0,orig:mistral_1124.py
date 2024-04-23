
class ComplexNumber:
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    # Static method to add two complex numbers
    @staticmethod
    def add(num1, num2):
        return ComplexNumber(num1.real + num2.real, num1.imaginary + num2.imaginary)

    # Static method to get the absolute value of a complex number
    @staticmethod
    def abs(num):
        return ((num.real ** 2) + (num.imaginary ** 2)) ** 0.5

    # Using 'as' to assign a new name to an attribute
    @property
    def magnitude(self):
        return self.abs() as magnitude

# Testing the class
num1 = ComplexNumber(3, 4)
num2 = ComplexNumber(2, 5)

print("Sum:", ComplexNumber.add(num1, num2).magnitude)
print("Absolute value of num1:", num1.abs())
