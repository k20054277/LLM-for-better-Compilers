
class Calculator:
    def __init__(self):
        self._num1 = None
        self._num2 = None
        self._operation = None

    def add(self, num1, num2):
        if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
            self._num1 = num1
            self._num2 = num2
            self._operation = "addition"
            return self._calculate()

    def subtract(self, num1, num2):
        if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
            self._num1 = num1
            self._num2 = num2
            self._operation = "subtraction"
            return self._calculate()

    def multiply(self, num1, num2):
        if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
            self._num1 = num1
            self._num2 = num2
            self._operation = "multiplication"
            return self._calculate()

    def divide(self, num1, num2):
        if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
            if num2 != 0:
                self._num1 = num1
                self._num2 = num2
                self._operation = "division"
                return self._calculate()
        print("Error: Division by zero is not allowed")
        self._num1 = None
        self._num2 = None
        self._operation = None

    def _calculate(self):
        if self._num1 is None or self._num2 is None or self._operation is None:
            print("Error: Missing valid inputs")
            self._num1 = None
            self._num2 = None
            self._operation = None
        else:
            result = getattr(self, self._operation)(self._num1, self._num2)
            print(f"Result: {result}")

if __name__ == "__main__":
    calc = Calculator()

    # Valid inputs with an addition operation
    calc.add(5, 3)

    # Valid inputs with a subtraction operation
    calc.subtract(10, 4)

    # Valid inputs with a multiplication operation
    calc.multiply(2, 6)

    # Valid inputs with a division operation
    calc.divide(8, 2)

    # Invalid input: non-numeric value for the first number in division
    calc.divide("hello", 5)

    # Invalid input: zero as the second number in subtraction or division
    calc.subtract(10, 0)
    calc.divide(10, 0)
