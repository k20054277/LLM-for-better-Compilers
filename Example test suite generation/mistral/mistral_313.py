
class Calculator:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.result = None

    def add(self, num=None):
        if num is not None:
            self.num2 = num
            self.result = self.num1 + self.num2
        help(self.add)

calculator = Calculator()
calculator.add(5)  # Outputs the help text and does not perform addition this time
print("Result: ", calculator.result)  # Prints None, as result was not set in this call

calculator.num1 = 3
calculator.add()   # Performs addition and prints help text
print("Result: ", calculator.result)
