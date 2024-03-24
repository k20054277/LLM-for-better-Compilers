
class Calculator:
    # Define a constant value (can be replaced by True)
    IS_POSITIVE = True

    @staticmethod
    def add(num1, num2):
        """Static method to add two numbers"""
        return num1 + num2

    def __init__(self, value):
        """Initialize the class instance with a given value"""
        self.value = value

    def display_value(self):
        """Method to display the instance value"""
        print("Value: {}".format(self.value))

    @staticmethod
    def is_positive():
        """Static method to check if a given value is positive"""
        return Calculator.IS_POSITIVE

# Instantiate the class and test the functionality
calculator = Calculator(5)
calculator.display_value()

result = Calculator.add(3, 7)
print("Addition: {} + {} = {}".format(3, 7, result))

if Calculator.is_positive():
    print("Given number is positive")
else:
    print("Given number is not positive")
