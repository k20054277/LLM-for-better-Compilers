
class Calculator:
    def __init__(self):
        self._number_one = None
        self._number_two = None
        self._result = None

    def set_numbers(self, number_one, number_two):
        if number_one is not None and number_two is not None:
            self._number_one = number_one
            self._number_two = number_two
        else:
            print("Both number_one and number_two must be provided.")

    def add(self):
        if self._number_one is not None and self._number_two is not None:
            self._result = self._number_one + self._number_two
        else:
            print("Error: Both numbers must be set before adding them.")

    def get_result(self):
        return self._result

# Usage
calculator = Calculator()
calculator.set_numbers(3, 4)
calculator.add()
print("Result:", calculator.get_result())  # Output: Result: 7
