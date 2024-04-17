
class Number:
    def __init__(self, num=0):
        self.num = num

    # A class method that checks if the given number is even or not
    @classmethod
    def is_even(cls, num):
        return cls.__is_even(abs(num))

    @staticmethod
    def __is_even(num):
        """A static utility method to check if a given number is even or not"""
        return num % 2 == 0

if __name__ == "__main__":
    num1 = Number()
    num2 = Number(5)
    num3 = Number(-6)

    print(f"Number {num1.num} is even: {Number.is_even(num1)}")  # True by default
    print(f"Number {num2.num} is even: {Number.is_even(num2)}")  # False
    print(f"Number {num3.num} is even: {Number.is_even(num3)}")  # True (negative numbers are also even if their last digit is)
