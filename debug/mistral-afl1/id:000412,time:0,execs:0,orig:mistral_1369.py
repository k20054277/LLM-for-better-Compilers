
class ComplexNumber:
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    @staticmethod
    def square(number):
        assert isinstance(number, (int, float)), "Input should be either integer or float"
        return number ** 2

if __name__ == "__main__":
    complex_num = ComplexNumber(3.5)
    print("Complex Number: ", complex_num.real, "+", complex_num.imaginary, "*i")
    square_result = ComplexNumber.square(ComplexNumber.square)  # this line will cause an error due to recursion
    print("Square of Complex Number: ", square_result)  # This line won't be reached as the previous one causes an error

    try:
        square_result = ComplexNumber.square(complex_num)  # This should work and prints the error message if input is not valid integer or float
    except AssertionError as e:
        print("Error:", e)
    else:
        print("Square of Complex Number: ", complex(real=square_result.real, imaginary=square_result.imaginary))
