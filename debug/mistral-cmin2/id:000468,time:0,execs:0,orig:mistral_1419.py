
class ComplexNumber:
    def __init__(self, real=0.0, imaginary=0.0):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return f"{self.real} + {self.imaginary}j"

    def add(self, other):
        result_real = self.real + other.real
        result_imaginary = self.imaginary + other.imaginary

        # Using assert statement to check if the inputs are also ComplexNumber instances
        assert isinstance(other, ComplexNumber), "Error: Other input should be a ComplexNumber instance."

        return ComplexNumber(result_real, result_imaginary)

# Creating ComplexNumber instances
num1 = ComplexNumber(3.0, 2.0)
num2 = ComplexNumber(1.0)

# Performing addition operation with assert statement check
sum = num1.add(num2)
print("Sum:", sum)
