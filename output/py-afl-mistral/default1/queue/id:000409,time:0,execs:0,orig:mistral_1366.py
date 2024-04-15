
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        result = self.a + self.b
        assert result >= 0, "The sum of two numbers should be non-negative"
        return result

    def set_number(self, name, value):
        setattr(self, name, value)

calculator = Calculator(-1, 2)  # Initialize calculator with negative number
try:
    print("Sum is:", calculator.add())
except AssertionError as e:
    print(e)

calculator.set_number("a", 3)
print("New sum is:", calculator.add())
