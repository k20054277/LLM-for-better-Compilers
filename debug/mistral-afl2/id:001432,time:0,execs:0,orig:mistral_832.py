
class ComplexNumber:
    def __init__(self, real=0.0, imaginary=0.0):
        self.real = real
        self.imaginary = imaginary

    @classmethod
    def from_polar_coordinates(cls, r, theta):
        return cls(r * math.cos(theta), r * math.sin(theta))

    def __add__(self, other):
        result = ComplexNumber(
            self.real + other.real,
            self.imaginary + other.imaginary
        )
        return result

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

if __name__ == "__main__":
    num1 = ComplexNumber(1.0, 2.0)
    num2 = ComplexNumber(3.0, 4.0)

    print("num1: ", num1)
    print("num2: ", num2)

    print("sum: ", num1 + num2)
    print("difference: ", num1 - num2)

    num3 = ComplexNumber.from_polar_coordinates(5.0, math.pi/4)
    print("num3 from polar: ", num3)
    print("conjugate of num1: ", num1.conjugate())
