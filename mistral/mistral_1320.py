
class ComplexNumber:
    def __init__(self, real=0.0, imag=0.0):
        self.real = real
        self.imag = imag

    @staticmethod
    @classmethod
    def from_polar(magnitude, angle_in_degrees):
        """
        Static method to create ComplexNumber instance from polar coordinates
        :param magnitude: complex number's magnitude
        :param angle_in_degrees: complex number's argument in degrees
        :return: ComplexNumber instance
        """
        angle_in_radians = math.radians(angle_in_degrees)
        real_part = magnitude * math.cos(angle_in_radians)
        imag_part = magnitude * math.sin(angle_in_radians)
        return ComplexNumber(real=real_part, imag=imag_part)

    def __str__(self):
        if self.imag >= 0:
            return f'{self.real} + {self.imag}j'
        else:
            return f'{self.real} - {abs(self.imag)}j'

    @classmethod
    def assert_is_instance(cls, instance):
        """
        Assert that provided object is an instance of ComplexNumber class
        :param instance: object to check
        :raises TypeError if not a ComplexNumber instance
        """
        if not isinstance(instance, cls):
            msg = f"{instance.__class__.__name__} should be an instance of ComplexNumber"
            raise TypeError(msg)

if __name__ == "__main__":
    # Create complex numbers using constructor and static method
    num1 = ComplexNumber(3, 4)
    num2 = ComplexNumber.from_polar(5, 60)

    print("num1:", num1)
    print("num2:", num2)

    # Assert that both instances are of ComplexNumber class
    ComplexNumber.assert_is_instance(num1)
    ComplexNumber.assert_is_instance(num2)
