
# A simple calculator program that demonstrates the use of None and //=

class Calculator:
    def __init__(self, dividend=None):
        self.dividend = dividend if dividend is not None else 0
        self.divisor = 1

    def divide(self, divisor):
        self.divisor = divisor
        quotient = self.dividend // self.divisor
        self.dividend = quotient

# Usage example:
calculator = Calculator(10)
calculator.divide(3)
print(f'Quotient is {calculator.dividend}') # Quotient is 3

calculator.divide(None)
print(f'Quotient after division by None: {calculator.dividend}') # Quotient after division by None: 0
