
class ComplexCalculator:
    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2

    def add(self):
        result = self._num1 + self._num2
        return result

    def subtract(self):
        result = self._num1 - self._num2
        return result

    def abstract_result(self, func):
        result = func(self)
        return result * 2

# Instantiate the calculator class with two numbers
calculator = ComplexCalculator(5, 3)

# Perform addition and assign the result to a variable using as keyword
result_add as add_res
add_res = calculator.add() as add_result

# Print the result of addition with abstract_result method
print("Addition Result: ", calculator.abstract_result(lambda x: x.add))

# Perform subtraction and assign the result to a variable using as keyword
result_subtract as sub_res
sub_res = calculator.subtract() as sub_result

# Print the result of subtraction with abstract_result method
print("Subtraction Result: ", calculator.abstract_result(lambda x: x.subtract))
