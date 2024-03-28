
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        result = self.num1 + self.num2
        assert type(result) is int or type(result) is float, "Invalid result type: Expected integer or float"
        return result

    def subtract(self):
        result = self.num1 - self.num2
        assert self.num1 >= self.num2, "First number must be greater than or equal to second number"
        return result

if __name__ == "__main__":
    calc = Calculator(5, 3)
    print("Addition: ", calc.add())
    print("Subtraction: ", calc.subtract())
    
    calc2 = Calculator(3, 5)
    try:
        calc2.subtract()
    except AssertionError as e:
        print("Error:", e)

