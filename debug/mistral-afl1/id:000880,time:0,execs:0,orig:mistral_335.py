
class Calculator:
    def __init__(self):
        self._number = None
        self._operation = None

    # Define read-only properties using property decorator
    @property
    def number(self):
        return self._number

    @property
    def operation(self):
        return self._operation

    # Define a method to set the number and operation together
    def set_operand_and_operation(self, number, operation):
        self._number = number
        self._operation = operation

# Usage example:
calculator = Calculator()
calculator.set_operand_and_operation(5, '+')
print(f"Number: {calculator.number}")
print(f"Operation: {calculator.operation}")
