
# Define a simple Calculator class
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    # Add two numbers
    def add(self):
        result = self.num1 + self.num2
        assert type(result) is int or type(result) is float, "Invalid result type: expected int or float"
        return result

    # Subtract second number from first number
    def subtract(self):
        result = self.num1 - self.num2
        assert self.num2 >= 0, "Cannot subtract a negative number"
        return result

# Create an instance of Calculator class and test methods
calc = Calculator(5, 3)
print("Addition:", calc.add()) # Addition: 8
print("Subtraction:", calc.subtract()) # Subtraction: 2

calc = Calculator(5, -3) # Test case with negative number
# Uncomment the line below to see assert error message
# print("Calculation:", calc.add())

# Test adding a float number
calc_float = Calculator(3.1, 2.0)
print("Addition of floats:", calc_float.add()) # Addition of floats: 5.1
