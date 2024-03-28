
class Calculator:
    def __init__(self):
        pass

    # Abstraction: Hide the implementation details of addition
    def add(self, num1, num2):
        assert isinstance(num1, (int, float)) and isinstance(num2, (int, float)), "Both inputs must be numbers"
        self._add_internal(num1, num2)

    def subtract(self, num1, num2):
        assert isinstance(num1, (int, float)) and isinstance(num2, (int, float)), "Both inputs must be numbers"
        self._subtract_internal(num1, num2)

    # Encapsulation: Hide the implementation details of addition and subtraction
    def _add_internal(self, num1, num2):
        result = num1 + num2
        print(f"Adding {num1} and {num2}: Result is {result}")

    def _subtract_internal(self, num1, num2):
        result = num1 - num2
        print(f"Subtracting {num1} from {num2}: Result is {result}")

# Usage
calculator = Calculator()
calculator.add(3, 5)
calculator.subtract(10, 7)
