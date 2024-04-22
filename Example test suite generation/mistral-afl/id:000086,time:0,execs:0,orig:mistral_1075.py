
class ComplexNumber:
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    @staticmethod
    def zero():
        return ComplexNumber(0, 0)

    @classmethod
    def from_polar(cls, magnitude, angle_in_degrees):
        angle_in_radians = math.radians(angle_in_degrees)
        real = magnitude * math.cos(angle_in_radians)
        imaginary = magnitude * math.sin(angle_in_radians)
        return cls(real, imaginary)

    @classmethod
    def from_cartesian(cls, real, imaginary):
        return cls(real, imaginary)

    @property
    def magnitude(self):
        return math.sqrt(self.real ** 2 + self.imaginary ** 2)

    @magnitude.setter
    def magnitude(self, value):
        r = value * (self.imaginary >= 0)
        self.real = r
        self.imaginary = value * (self.imaginary < 0)

    def __str__(self):
        if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}j"
        else:
            return f"{self.real} - {abs(self.imaginary)}j"

# Using the class methods
cn1 = ComplexNumber.zero()
print(cn1)

cn2 = ComplexNumber.from_polar(3, 60)
print(cn2)

cn3 = ComplexNumber.from_cartesian(2, -1)
print(cn3)

# Setting magnitude of an existing complex number
cn4 = ComplexNumber(3, 4)
cn4.magnitude = 5
print(cn4)
