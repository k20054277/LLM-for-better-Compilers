
class Calculator:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def add(self, num):
        self.num1 += num
        return self.num1

    def subtract(self, num):
        self.num1 -= num
        return self.num1

    def multiply(self, num):
        result = self.num1 * num
        self.num1 = result
        return result

    def divide(self, num):
        if num == 0:
            raise ValueError("Cannot divide by zero")
        result = self.num1 / num
        self.num1 = result
        return result
